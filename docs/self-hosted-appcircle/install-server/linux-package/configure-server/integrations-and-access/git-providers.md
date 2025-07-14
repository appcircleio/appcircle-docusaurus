---
title: Git Providers
description: Configure git providers in self-hosted Appcircle
tags: [self-hosted, git providers, configuration, gitlab, azure, bitbucket, github]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';

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

You can configure only the self-hosted or cloud "Bitbucket" options using the relevant sections.

- The `bitbucket` section is used to manage **Bitbucket (Cloud)**.
- The `bitbucketServer` section is used to manage **Bitbucket Server**.

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

You can configure only the self-hosted or cloud "Azure DevOps" options using the relevant sections.

- The `azureDevopsServices` section is used to manage **Azure DevOps Services (Cloud)**.
- The `azureDevopsServer` section is used to manage **Azure DevOps Server**.

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

You can configure only the self-hosted or cloud "GitLab" options using the relevant sections.

- The `gitlab` section is used to manage **GitLab (Cloud)**.
- The `gitlabSelfHosted` section is used to manage **GitLab Self-Managed**.

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

You can configure only the self-hosted or cloud "GitHub" options using the relevant sections.

- The `githubApp` section is used to manage **GitHub (Cloud)**.
- The `githubEnterpriseServer` section is used to manage **GitHub Enterprise Server**.

For more details about "GitHub" usage, see related docs in the [Connecting to GitHub](/build/manage-the-connections/adding-a-build-profile/connecting-to-github) page.

To apply the changes, please follow the [Applying Git Provider Changes](#applying-git-provider-changes) section at the end.

:::info
GitHub Enterprise Server option is available in version `3.28.2` or later.
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

Let's assume we want to disable both "Connect via SSH" and "Connect via URL" options. Then we need to add below section to our `global.yaml`.

```yaml
build:
  oauths:
    ssh:
      enabled: false
    publicRepository:
      enabled: false
```

:::caution

You should have only one `build.oauths` section in your `global.yaml` file.

Keep in mind that if you have multiple `build.oauths` sections in `global.yaml`, then the last one will be used in the Appcircle server runtime.

Be careful while configuring different connection options at the same time. Union them under one `build.oauths` section in the `global.yaml`.

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
