---
title: Git Providers Configuration
description: Learn how to configure git providers
tags: [self-hosted, helm, configuration, kubernetes]
sidebar_position: 70
---

import Screenshot from '@site/src/components/Screenshot';
import NeedHelp from '@site/docs/\_need-help.mdx';

## Overview

With default installation, self-hosted Appcircle comes with the connection options below:

- Bitbucket
- Azure
- GitLab
- Connect via SSH
- Connect via URL

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2031-git-providers-v2.png' />

But you're not limited with these options. You can configure the git providers and use them within your self-hosted Appcircle server.

### Enable/Disable Git Providers

If you want to enable or disable any of these providers, you can do so by updating your `values.yaml` file.

In the example below, there are enabled git providers list with comma separated:

```yaml
web:
  web-app:
    selfHostedGitProviders:
      - "bitbucketServer"
      - "azureDevopsServer"
      - "gitlabSelfHosted"
      - "ssh"
      - "publicRepository"
```

You can delete the providers you do not need by removing them from `selfHostedGitProviders` list above.

For more details about "Bitbucket" usage, see related docs in the [Connecting to Bitbucket](/build/manage-the-connections/adding-a-build-profile/connecting-to-bitbucket) page.

For more details about "Azure" usage, see related docs in the [Connecting to Azure DevOps](/build/manage-the-connections/adding-a-build-profile/connecting-to-azure) page.

For more details about "GitLab" usage, see related docs in the [Connecting to GitLab](/build/manage-the-connections/adding-a-build-profile/connecting-to-gitlab) page.

For more details about "Connect via SSH" usage, see related docs in the [Connect via SSH](/build/manage-the-connections/adding-a-build-profile/connecting-to-private-repository-via-ssh) page.

For more details about "Connect via URL" usage, see related docs in the [Connect via URL](/build/manage-the-connections/adding-a-build-profile/connecting-to-public-repository) page.

<NeedHelp />