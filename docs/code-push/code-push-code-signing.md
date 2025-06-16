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



