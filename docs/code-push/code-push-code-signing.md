---
title: CodePush Code Signing
description: Learn how to sign your application with Appcircle CodePush feature for React Native projects.
tags: [appcircle codepush, signing, codepush, react native]
sidebar_position: 3
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CodePush Code Signing

CodePush Code Signing ensures that every over‑the‑air (OTA) JavaScript bundle your React Native application receives originates from a trusted source and has not been altered in transit. In this guide, you will learn how to generate signing keys, configure Appcircle to sign your CodePush releases automatically, and enable runtime verification so that your React Native app installs only properly signed updates.


## Configuration of Code Signing

Before you can sign your CodePush release, you must perform a few prerequisite configuration steps. Appcircle leverages these settings to verify the signature and safeguard your CodePush releases. The configuration details are explained step‑by‑step below.

- Generate the key pairs. Use OpenSSL (or your preferred cryptographic toolkit) to create a 4096‑bit RSA key pair—or an ECC key with curve P‑256—store the private key securely. And then store the private key securely.

```bash
# generate private RSA key
openssl genrsa -out private_codepush_signing_key.pem
# export public key
openssl rsa -pubout -in private_codepush_signing_key.pem -out public_codepush_signing_key.pem
```

## Setup and Installation

After generating the private and public keys locally, you must make a few configuration changes in your application. Begin by adding the generated **public key** to the project that you intend to sign, ensuring it is accessible at build time for signature verification.

<Tabs defaultValue="react-native-ios" values={[
{ label: 'Info.plist for iOS', value: 'react-native-ios' },
{ label: 'Strings.xml for Android', value: 'react-native-android' },
]}>

  <TabItem value="react-native-ios">
    ```swift
    <key>CodePushPublicKey</key>
        <string>-----BEGIN PUBLIC KEY-----
            Here is your public key
        -----END PUBLIC KEY-----</string>
    ```
  </TabItem>

  <TabItem value="react-native-android">
  
    ```java
        <resources>
            <string name="app_name">my_app</string>
            <string name="CodePushPublicKey">-----BEGIN PUBLIC KEY-----
                Here is your public key
            -----END PUBLIC KEY-----</string>
        </resources>
    ```
  </TabItem>

</Tabs>


### Signing CodePush Release

To create a signed CodePush release, you must first generate a build from your codebase with the public key already embedded. The resulting `.ipa` and `.apk` artifacts now contain the public key, enabling them to identify properly signed CodePush releases and safely apply OTA updates.


Once your binary is configured with the public key, you can publish a **signed** CodePush release through the **Appcircle CodePush CLI**:

```bash
appcircle-code-push release-react <YOUR_APP_PROFILE_NAME> <platform> -d <DEPLOYMENT_CHANNEL_NAME> --privateKeyPath <YOUR_PRIVATE_KEY_PATH>
```

Replace `<YOUR_APP_PROFILE_NAME>` with the CodePush Profile name shown in the Appcircle dashboard, update the `-d` flag as needed (e.g., *Staging*). The `--privateKeyPath` flag must reference the **same private key** you used to generate the public key embedded in the app; the CLI will sign the bundle before uploading it to Appcircle.


For a full list of commands and advanced options, see the Appcircle CodePush CLI [documentation.](/code-push/code-push-cli).
