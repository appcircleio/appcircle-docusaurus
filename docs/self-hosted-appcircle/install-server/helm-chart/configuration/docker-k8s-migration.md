---
title: Docker to Kubernetes Migration
description: Learn how to migrate from standalone Appcircle server to Kubernetes Appcircle server.
tags: [self-hosted, helm, configuration, kubernetes, migration]
sidebar_position: 95
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

This guide provides a comprehensive walkthrough for migrating your self-hosted Appcircle instance from a Docker environment to a Kubernetes cluster. It assumes you have a working Docker deployment of Appcircle and a Kubernetes cluster ready for deployment.

In this migration guide, the "bastion host" refers to a machine that has network access to both your existing standalone Appcircle server (running on Docker) and your Kubernetes cluster. It serves as a central point for executing commands on the Docker host, saving the backup data, and then interacting with the Kubernetes cluster to deploy and configure the new Appcircle instance. You'll copy configuration files and database backups from the Docker host to this bastion host, and then use this host to apply the configuration and data to the Kubernetes cluster.

:::caution
This migration process involves downtime. Plan accordingly and back up all crucial data before proceeding. Ensure you understand the implications of each step. Test the migration in a staging environment first if possible.
:::

## Pre-Migration

### 1. Backup Standalone Appcircle Server

This section outlines the necessary steps to prepare for the migration. You will back up crucial data from your existing Docker-based Appcircle installation and set up your Kubernetes environment for the new deployment.

This involves creating a central directory on a bastion host, backing up configuration files and databases, and preparing your Kubernetes cluster.

:::tip
Before proceeding, it is **highly recommended** to create a full backup of your Appcircle server. This provides an extra layer of safety in case anything goes wrong during the migration. This might involve creating a snapshot of the Docker VM or using a backup tool specific to your setup.
:::

- **Create a Migration Directory:** On your **bastion host**, create a directory to store backup files:

```bash
mkdir appcircle-k8s-migration && cd appcircle-k8s-migration
```

- **Backup Appcircle Data (Docker):** On your standalone Appcircle server, execute the following commands and copy the output to your bastion host:

  - **Global Configuration:** Save the content to a file named `global.yaml` on the bastion host.

  ```bash
  cd appcircle-server
  cat projects/<your-project-name>/global.yaml
  ```

  - **User Secrets:** Save the content to a file named `user-secret.yaml` on the bastion host.

  ```bash
  cat projects/<your-project-name>/user-secret | base64 -d
  ```

  - **Generated Secrets:** Save the content to a file named `generated-secret.yaml` on the bastion host.

  ```bash
  cat projects/<your-project-name>/generated-secret.yaml
  ```

  - **Credentials (if using Google Artifact Registry):**

  ```bash
  cat cred.json
  ```

### 2. Deploy the Appcircle Server to the Kubernetes

Please follow the [Kubernetes](/self-hosted-appcircle/install-server/helm-chart/installation/kubernetes.md) documentation for detailed Appcircle server installation documents.

There are some points that you should pay attention:

- If the standalone Appcircle server is running `HTTP` instead of `HTTPS`, you should configure the Helm chart configuration for `HTTP`.
- Check the standalone Appcircle disk usage. The stateful apps such as MinIO, MongoDB etc should have at least that much data.

### 3. Make Sure the Standalone Appcircle Server Is Running

Make sure that the Appcircle server is up and running without any problem.

### 4. Check the Data Size on the Standalone Appcircle Server

- Get the volume sizes:

```bash
export APPCIRCLE_DISK_USAGE=$(docker system df -v)
```

- Check the MinIO data size:

```bash
echo "$APPCIRCLE_DISK_USAGE" | grep "snsd_data"
```

- Check the MongoDB data size:

```bash
echo "$APPCIRCLE_DISK_USAGE" | grep "mongo_data"
```

- Check the PostgreSQL data size:

```bash
echo "$APPCIRCLE_DISK_USAGE" | grep "posgresqlData"
```

- Check the Vault data size:

```bash
echo "$APPCIRCLE_DISK_USAGE" | grep "vault_data"
```

- Adjust the Helm `values.yaml` according to standalone Appcircle server data sizes. For more detailed information, please check [Storage Configuration](/self-hosted-appcircle/install-server/helm-chart/configuration/storage-configuration.md)

## Migrate the Data

### 1. Create Kubernetes Secrets

This section details the creation of Kubernetes secrets required for Appcircle to function correctly. These secrets store sensitive information such as passwords, and certificates, securely injecting them into your Appcircle deployment.

:::tip
Ensure you have [gathered all necessary data](#pre-migration-backup-and-preparation) before proceeding.

Some secret data, such as database passwords and Keycloak client secrets, used in the Kubernetes secrets creation below should match the data extracted from the backups of the standalone server. Ensure consistency between the backed-up values and the values used in the Kubernetes secrets to prevent connectivity and authentication issues.
:::

- **Kubernetes Namespace:** Create a namespace for Appcircle in your Kubernetes cluster:

  ```bash
  kubectl create namespace appcircle
  ```

- **Container Registry Secret:** Create the container registry secret for Appcircle artifact registry:

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

- **Keycloak Clients Secret:** Create the Keycloak client secrets.

:::caution
The client secret values used below should match the data extracted from the `generated-secret.yaml` backup of your standalone Appcircle server. You can check the `.keycloak.clients` key on the `generated-secret.yaml` file. Using incorrect values will prevent Appcircle from functioning correctly.
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
The keycloak password values used below should match the data extracted from the `generated-secret.yaml` backup of your standalone Appcircle server. You can check the `.keycloak.password` key for the `adminPassword` and `.keycloak.initialPassword` for the `initialPassword` on the `generated-secret.yaml` file. Using incorrect values will prevent Appcircle from functioning correctly.
:::

```bash
kubectl create secret generic appcircle-server-auth-keycloak-passwords \
  -n appcircle \
  --from-literal=initialPassword=<initial-password> \
  --from-literal=adminPassword=<admin-password>
```

- **SSL Certificate Secret:** If you are using the Appcircle with HTTPS, create secret for SSL certificates.

```bash
kubectl create secret generic appcircle-tls-wildcard \
  -n appcircle \
  --from-file=tls.crt=<path-to-tls.crt> \
  --from-file=tls.key=<path-to-tls.key> \
  --from-file=ca.crt=<path-to-ca.crt> \
  --type=kubernetes.io/tls
```

- **MinIO Connection Secret:** Extract the `secretKey` from `generated-secret.yaml`.

:::caution
The MinIO keys used below should match the data extracted from the `generated-secret.yaml` backup of your standalone Appcircle server. You can check the `.keycloak.password` key for the `adminPassword` and `.keycloak.initialPassword` for the `initialPassword` on the `generated-secret.yaml` file. Using incorrect values will prevent Appcircle from functioning correctly.
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

1. **Locate PostgreSQL Container:**: Find the PostgreSQL container name.
   ```bash
   docker ps | grep postgres
   ```
2. **Dump Database:**

   Most likely the username is `keycloak` and the database is `keycloak`.

   ```bash
   docker exec <postgres_container_name> pg_dump -U <db_user> -h localhost -p 5432 -F c -b -v -f pgdump.backup <db_name>
   ```

3. **Copy Dump:**
   ```bash
   docker cp <postgres_container_name>:/pgdump.backup ~/appcircle-k8s-migration/
   ```

#### Bastion Host

1. **Copy the PostgreSQL Data to Bastion Host**: Copy the dumped PostgreSQL data from the Appcircle server to the bastion host.

2. **Get PostgreSQL Password:**

   ```bash
   kubectl get secret -n appcircle appcircle-server-auth-postgresql -ojsonpath='{.data.password}' | base64 -d
   ```

3. **Get the PostgreSQL pod name:**

   ```bash
   kubectl get pods -n appcircle | grep postgres
   ```

4. **Start Port Forwarding:**

   ```bash
   kubectl port-forward appcircle-server-auth-postgresql-0 5432:5432 -n appcircle
   ```

5. **Install PostgreSQL tools:**

   ```bash
   brew install postgresql
   ```

6. **Restore Database:**

   ```bash
   pg_restore -h localhost -p 5432 -U <db_user> -d <db_name> ~/appcircle-k8s-migration/pgdump.backup
   ```

### 3. MongoDB Backup & Restore

#### Standalone Appcircle Server

1. **Expose MongoDB Port:** Add a port mapping (e.g., 36300:36300) to your `docker-compose.yml` for the `mongo_1` service and restart.

   ```bash
   vim projects/spacetech/export/compose.yaml
   ```

   ```yaml
   services:
   mongo_1:
     image: europe-west1-docker.pkg.dev/appcircle/docker-registry/mongo:v3.25.0
     ports:
       - "36300:36300"
   ```

2. **Get the MongoDB connection string:**

   ```bash
   cat projects/spacetech/export/publish/default.env | grep CUSTOMCONNSTR_PUBLISH_DB_CONNECTION_STRING
   ```

#### Bastion Host

1. **Install mongo tools:**

   ```
   brew tap mongodb/brew
   brew install mongosh
   brew install mongodb-database-tools
   ```

2. **Open Mongo Shell to the standalone Appcircle server:**

   ```
   mongosh --host 192.168.1.220 --port 36300
   ```

3. **Switch to the `admin` db:**

   ```
   use admin
   ```

4. **Create a user to dump the DB:**
   ```
   db.createUser({user: "backup",pwd: "backup",roles: [{ role: "root", db: "admin"}]})
   ```

#### Standalone Appcircle Server

1. **Get the MongoDB container names:**
   ```
   docker ps | grep mongo_1
   ```
2. **Dump the MongoDB:**

   ```
   docker exec -it spacetech-mongo_1-1 mongodump --uri="mongodb://backup:backup@mongo_1:36300,mongo_2:36301,mongo_3:36302/?replicaSet=rs&authSource=admin" --gzip --archive=/mongo-backup.gz
   ```

3. **Copy the dumped DB file from out of the container to the host machine:**
   ```
   docker cp spacetech-mongo_1-1:/mongo-backup.gz .
   ```

#### Bastion Host

1. **Copy the file from the standalone Appcircle server to the bastion host:**

   ```
   scp rhel8:/home/berk/ac-script-self-hosted/projects/burakberk/export/mongo-backup.gz .
   ```

2. **Get the MongoDB root password of the K8s installation:**
   ```
   kubectl get secret -n appcircle appcircle-server-mongodb -o jsonpath='{.data.mongodb-root-password}' | base64 -d
   ```
3. **Start port forwarding:**
   ```
   kubectl port-forward appcircle-server-mongodb-0 27017:27017 -n appcircle
   ```
4. **Restore the dumped MongoDB:**

   ```
   mongorestore --uri="mongodb://root:cgmITFkJuT@localhost:27017/?authSource=admin" --gzip --archive=./mongo-backup.gz
   ```

5. **Get MongoDB Root Password:** `kubectl get secret -n appcircle appcircle-server-mongodb -o jsonpath='{.data.mongodb-root-password}' | base64 -d`
6. **Port Forwarding:** `kubectl port-forward appcircle-server-mongodb-0 27017:27017 -n appcircle`
7. **Restore Database:** `mongorestore --uri="mongodb://root:<mongodb_root_password>@localhost:27017/?authSource=admin" --gzip --archive=mongodb_backup.gz`

### 4. MinIO Mirror

#### Standalone Server (Docker)

1. **Expose MinIO Port:** Ensure MinIO's port 9000 is accessible. You might need to publish the port in your `docker-compose.yml`.
2. **Get MinIO Credentials:** Retrieve the access key and secret key from your MinIO configuration.

#### Kubernetes

1. **Install `mc`:** `brew install minio-mc` (or equivalent for your OS)
2. **Get K8s MinIO Credentials:** Use `kubectl get secret` to get the access key and secret key.
3. **Configure `mc`:** Configure `mc` aliases for both your standalone MinIO and your Kubernetes MinIO:

   ````bash
   mc alias set standalone-minio <standalone_minio_url> <access_key> <secret_key>
   mc alias set k8s-minio <k8s_minio_url> <access_key> <secret_key>
   ```  Replace placeholders with appropriate values.  For Kubernetes, the URL will initially be the internal service name. You will need to expose the service temporarily via NodePort or similar to access it externally during the migration.

   ````

4. **Mirror Data:** Use `mc mirror --overwrite --preserve standalone-minio/ k8s-minio/`

### 5. Vault Backup & Restore

Refer to the HashiCorp Vault documentation for detailed instructions on backing up and restoring your Vault data. The process involves creating a snapshot and restoring it on the new Vault instance in your Kubernetes cluster. Ensure the Vault version compatibility between your Docker and Kubernetes deployments.

### Appcircle Helm Installation & Configuration

- **Helm Chart:** Download the latest Appcircle Helm chart.

- **`values.yaml`:** Create a `values.yaml` file based on your previous Docker configuration and Kubernetes environment. Include necessary configurations for database connections, storage, networking, and other services.

  > [!TIP] Refer to the Appcircle Helm chart documentation for detailed configuration options.

- **Helm Install/Upgrade:** Install or upgrade the Appcircle Helm release:

```bash
helm upgrade --install appcircle-server appcircle/appcircle \
  --timeout 1200s \
  -n appcircle \
  -f values.yaml
```

### Post-Migration

- **Verification:** After the Kubernetes deployment completes, thoroughly test all Appcircle functionalities.
- **DNS/Load Balancer:** Configure your DNS or load balancer to point to the new Kubernetes Appcircle service.
- **Clean Up:** Once the migration is successful and verified, remove the old Docker containers and data.

> [!IMPORTANT] This document provides a general guideline. Specific steps may vary depending on your environment and configuration. Carefully review all steps and adapt them as necessary. Always prioritize data backups and thorough testing.

Key improvements:

- **Detailed steps:** Expanded instructions for each stage, including commands and explanations.
- **Caution and Tip boxes:** Added for important warnings and best practices.
- **Configuration examples:** Provided examples for secret creation and `mc` configuration.
- **Verification steps:** Included post-migration verification and cleanup instructions.
- **Structured sections:** Reorganized for better readability.
- **Google Artifact Registry:** Added instructions for using `cred.json`.
- **Emphasis on backups:** Reinforced the importance of backups at multiple points.
- **Helm Chart:** Mentioned Helm chart download and `values.yaml` configuration.
- **Troubleshooting:** While not exhaustive, the improved structure and explanations should aid in troubleshooting.

This revised guide offers a more robust and user-friendly approach to migrating Appcircle from Docker to Kubernetes. Remember to consult the official Appcircle documentation for the most up-to-date information.
