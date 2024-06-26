---
title: Apple Certificates
description: Learn how to manage iOS certificates in Appcircle
tags: [signing identities, ios certificates, provisioning profiles]
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';
import Screenshot from '@site/src/components/Screenshot';

# Apple Certificates Overview

Certificate files can be in .p12 file format as a private-public key pair. There are 2 main types of iOS certificates:

**1. Apple Development:** Used for development and testing.

The development certificates allow deploying apps to the developer devices (connected physically for testing and debugging) during the actual development process on Xcode.

The common practice is to generate this certificate automatically on Xcode through manual generation is also available. Binaries built with a development certificate cannot be distributed.

**2. Apple Distribution:** Used for submitting applications to the App Store, or for Ad Hoc and Enterprise distribution. (Refer to the provisioning profiles section for the differences between these distribution types.)

In most cases, you will be using a distribution certificate with the combination of a provisioning profile to build and distribute apps in Appcircle.

There is a one-to-many relationship between certificates and provisioning profiles, so you may have multiple provisioning profiles associated with a single certificate.


## Using Appcircle Signing Identity module for Apple Certificates

### Generate or Upload Apple Certificates

To generate or upload your Apple Certificate, select **Apple Certificates** from the signing module.

:::info

All types of Apple certificates are supported, including development, ad hoc, in-house, or App Store distribution.

:::

Click on "Add New" button to upload or create your Apple Certificate.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3953-appleCert.png' />

You can either upload your readily available certificate bundle (P12) along with the bundle password or create a certificate signing request (CSR) to generate a new certificate from the Apple Developer portal and then upload the certificate (CER) to create a certificate bundle (P12). No Mac device is needed.

### Creating P12 File Without Mac

<Screenshot url='https://cdn.appcircle.io/docs/assets/02-02-Add-iOS-Certificates.png' />

To generate your iOS certificates, simply fill in your details and Appcircle will provide a CSR (certificate signing request) which you can use on Apple Developer Portal to generate your signing certificate.

- Create a CSR File

<Screenshot url='https://cdn.appcircle.io/docs/assets/02-07-Generate-iOS-Cert.png' />

- Download your CSR file
- Go to Apple Developer Portal and select Certificates, IDs & Profiles -> Certificates from the left menu
  <Screenshot url='https://cdn.appcircle.io/docs/assets/apple-addcertificate.png' />

- Select the type of certificate you want to create. If you want to distribute to TestFlight,Adhoc or AppStore, you should select Apple Distribution. If you're creating a certificate for local development environment, you should select Apple Development.

<Screenshot url='https://cdn.appcircle.io/docs/assets/apple-select-certificate-type.png' />

- Upload the csr file you have created on Appcircle

<Screenshot url='https://cdn.appcircle.io/docs/assets/apple-selectscr.png' />

- Download your generated CER file from the Apple Developer portal

- Upload the CER file to the signing identities module by clicking on the upload button next to the CSR file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ac-csr-list.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/ac-createp12.png' />

- Your CSR will now be converted to a P12 file as an iOS signing certificate. (Please note that the P12 file comes with an empty password.)

### Uploading P12 Certificate

To upload your Apple Certificate, select "Upload Certificate Bundle (.p12)" button and upload your pre-obtained Apple Certificate file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/02-02-Upload-iOS-Certificates.png' />

You can see a list of your created or uploaded certificates. Each certificate will display the certificate name, certificate type (development, ad-hoc, in-house, or app store distribution) along with expiration dates.

:::caution

If your password contains special characters such as `$` and `#`, your workflow may fail with `MAC verification failed during PKCS12 import` message. If you receive such an error, please export your P12 file by removing that symbol.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/02-08-CertificateList.png' />
