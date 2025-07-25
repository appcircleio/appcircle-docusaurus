---
title: SSL Configuration
description: Learn how to configure SSL for your self-hosted Appcircle server
tags: [self-hosted, ssl, https, certificate, custom domain, enterprise app store, external services]
sidebar_position: 3
---

import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_restart-appcircle-server.mdx';
import SpacetechExampleInfo from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_spacetech-example-info.mdx';
import DowntimeCaution from '@site/docs/self-hosted-appcircle/install-server/linux-package/configure-server/\_appcircle-server-downtime-caution.mdx';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Overview

Although auto-generated `global.yaml` template has "HTTPS enabled" by default, in our sample scenario and configuration it was "HTTPS disabled" to keep it simple to understand. Refer [here](/self-hosted-appcircle/install-server/linux-package/installation/docker#3-configure) for sample configuration told at installation.

SSL configuration has some specific details for its own use cases and it should have a dedicated section.

So, in this section we will document all the details about configuring HTTPS with your own certificates for your own domain.

:::caution

Self-hosted Appcircle server does not support using a proxy, load balancer or some other external device to terminate SSL. You should do it inside Appcircle instance with configuration told in below sections.

:::

:::info

For now, self-hosted Appcircle server does not have Let’s Encrypt integration or an automated way of renewing certificates.

You should manage certificates from configuration file manually and renew them with same method when expired.

:::

:::info

If your cert format `PKCS#7` (known as p7b or p7c) , you can convert it to pem format with openssl.

See the example command below:

```bash
openssl pkcs7 -print_certs -in cert.p7b -out cert.pem
```

:::

:::info

If your cert format is `PFX` (known as p12), you can convert it to pem format with openssl.

See the example commands below:

- Extract the cert from archive.

```bash
openssl pkcs12 -in cert.p12 -clcerts -nokeys -out cert.pem
```

- Extract the key without password.

```bash
openssl pkcs12 -in cert.p12 -nocerts -nodes -out key.pem
```

- Extract the key with password.

```bash
openssl pkcs12 -in cert.p12 -nocerts -out key.pem
```

:::

:::info
When configuring Appcircle with HTTPS, you have the option to use self-signed or untrusted root certificates. However, if you choose to do so, it is essential to add the certificate or the root CA certificate to the trusted certificates. Failure to do this may result in connection errors. For detailed instructions about adding trusted CA certificates, refer to the [External Services](#external-services) section.
:::

## Configure HTTPS

First of all, you need to set `external.scheme` as `https` at `global.yaml` to enable HTTPS for all [subdomains](/self-hosted-appcircle/install-server/linux-package/installation/docker#4-dns-settings).

```yaml
external:
  scheme: https
```

:::caution

`global.yaml` configuration file is located under **project** folder.

- `projects/${YOUR_PROJECT}`

You can see an example project configuration from [here](/self-hosted-appcircle/install-server/linux-package/installation/docker#3-configure).

:::

:::caution

Changing `external.scheme` from `http` to `https` or from `https` to `http` after using Appcircle server some time, requires configuration reset which results with data cleanup.

So, we suggest you to be sure with your configuration before using it in production environment.

Refer to [reset configuration](/self-hosted-appcircle/install-server/linux-package/installation/docker#reset-configuration) section for more details.

:::

Set your private key and public certificate to `nginx` environment variables in `global.yaml` as below.

```yaml
nginx:
  sslCertificate: |
    -----BEGIN CERTIFICATE-----
    MIIFLTCCBBWgAwIBAgISBB5v1NxtkwmxzOryHdHkWuwoMA0GCSqGSIb3DQEBCwUA
    MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
...
    Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
    -----END CERTIFICATE-----
  sslCertificateKey: |
    -----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWkSbzuxqDY9hb
    giZbOvH6ZEWJNgk5x+jsocsH+f2nsi6IsmnZqm5z068IxV4o7u2NtPQ1Yl4v4F7y
...
    J8lYxh0PCOmuCZ02FAvoi0r8
    -----END PRIVATE KEY-----
```

- `sslCertificate` is the public certificate. (content of `.crt` file)
- `sslCertificateKey` is the private key. (content of `.key` file)

:::caution

You must use the full certificate chain, in the correct order, to prevent SSL errors when clients connect. For example, you may get an _"unable to verify the first certificate"_ error on a missing case.

Order should be like this: first the server certificate, then all intermediate certificates, and finally the root CA.

:::

:::info

If you want to hide these secrets from human-readable `global.yaml`, you can use base64 encoded `user-secret` file for the same environment variables.

Refer to [installation](/self-hosted-appcircle/install-server/linux-package/installation/docker#3-configure) docs for details of `user-secret` usage.

:::

:::caution

For now, self-hosted Appcircle does not support usage of password protected private keys.

:::

### Sample Configuration

:::info

We're assuming that previously you reviewed or followed [install self-hosted appcircle](/self-hosted-appcircle/install-server/linux-package/installation/docker#3-configure) section in docs and applied example scenario.

Following steps are using example project as project naming, which was told there.

Current working directory is assumed `appcircle-server` for following steps. See [here](/self-hosted-appcircle/install-server/linux-package/installation/docker#1-download) for installation details.

:::

Let's assume we have `_wildcard.appcircle.spacetech.com.key` as private key file for our sample domain.

```bash
$ cat _wildcard.appcircle.spacetech.com.key
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWkSbzuxqDY9hb
giZbOvH6ZEWJNgk5x+jsocsH+f2nsi6IsmnZqm5z068IxV4o7u2NtPQ1Yl4v4F7y
...
J8lYxh0PCOmuCZ02FAvoi0r8
-----END PRIVATE KEY-----
```

And we have `_wildcard.appcircle.spacetech.com.crt` as public certificate file for our sample domain. It's a full chain certificate file which has server certificate, all intermediate certificates, and finally the root CA.

```bash
$ cat _wildcard.appcircle.spacetech.com.crt
-----BEGIN CERTIFICATE-----
MIIFLTCCBBWgAwIBAgISBB5v1NxtkwmxzOryHdHkWuwoMA0GCSqGSIb3DQEBCwUA
MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
...
hXg7TJ+Y8MmrBmw4il+i4GfwZN4h7TMuRm17w9+EfVgw
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
...
nLRbwHOoq7hHwg==
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
...
Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
-----END CERTIFICATE-----
```

HTTPS related settings in `global.yaml` file should be like this.

```yaml
---
environment: Production
enableErrorHandling: "true"
external:
  scheme: https
  mainDomain: ".appcircle.spacetech.com"
...
...
nginx:
  sslCertificate: |
    -----BEGIN CERTIFICATE-----
    MIIFLTCCBBWgAwIBAgISBB5v1NxtkwmxzOryHdHkWuwoMA0GCSqGSIb3DQEBCwUA
    MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
...
    hXg7TJ+Y8MmrBmw4il+i4GfwZN4h7TMuRm17w9+EfVgw
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
    TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
...
    nLRbwHOoq7hHwg==
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
    MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
...
    Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
    -----END CERTIFICATE-----
  sslCertificateKey: |
    -----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDWkSbzuxqDY9hb
    giZbOvH6ZEWJNgk5x+jsocsH+f2nsi6IsmnZqm5z068IxV4o7u2NtPQ1Yl4v4F7y
...
    J8lYxh0PCOmuCZ02FAvoi0r8
    -----END PRIVATE KEY-----
```

After running server, open your browser and go to `https://my.appcircle.spacetech.com`.

You should see "Connection Secure" icon in browser's address bar which shows successful HTTPS connection.

:::info

#### Redirect HTTP requests to HTTPS

By default, when you enable HTTPS for `external.scheme`, NGINX listens for unencrypted HTTP traffic on port 80 but redirects them as HTTPS with 301 response code automatically.

You don't need to do any manual configuration to redirect HTTP requests to HTTPS.

:::

:::tip

In order to keep your configuration simple, we're suggesting to use wildcard certificate for `external.mainDomain`.

For our sample scenario, we used certificate signed for `*.appcircle.spacetech.com` domain.

Wildcard certificate created for main domain will cover all subdomains listed in [here](/self-hosted-appcircle/install-server/linux-package/installation/docker#4-dns-settings).

Although you can create and use dedicated certificates for all subdomains, in our opinion it won't be useful. It will be harder to configure and maintain lots of certificates.

:::

## Configure TLS Versions

The Appcircle server by default accepts connections over `TLSv1` and above. You can choose which TLS versions to support based on your security requirements. To restrict the TLS versions used by the Appcircle server, you can set the `.nginx.sslProtocols` variable in the `global.yaml` of the project.

:::info
When configuring TLS versions for your Appcircle server, keep in mind that this setting applies to all services, including the Dashboard, Testing Distribution, Enterprise App Store, Authentication, and others, including the [Appcircle DMZ Server](/self-hosted-appcircle/install-server/linux-package/configure-server/advanced-configuration/store-dist-dmz) if you are using Appcircle in DMZ mode.
:::

:::info
Configurable TLS version support requires Appcircle server `3.23.0` or later.
:::

To make Appcircle server to work with `TLSv1.2` and above:

<DowntimeCaution/>

- Login to the Appcircle server with SSH.

- Go to the `appcircle-server` directory.

```bash
cd appcircle-server
```

<SpacetechExampleInfo/>

- Edit the `global.yaml` file of your project.

```bash
vi ./projects/spacetech/global.yaml
```

- Add or update the `nginx.sslProtocols` parameter as below.

:::info

Please keep in mind that the `nginx` key might already exist in your `global.yaml` file. In that case, just add the `sslProtocols` key. If `nginx` does not exist you can add it to the `global.yaml` file of your project.

:::

:::caution

#### TLSv1.2 is Required for MacOS Runners 🚫

It is important to note, however, that if macOS runners are included in a self-hosted runner pool, `TLSv1.2` support should remain enabled. Currently, .NET on macOS does not support the latest TLS protocol versions, and disabling `TLSv1.2` will disrupt communication with macOS-based runners.
:::

```yaml
nginx:
  sslProtocols: TLSv1.2 TLSv1.3
```

<RestartAppcircleServer />

## Enterprise App Store

`global.yaml` configuration has its own dedicated section for Enterprise App Store domain settings. Below we will explain some use cases for Enterprise App Store, when you enable HTTPS.

:::info

After installation, you can view domain settings from "Enterprise App Store > Settings > Store Domain" page in web UI. But you can not change settings from there.

If you want to change domain settings, you should take the same steps told below and make changes from `global.yaml`.

:::

### Default Domain

You can use Enterprise App Store with its default domain without any custom domain configuration.

`global.yaml` section should be like this for default domain.

```yaml
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: false
```

When you use wildcard certificate for main domain, you don't need to create an extra certificate for enterprise app store domain.

Although your wildcard certificate does not include "Store Prefix", on self-hosted Appcircle server installations "Store Prefix" is not used actively since there is only one organization.

Prefixed web requests will always be redirected to default store subdomain. And store subdomain is covered by your wildcard certificate.

- `${PREFIX}.store` :arrow_right: `store`

For our sample scenario, an example redirection will be like this,

- `5bgnsirt10fj.store.appcircle.spacetech.com` :arrow_right: `store.appcircle.spacetech.com`

For this reason, you can only use `store.appcircle.spacetech.com` for all your needs.

### Custom Domain

It's possible to use a custom domain for the Enterprise App Store. In this case we need to make extra configuration for our custom domain.

Most likely, our custom domain won't be covered by main domain certificate. So we may need to create new public certificate and private key pair for the custom domain.

Even if the main domain certificate covers the custom domain, you still need to explicitly configure the store’s custom domain certificate under `storeWeb.customDomain`. Because, when the store custom domain is enabled, the HTTPS certificate defined in the `storeWeb.customDomain` section is used for the Enterprise App Store instead of the certificate defined in `nginx.sslCertificate`.

Custom domain settings are available for both HTTP and HTTPS configurations.

Let's assume we want to use `apps.spacetech.com` as custom domain for our sample scenario.

#### HTTPS Configuration

Custom domain HTTPS settings are similar to the main domain conceptually. After enabling HTTPS for the main domain, it won't be hard to enable HTTPS for the Enterprise App Store custom domain.

Configure the `storeWeb` section in your `global.yaml` as follows:

<Tabs
defaultValue="docker"
groupId="container-engine"
values={[
{label: 'Docker', value: 'docker'},
{label: 'Podman', value: 'podman'},
]}>

<TabItem value="docker">

```yaml
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: apps.spacetech.com
    port: 443
    enabledTls: true
    publicKey: |
      -----BEGIN CERTIFICATE-----
      MIIFOjCCBCKgAwIBAgISBAqWQRxIkc0kW2OZsPY2qH4dMA0GCSqGSIb3DQEBCwUA
      MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
...
      fLDoKQyylhH5aZgQvRWmvGjAvMCaU4me6rfq7ExudsrImuHZuxv0+mL1OvHsJA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
      TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
...
      nLRbwHOoq7hHwg==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
      MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
...
      Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
      -----END CERTIFICATE-----
    privateKey: |
      -----BEGIN PRIVATE KEY-----
      MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDL0BJ4P5hBrjIf
      uDOL6OsB3AvdwTIwCTfpaJOSRi1ZXbxVGXv2f429gqQ4WADxRnLIsmcZtbAyrubO
...
      LUBOU4QRP9V6qpS0TrLmIoM=
      -----END PRIVATE KEY-----
```

:::caution
The `storeWeb.customDomain.port` must be `443` if the `enabledTls` option is set to `true`.
:::

</TabItem>

<TabItem value="podman">

```yaml
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: apps.spacetech.com
    port: 8443
    enabledTls: true
    publicKey: |
      -----BEGIN CERTIFICATE-----
      MIIFOjCCBCKgAwIBAgISBAqWQRxIkc0kW2OZsPY2qH4dMA0GCSqGSIb3DQEBCwUA
      MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
...
      fLDoKQyylhH5aZgQvRWmvGjAvMCaU4me6rfq7ExudsrImuHZuxv0+mL1OvHsJA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
      TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
...
      nLRbwHOoq7hHwg==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
      MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
...
      Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
      -----END CERTIFICATE-----
    privateKey: |
      -----BEGIN PRIVATE KEY-----
      MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDL0BJ4P5hBrjIf
      uDOL6OsB3AvdwTIwCTfpaJOSRi1ZXbxVGXv2f429gqQ4WADxRnLIsmcZtbAyrubO
...
      LUBOU4QRP9V6qpS0TrLmIoM=
      -----END PRIVATE KEY-----
```

:::caution
The `storeWeb.customDomain.port` must be `8443` if the `enabledTls` option is set to `true`.

Since we forward the `TCP/443` to the `TCP/8443` port with [Socat](/self-hosted-appcircle/install-server/linux-package/installation/podman#overcoming-privileged-port-limitations) on the host, you will connect to the Enterprise App Store with the `TCP/443` port.
:::

</TabItem>

</Tabs>

- `publicKey` is the public certificate. (content of `.crt` file)
- `privateKey` is the private key. (content of `.key` file)

You should use the full certificate chain for `publicKey` similar to main domain `sslCertificate`, to prevent SSL errors when clients connect.

:::caution

For now, self-hosted Appcircle does not support usage of password protected private keys for Enterprise App Store custom domains.

:::

#### HTTP Configuration

If you want to use HTTP for your Enterprise App Store custom domain, you can configure it by setting `enabledTls` to `false` and using the appropriate HTTP port.

Configure the `storeWeb` section in your `global.yaml` as follows:

<Tabs
defaultValue="docker"
groupId="container-engine"
values={[
{label: 'Docker', value: 'docker'},
{label: 'Podman', value: 'podman'},
]}>

<TabItem value="docker">

```yaml
storeWeb:
  customDomain:
    enabled: true
    domain: apps.spacetech.com
    port: 80
    enabledTls: false
    # No publicKey or privateKey
```

:::caution
The `storeWeb.customDomain.port` must be `80` when using HTTP with Docker.
:::

</TabItem>

<TabItem value="podman">

```yaml
storeWeb:
  customDomain:
    enabled: true
    domain: apps.spacetech.com
    port: 8080
    enabledTls: false
    # No publicKey or privateKey
```

:::caution
The `storeWeb.customDomain.port` must be `8080` when using HTTP with Podman.

Since we forward the `TCP/80` to the `TCP/8080` port with [Socat](/self-hosted-appcircle/install-server/linux-package/installation/podman#overcoming-privileged-port-limitations) on the host, you will connect to the Enterprise App Store with the `TCP/80` port.
:::

</TabItem>

</Tabs>

:::info
When `enabledTls` is set to `false`, no certificate configuration is needed or used. Connections will be unencrypted and HTTP only.
:::

## Testing Distribution

`global.yaml` configuration has its own dedicated section for [Testing Distribution](/testing-distribution) domain settings. Below, we will explain some use cases for Testing Distribution, when you enable HTTPS.

### Default Domain

By default, Testing Distribution has a **[dist](https://docs.appcircle.io/self-hosted-appcircle/install-server/linux-package/installation/docker#4-dns-settings)** subdomain under the main domain on self-hosted Appcircle servers.

For example, if your `external.mainDomain` in the `global.yaml` file is `.appcircle.spacetech.com`, then the default Testing Distribution domain name should be `dist.appcircle.spacetech.com`.

If you have configured the Appcircle server as HTTPS using the `external.scheme` as explained [here](#configure-https), the certificate of the Appcircle server also includes the default Testing Distribution subdomain, and it works with HTTPS.

### Custom Domain

It's possible to use a custom domain for the Testing Distribution. In this case, you need to make extra configurations for our custom domain.

:::caution
Please be aware that, after you change the Testing Distribution domain or the SSL settings, the links in the **emails that were sent to the testers with the previous domain and previous SSL settings will be invalid.**
:::

Most likely, our custom domain won't be covered by the main domain certificate. In this case, we need to create a new public certificate and private key pair for the custom domain.

Custom domain HTTPS settings are similar to the main domain configuration conceptually. After enabling HTTPS for the main domain, it won't be hard to enable HTTPS for the Testing Distribution custom domain.

Let's assume we want to use `dist.spacetech.com` as a custom domain for our sample scenario. Then the `global.yaml` section should be like below for this case.

:::note
If you don't have the `testerWeb` section defined in the `global.yaml` file, you should add it as below.

If you have a `testerWeb` section previously defined in the `global.yaml` file for some reason, you should update that section with the `customDomain` settings below instead of adding a new one.
:::

<Tabs
defaultValue="docker"
groupId="container-engine"
values={[
{label: 'Docker', value: 'docker'},
{label: 'Podman', value: 'podman'},
]}>

<TabItem value="docker">

```yaml
testerWeb:
  customDomain:
    enabled: true
    domain: dist.spacetech.com
    port: 443
    enabledTls: true
    publicKey: |
      -----BEGIN CERTIFICATE-----
      MIIFOjCCBCKgAwIBAgISBAqWQRxIkc0kW2OZsPY2qH4dMA0GCSqGSIb3DQEBCwUA
      MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
...
      fLDoKQyylhH5aZgQvRWmvGjAvMCaU4me6rfq7ExudsrImuHZuxv0+mL1OvHsJA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
      TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
...
      nLRbwHOoq7hHwg==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
      MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
...
      Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
      -----END CERTIFICATE-----
    privateKey: |
      -----BEGIN PRIVATE KEY-----
      MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDL0BJ4P5hBrjIf
      uDOL6OsB3AvdwTIwCTfpaJOSRi1ZXbxVGXv2f429gqQ4WADxRnLIsmcZtbAyrubO
...
      LUBOU4QRP9V6qpS0TrLmIoM=
      -----END PRIVATE KEY-----
```

:::caution
The `testerWeb.customDomain.port` must be `443` if the `enabledTls` option is set to `true`.
:::

</TabItem>

<TabItem value="podman">

```yaml
testerWeb:
  customDomain:
    enabled: true
    domain: dist.spacetech.com
    port: 8443
    enabledTls: true
    publicKey: |
      -----BEGIN CERTIFICATE-----
      MIIFOjCCBCKgAwIBAgISBAqWQRxIkc0kW2OZsPY2qH4dMA0GCSqGSIb3DQEBCwUA
      MDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD
...
      fLDoKQyylhH5aZgQvRWmvGjAvMCaU4me6rfq7ExudsrImuHZuxv0+mL1OvHsJA==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw
      TzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh
...
      nLRbwHOoq7hHwg==
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
      MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
...
      Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
      -----END CERTIFICATE-----
    privateKey: |
      -----BEGIN PRIVATE KEY-----
      MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDL0BJ4P5hBrjIf
      uDOL6OsB3AvdwTIwCTfpaJOSRi1ZXbxVGXv2f429gqQ4WADxRnLIsmcZtbAyrubO
...
      LUBOU4QRP9V6qpS0TrLmIoM=
      -----END PRIVATE KEY-----
```

:::caution
The `testerWeb.customDomain.port` must be `8443` if the `enabledTls` option is set to `true`.

Since we forward the `TCP/443` to the `TCP/8443` port with [Socat](/self-hosted-appcircle/install-server/linux-package/installation/podman#overcoming-privileged-port-limitations) on the host, you will connect to the Testing Distribution with the `TCP/443` port.
:::

</TabItem>

</Tabs>

- `publicKey` is the public certificate. (content of `.crt` file)
- `privateKey` is the private key. (content of `.key` file)

You should use the full certificate chain for `publicKey`, similar to the main domain `sslCertificate`, to prevent SSL errors when clients connect.

:::caution

For now, self-hosted Appcircle does not support the usage of password-protected private keys for the Testing Distribution custom domains.

:::

## External Services

If you are using external services that have self-signed SSL certificates, you will need to add their public certificate to the `global.yaml` file. These external services can be self-hosted git providers like GitLab, Azure Devops Server, Bitbucket, or LDAP servers used for authentication.

You can add **multiple** certificates to the `external.ca` section. If you are using multiple services, you will need to add each certificate to this section.

:::info

A certificate included in `external.ca` must be in PEM form.

A PEM-formatted certificate is human-readable in base64 format, and starts with the lines ----BEGIN CERTIFICATE----.

:::

:::caution

If your external service has **Subordinate CA** (sub CA) in certificate chain, it should also be included in `external.ca` along with **Root CA**.

:::

```yaml
external:
  scheme: https
  mainDomain: ".appcircle.spacetech.com"
  ca: |
    -----BEGIN CERTIFICATE-----
    MIIEvTCCAyWgAwIBAgIQNVqUQw+7fmeXJBAtns5HyjANBgkqhkiG9w0BAQsFADB3
    MR4wHAYDVQQKExVta2NlcnQgZGV2ZWxvcG1lbnQgQ0ExJjAkBgNVBAsMHW9zYm94
    ...
    nLRbwHOoq7hHwg==
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    MIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/
    MSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT
    ...
    Dfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5
    -----END CERTIFICATE-----
```

:::caution

When editing the yaml file, pay close attention to the indentation level to ensure the file is properly formatted. Wrong indentation will cause runtime issues.

:::
