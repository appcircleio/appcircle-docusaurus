---
title: External Image Registries
description: Learn how to configure external image registries in Appcircle
tags: [self-hosted, external image registry, registry, quay, mirror images, insecure registry, pull images one by one]
sidebar_position: 110
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Overview

In the Appcircle's orchestrated application ecosystem, users have the flexibility to access container images through various external image registries.

These external repositories serve as integral components, offering users different avenues to retrieve and manage container images based on their preferences and infrastructure requirements.

These services act as intermediaries, facilitating seamless image retrieval, caching frequently accessed images, and providing enhanced security measures for image distribution.

## Appcircle Registry Configuration

For the Appcircle server to work with your own container image registry, you should add an additional setting to the `values.yaml` file of your deployment.

:::info

In this documentation, we will use `registry.spacetech.com` as an __example registry domain__, spacetech as an __example organization name__ and `appcircle` as __example namespace name__.

To see name and namespace of your existing helm deployments, you can use the command below.

```bash
helm list --all-namespaces
```

:::

- Find the `imageRegistry` and `imageRepositoryPath` keys in your `values.yaml`. If they don't exist, you should add them.

```yaml
  # Container Image Registry host for container images
  imageRegistry: registry.spacetech.com:8083
  # Container Image Repository path between registry host and image name
  imageRepositoryPath: appcircle/docker-registry
```

- Then create a secret with credentials for the external registry.

```bash
oc create secret docker-registry containerregistry \
  -n appcircle \
  --docker-server='registry.spacetech.com:8083' \
  --docker-username='yourRegistryUsername' \
  --docker-password='superSecretRegistryPassword'
```

- To apply changes, run the command below.

```bash
helm upgrade appcircle-server appcircle/appcircle \
  -n appcircle \
  -f values.yaml
```

## Quay Configuration

Red Hat Quay provides a robust container registry solution that integrates well with Kubernetes and OpenShift environments. To configure Quay as your proxy registry, follow these steps:

- Create a new organization in Quay (e.g., appcircle)

- Create a robot account for authentication:

  - Go to your organization → Robot Accounts → Create Robot Account
  - Name it (e.g., appcircle-puller)
  - Grant appropriate permissions (typically read access)
  - Save the credentials securely and use them while creating the `containerregistry` secret. See the [Appcircle Registry Configuration](#appcircle-registry-configuration) section for more details.

## Using Quay Repository Mirroring

You can create mirror images in Quay and sync them with Appcircle registry. See detailed instructions in the [Quay Repository Mirroring documentation](https://docs.redhat.com/en/documentation/red_hat_quay/3/html/manage_red_hat_quay/repo-mirroring-in-red-hat-quay).

<!-- TODO: Add script to create mirror images automatically using Quay API. -->

## Mirroring Images Manually

<!--  You can mirror Appcircle container images from the Google Artifact Registry to your local registry.

Since there are many images to mirror, you can use a bash script to mirror the images instead of pulling, re-tagging, and pushing them back to your local registry.

To mirror images automatically, you can follow the steps below:

As a **pre-requirement**, you need to be authenticated to the Google Artifact Registry.

- You should already have a `cred.json` file, which you should have taken from us.

To authenticate with your container engine, run the command below:

<Tabs>
  <TabItem value="docker" label="Docker" default>

```bash
cat cred.json | docker login -u _json_key --password-stdin  europe-west1-docker.pkg.dev/appcircle/docker-registry
```

  </TabItem>

  <TabItem value="podman" label="Podman">

```bash
cat cred.json | podman login -u _json_key --password-stdin  europe-west1-docker.pkg.dev/appcircle/docker-registry
```

  </TabItem>
</Tabs>

You should see the "Login Succeeded" message after the command execution.

You can find all container images in the `docker-images.txt` file, which is in the Appcircle server package.

- Create the `docker-images.txt` file and copy the following image names into it.

```bash
vi docker-images.txt
```

```bash

```

```bash

- Create a bash script to mirror the container images.

```bash
vi mirror-images.sh
```

- Copy and paste the following code into the bash script:

<Tabs>
  <TabItem value="docker" label="Docker" default>

```bash
#!/bin/bash

# Set the source registry URL
SRC_REGISTRY_URL="europe-west1-docker.pkg.dev/appcircle/docker-registry"

# Set the destination registry URL
DEST_REGISTRY_URL="registry.spacetech.com:8083/appcircle"

# Loop through each line of the file and pull, tag, and push the Docker image
while read -r IMAGE_NAME || [ -n "$IMAGE_NAME" ]; do
    if [[ ${IMAGE_NAME:0:1} == "#" ]]; then
        continue
    fi
    echo "Pulling image: $IMAGE_NAME"
    docker pull $IMAGE_NAME
    if [ $? -eq 0 ]; then
        echo "Image pulled successfully: $IMAGE_NAME"
        # Replace source registry URL  with the new registry URL
        IMAGE_TAG="${IMAGE_NAME/$SRC_REGISTRY_URL/$DEST_REGISTRY_URL}"
        # Tag the image with the destination registry URL and repository name
        docker tag $IMAGE_NAME $IMAGE_TAG
        # Push the tagged image to the destination registry
        docker push $IMAGE_TAG
        if [ $? -eq 0 ]; then
            echo "Image pushed successfully: $IMAGE_NAME"
        else
            echo "Failed to push image: $IMAGE_NAME"
        fi
    else
        echo "Failed to pull image: $IMAGE_NAME"
    fi
done < docker-images.txt
```

  </TabItem>

  <TabItem value="podman" label="Podman">

```bash
#!/bin/bash

# Set the source registry URL
SRC_REGISTRY_URL="europe-west1-docker.pkg.dev/appcircle/docker-registry"

# Set the destination registry URL
DEST_REGISTRY_URL="registry.spacetech.com:8083/appcircle"

# Loop through each line of the file and pull, tag, and push the Docker image
while read -r IMAGE_NAME || [ -n "$IMAGE_NAME" ]; do
    if [[ ${IMAGE_NAME:0:1} == "#" ]]; then
        continue
    fi
    echo "Pulling image: $IMAGE_NAME"
    podman pull $IMAGE_NAME
    if [ $? -eq 0 ]; then
        echo "Image pulled successfully: $IMAGE_NAME"
        # Replace source registry URL  with the new registry URL
        IMAGE_TAG="${IMAGE_NAME/$SRC_REGISTRY_URL/$DEST_REGISTRY_URL}"
        # Tag the image with the destination registry URL and repository name
        podman tag $IMAGE_NAME $IMAGE_TAG
        # Push the tagged image to the destination registry
        podman push $IMAGE_TAG
        if [ $? -eq 0 ]; then
            echo "Image pushed successfully: $IMAGE_NAME"
        else
            echo "Failed to push image: $IMAGE_NAME"
        fi
    else
        echo "Failed to pull image: $IMAGE_NAME"
    fi
done < docker-images.txt
```

  </TabItem>
</Tabs>

:::caution
The sample value for **`DEST_REGISTRY_URL`** in the script above must be changed with your container image registry.

To find your destination registry URL, please head to your external image registry and check for pull/push command.

For example, if you're using

- `registry.spacetech.com:8083/appcircle/imagename:latest`

template for pull/push, the destination registry URL (**`DEST_REGISTRY_URL`**) should be

- `registry.spacetech.com:8083/appcircle`

Keep in mind that the destination image registry url **must not** end with `/`.
:::

- Make the `mirror-images.sh` script file executable.

```bash
chmod +x mirror-images.sh
```

- Run the script to mirror all the container images.

```bash
./mirror-images.sh
```

:::info

If your registry is not using HTTPS, you may get an error during the Docker/Podman push step.

You need to add your registry as an insecure registry. Please check the [Insecure Registry](#insecure-registry) section to configure an HTTP registry.

::: -->

## Insecure Registry

To use a registry with HTTP, you need to introduce your registry to both container engines (Docker, Podman) and orchestration tools (Kubernetes, OpenShift) as an insecure registry.

### 1. Insecure Registry for Docker and Podman

<Tabs>
  <TabItem value="docker" label="Docker" default>

By default, Docker tries to connect to the server with HTTPS and from the `443` port.

If your registry is running over HTTP, then you should define your registry as an **insecure registry** in the Docker daemon.

Edit the `daemon.json` file, whose default location is `/etc/docker/daemon.json`.

```bash
sudo vi /etc/docker/daemon.json
```

If the `daemon.json` file does not exist, you should create it. Assuming there are no other settings in the file, it should have the following contents:

```json
{
  "insecure-registries": ["registry.spacetech.com:8083"]
}
```

:::info
If you don't specify the port number in the `daemon.json` above, Docker will try to use the default HTTP port, which is `80`.

If your registry runs on a port other than `80`, you must specify it in the `daemon.json` file, like in the example above.
:::

Restart the Docker daemon for the changes to take effect.

```bash
sudo systemctl restart docker
```

  </TabItem>

  <TabItem value="podman" label="Podman">

By default, Podman tries to connect to the server with HTTPS and from the `443` port.

If your registry is running over HTTP, then you should define your registry as an **insecure registry** in the Podman configuration.

Edit the `registries.conf` file, whose default location is `/etc/containers/registries.conf`.

```bash
sudo vi /etc/containers/registries.conf
```

Copy the template content below, change the `location` to your registry URL, and paste it at the bottom of the `registries.conf` file.

```conf
[[registry]]
location = "registry.spacetech.com:8083"
insecure = true
```

:::info
If you don't specify the port number in the `registries.conf` above, Podman will try to use the default HTTP port, which is `80`.

If your registry runs on a port other than `80`, you must specify it in the `registries.conf` file, like in the example above.
:::

  </TabItem>
</Tabs>

Now you can connect to your registry with HTTP without any errors.

### 2. Insecure Registry for Kubernetes and OpenShift

Edit the `image.config` file to add your insecure registry.

```bash
oc edit image.config cluster
```

Add your registry address to the `insecureRegistries` section as shown below.

```yaml
...
spec:
...
  registrySources:
    insecureRegistries:
    - registry.spacetech.com:8083"
...
```

Then save file and exit.
