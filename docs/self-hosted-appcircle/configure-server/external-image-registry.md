---
title: External Image Registries
metaTitle: External Image Registries
metaDescription: External Image Registries Configurations
sidebar_position: 13
---

## Overview

In the Appcircle's containerized application ecosystem, users have the flexibility to access container images through various external image registries.

These external repositories serve as integral components, offering users different avenues to retrieve and manage container images based on their preferences and infrastructure requirements.

These services act as intermediaries, facilitating seamless image retrieval, caching frequently accessed images, and providing enhanced security measures for image distribution.

## Mirroring Images

You can mirror Appcircle container images from the Google Artifact Registry to your local registry.

Since there are many images to mirror, you can use a bash script to mirror the images instead of pulling, re-tagging and pushing back to your local registry.

To mirror images automatically, you can use the steps below:

- As a pre-requirement, you need to be authenticated to the Google Artifact Registry.

  - You should already have a `cred.json` file which you should have take from us.

  - To auth with Docker, run the command below:

```bash
cat cred.json | docker login -u _json_key --password-stdin  europe-west1-docker.pkg.dev/appcircle/docker-registry
```

You should see Login Succeeded message.

- You can find the all images names in the `docker-images.txt` file which is in the Appcircle server package.

- If you are in the Appcircle server machine, go to the `appcircle-server` directory to find `docker-images.txt` file.

```bash
cd appcircle-server
```

- Create a bash script to mirror the images.

```bash
vi mirror-images.sh
```

- Copy and paste the following code into the script.

```bash
#!/bin/bash

# Set the source registry URL
SRC_REGISTRY_URL="europe-west1-docker.pkg.dev/appcircle/docker-registry"

# Set the destination registry URL
DEST_REGISTRY_URL="reg.appcircle.spacetech.com/appcircle"

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

:::caution
`DEST_REGISTRY_URL` should be update in the script above.

To find your destination registry URL, please head to your external image registry and check for pull/push command.

If the `reg.appcircle.spacetech.com/appcircle/imagename:latest`, the destination registry URL is `reg.appcircle.spacetech.com/appcircle`.

Destination image registry url **mustn't** end with `/`.
:::

- Make the `mirror-images.sh` file executable.

```bash
chmod +x mirror-images.sh
```

- Run the script to mirror all images.

```bash
./mirror-images.sh
```

:::info

If your registry is not using `https`, you may get an error during docker push step. You need to add your registry as insecure registry.

Please check [Insecure Registries](#insecure-registries) section to configure a `http` registry.

:::

## Insecure Registries

### Docker Insecure Registry

Edit the `daemon.json` file, whose default location is `/etc/docker/daemon.json` on Linux.

If the daemon.json file does not exist, create it. Assuming there are no other settings in the file, it should have the following contents:

```json
{
  "insecure-registries": ["http://reg.appcircle.spacetech.com"]
}
```

### Podman Insecure Registry

Edit the `registries.conf` file, whose default location is `/etc/containers/registries.conf` on Linux.

The `registries.conf` file should contain your `http` registry.

```conf
... Some other configurations ...
[[registry]]
location = "reg.appcircle.spacetech.com"
insecure = true
```

## Sonatype Nexus Registry Configuration

To use Sonatype Nexus as your proxy registry, you should follow the below steps.

- Create a new repository in Nexus with the type of `docker (proxy)`.
- Set the `Registry Name` name and `port` as you wish.
- Set the `Remote Storage` as `https://europe-west1-docker.pkg.dev`.
- For the authentication section, you should set `Username` as `_json_key` and `Password` as the content of the `cred.json` file. See the sample screenshot [here.](https://cdn.appcircle.io/docs/assets/nexus-proxy-settings-3.png)
- For SSL, the recommended way is to use a reverse proxy in front of Nexus.
- After you created the repository, you should add the below section to the `global.yaml` file with your Nexus `repository url`, `username` and `password`.
- If you can access your Nexus repository without authentication, you should leave the `username` and `password` fields empty and set `requiredLogin` to `false`.

```yaml
image:
  registry:
    url: reg.appcircle.spacetech.com:8443/appcircle/docker-registry
    username:
    password:
    requiredLogin: true
```

:::caution

In order to proxy Appcircle's registry, the repository url in `global.yaml` must end with `/appcircle/docker-registry`.

:::

:::tip

You can see some example configuration screenshots below for Nexus UI.

- [Proxy repository settings](https://cdn.appcircle.io/docs/assets/nexus-proxy-settings-1.png)
- [Remote storage settings](https://cdn.appcircle.io/docs/assets/nexus-proxy-settings-2.png)
- [Authentication settings](https://cdn.appcircle.io/docs/assets/nexus-proxy-settings-3.png)

:::

:::info

If you face any issue about "manifest not found" when you try to run `./ac-self-hosted.sh -n "spacetech" up`, try pulling the images one by one from Nexus proxy registry.

By looking at the [Pulling Images On By One](#pulling-images-on-by-one) script below, you can pull images from the proxy repository with it. This will force Nexus to pull the images from Appcircle's registry one by one, not in parallel.

Nexus have some issues when pulling images in parallel.

:::

## Pulling Images One By One

If you are having problems while pulling all the images in parallel, like happens in `Nexus`, you can use the script below to pull image one by one.

- Lets assume that the URL of your `Nexus` registry is `reg.appcircle.spacetech.com:8443` and your pull command without image name is `reg.appcircle.spacetech.com:8443/appcircle/docker-registry`.

- You should change

```bash
#!/bin/bash

# Don't change this.
SRC_REGISTRY_URL="europe-west1-docker.pkg.dev/appcircle/docker-registry"

# Set the destination registry URL
DEST_REGISTRY_URL="reg.appcircle.spacetech.com/appcircle"

sed -i "s|${SRC_REGISTRY_URL}|${DEST_REGISTRY_URL}|g" docker-images.txt

# Loop through each line of the file and pull, tag, and push the Docker image
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

## Appcircle Configuration

For Appcircle server work with your own container image registry, you should also add an additional setting to the `global.yaml` file of your project.

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

  - url: Registry URL. (For our example, "reg.appcircle.spacetech.com/appcircle").
  - username: Username of the registry.
  - password: Password of the registry.
  - requiredLogin: If this variable is set to true, the script will use the username and password variables to login to the registry. If the end-user is logged in to his artifact registry manually, or the registry doesn't need auth, then this variable should be false.

```yaml
image:
  registry:
    url: reg.appcircle.spacetech.com/appcircle
    username: registryUsername
    password: superSecretPassword
    requiredLogin: true
```
