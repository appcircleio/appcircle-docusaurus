---
title: Install Certificates and Provision Profiles
metaTitle: Install Certificates and Provision Profiles
metaDescription: Install Certificates and Provision Profiles
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

This step installs the specified certificate and provision profile files to sign the project.

:::info
If you are using automatic code sign you can remove this step. Since automatic code signing is managed by Xcode, this step will not be needed.
:::

:::warning
Please remember. If you are using **manual sign**, you should definitely use this step and run it after the **Git Clone** step.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2786-cert_order.png' />

https://github.com/appcircleio/appcircle-ios-install-certificates-and-profiles-component

## Input Variables

The parameters required for this step to work are listed in the table below. These parameters are default.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2786-cert_input.png' />

| Variable Name                 | Description                                    | Required |
|-------------------------------|------------------------------------------------|----------|
| `$AC_CERTIFICATES`            | Concatenated strings of 'cert_pass\|cert_path' combined with a pipe ('\|') character that have the paths of the certificates and their passwords if they exist. <br/><br/> For instance, when we have two certificates A and B that require passwords, then it should be like 'a_cert_pass\|a_cert_path\|b_cert_pass\|b_cert_path'. <br/><br/> If there is no password, its field will be empty, like '\|a_cert_path'. | ✅ |
| `$AC_PROVISIONING_PROFILES` | Paths of the provisioning profiles | ✅ |


## Output Variables

The output parameters after this step is executed are as follows.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2786-cert_output.png' />

| Variable Name                 | Description                                    | Required |
|-------------------------------|------------------------------------------------|----------|
| `$AC_KEYCHAIN_PATH`          | Path created after the certificate is added to the current runner's keychain | ✅ |
| `$AC_KEYCHAIN_PASSWORD`      | After this certificate is added to the keychain, the password assigned on the keychain | ✅ |


https://github.com/appcircleio/appcircle-ios-install-certificates-and-profiles-component
