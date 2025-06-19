---
title: S3-Compatible Object Storage Configuration
description: Learn how to configure any S3-compatible object storage (MinIO, Wasabi, DigitalOcean Spaces, etc.) for Appcircle server using the Helm chart
sidebar_position: 60
tags:
  [self-hosted, object-storage]
---

import NeedHelp from '@site/docs/_need-help.mdx';

## Overview

Appcircle server requires object storage to store various artifacts, including build logs and application binaries. While AWS S3 and GCP Cloud Storage are popular options, you can use **any S3-compatible object storage** (such as MinIO, Wasabi, DigitalOcean Spaces, Backblaze B2, etc.) for production deployments.

This guide will walk you through the process of configuring any S3-compatible object storage as your backend for the Appcircle server Helm chart.

:::info
This guide is for any S3-compatible provider. For [AWS S3](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness/aws-s3-configuration) or [GCP Cloud Storage](/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness/gcp-cloud-storage-configuration), see their dedicated guides.
:::

## Prerequisites

- An S3-compatible object storage provider (MinIO, Wasabi, DigitalOcean Spaces, etc.)
- Access to the provider's management console or CLI
- The Helm chart [installed](https://helm.sh/docs/intro/install/) and [configured](https://helm.sh/docs/intro/quickstart/) for your Kubernetes cluster
- Basic understanding of object storage, access keys, and Kubernetes

## Create and Configure Buckets

You need to create the following buckets for Appcircle:

- `${BUCKET_PREFIX}-temp`
- `${BUCKET_PREFIX}-build`
- `${BUCKET_PREFIX}-distribution`
- `${BUCKET_PREFIX}-storesubmit`
- `${BUCKET_PREFIX}-store`
- `${BUCKET_PREFIX}-agent-cache`
- `${BUCKET_PREFIX}-backup`
- `${BUCKET_PREFIX}-publish`

:::tip
Choose a unique bucket prefix for your organization or environment (e.g., `appcircle-yourorg`).
:::

### Example: Creating Buckets with MinIO Client (mc)

```bash
# Set your bucket prefix
BUCKET_PREFIX="appcircle-yourorg"

# Create buckets
mc mb myminio/${BUCKET_PREFIX}-temp
mc mb myminio/${BUCKET_PREFIX}-build
mc mb myminio/${BUCKET_PREFIX}-distribution
mc mb myminio/${BUCKET_PREFIX}-storesubmit
mc mb myminio/${BUCKET_PREFIX}-store
mc mb myminio/${BUCKET_PREFIX}-agent-cache
mc mb myminio/${BUCKET_PREFIX}-backup
mc mb myminio/${BUCKET_PREFIX}-publish
```

:::info
Replace `myminio` with your MinIO alias or use your provider's CLI/console as appropriate.
:::

## IAM/User Setup and Access Keys

Create a user (or access key pair) with permissions to manage objects in the above buckets. The process varies by provider:

- **MinIO**: Use the MinIO Console or `mc admin user add` to create a user and assign policies.
- **Wasabi, DigitalOcean Spaces, etc.**: Use the provider's dashboard to create an access key/secret key pair with full access to the relevant buckets.

:::caution
Restrict permissions to only the required buckets for better security.
:::

## CORS Configuration

To allow the Appcircle web UI to directly access object storage (such as for client-based uploads and downloads), you must configure CORS on the `${BUCKET_PREFIX}-temp` bucket.

```json
[
  {
    "AllowedOrigins": ["https://my.appcircle.spacetech.com"],
    "AllowedMethods": ["GET", "PUT", "POST", "DELETE", "HEAD"],
    "AllowedHeaders": ["*"],
    "ExposeHeaders": [],
    "MaxAgeSeconds": 3600
  }
]
```

Refer to your provider's documentation for how to apply CORS settings.

## Create a Kubernetes Secret with Access Keys

Create a Kubernetes secret with your S3-compatible access and secret keys:

```bash
kubectl create secret generic appcircle-server-minio-connection \
  -n appcircle \
  --from-literal=accessKey=YOUR_ACCESS_KEY \
  --from-literal=secretKey=YOUR_SECRET_KEY
```

:::caution
- Replace `appcircle` with your actual namespace if different.
- **Do not change** the `appcircle-server-minio-connection` secret name.
:::

## Configure Appcircle Server to Use S3-Compatible Storage

Add the following to your `values.yaml`:

```yaml
global:
  minio:
    url: "https://your-s3-endpoint.com" # e.g., http://minio.yourdomain.com:9000
    region: "us-east-1" # Use your provider's region or leave blank if not required
    useHttp: "false" # Set to "true" if your endpoint uses HTTP
    bucketPrefix: "appcircle-yourorg-"
resource:
  s3:
    clientProvider: "S3" # Use "S3" for generic S3-compatible providers
    cdnProvider: ""
minio:
  enabled: false
```

:::caution
- Set `useHttp` to `true` only if your endpoint does not support HTTPS (not recommended for production).
- Check your provider's documentation for the correct endpoint URL and region.
:::

## Next Steps

After configuring your object storage and Helm values, return to the [Installation](/self-hosted-appcircle/install-server/helm-chart/installation) guide to continue.

<NeedHelp /> 