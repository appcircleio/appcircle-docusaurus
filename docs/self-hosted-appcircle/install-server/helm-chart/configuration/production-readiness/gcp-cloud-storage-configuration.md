---
title: GCP Cloud Storage Configuration
description: Learn how to configure GCP Cloud Storage as object storage for Appcircle server when installing using a Helm chart
tags:
  [
    self-hosted,
    gcp,
    cloud-storage,
    object-storage,
  ]
sidebar_position: 60
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import NeedHelp from '@site/docs/_need-help.mdx';
import S3MinimumVersionCaution from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_s3-minimum-version-caution.mdx';
import S3MigrationCaution from '@site/docs/self-hosted-appcircle/install-server/helm-chart/configuration/\_s3-migration-caution.mdx';

## Overview

This guide provides comprehensive instructions for configuring **Google Cloud Storage (GCS)** as your object storage backend for the Appcircle server. While the default Helm chart deployment includes MinIO as an in-cluster object storage solution, **production environments** benefit from using a more robust and scalable solution like GCP Cloud Storage.

<S3MinimumVersionCaution />

### What This Guide Covers

This guide will walk you through the process of configuring GCP Cloud Storage as your object storage backend for the Appcircle server. To use GCP Cloud Storage with Appcircle server, you need to:

- **Set up GCP infrastructure**: GCS buckets, IAM service accounts, and permissions
- **Configure Appcircle server**: Update Helm values to use GCS
- **Optional CDN setup**: Google Cloud CDN for performance optimization

<S3MigrationCaution />

## Prerequisites

To complete this guide, you must have the following:

### 1. GCP Account and Permissions

A **Google Cloud Platform (GCP) account** with appropriate permissions to create and manage Cloud Storage buckets, IAM service accounts, and roles.

<details>
    <summary>Click to view more details about GCP permissions.</summary>

You need the following GCP permissions to complete this configuration:

- **Cloud Storage permissions**: Create buckets, configure CORS, manage bucket policies
- **IAM permissions**: Create service accounts, roles, and manage IAM bindings
- **Project permissions**: Access to the GCP project where resources will be created

If you're working in a restricted environment, ensure you have the necessary permissions before proceeding.

</details>

### 2. Google Cloud SDK

The **Google Cloud SDK** is **required** and must be **[installed](https://cloud.google.com/sdk/docs/install)** and **[configured](https://cloud.google.com/sdk/docs/authorizing)** on your machine.

<details>
    <summary>Click to view more details about Google Cloud SDK configuration.</summary>

To configure Google Cloud SDK, you need:

- **Project ID** for your GCP project
- **Service account credentials** for authentication

You can configure Google Cloud SDK using:
```bash
gcloud init
```

Or by setting environment variables:
```bash
export GOOGLE_CLOUD_PROJECT="your-project-id"
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service-account-key.json"
```

</details>

### 3. Kubernetes/OpenShift Access

**`kubectl`** (for Kubernetes) or **`oc`** (for OpenShift) CLI is **required** and must be configured to access your cluster.

:::info
This guide assumes you have administrative access to your GCP project and Kubernetes/OpenShift cluster. If you're working in a restricted environment, ensure you have the necessary permissions before proceeding.
:::

### 4. Basic Understanding

Basic understanding of **GCP IAM**, **Cloud Storage**, and **Kubernetes/OpenShift** concepts is recommended.

### 5. Optional: Domain and SSL Certificates

For Google Cloud CDN setup (optional), you'll need:
- **Domain name**: For custom CDN domains
- **SSL certificates**: For HTTPS access to your CDN

## Configuration Steps

### 1. Set Up Environment Variables

**Set up your environment variables** before proceeding with the configuration. These variables will be used throughout the configuration process.

:::note
In this documentation, we will use `spacetech` as an **example organization name** and `us-east1` as an **example GCP region**. You should **replace these values** with your actual organization name and preferred GCP region.
:::

```bash
# Set your organization name and GCP project details
ORG_NAME="spacetech" # Replace with your organization name
PROJECT_ID="my-gcp-project" # Replace with your actual GCP project ID
BUCKET_PREFIX="appcircle-${ORG_NAME}-" # Make sure to add a hyphen at the end of the bucket prefix
LOCATION="us-east1" # Replace with your preferred GCP region
SERVICE_ACCOUNT_NAME="appcircle-server"
```

:::caution
- Replace `spacetech` with your organization name in the `ORG_NAME` variable
- Replace `my-gcp-project` with your actual GCP project ID in the `PROJECT_ID` variable
- Replace `us-east1` with your preferred GCP region in the `LOCATION` variable
- Ensure your organization name follows GCS naming conventions:
  - 3-63 characters long
  - Lowercase letters, numbers, dots (.), and hyphens (-)
  - Must start and end with a letter or number
  - Must be DNS-compliant
:::

### 2. Create GCP Cloud Storage Buckets

**Create the required GCS buckets** to store the artifacts generated by the Appcircle server.

Appcircle server requires the following GCS buckets for different purposes:

- **`${BUCKET_PREFIX}temp`**: Temporary files and uploads (requires CORS configuration for direct uploads/downloads from the client browsers)
- **`${BUCKET_PREFIX}build`**: Build artifacts and logs
- **`${BUCKET_PREFIX}distribution`**: Testing Distribution files
- **`${BUCKET_PREFIX}storesubmit`**: Appcircle Store Submit files
- **`${BUCKET_PREFIX}store`**: Enterprise App Store files
- **`${BUCKET_PREFIX}agent-cache`**: Appcircle Runner cache files
- **`${BUCKET_PREFIX}backup`**: Backup files
- **`${BUCKET_PREFIX}publish`**: Published mobile app binaries

:::tip
**Bucket Naming**: Bucket names must be globally unique across all GCP projects. Using your organization name as a prefix ensures uniqueness.
:::

**Create all required buckets:**

```bash
# Create all required buckets
gsutil mb -l ${LOCATION} gs://${BUCKET_PREFIX}temp/
gsutil mb -l ${LOCATION} gs://${BUCKET_PREFIX}build/
gsutil mb -l ${LOCATION} gs://${BUCKET_PREFIX}distribution/
gsutil mb -l ${LOCATION} gs://${BUCKET_PREFIX}storesubmit/
gsutil mb -l ${LOCATION} gs://${BUCKET_PREFIX}store/
gsutil mb -l ${LOCATION} gs://${BUCKET_PREFIX}agent-cache/
gsutil mb -l ${LOCATION} gs://${BUCKET_PREFIX}backup/
gsutil mb -l ${LOCATION} gs://${BUCKET_PREFIX}publish/
```

:::info
The bucket names use your organization name to ensure global uniqueness, as GCS bucket names must be unique across all GCP projects worldwide.
:::

### 3. Configure CORS Settings

**Configure CORS settings** for the `temp` bucket to allow cross-origin requests from your Appcircle server dashboard.

:::caution
Replace the `https://my.appcircle.spacetech.com` with the dashboard URL that you will use to access the Appcircle server. For example, if you are using `.appcircle.spacetech.com` as the domain in the Helm `values.yaml` file, the dashboard URL will be `https://my.appcircle.spacetech.com`.
:::

- Create a CORS configuration file:

```bash
cat << 'EOF' > appcircle-gcs-policy.json
[
  {
    "origin": ["https://my.appcircle.spacetech.com"],
    "method": ["GET", "PUT", "POST", "DELETE", "HEAD"],
    "responseHeader": ["*"],
    "maxAgeSeconds": 3600
  }
]
EOF
```

- Apply the CORS configuration:

```bash
gsutil cors set appcircle-gcs-policy.json gs://${BUCKET_PREFIX}temp
```

:::tip
- The CORS configuration is only required for the `temp` bucket.
- Other buckets don't require CORS configuration, as they are accessed server-side.
- If you're using HTTP instead of HTTPS, replace `https://` with `http://` in the **`origin`**.
:::

### 4. Create Service Account and Permissions

**Create a service account with minimal permissions** to make the Appcircle server able to access the GCS buckets.

- **Create a service account** for Appcircle server to access the GCS buckets.

```bash
gcloud iam service-accounts create ${SERVICE_ACCOUNT_NAME} \
  --description="Appcircle GCS access service account" \
  --display-name="Appcircle server"
```

- **Create a custom role** with granular access for better security:

```bash
gcloud iam roles create AppcircleGCSRole \
  --project=$PROJECT_ID \
  --title="Appcircle GCS Role" \
  --description="For Appcircle server to access GCS buckets" \
  --permissions="storage.objects.get,storage.objects.list,storage.objects.create,storage.objects.delete" \
  --stage=GA
```

**Bind the role to the service account for each bucket:**

```bash
# Bind permissions to each bucket
gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}temp \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="projects/${PROJECT_ID}/roles/AppcircleGCSRole"

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}build \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="projects/${PROJECT_ID}/roles/AppcircleGCSRole"

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}distribution \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="projects/${PROJECT_ID}/roles/AppcircleGCSRole"

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}storesubmit \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="projects/${PROJECT_ID}/roles/AppcircleGCSRole"

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}store \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="projects/${PROJECT_ID}/roles/AppcircleGCSRole"

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}agent-cache \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="projects/${PROJECT_ID}/roles/AppcircleGCSRole"

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}backup \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="projects/${PROJECT_ID}/roles/AppcircleGCSRole"

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}publish \
  --member="serviceAccount:${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com" \
  --role="projects/${PROJECT_ID}/roles/AppcircleGCSRole"
```

### 5. Generate Service Account Credentials

**Generate and download credentials** for the service account:

```bash
gcloud iam service-accounts keys create appcircle-sa-key.json \
  --iam-account=${SERVICE_ACCOUNT_NAME}@${PROJECT_ID}.iam.gserviceaccount.com
```

:::warning
**CRITICAL: Save the service account key file (`appcircle-sa-key.json`) securely.** You'll need these credentials in the next step to create the Kubernetes secret.
:::

### 6. Optional: Create CDN for Google Storage Buckets

Google Cloud CDN can improve performance by caching your GCS content at edge locations worldwide. This reduces latency and improves download speeds for your users.

:::tip
- **Follow this guide** if you need production-grade performance to serve your users globally.
- **Skip this section** if you're setting up for development/testing or have a small or medium team.
  - You can always enable Google Cloud CDN later without reinstalling the Appcircle server.
    - **Skip to** the [Create Kubernetes Secret](#create-kubernetesopenshift-secret-for-gcp-credentials) step if you do not need CDN configuration.
:::

This guide will walk you through the process of creating a CDN for your GCS buckets with the `gcloud` CLI.

:::info
**Flexibility Note**: You can achieve the same results with other tools (GCP Console, Terraform, etc.) as long as you create the same infrastructure components described in this documentation. You can also add additional configurations (security policies, monitoring, etc.) as long as you don't break the core requirements:
- CDN must be configured to serve the GCS buckets
- GCS bucket policies must be updated to allow CDN access
- URL signing key must be created and configured
- SSL certificate should be managed or imported for the CDN
- DNS must be configured to point to the CDN endpoint
- Kubernetes secret must contain the correct credentials for the URL signing key
- Helm values must include the specified CDN configuration for the Appcircle server
:::

#### Step 6.1: Create Backend Buckets and Enable CDN

**For each bucket you want to serve via CDN, create a backend bucket and enable CDN:**

```bash
gcloud compute backend-buckets create ${BUCKET_PREFIX}distribution-bucket \
    --gcs-bucket-name=${BUCKET_PREFIX}distribution \
    --enable-cdn \
    --cache-mode=FORCE_CACHE_ALL \
    --project=$PROJECT_ID

gcloud compute backend-buckets create ${BUCKET_PREFIX}build-bucket \
    --gcs-bucket-name=${BUCKET_PREFIX}build \
    --enable-cdn \
    --cache-mode=FORCE_CACHE_ALL \
    --project=$PROJECT_ID

gcloud compute backend-buckets create ${BUCKET_PREFIX}publish-bucket \
    --gcs-bucket-name=${BUCKET_PREFIX}publish \
    --enable-cdn \
    --cache-mode=FORCE_CACHE_ALL \
    --project=$PROJECT_ID

gcloud compute backend-buckets create ${BUCKET_PREFIX}store-bucket \
    --gcs-bucket-name=${BUCKET_PREFIX}store \
    --enable-cdn \
    --cache-mode=FORCE_CACHE_ALL \
    --project=$PROJECT_ID

gcloud compute backend-buckets create ${BUCKET_PREFIX}storesubmit-bucket \
    --gcs-bucket-name=${BUCKET_PREFIX}storesubmit \
    --enable-cdn \
    --cache-mode=FORCE_CACHE_ALL \
    --project=$PROJECT_ID
```

#### Step 6.2: Create URL Signing Key

**Create a URL signing key** to sign the URLs of the GCS buckets.

```bash
head -c 16 /dev/random | base64 | tr +/ -_ > url-signing-key.txt
```

#### Step 6.3: Add Signed URL Key to Backend Buckets

**Add the URL signing key to the backend buckets.**

```bash
gcloud compute backend-buckets add-signed-url-key ${BUCKET_PREFIX}distribution-bucket \
    --key-name=appcircle-sign-key \
    --key-file=url-signing-key.txt \
    --project=$PROJECT_ID

gcloud compute backend-buckets add-signed-url-key ${BUCKET_PREFIX}build-bucket \
    --key-name=appcircle-sign-key \
    --key-file=url-signing-key.txt \
    --project=$PROJECT_ID

gcloud compute backend-buckets add-signed-url-key ${BUCKET_PREFIX}publish-bucket \
    --key-name=appcircle-sign-key \
    --key-file=url-signing-key.txt \
    --project=$PROJECT_ID
    
gcloud compute backend-buckets add-signed-url-key ${BUCKET_PREFIX}store-bucket \
    --key-name=appcircle-sign-key \
    --key-file=url-signing-key.txt \
    --project=$PROJECT_ID

gcloud compute backend-buckets add-signed-url-key ${BUCKET_PREFIX}storesubmit-bucket \
    --key-name=appcircle-sign-key \
    --key-file=url-signing-key.txt \
    --project=$PROJECT_ID
```

#### Step 6.4: Import SSL Certificate

**If you want to use custom domains (like `cdn.yourcompany.com`), you need an SSL certificate.**

:::info
You can skip this step if you already have an SSL certificate in your GCP project.
:::

```bash
gcloud compute ssl-certificates create appcircle-cdn-ssl-cert \
    --certificate=<path-to-your-certificate> \
    --private-key=<path-to-your-private-key> \
    --global
```

#### Step 6.5: Reserve a Global Static External IP Address

**Reserve a global static external IP address** to use as the CDN endpoint.

```bash
gcloud compute addresses create appcircle-cdn-ip \
    --network-tier=PREMIUM \
    --ip-version=IPV4 \
    --global
```

#### Step 6.6: Create URL Map for Backend Buckets

**Create a URL map** for the backend buckets.

```bash
gcloud compute url-maps create appcircle-cdn-url-map \
  --default-backend-bucket=${BUCKET_PREFIX}build-bucket \
  --global
```

#### Step 6.7: Create Target HTTPS Proxy for the URL Map

**Create a target HTTPS proxy** for the URL map.

```bash
gcloud compute target-https-proxies create appcircle-https-lb-proxy \
  --ssl-certificates=appcircle-cdn-ssl-cert \
  --url-map=appcircle-cdn-url-map
```

#### Step 6.8: Create Global Forwarding Rule for the Target HTTPS Proxy

**Create a global forwarding rule** for the target HTTPS proxy.

```bash
gcloud compute forwarding-rules create appcircle-cdn-forwarding-rule \
  --address=appcircle-cdn-ip \
  --global \
  --target-https-proxy=appcircle-https-lb-proxy \
  --ports=443 \
  --load-balancing-scheme=EXTERNAL \
  --network-tier=PREMIUM \
  --project=$PROJECT_ID
```

#### Step 6.9: Add Additional URL Maps for Backend Buckets

**Add additional URL maps** for the backend buckets.

```bash
gcloud compute url-maps add-path-matcher appcircle-cdn-url-map \
  --path-matcher-name=appcircle-distribution-matcher \
  --new-hosts=appcircle-distribution-cdn.spacetech.com \
  --default-backend-bucket=${BUCKET_PREFIX}distribution-bucket \
  --project=$PROJECT_ID

gcloud compute url-maps add-path-matcher appcircle-cdn-url-map \
  --path-matcher-name=appcircle-publish-matcher \
  --new-hosts=appcircle-publish-cdn.spacetech.com \
  --default-backend-bucket=${BUCKET_PREFIX}publish-bucket \
  --project=$PROJECT_ID

gcloud compute url-maps add-path-matcher appcircle-cdn-url-map \
  --path-matcher-name=appcircle-store-matcher \
  --new-hosts=appcircle-store-cdn.spacetech.com \
  --default-backend-bucket=${BUCKET_PREFIX}store-bucket \
  --project=$PROJECT_ID

gcloud compute url-maps add-path-matcher appcircle-cdn-url-map \
  --path-matcher-name=appcircle-storesubmit-matcher \
  --new-hosts=appcircle-storesubmit-cdn.spacetech.com \
  --default-backend-bucket=${BUCKET_PREFIX}storesubmit-bucket \
  --project=$PROJECT_ID
```

#### Step 6.10: Grant CDN Service Account Access to Buckets

**Grant CDN service account access to the buckets.**

```bash
PROJECT_NUMBER=$(gcloud projects describe $PROJECT_ID --format='get(projectNumber)')
```

**Assign the `roles/storage.objectViewer` to the LoadBalancer service account to make it able to access the private GCS buckets:**

```bash
gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}distribution \
  --member=serviceAccount:service-${PROJECT_NUMBER}@cloud-cdn-fill.iam.gserviceaccount.com \
  --role=roles/storage.objectViewer

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}build \
  --member=serviceAccount:service-${PROJECT_NUMBER}@cloud-cdn-fill.iam.gserviceaccount.com \
  --role=roles/storage.objectViewer

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}publish \
  --member=serviceAccount:service-${PROJECT_NUMBER}@cloud-cdn-fill.iam.gserviceaccount.com \
  --role=roles/storage.objectViewer

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}store \
  --member=serviceAccount:service-${PROJECT_NUMBER}@cloud-cdn-fill.iam.gserviceaccount.com \
  --role=roles/storage.objectViewer

gcloud storage buckets add-iam-policy-binding gs://${BUCKET_PREFIX}storesubmit \
  --member=serviceAccount:service-${PROJECT_NUMBER}@cloud-cdn-fill.iam.gserviceaccount.com \
  --role=roles/storage.objectViewer
```

#### Step 6.11: Create Kubernetes Secret for CDN URL Sign Key

**Create a Kubernetes secret** for the URL signing key.

```bash
kubectl create secret generic appcircle-cdn-url-sign-key -n appcircle \
  --from-literal='cdn-url-sign-key-name=appcircle-sign-key' \
  --from-literal="cdn-url-sign-key=$(cat url-signing-key.txt)"
```

## Create Kubernetes/OpenShift Secret for GCP Credentials

<Tabs groupId="Platform">

  <TabItem value="kubernetes" label="Kubernetes">

- Create the namespace that Appcircle server will be installed in if you haven't yet:
```bash
kubectl create namespace appcircle
```

- **Create a Kubernetes secret** named `<helm-release-name>-gcs-credentials` with the GCP credentials to be used by Appcircle server.

```bash

# Convert the service account key to base64
ENCODED_CREDENTIALS=$(cat appcircle-sa-key.json | base64 -w 0)

# Create the Kubernetes secret
kubectl create secret generic appcircle-gcs-credentials \
  -n appcircle \
  --from-literal=gcs-credentials-base64="${ENCODED_CREDENTIALS}"
```

  </TabItem>
  <TabItem value="openshift" label="OpenShift">

- Create the project that Appcircle server will be installed in if you haven't yet:

```bash
oc new-project appcircle
```

- **Create a OpenShift secret** named `<helm-release-name>-gcs-credentials` with the GCP credentials to be used by Appcircle server.

```bash
# Convert the service account key to base64
ENCODED_CREDENTIALS=$(cat appcircle-sa-key.json | base64 -w 0)

# Create the OpenShift secret
oc create secret generic appcircle-gcs-credentials \
  -n appcircle \
  --from-literal=gcs-credentials-base64="${ENCODED_CREDENTIALS}"
```

  </TabItem>
</Tabs>

:::caution
- Replace `appcircle` with the actual namespace/project where Appcircle server will be installed
- Ensure the `appcircle-sa-key.json` file is in your current directory
- The secret name `appcircle-gcs-credentials` will be referenced in the Helm configuration
:::

## Configure Helm Values

**Configure your `values.yaml` file** to use GCP Cloud Storage instead of MinIO.

Add or update the following configuration to your `values.yaml` file:

<Tabs groupId="CloudCDNEnabled">

  <TabItem value="true" label="Cloud CDN Enabled">

```yaml
global:
  minio:
    url: https://storage.googleapis.com # Do not replace this value
    region: "us-east1" # Replace with your GCP region
    useHttp: "false" # Set to "false" if you're using HTTPS GCS endpoint
    bucketPrefix: "appcircle-spacetech-" # Replace with your bucket prefix
resource:
  s3:
    clientProvider: "GCLOUD" # Set to "GCLOUD" to use GCP Cloud Storage
    cdnProvider: "GCLOUD" # Set to "GCLOUD" to use GCP Cloud Storage
    urlSignKeySecretName: "appcircle-cdn-url-sign-key" # Reference to the secret created above
    googleCredentialsSecretName: "appcircle-gcs-credentials" # Reference to the secret created above
    cdnMapping: "Build=https://appcircle-build-cdn.spacetech.com,Distribution=https://appcircle-distribution-cdn.spacetech.com,Storesubmit=https://appcircle-storesubmit-cdn.spacetech.com,Store=https://appcircle-store-cdn.spacetech.com,Publish=https://appcircle-publish-cdn.spacetech.com" # Replace with your CDN mapping
minio:
  enabled: false
```
  </TabItem>
  <TabItem value="false" label="Cloud CDN Disabled">

```yaml
global:
  minio:
    url: https://storage.googleapis.com # Do not replace this value
    region: "us-east1" # Replace with your GCP region
    useHttp: "false" # Set to "false" if you're using HTTPS GCS endpoint
    bucketPrefix: "appcircle-spacetech-" # Replace with your bucket prefix
resource:
  s3:
    clientProvider: "GCLOUD" # Set to "GCLOUD" to use GCP Cloud Storage
    googleCredentialsSecretName: appcircle-gcs-credentials # Reference to the secret created above
minio:
  enabled: false # Disable internal MinIO deployment
```

  </TabItem>
</Tabs>

:::caution
- Do not change the `https://storage.googleapis.com` value. It is set to the default GCS endpoint.
- Replace `us-east1` with your GCP region.
  - Run `echo $LOCATION` to get your GCP region from the variables defined in the previous steps.
- Replace `appcircle-spacetech-` with your actual bucket prefix.
  - Run `echo $BUCKET_PREFIX` to get your bucket prefix from the variables defined in the previous steps.
- Set `useHttp` to `true` only if you're using HTTP instead of HTTPS (not recommended for production)
- Ensure `googleCredentialsSecretName` matches the secret name created in the previous step
:::

## Next Steps

After completing the GCP Cloud Storage configuration:

1. **Return to the main installation guide**:
   - For Kubernetes: [Kubernetes Installation](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes)
   - For OpenShift: [OpenShift Installation](/self-hosted-appcircle/install-server/helm-chart/installation/openshift)

2. **Continue with the installation process** using your configured `values.yaml` file

3. **Verify the configuration** by checking that Appcircle server can access the GCS buckets after installation

<NeedHelp />
