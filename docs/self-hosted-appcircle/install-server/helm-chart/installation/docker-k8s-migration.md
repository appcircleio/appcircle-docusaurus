---
title: Docker to Kubernetes Migration
description: Learn how to migrate from standalone Appcircle server to Kubernetes Appcircle server.
tags: [self-hosted, helm, configuration, kubernetes, migration]
sidebar_position: 30
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_spacetech-example-info.mdx';

## Overview

This guide provides a step-by-step walkthrough for migrating your self-hosted **Appcircle** instance from a standalone Docker environment to a Kubernetes cluster. It assumes that you already have:

1. A fully operational Docker deployment of Appcircle server.
2. A Kubernetes cluster ready for deployment.

In this guide, the **standalone Appcircle server** refers to the machine that hosts the Appcircle server with Docker.

Also the **bastion host** refers to a machine with network access to both:

- The existing standalone Appcircle server.
- The Kubernetes cluster.

The bastion host serves as a central point for executing commands, transferring backup data, and applying configurations. During the migration process, you will:

- Copy configuration files and database backups from the Docker host to the bastion host.
- Use the bastion host to deploy and configure the new Appcircle instance in the Kubernetes cluster.

:::caution Downtime Alert  
This migration process involves downtime. To minimize disruption, **plan accordingly** and:

- Back up all crucial data before starting the migration.
- Thoroughly review each step and ensure you understand its implications.
- Test the migration process in a staging or non-production environment if possible.
- Notify users about the expected downtime and migration schedule.  
  :::


## Prerequisites

To complete this guide, you must have the following:

### 1. Domain Name

A main **domain name**, which will have **subdomains**, is **required** for the Appcircle server. Since the standalone Appcircle server already has a configured domain name, you should retain the same domain name when migrating to the Kubernetes cluster.

:::note
In this documentation, we will use `appcircle.spacetech.com` as an **example main domain** and `spacetech` as an **example organization name**.
:::

<details>
    <summary>Click to view more details about domain name prerequisite.</summary>

By default, Appcircle uses seven subdomains. These subdomains are:

1. api.appcircle.spacetech.com
2. auth.appcircle.spacetech.com
3. dist.appcircle.spacetech.com
4. hook.appcircle.spacetech.com
5. resource.appcircle.spacetech.com
6. my.appcircle.spacetech.com
7. redis.appcircle.spacetech.com

**Upon completing the deployment** of the Appcircle server, you will need to create DNS records based on the Ingress objects created in Kubernetes.

</details>

### 2. SSL Certificate

An **SSL certificate** is **required** to deploy the Appcircle server for **production** environments.

You **can skip** SSL certificate if you are deploying Appcircle server **for trial purposes**.

<details>
    <summary>Click to view more details about SSL certificate prerequisite.</summary>

- The SSL certificate private key shouldn't be password protected.

- The SSL certificate should be in PEM format.

- Ensure the **one certificate** covers **all the subdomains** in the [domain name](#1-domain-name) section.

- Make sure to configure the Appcircle server with a **fullchain certificate**, which should include the leaf (or app) certificate, intermediate certificates, and the root certificate.

:::tip
You can use a **wildcard certificate** to cover all the subdomains, simplifying the certificate management process. For example, a wildcard certificate for **`*.appcircle.spacetech.com`** will be enough.
:::

:::caution
If you use a domain like `appcircle.spacetech.com`, it will have **two levels of subdomains**. Ensure that both your DNS provider and SSL certificate provider support multi-level subdomains for proper configuration.
:::

</details>

## Pre-Migration Steps

### Standalone Appcircle Server Steps

This section outlines the essential steps to back up data from your existing Standalone Appcircle server installation and prepare your Kubernetes environment for the migration.

You will:

- Create a directory on the **bastion host** to store backups.
- Backup configuration files, secrets, and database credentials from the Standalone Appcircle server host.

:::tip Recommended Backup Strategy  
Before starting, create a full backup of your Appcircle server. Options include:

- Creating a VM snapshot of the Docker host.
- Using a backup tool specific to your infrastructure.
- Ensuring configuration files and database dumps are included in your backups.  
  :::

#### 1. Create a Migration Directory

On your **bastion host**, create a directory to store all migration files:

```bash
mkdir appcircle-k8s-migration && cd appcircle-k8s-migration
```

#### 2. Backup Appcircle Configuration Data

On the **standalone Appcircle server**, execute the following commands to back up the necessary files. Transfer the outputs to the migration directory on the bastion host.

- **Appcircle Server Directory:**
  Change directory to the `appcircle-server`.
  ```bash
  cd appcircle-server
  ```
  <SpacetechExampleInfo/>
- **`global.yaml` Configuration:**
  Print the `global.yaml` file and save it on the bastion host:

  ```bash
  cat projects/spacetech/global.yaml
  ```

- **User Secrets:**
  Decode and print the `user-secret.yaml` file and save it on the bastion host:

  ```bash
  cat projects/spacetech/user-secret | base64 -d
  ```

- **Generated Secrets:**
  Print the `generated-secret.yaml` file and save it on the bastion host:

  ```bash
  cat projects/spacetech/generated-secret.yaml
  ```

- **`cred.json` file:**
  Print the `cred.json` file and save it on the bastion host:
  ```bash
  cat cred.json
  ```

#### 3. Check the Data Size on the Standalone Appcircle Server

- **Get the volume sizes:**

  ```bash
  export APPCIRCLE_DISK_USAGE=$(docker system df -v)
  ```

- **Check the MinIO data size:**

  ```bash
  echo "$APPCIRCLE_DISK_USAGE" | grep "snsd_data"
  ```

- **Check the MongoDB data size:**

  ```bash
  echo "$APPCIRCLE_DISK_USAGE" | grep "mongo_data"
  ```

- **Check the PostgreSQL data size:**

  ```bash
  echo "$APPCIRCLE_DISK_USAGE" | grep "posgresqlData"
  ```

- **Check the Vault data size:**
  ```bash
  echo "$APPCIRCLE_DISK_USAGE" | grep "vault_data"
  ```

You will use those values while configuring the `values.yaml` of the Appcircle server Helm chart.

#### 4. Make Sure the Standalone Appcircle Server Is Running

Before proceeding with the migration, verify that the standalone Appcircle server is operational and healthy. This ensures you can create accurate backups without issues.

Additionally:

- There should be no running builds on the Appcircle during the migration.
- Prevent external requests while keeping the server healthy by stopping the Nginx service.

To achieve that, you can follow the steps below:

1. **Log in to the standalone Appcircle server:**

2. **Change directory to the `appcircle-server`:**

   ```bash
   cd appcircle-server
   ```

3. **Change directory to the `export` directory of the project:**
   <SpacetechExampleInfo/>

   ```bash
   cd projects/spacetech/export
   ```

4. **Stop the Nginx service:**
   ```bash
   docker compose stop nginx
   ```

### Kubernetes Appcircle Server Steps

This section outlines the steps and considerations for deploying the Appcircle server to a Kubernetes cluster. Ensure you review the [Key Considerations](#2-key-considerations) below before proceeding.

#### 1. Prepare for Helm Chart Installation

After reviewing the key considerations, follow the [Appcircle Server Kubernetes Installation Guide](https://docs.appcircle.io/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes) for detailed Appcircle server Helm chart deployment instructions.

#### 2. Key Considerations

- **Stateful Applications:**
  This guide assumes you are migrating from a standalone Appcircle server to a Kubernetes cluster with stateful applications (e.g., PostgreSQL, MinIO, MongoDB, Vault) managed by the Appcircle Helm chart.

  - If you choose to manage stateful apps **outside the Helm chart's scope**, modify the commands and configurations accordingly.
  - Refer to the [Production Readiness](https://docs.appcircle.io/self-hosted-appcircle/install-server/helm-chart/configuration/production-readiness) page for additional guidance.

- **Protocol Configuration (HTTP/HTTPS):**
  Match the protocol used by your standalone Appcircle server:

  - If the standalone server is using `HTTPS`, configure the Helm chart for `HTTPS`.
  - If the server is running on `HTTP`, adjust the Helm chart configuration for `HTTP`.

- **Storage Allocation:**
  Update your Helm chart's `values.yaml` file with storage sizes based on the data extracted in the [Check the Data Size](#3-check-the-data-size-on-the-standalone-appcircle-server) section.

  - Refer to the [Storage Configuration](https://docs.appcircle.io/self-hosted-appcircle/install-server/helm-chart/configuration/storage-configuration) page for detailed instructions.

- **Prepare `values.yaml` for Migration:**
  Make the following adjustments to your `values.yaml` file **before deploying the Helm chart**:

  ```yaml
  auth:
    auth-keycloak:
      replicas: 0
      organizationName: spacetech
      initialOrganizationId: a0c5c671-35a7-47a9-a32d-eaf4edac574a
  mongodb:
    resourcesPreset: "large"
  ```

  - Setting `auth-keycloak.replicas` to `0` disables Keycloak authentication during migration to prevent conflicts.
  - Setting `resourcesPreset` to `"large"` ensures MongoDB has sufficient resources for handling large datasets.

## Migrate the Data

### 1. Create Kubernetes Secrets

This section details the creation of Kubernetes secrets required for Appcircle to function correctly. These secrets store sensitive information such as passwords and certificates, securely injecting them into your Appcircle deployment.

:::tip
Ensure you have [gathered all necessary data](#2-backup-appcircle-configuration-data) before proceeding.

Some secret data, such as database passwords and Keycloak client secrets, used in the Kubernetes secrets creation below should match the data extracted from the backups of the standalone server. Ensure consistency between the backed-up values and the values used in the Kubernetes secrets to prevent connectivity and authentication issues.
:::

- **Kubernetes Namespace:** Create a namespace for Appcircle in your Kubernetes cluster:

  ```bash
  kubectl create namespace appcircle
  ```

- **Container Registry Secret:** Create the container registry secret for the Appcircle artifact registry:

:::info
If you are using your own container registry, follow the `Custom Registry` section below.

If your registry doesn't require authentication, you can skip this section.
:::

<Tabs groupId="Image Registry">

  <TabItem value="appcircle-registry" label="Appcircle Registry">

- Save the `cred.json` file.

- Create the container registry secret:

```bash
kubectl create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='europe-west1-docker.pkg.dev' \
  --docker-username='_json_key' \
  --docker-password="$(cat cred.json)"
```

  </TabItem>
  <TabItem value="custom-registry" label="Custom Registry">

- Update the `server`, `username`, and `password` fields for your own custom registry and create the container registry secret:

```bash
kubectl create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='registry.spacetech.com' \
  --docker-username='yourRegistryUsername' \
  --docker-password='superSecretRegistryPassword'
```

  </TabItem>
</Tabs>

- **SMTP Password Secret:** Create the SMTP server password if the SMTP server that the Appcircle server will use requires authentication.

```bash
kubectl create secret generic appcircle-server-smtp \
  -n appcircle \
  --from-file=password=<path-to-smtp-password-file>
```

- **Keycloak Clients Secret:**

:::caution
The client secret values used below should match the data extracted from the `generated-secret.yaml` backup of your standalone Appcircle server. You can check the `.keycloak.clients` key in the `generated-secret.yaml` file. Using incorrect values will prevent Appcircle from functioning correctly.
:::

```bash
kubectl create secret generic appcircle-server-auth-keycloak-clients-secret \
  -n appcircle \
  --from-literal=appcircleWeb='dc589939-******-87b57fc1a1c7' \
  --from-literal=buildServer='307f6946-******-9d7743294f6a' \
  --from-literal=distributionAdminService='a286d519-******-227dec040f53' \
  --from-literal=distributionTesterWeb='7cc0c02a-******-5e7139d63f3c' \
  --from-literal=licenseServer='e198b11a-******-1ac96174d6f7' \
  --from-literal=publishServer='7965798e-******-0b4e8af8afed' \
  --from-literal=reportingServer='88e3abfd-******-afd2e2a1263f' \
  --from-literal=storeAdminService='f263f48f-******-588c9f55b4e3' \
  --from-literal=storeServer='08839b8d-******-aff4ecb63703' \
  --from-literal=storeWeb='9f6a406e-******-a88c17d7c2f6' \
  --from-literal=distributionServer='7cc0c02a-******-5e7139d63f3c'
```

- **Keycloak Passwords Secret:**

:::caution
The Keycloak password values used below should match the data extracted from the `generated-secret.yaml` backup of your standalone Appcircle server. You can check the `.keycloak.password` key for the `adminPassword` and `.keycloak.initialPassword` for the `initialPassword` in the `generated-secret.yaml` file. Using incorrect values will prevent Appcircle from functioning correctly.
:::

```bash
kubectl create secret generic appcircle-server-auth-keycloak-passwords \
  -n appcircle \
  --from-literal=initialPassword=<initial-password> \
  --from-literal=adminPassword=<admin-password>
```

- **SSL Certificate Secret:** If you are using the Appcircle with HTTPS, create a secret for SSL certificates.

```bash
kubectl create secret generic appcircle-tls-wildcard \
  -n appcircle \
  --from-file=tls.crt=<path-to-tls.crt> \
  --from-file=tls.key=<path-to-tls.key> \
  --from-file=ca.crt=<path-to-ca.crt> \
  --type=kubernetes.io/tls
```

- **MinIO Connection Secret:**

:::caution
The MinIO keys used below should match the data extracted from the `generated-secret.yaml` backup of your standalone Appcircle server. You can check the `.minio.secretKey` key in the `generated-secret.yaml` file for the `accessKey` and `root-password` in the example command below. Using incorrect values will prevent Appcircle from functioning correctly.
:::

```bash
kubectl create secret generic appcircle-server-minio-connection \
  -n appcircle \
  --from-literal=accessKey=admin \
  --from-literal=secretKey=<your-minio-secret-key> \
  --from-literal=root-user=admin \
  --from-literal=root-password=<your-minio-root-password>
```

### 2. PostgreSQL Backup & Restore

#### Standalone Appcircle Server

1. **Locate PostgreSQL Container:** Find the PostgreSQL container name.

   ```bash
   docker ps | grep postgres
   ```

2. **Dump Database:** Save the database data to a file.

   ```bash
   docker exec <postgres_container_name> pg_dump -U keycloak -h localhost -p 5432 -F c -b -v -f pgdump.backup keycloak
   ```

3. **Copy Dump:** Copy the file from container to Appcircle server host.
   ```bash
   docker cp <postgres_container_name>:/pgdump.backup ~/appcircle-k8s-migration/
   ```

#### Bastion Host

1. **Copy the PostgreSQL Data to Bastion Host**: Copy the dumped PostgreSQL data from the Appcircle server to the bastion host.

   ```bash
   scp standalone-appcircle-server/app/appcircle-server/projects/spacetech/export/mongo-backup.gz .
   ```

2. **Get PostgreSQL Password:**

   ```bash
   kubectl get secret -n appcircle appcircle-server-auth-postgresql -ojsonpath='{.data.password}' | base64 -d
   ```

3. **Get the PostgreSQL pod name:**

   ```bash
   kubectl get pods -n appcircle | grep postgres
   ```

4. **Install PostgreSQL tools:**

   ```bash
   brew install postgresql
   ```

5. **Start Port Forwarding:**

   ```bash
   kubectl port-forward appcircle-server-auth-postgresql-0 5432:5432 -n appcircle
   ```

6. **Restore the Database:**
   ```bash
   pg_restore -h localhost -p 5432 -U keycloak -d keycloak ~/appcircle-k8s-migration/pgdump.backup
   ```

### 3. MongoDB Backup & Restore

#### Standalone Appcircle Server

<SpacetechExampleInfo/>

1. **Change directory to appcircle-server:**

   ```bash
   cd appcircle-server
   ```

2. **Expose MongoDB Port:** Add a port mapping (e.g., 36300:36300) to your `docker-compose.yml` for the `mongo_1` service and restart.

   - Edit the `compose.yaml` file.

   ```bash
   vim projects/spacetech/export/compose.yaml
   ```

   - Add the `ports` key to the `mongo_1` service.

   ```yaml
   services:
   mongo_1:
     image: europe-west1-docker.pkg.dev/appcircle/docker-registry/mongo:v3.25.0
     ports:
       - "36300:36300"
   ```

   - Restart the services.

   ```bash
   ./ac-self-hosted -n spacetech up
   ```

3. **Install the `mongosh` tool.**

   To install `mongosh` on the standalone Appcircle server, please check the [official MongoDB documentation](https://www.mongodb.com/docs/mongodb-shell/install/).

4. **Open Mongo Shell to the standalone Appcircle server:**

   ```bash
   mongosh --host 127.0.0.1 --port 36300
   ```

5. **Switch to the `admin` db:**

   ```mongosh
   use admin
   ```

6. **Create a user to dump the DB:**

   ```mongosh
   db.createUser({user: "backup",pwd: "backup",roles: [{ role: "root", db: "admin"}]})
   ```

7. **Get the MongoDB container name:**

   ```bash
   docker ps | grep mongo_1
   ```

8. **Get the MongoDB connection string:**

   ```bash
   cat projects/spacetech/export/publish/default.env | grep "CUSTOMCONNSTR_PUBLISH_DB_CONNECTION_STRING"
   ```

9. **Dump the MongoDB:**

   ```bash
   docker exec -it spacetech-mongo_1-1 mongodump --uri="mongodb://backup:backup@mongo_1:36300,mongo_2:36301,mongo_3:36302/?replicaSet=rs&authSource=admin" --gzip --archive=/mongo-backup.gz
   ```

10. **Copy the dumped DB file from out of the container to the host machine:**
    ```bash
    docker cp spacetech-mongo_1-1:/mongo-backup.gz .
    ```

#### Bastion Host

1. **Copy the file from the standalone Appcircle server to the bastion host:**

   ```bash
   scp standalone-appcircle-server/app/appcircle-server/projects/spacetech/export/mongo-backup.gz .
   ```

2. **Install MongoDB Database Tools:**

   To install MongoDB Database Tools, please check the [official MongoDB documentation](https://www.mongodb.com/docs/database-tools/installation/installation/#installation).

3. **Get the MongoDB root password of the K8s installation:**

   ```bash
   kubectl get secret -n appcircle appcircle-server-mongodb -o jsonpath='{.data.mongodb-root-password}' | base64 -d
   ```

4. **Start port forwarding:**
   ```bash
   kubectl port-forward appcircle-server-mongodb-0 27017:27017 -n appcircle
   ```
5. **Restore the dumped MongoDB:**
   ```bash
   mongorestore --uri="mongodb://root:<mongodb-root-password>@localhost:27017/?authSource=admin" --gzip --archive=./mongo-backup.gz
   ```

### 4. MinIO Mirror

#### Standalone Appcircle Server

1. **Log in to the standalone Appcircle server:**

2. **Change directory to appcircle-server:**

   ```bash
   cd appcircle-server
   ```

3. **Expose MinIO Port:** Ensure MinIO's port 9000 is accessible. You might need to publish the port in your `docker-compose.yml`.
   ```bash
   docker ps | grep snsd
   ```

<SpacetechExampleInfo/>

4. **Get MinIO credentials:** Retrieve the access key and secret key from your MinIO configuration.
   ```bash
   cat projects/spacetech/export/minio/access.env
   ```

#### Bastion Host

1. **Log in to the bastion:**

2. **Get the Kubernetes MinIO access and secret keys:**

   ```bash
   kubectl get secret -n appcircle appcircle-server-minio-connection -ojsonpath='{.data.accessKey}' | base64 -d && \
   echo && \
   kubectl get secret -n appcircle appcircle-server-minio-connection -ojsonpath='{.data.secretKey}' | base64 -d
   ```

3. **Get the MinIO service name:**

   ```bash
   kubectl get services -n appcircle | grep minio
   ```

4. **Change MinIO service to NodePort for temporary:**

   :::info
   We recommend opening the MinIO service to the external network temporarily instead of using `kubectl port-forward` since you might have problems while transferring large files over port forwarding of the `kubectl`.

   Note that this doesn't make the MinIO data public as long as you keep the MinIO password secret.
   :::

   ```bash
   kubectl patch service appcircle-server-minio -n appcircle --type='json' -p='[{"op": "replace", "path": "/spec/type", "value": "NodePort"}, {"op": "add", "path": "/spec/ports/0/nodePort", "value": 30534}, {"op": "add", "path": "/spec/ports/1/nodePort", "value": 32761}]'
   ```

5. **Install `rclone` tool:**

   :::info
   We recommended using `rclone` tool instead of `mc`.
   :::

   To install `rclone`, please check the [official rclone documentation](https://rclone.org/install/).

6. **Add Rclone Configuration for Standalone Server:**

   To configure Rclone for the standalone Appcircle server, follow these steps:

   - Start the Rclone configuration process:

     ```bash
     rclone config
     ```

   - Use the following inputs during the configuration process:

     ```plaintext
     n                                # Create a new remote
     name> ac-standalone              # Provide a descriptive name for the remote
     Storage> 4                       # Select "Amazon S3 Compliant Storage Provider" (4)
     provider> 7                      # Select "Minio Object Storage" (7)
     env_auth> "false"                # Set environment authentication to "false"
     access_key_id> <access_key>      # Enter the standalone Appcircle server's access key
     secret_access_key> <secret_key>  # Enter the standalone Appcircle server's secret access key
     region>                          # Leave this empty
     endpoint>                        # Provide the standalone Appcircle server's IP and MinIO port. Example: http://192.168.1.220:9040
     location_constraint:             # Leave this empty
     acl:                             # Leave this empty
     server_side_encryption:          # Leave this empty
     sse_kms_key_id:                  # Leave this empty
     Edit advanced config? (y/n): n   # Skip advanced configuration
     ```

7. **Add Rclone config for Kubernetes Appcircle server:**

   To configure `rclone` for the Kubernetes Appcircle server, follow these steps:

   - Start the `rclone` configuration process:

     ```bash
     rclone config
     ```

   - Use the following inputs during the configuration process:

     ```plaintext
     n                                # Create a new remote
     name> ac-k8s                     # Provide a descriptive name for the remote
     Storage> 4                       # Select "Amazon S3 Compliant Storage Provider" (4)
     provider> 7                      # Select "Minio Object Storage" (7)
     env_auth> "false"                # Set environment authentication to "false"
     access_key_id> <access_key>      # Enter the standalone Appcircle server's access key
     secret_access_key> <secret_key>  # Enter the standalone Appcircle server's secret access key
     region>                          # Leave this empty
     endpoint>                        # Provide the standalone Appcircle server's IP and MinIO port. Example: http://192.168.1.220:9040
     location_constraint:             # Leave this empty
     acl:                             # Leave this empty
     server_side_encryption:          # Leave this empty
     sse_kms_key_id:                  # Leave this empty
     Edit advanced config? (y/n): n   # Skip advanced configuration
     ```

8. **Start copying files:**

   ```bash
   rclone copy --progress --checksum --update ac-standalone: ac-k8s:
   ```

### 5. Vault Backup & Restore

#### Standalone Server Steps

1. **Log in to the standalone Appcircle server:**

2. **Change directory to appcircle-server:**

   ```bash
   cd appcircle-server
   ```

3. **Create a file named `migrate.hcl`:**

   ```bash
   cat > migrate.hcl <<'EOL'
   storage_source "file" {
   path = "/vault/data/"
   }

   storage_destination "file" {
   path = "/vault/target/"
   }

   cluster_addr="http://127.0.0.1:8201"
   EOL
   ```

4. **Get the Vault container name:**

   ```bash
   docker ps | grep vault
   ```

5. **Copy the migration file to the Vault container:**

   ```bash
   docker cp migrate.hcl spacetech-vault-1:/vault/
   ```

6. **Migrate the the Vault data to the target directory:**

   ```bash
   docker exec -it spacetech-vault-1 vault operator migrate --config=/vault/migrate.hcl
   ```

7. **Create a tarball of the Vault data:**

   ```bash
   docker exec -it spacetech-vault-1 sh -c "cd /vault && tar -czpvf  vaultd.tar.gz -C /vault/target/ ."
   ```

8. **Copy the tarball to the host machine:**

   ```bash
   docker cp spacetech-vault-1:/vault/vaultd.tar.gz .
   ```

9. **Get the full path of the copied tarball:**
   ```bash
   realpath vaultd.tar.gz
   ```

<SpacetechExampleInfo/>

10. **Get the unseal and root keys and save, you will use for unsealing the vault:**
    ```bash
    grep -A 7 "vault" projects/spacetech/generated-secret.yaml
    ```

#### Bastion Host

1. **Copy the vault data tar ball to the bastion host:**

   ```bash
   scp standalone-appcircle-server/app/appcircle-server/vaultd.tar.gz .
   ```

2. **Get the Vault statefulset name:**

   ```bash
   kubectl get statefulsets -n appcircle | grep vault
   ```

3. **Edit the vault `statefulset` for safe operations:**

   ```bash
   kubectl patch statefulset -n appcircle appcircle-server-vault -p '{"spec": {"template": {"spec":{"containers":[{"name":"vault","command": ["sh", "-c", "tail -f /dev/null" ], "args": null, "readinessProbe": null, "lifecycle": null  }]}}}}'
   ```

4. **Delete the pod for it to be re-created:**

   ```bash
   kubectl delete pod appcircle-server-vault-0 -n appcircle
   ```

5. **Copy the vault data to the target pod:**

   ```bash
   kubectl cp "./vaultd.tar.gz" "appcircle-server-vault-0:/vault/data/vaultd.tar.gz" -n appcircle
   ```

6. **Open shell in the vault container:**

   ```bash
   kubectl exec -it appcircle-server-vault-0 -- bash
   ```

7. **Run the following commands in the shell:**

   ```bash
   cd /vault/data
   tar -xzvf vaultd.tar.gz -C .
   /usr/local/bin/docker-entrypoint.sh vault server -config=/vault/config/extraconfig-from-values.hcl
   ```

8. **Don't close the upper terminal until the process finishes:**

9. **Open a new terminal in the vault container:**

   ```bash
   kubectl exec -it appcircle-server-vault-0 -- bash
   ```

10. **Unseal the vault with the saved keys from the steps above:**

    ```bash
    vault operator unseal dnaDMnwLuRni******M0EPJ2gAlyeHmOAy
    vault operator unseal FRTs/BO606ty******1nm9pJssLZjqVULR
    vault operator unseal f35t4MU6gojw******/bH92wR9t6MzzIYc
    ```

11. **Delete the vault data tar ball:**

    ```bash
    rm /vault/data/vaultd.tar.gz
    ```

12. **Exit from the first and second vault terminal:**

13. **Edit the secret with old unseal keys:**
    ```bash
    kubectl patch secret appcircle-server-vault-seal -n appcircle \
    --patch='{"stringData": { "token": "*hvs*.U5LLy********F2bOy", "unseal_keys": "dnaDMnwLuRni******M0EPJ2gAlyeHmOAy FRTs/BO606ty******1nm9pJssLZjqVULR f35t4MU6gojw******/bH92wR9t6MzzIYc" }}'
    ```

## Post-Migration Steps

After completing the migration, follow these steps to finalize and verify the setup:

### 1. Update the `values.yaml`

- **Remove Keycloak Replica Override:**  
  Delete the `replicas: 0` setting under `auth-keycloak`.

- **Remove MongoDB Resource Preset:**  
  Delete the `resourcesPreset` setting under `mongodb` if you don't need it.

### 2. Upgrade the Helm Release

Apply the updated `values.yaml` configuration to the Appcircle server Helm chart:

```bash
helm upgrade --install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

### 3. Update DNS Records

- **Shift DNS to the New Cluster:**  
  Update the DNS records to point to the new Appcircle Kubernetes cluster.

- **Redis Subdomain Change:**  
  Replace the `redis` subdomain from the standalone server (e.g., `redis.appcircle.spacetech.com`) with the `kvs` subdomain for Kubernetes (e.g., `kvs.appcircle.spacetech.com`).

- **Reference:**  
  For detailed instructions, see the [DNS Records Section](https://docs.appcircle.io/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes#1-add-dns-records).

### 4. Verification

- Test the following functionalities and ensure all data and features are operational post-migration.
  - **Builds**
  - **Publish**
  - **Enterprise App Store**
  - **Testing Distribution**
  - **LDAP / SSO Settings**

### 5. Clean Up

Once the migration has been confirmed as successful:

- Remove old Docker containers from the standalone Appcircle server.
- Delete any residual data no longer needed.
