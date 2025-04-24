---
title: Active SSH Private Key
description: Secure your connections with an Active SSH Private Key. Enhance security and manage your remote operations smoothly and safely.
tags: [secure, ssh, connections, private key]
---

import Screenshot from '@site/src/components/Screenshot';

# Active SSH Private Key

This step sets up your SSH key in the build machine if you used one to connect your repository. This allows the build machine to connect to your private repository using your SSH key.

### Prerequisites

There are no prerequisites required before using the **Active SSH Private Key** step.

:::caution

If you connect to your repository via SSH, use this step before the [**Git Clone**](/workflows/common-workflow-steps/git-clone) step. To securely clone repositories connected via SSH, you must define the SSH key for the relevant build agent.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3151-sshOrder.png' />

:::

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3151-sshInput.png' />

| Variable Name                 | Description                                    | Status           |
|-------------------------------|------------------------------------------------|------------------|
| `$AC_REPOSITORY_SSH_KEY`      | SSH private key in RSA format. This value defaults to `$AC_REPOSITORY_SSH_KEY`. It is automatically defined as the [**Reserved Environment Variables**](/environment-variables/appcircle-specific-environment-variables) when an SSH connection is made. | Optional |


### Output Variables

The output(s) resulting from the operation of this component are as follows:


| Variable Name                 | Description                                    |
|-------------------------------|------------------------------------------------|
| `SSH_AUTH_SOCK`              | This is the path to the SSH Auth Socket.       | 

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-activate-ssh-key-component