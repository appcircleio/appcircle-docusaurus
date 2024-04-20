---
title: Active SSH Private Key
description: Secure your connections with an Active SSH Private Key. Enhance security and manage your remote operations smoothly and safely.
tags: [secure, ssh, connections, private key]
sidebar_position: 4
---

import Screenshot from '@site/src/components/Screenshot';

# Active SSH Private Key

This step sets up your SSH key in the build machine if you used one to connect your repository. This allows the build machine to connect to your private repository using your SSH key.

### Prerequisites

:::caution

If you connected to your repository via SSH, you need to use this step before the [Git Clone](/workflows/common-workflow-steps/git-clone) step. In order to securely clone repositories connected via SSH, the SSH key must be defined for the relevant Build agent.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3151-sshOrder.png' />

:::

### Input Variables

Below are the parameters required for this step, along with detailed explanations.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3151-sshInput.png' />

| Variable Name                 | Description                                    | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_REPOSITORY_SSH_KEY`      | SSH private key in RSA format. This value defaults to `AC_REPOSITORY_SSH_KEY`. It is automatically defined as the [**Reserved Environment Variables**](/environment-variables/appcircle-specific-environment-variables) when an SSH connection is made. | Optional |


### Output Variables

| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `$SSH_AUTH_SOCK`              | The path of the SSH Auth Socket.               | 