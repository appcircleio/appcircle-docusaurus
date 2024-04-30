---
title: Install Certificates and Provisioning Profiles
description: Learn how to install certificates and provisioning profiles for iOS distribution in Appcircle.
tags: [build, test, distribute, ios, workflow, step]
---

import Screenshot from '@site/src/components/Screenshot';

# Install Certificates and Provisioning Profiles

This step installs the specified [certificate](https://developer.apple.com/support/certificates/) and [provisioning profile](https://developer.apple.com/help/account/manage-profiles/create-a-development-provisioning-profile/) files to sign the project.
For more detailed information on **iOS Certificates and Provisioning Profiles**, please refer to [this document](https://docs.appcircle.io/signing-identities/ios-certificates-and-provisioning-profiles/).

### Prerequisites

:::info
If you are using an automatic code sign, you can remove this step. Since automatic code signing is managed by Xcode, this step will not be needed.
:::

| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | Clone your repository to the runner machine. Use the Install Certificates and Provisiong Profiles step after this step. This step will clone your repository to be able to use provisioning profiles and certificates. |

:::warning
Please remember. If you are using **manual sign**, you should definitely use this step and run it after the **Git Clone** step.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2786-cert_order.png' />


### Input Variables

The parameters required for this step to work are listed in the table below. These parameters are defaults.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2786-cert_input.png' />


| Variable Name                 | Description                                    | Status      |
|-------------------------------|------------------------------------------------|-------------|
| `$AC_CERTIFICATES`            | Concatenated strings of `cert_pass`\|`cert_path` combined with a pipe ('\|') character that have the paths of the certificates and their passwords if they exist. <br/><br/> For instance, when we have two certificates A and B that require passwords, then it should be like '`a_cert_pass`\|`a_cert_path`\|`b_cert_pass`\|`b_cert_path`'. <br/><br/> If there is no password, its field will be empty, like '\|`a_cert_path`'. | Required |
| `$AC_PROVISIONING_PROFILES` | Paths of the provisioning profiles. | Required | 


### Output Variables

The output parameters after this step is executed are as follows:

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2786-cert_output.png' />

| Variable Name                 | Description                                    | 
|-------------------------------|------------------------------------------------|
| `$AC_KEYCHAIN_PATH`          | A path is created after the certificate is added to the current runner's keychain. | 
| `$AC_KEYCHAIN_PASSWORD`      | After this certificate is added to the keychain, the password assigned to the keychain | 

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-ios-install-certificates-and-profiles-component
