---
title: Git Providers
description: Configure git providers in self-hosted Appcircle
tags: [self-hosted, git providers, configuration, gitlab, azure, bitbucket, github]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/_spacetech-example-info.mdx';

With default installation, self-hosted Appcircle comes with the connection options below:

- Bitbucket
- Azure
- GitLab
- GitHub
- Connect via SSH
- Connect via URL

<Screenshot
  url="https://cdn.appcircle.io/docs/assets/BE-6543-git-providers.png"
  alt="Select the Git provider for the source code of your app"
/>

You can configure the Git providers and use them within your self-hosted Appcircle server, the same as in the cloud.

The following sections will give you more details about how to enable or disable Git providers according to your requirements in your hosted environment.

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](/self-hosted-appcircle/install-server/linux-package/installation/docker#3-configure) section in docs, understood configuration made there and scenarios told there.

:::

:::caution

Current working directory is assumed `appcircle-server` for following steps. See [here](/self-hosted-appcircle/install-server/linux-package/installation/docker#1-download) for installation details.

:::

:::caution

`global.yaml` configuration file is located under **project** folder.

- `projects/${YOUR_PROJECT}`

You can see an example project configuration from [here](/self-hosted-appcircle/install-server/linux-package/installation/docker#3-configure).

:::

## Connect to Bitbucket

To disable the "Bitbucket" option, add the below configuration to `global.yaml`.

```yaml
build:
  oauths:
    bitbucket:
      enabled: false
    bitbucketServer:
      enabled: false
```

If you want to re-enable "Bitbucket" again, you can set the `enabled` to `true`.

You can configure only the self-hosted or cloud "Bitbucket" options using the relevant keys.

- The `bitbucket` key is used to manage **Bitbucket (Cloud)**.
- The `bitbucketServer` key is used to manage **Bitbucket Server**.

For more details about "Bitbucket" usage, see related docs in the [Connecting to Bitbucket](/build/manage-the-connections/adding-a-build-profile/connecting-to-bitbucket) page.

To apply the changes, please follow the [Applying Git Provider Changes](#applying-git-provider-changes) section at the end.

## Connect to Azure DevOps

To disable the "Azure DevOps" option, add the below configuration to `global.yaml`.

```yaml
build:
  oauths:
    azureDevopsServices:
      enabled: false
    azureDevopsServer:
      enabled: false
```

If you want to re-enable "Azure DevOps" again, you can set the `enabled` to `true`.

You can configure only the self-hosted or cloud "Azure DevOps" options using the relevant keys.

- The `azureDevopsServices` key is used to manage **Azure DevOps Services (Cloud)**.
- The `azureDevopsServer` key is used to manage **Azure DevOps Server**.

For more details about "Azure DevOps" usage, see related docs in the [Connecting to Azure DevOps](/build/manage-the-connections/adding-a-build-profile/connecting-to-azure) page.

To apply the changes, please follow the [Applying Git Provider Changes](#applying-git-provider-changes) section at the end.

## Connect to GitLab

To disable the "GitLab" option, add the below configuration to `global.yaml`.

```yaml
build:
  oauths:
    gitlab:
      enabled: false
    gitlabSelfHosted:
      enabled: false
```

If you want to re-enable "GitLab" again, you can set the `enabled` to `true`.

You can configure only the self-hosted or cloud "GitLab" options using the relevant keys.

- The `gitlab` key is used to manage **GitLab (Cloud)**.
- The `gitlabSelfHosted` key is used to manage **GitLab Self-Managed**.

For more details about "GitLab" usage, see related docs in the [Connecting to GitLab](/build/manage-the-connections/adding-a-build-profile/connecting-to-gitlab) page.

To apply the changes, please follow the [Applying Git Provider Changes](#applying-git-provider-changes) section at the end.

## Connect to GitHub

To disable the "GitHub" option, add the below configuration to `global.yaml`.

```yaml
build:
  oauths:
    githubApp:
      enabled: false
    githubEnterpriseServer:
      enabled: false
```

If you want to re-enable "GitHub" again, you can set the `enabled` to `true`.

You can configure only the self-hosted or cloud "GitHub" options using the relevant keys.

- The `githubApp` key is used to manage **GitHub (Cloud)**.
- The `githubEnterpriseServer` key is used to manage **GitHub Enterprise Server**.

For more details about "GitHub" usage, see related docs in the [Connecting to GitHub](/build/manage-the-connections/adding-a-build-profile/connecting-to-github) page.

To apply the changes, please follow the [Applying Git Provider Changes](#applying-git-provider-changes) section at the end.

:::info
GitHub Enterprise Server option is available in version `3.28.2` or later.
:::

### GitHub App Cloud

The [GitHub App](https://docs.github.com/en/apps/using-github-apps/about-using-github-apps) option is `disabled` by default since it needs further custom configuration for your setup.

If you want to connect to GitHub Cloud using the GitHub App, you need to **[create your own GitHub App](https://docs.github.com/en/apps/creating-github-apps/about-creating-github-apps/about-creating-github-apps)** for your organization. Below are the key points that you should follow while creating a GitHub App for your Appcircle server.

#### Requirements

:::info
"GitHub App Cloud `OAuth2`" connection option is available in version `3.29.3` or later.
:::

While creating your own GitHub App, you will need some domains from the Appcircle server for URLs. Therefore, before beginning, you should have been gotten the below domains ready for your GitHub App configuration.

- Log in to the Appcircle server with SSH or a remote connection.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

<SpacetechExampleInfo />

- Update the environment variable `PATH` with the required dependencies.

```bash
export PATH=$PATH:$(pwd)/deps/bin
```

:::info
URL samples in the following steps are based on sample [DNS settings](/self-hosted-appcircle/install-server/linux-package/installation/docker#4-dns-settings) from the Appcircle server installation.
:::

**1.** Get **dashboard** URL.

```bash
yq '.webApp.external.url' ./projects/spacetech/export/.global.yaml
```

For example, `https://my.appcircle.spacetech.com`

**2.** Get **IAM** URL.

```bash
yq '.keycloak.external.url' ./projects/spacetech/export/.global.yaml
```

For example, `https://auth.appcircle.spacetech.com`

**3.** Get **API** URL.

```bash
yq '.apiGateway.external.url' ./projects/spacetech/export/.global.yaml
```

For example, `https://api.appcircle.spacetech.com`

#### Configuration

Below are the configuration steps you should follow for setting up the GitHub App.

1. Give a name to your GitHub App using the "GitHub App name" field.
   1. For example, `MyAwesomeApp`
2. Enter the **dashboard** URL in the "Homepage URL" field.
   1. For example, `https://my.appcircle.spacetech.com`
3. Add "Callback URL" using the **API** URL and appending `/build/v1/callback?gitProvider=GithubApp` to the end of the URL.
   1. For example, `https://api.appcircle.spacetech.com/build/v1/callback?gitProvider=GithubApp`
4. Add "Callback URL" using the **IAM** URL and appending `/auth/realms/appcircle/broker/githubapp/endpoint?gitProvider=GithubApp` to the end of the URL.
   1. For example, `https://auth.appcircle.spacetech.com/auth/realms/appcircle/broker/githubapp/endpoint?gitProvider=GithubApp`
5. The "Request user authorization (OAuth) during installation" option in the "Identifying and authorizing users" section should be in the `checked` state.
6. The "Redirect on update" option in the "Post installation" section should be in the `checked` state.
7. Webhook should be "Active", and enter the **API** URL as "Webhook URL" by appending `/build/v1/hooks/github` at the end.
   1. For example, `https://api.appcircle.spacetech.com/build/v1/hooks/github`
8. Select the "Enable SSL verification" option in the "SSL Verification" for better security practices if your SSL certificates can be trusted by GitHub.
9. Select required "Repository" permissions using [permissions for the GitHub integration](https://docs.appcircle.io/build/manage-the-connections/adding-a-build-profile/connecting-to-github#oauth2-and-personal-access-token-permissions-for-github-integration) guide.
10. Select "Webhooks" as "Read and Write" in the "Organization" permissions.
11. Select the below events in the "Subscribe to events" to be triggered from GitHub:
    1. `Create`
    2. `Commit comment`
    3. `Delete`
    4. `Pull request`
    5. `Push`
    6. `Repository`
    7. `Status`

When you complete your GitHub App configuration on GitHub, you are ready to move on to using it in the Appcircle.

---

In order to **activate your GitHub app on the Appcircle server**, you should fill in the below settings in your `global.yaml` using your GitHub App properties.

```yaml
build:
  oauths:
    githubAppOauth:
      enabled: true
      clientId: 
      clientSecret: 
      authorizeUrl: 
```

You can find all the required values in the "About" page under the "General" tab at the GitHub App configuration page.

- **`clientId`**: It's the "Client ID" of your GitHub App.
  - For example, `Iv2***qEI***x8H***ys`
- **`clientSecret`**: "Create a new client secret" for your GitHub App.
  - For example, `222***a8f***2a1***4a0***5f3***b8a***b8a8`
- **`authorizeUrl`**: Use "Public link", appending `/installations/new` to the end.
  - For example, `https://github.com/apps/myawesomeapp/installations/new`

:::caution

As in the example above, replace the `{app_name}` with your actual GitHub application name;  
- `https://github.com/apps/{app_name}/installations/new`

:::

According to the sample GitHub App properties above, your `global.yaml` settings should be like below.

```yaml
build:
  oauths:
    githubAppOauth:
      enabled: true
      clientId: "Iv2***qEI***x8H***ys"
      clientSecret: "222***a8f***2a1***4a0***5f3***b8a***b8a8"
      authorizeUrl: "https://github.com/apps/myawesomeapp/installations/new"
```

To apply the changes, please follow the [Applying Git Provider Changes](#applying-git-provider-changes) section at the end.

After successfully applying, the "GitHub App Cloud `OAuth2`" option will be visible under "GitHub Cloud Connection" options when you create a new connection for a build profile.

:::info
"GitHub App Cloud `OAuth2`" connection option is available in version `3.29.3` or later.
:::

:::caution
Currently, GitHub App connection is **supported for only GitHub Cloud** (github.com) connections.

You cannot use the GitHub App for a GitHub Enterprise Server connection.
:::

## Connect via SSH

To disable the "Connect via SSH" option, add the below configuration to `global.yaml`.

```yaml
build:
  oauths:
    ssh:
      enabled: false
```

If you want to re-enable "Connect via SSH" again, you can set the `enabled` to `true`.

For more details about "Connect via SSH" usage, see related docs in the [Connect via SSH](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh) page.

To apply the changes, please follow the [Applying Git Provider Changes](#applying-git-provider-changes) section at the end.

## Connect via URL

To disable the "Connect via URL" option, add the below configuration to `global.yaml`.

```yaml
build:
  oauths:
    publicRepository:
      enabled: false
```

If you want to re-enable "Connect via URL" again, you can set the `enabled` to `true`.

For more details about "Connect via URL" usage, see related docs in the [Connect via URL](/build/manage-the-connections/adding-a-build-profile/connecting-to-public-repository) page.

To apply the changes, please follow the [Applying Git Provider Changes](#applying-git-provider-changes) section at the end.

## Applying Git Provider Changes

You can add or remove git providers at [installation](/self-hosted-appcircle/install-server/linux-package/installation/docker) steps or later when you need. Following sections will explain how to apply changes especially after installation.

Let's assume we want to disable both "Connect via SSH" and "Connect via URL" options. Then we need to add below configuration to our `global.yaml`.

```yaml
build:
  oauths:
    ssh:
      enabled: false
    publicRepository:
      enabled: false
```

:::caution

You should have only one `build.oauths` key in your `global.yaml` file.

Keep in mind that if you have multiple `build.oauths` keys in `global.yaml`, then the last one will be used in the Appcircle server runtime.

Be careful while configuring different connection options at the same time. Union them under one `build.oauths` key in the `global.yaml`.

:::

If we **do** this at installation time then there is no extra step to take. These options will be disabled on first boot without any extra effort.

If we **don't do** the configuration at installation, then after editing `global.yaml`, we need to apply below steps to activate changes.

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](/self-hosted-appcircle/install-server/linux-package/installation/docker#3-configure) section in docs and applied example scenario.

Following steps are using example project as project naming, which was told there.

:::

1. Shutdown Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" down
```

2. Apply configuration changes.

```bash
./ac-self-hosted.sh -n "spacetech" export
```

3. Boot Appcircle server.

```bash
./ac-self-hosted.sh -n "spacetech" up
```

On complete, refresh your browser and login to Appcircle with your account. You should see that "Connect via SSH" and "Connect via URL" option is disabled on the connection page. :tada:

<Screenshot
  url="https://cdn.appcircle.io/docs/assets/BE-6543-ssh-url-disabled.png"
  alt="Applying Git provider changes (sample)"
/>

<NeedHelp />
