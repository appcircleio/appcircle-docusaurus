---
title: External Image Registries
metaTitle: External Image Registries
metaDescription: External Image Registries Configurations
sidebar_position: 13
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

## Overview

In the Appcircle's containerized application ecosystem, users have the flexibility to access container images through various external image registries.

These external repositories serve as integral components, offering users different avenues to retrieve and manage container images based on their preferences and infrastructure requirements.

These services act as intermediaries, facilitating seamless image retrieval, caching frequently accessed images, and providing enhanced security measures for image distribution.

## Appcircle Configuration

For Appcircle server work with your own container image registry, you should add an additional setting to the `global.yaml` file of your project.

- Log in to Appcircle server with SSH or remote connection.

- Go to the `appcircle-server` directory.

- Edit the `global.yaml` file of your project.

:::info

The `spacetech` in the example codes below are example project name.

Please find your own project name and replace `spacetech` with your project name.

To see projects, you can check the `projects` directory.

```bash
ls -l ./projects
```

:::

```bash
vi ./projects/spacetech/global.yaml
```

- Find the `image` key. If it doesn't exists on the `global.yaml`, add it.

- The `image` key should be configured with your registry details:

  - url: Registry URL. (For our example, "registry.spacetech.com:8083/appcircle").
  - username: Username of the registry.
  - password: Password of the registry.
  - requiredLogin: If this variable is set to true, the script will use the username and password variables to login to the registry. If the end-user is logged in to his artifact registry manually, or the registry doesn't need auth, then this variable should be false.

```yaml
image:
  registry:
    url: registry.spacetech.com:8083/appcircle/docker-registry
    username: registryUsername
    password: superSecretPassword
    requiredLogin: true
```

## Mirroring Images

You can mirror Appcircle container images from the Google Artifact Registry to your local registry.

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

- If you are on the Appcircle server host, go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

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

If your registry is not using `https`, you may get an error during docker/podman push step.

You need to add your registry as an insecure registry. Please check the [Insecure Registries](#insecure-registries) section to configure an `http` registry.

:::

## Insecure Registries

<Tabs>
  <TabItem value="docker" label="Docker" default>

By default, Docker tries to connect to the server with `HTTPS` and from `443` port.

If your registry is running over `HTTP`, then you should define your registry as `insecure registry` to the Docker daemon.

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
If you don't specify the port number in the `daemon.json` above, Docker will try to use default `HTTP` port which is `80`.

If your registry runs on port other than `80`, you should specify it in the `daemon.json` file like in the example above.
:::

Restart the Docker daemon for the changes to take effect.

```bash
sudo systemctl restart docker
```

  </TabItem>

  <TabItem value="podman" label="Podman">

By default, Podman tries to connect to the server with `HTTPS` and from `443` port.

If your registry is running over `HTTP`, then you should define your registry as `insecure registry` in Podman configuration.

Edit the `registries.conf` file, whose default location is `/etc/containers/registries.conf`.

```bash
sudo vi /etc/containers/registries.conf
```

Copy the template content below, change the `location` with your registry URL and paste it bottom of the `registries.conf` file.

```conf
[[registry]]
location = "registry.spacetech.com:8083"
insecure = true
```

:::info
If you don't specify the port number in the `registries.conf` above, Podman will try to use default `HTTP` port which is `80`.

If your registry runs on port other than `80`, you should specify it in the `registries.conf` file like in the example above.
:::

  </TabItem>
</Tabs>

Now you can connect to your registry with `HTTP` without errors.

## Sonatype Nexus Registry Configuration

To use Sonatype Nexus as your proxy registry, you should follow the below steps.

- Create a new repository in Nexus with the type of `docker (proxy)`.
- Set the registry `name` and `port` as you wish.
- Set the `Remote Storage` as `https://europe-west1-docker.pkg.dev`.
- For the authentication section, you should set `Username` as `_json_key` and `Password` as the content of the `cred.json` file. See the sample screenshot [here.](https://cdn.appcircle.io/docs/assets/nexus-proxy-settings-3.png)
- For SSL, the recommended way is to use a reverse proxy in front of Nexus.

:::tip

You can see some sample screenshots below from Nexus UI for a sample configuration.

- [Proxy repository settings](https://cdn.appcircle.io/docs/assets/nexus-proxy-settings-1.png)
- [Remote storage settings](https://cdn.appcircle.io/docs/assets/nexus-proxy-settings-2.png)
- [Authentication settings](https://cdn.appcircle.io/docs/assets/nexus-proxy-settings-3.png)

:::

- After you created the repository, you should add the below section to the `global.yaml` file with your Nexus `repository url`, `username` and `password`.
- If you can access your Nexus repository without authentication, you should leave the `username` and `password` fields empty and set `requiredLogin` to `false`.

```yaml
image:
  registry:
    url: registry.spacetech.com:8083/appcircle/docker-registry
    username:
    password:
    requiredLogin: true
```

- For more detailed usage about the variables, you can check the [Appcircle Registry Configuration](#appcircle-configuration) section.

:::caution

In order to proxy Appcircle's registry from the Nexus registry, the **`registry.url`** in `global.yaml` must end with

- `/appcircle/docker-registry`

The example `global.yaml` section above is suitable with the example Nexus proxy registry settings shown in the screenshots above.

:::

:::info

If you face any issue about "manifest not found" when you try to run `./ac-self-hosted.sh -n "spacetech" up`, try pulling the images one by one from the Nexus proxy registry.

[Pulling Images On By One](#pulling-images-one-by-one) script below will force Nexus to pull the images from Appcircle's registry one by one, not in parallel.

Nexus has some issues when pulling images in parallel.

:::

## Pulling Images One By One

If you are having problems while pulling all the images in parallel, like happens in `Nexus`, you can use the script below to pull image one by one.

- You should create a bash script to pull images one by one.

```bash
vi pull-images.sh
```

- Then you should copy and paste the example script below into the `pull-images.sh` file.

<Tabs>
  <TabItem value="docker" label="Docker" default>

```bash
#!/bin/bash

# Don't change this.
SRC_REGISTRY_URL="europe-west1-docker.pkg.dev/appcircle/docker-registry"

# Set the proxy registry URL.
DEST_REGISTRY_URL="registry.spacetech.com:8083/appcircle/docker-registry"

sed -i "s|${SRC_REGISTRY_URL}|${DEST_REGISTRY_URL}|g" docker-images.txt

# Loop through each container image name and pull the container image.
while read -r IMAGE_NAME || [ -n "$IMAGE_NAME" ]; do
    if [[ ${IMAGE_NAME:0:1} == "#" ]]; then
        continue
    fi
    echo "Pulling image: $IMAGE_NAME"
    docker pull $IMAGE_NAME
    if [ $? -eq 0 ]; then
        echo "Image pulled successfully: $IMAGE_NAME"
    else
        echo "Failed to pull image: $IMAGE_NAME"
    fi
done < docker-images.txt

sed -i "s|${DEST_REGISTRY_URL}|${SRC_REGISTRY_URL}|g" docker-images.txt
```

  </TabItem>

  <TabItem value="podman" label="Podman">

```bash
#!/bin/bash

# Don't change this.
SRC_REGISTRY_URL="europe-west1-docker.pkg.dev/appcircle/docker-registry"

# Set the proxy registry URL.
DEST_REGISTRY_URL="registry.spacetech.com:8083/appcircle/docker-registry"

sed -i "s|${SRC_REGISTRY_URL}|${DEST_REGISTRY_URL}|g" docker-images.txt

# Loop through each container image name and pull the container image.
while read -r IMAGE_NAME || [ -n "$IMAGE_NAME" ]; do
    if [[ ${IMAGE_NAME:0:1} == "#" ]]; then
        continue
    fi
    echo "Pulling image: $IMAGE_NAME"
    podman pull $IMAGE_NAME
    if [ $? -eq 0 ]; then
        echo "Image pulled successfully: $IMAGE_NAME"
    else
        echo "Failed to pull image: $IMAGE_NAME"
    fi
done < docker-images.txt

sed -i "s|${DEST_REGISTRY_URL}|${SRC_REGISTRY_URL}|g" docker-images.txt
```

  </TabItem>

</Tabs>

:::info

You should replace the `DEST_REGISTRY_URL` variable as your needs.

Lets assume that the URL of your `Nexus` proxy registry is `registry.spacetech.com:8083` and your pull command without image name is `registry.spacetech.com:8083/appcircle/docker-registry`.

Then your `DEST_REGISTRY_URL` should be `registry.spacetech.com:8083/appcircle/docker-registry`.

:::

- Set the script permissions.

```bash
chmod +x pull-images.sh
```

- Pull the images one by one.

```bash
./pull-images.sh
```
