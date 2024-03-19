---
title: Testing Distribution & Enterprise App Store Reverse Proxy
metaTitle: Testing Distribution & Enterprise App Store Reverse Proxy
metaDescription: Testing Distribution & Enterprise App Store Reverse Proxy
sidebar_position: 14
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

import Screenshot from '@site/src/components/Screenshot';
import RestartAppcircleServer from '@site/docs/self-hosted-appcircle/configure-server/\_restart-appcircle-server.mdx';

## Overview

In this section, you will see how to configure Nginx as a reverse proxy. At the end, you will be able to access the Appcircle Testing Distribution and Enterprise App Store from the internet.

In enterprise environments, all incoming requests from the internet to the Appcircle server are blocked by default. If you want to access the Appcircle Testing Distribution and Enterprise App Store from the internet, you should create a reverse proxy which accepts requests from the internet and forwards requests to the Appcircle server.

As a result, your Testing Distribution users and Enterprise App Store users can access the resources like `apk` and `ipa` files in the Appcircle server.

If you have any other common loadbalancer, reverse proxy or firewall tool, you don't need to deploy another Nginx as a reverse proxy. You can configure your own tool. Here you can see the main logic to access Appcircle server from the internet.

## Overall Structure

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2624-common-view-diagram.png' />

In the diagram above, you can see the overall structure that you will deploy. The reverse proxy device that accepts requests from the internet and proxies to the Appcircle server. This way, Appcircle server won't be reached from the internet directly but with a reverse proxy.

There is one thing you should consider, the SSL certificates. Generally public SSL certificates are located in the reverse proxy and self-signed SSL certificate is located in the Appcircle server. So the testing distribution and enterprise app store users can connect to the Appcircle from internet without having untrusted SSL certificate problems.

There are several use-cases for SSL certificates and HTTP(S) connections while configuring the reverse proxy and the Appcircle server.

<Tabs groupId="use-case">

  <TabItem value="usecase1" label="Use-Case 1">

#### Use-Case 1

You may have installed the Appcircle server with an SSL certificate and configured the Enterprise App Store with a custom domain and an SSL certificate.

This is the recommended use-case because all the traffic between users, reverse-proxy and the Appcircle server will be encrypted for security purposes.

In this use-case;

- The reverse proxy will connect the Enterprise App Store with a custom domain and with `HTTPS`.
- The reverse proxy will connect the Testing Distribution with the default domain and with `HTTPS`.
- The Testing Distribution and the Enterprise App Store users will connect the reverse proxy with `HTTPS`.

To configure the Enterprise App Store SSL certificates, you can read the [Enterprise App Store Custom Domain SSL Configuration document](./ssl-configuration.md#custom-domain).

The `global.yaml` file of your Appcircle server should be as follows for this use-case. See the `external.scheme`, `external.mainDomain`, `storeWeb.customDomain`, `nginx` and keys.

- `external.scheme`: Indicates whether the Appcircle dashboard and the default domains for Testing Distribution and Enterprise App Store will work in http or https mode.

- `external.mainDomain`: Specifies the main domain for the Appcircle dashboard and the default domains for Testing Distribution and Enterprise App Store.

- `storeWeb.customDomain`: Specifies the custom domain settings for the Enterprise App Store.

- `nginx`: Specifies the SSL certificate settings for the Appcircle dashboard and default domain.

- According to the `global.yaml` configuration below:
  - The default Enterprise App Store domain is `store.appcircle.spacetech.com`.
  - The custom Enterprise App Store domain is `store.spacetech.com`.
  - The default Testing Distribution domain is `dist.appcircle.spacetech.com`.

```yaml
external:
  scheme: https
  mainDomain: '.appcircle.spacetech.com'
  ca: |
    -----BEGIN CERTIFICATE-----
    6mfNX340o8+jyOTbQN/mTEOWS5eTqzQ/HjxlxNknnF8oxaXRMkdvMXAnrBAexi2S
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    wW1aDz1sjGyAp5Ttal3vY1aJ5RmLTuUuxJ+6+fkTHhLUQCQoEUNatrbKKtzxf0it
    -----END CERTIFICATE-----
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: store.spacetech.com
    port: 443
    enabledTls: true
    publicKey: |
      -----BEGIN CERTIFICATE-----
      UOfez34s7hoPuzJr/nrVQvLQ+cO9oFazlS9JlmGlAdEbgP0RDOBeOAa/XXFj9zdj
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      FiMVxtvuaWheLrKDNpD80TGnizYXFQlmWBGRQSv1juCIx/c3JWElda3AWLf9KomB
      -----END CERTIFICATE-----
      -----BEGIN CERTIFICATE-----
      JBr5DP/2RTmkKFtc53xoSYXQCmg61T8vMycvrdxWX6eAa8VSDszAtl//QFJIrwY8
      -----END CERTIFICATE-----
    privateKey: |
      -----BEGIN PRIVATE KEY-----
      Okf/KOY+V77oMJN1DHKejOqDakyjHUBSYUCUawFTS8gge4gciI+oVmHvxTst7ykK
      -----END PRIVATE KEY-----
nginx:
  sslCertificate: |
    -----BEGIN CERTIFICATE-----
    4pXWp0Zmf79+sjCvtm5fYMHKVUpVdxQRfihQjCSYl/WzaXLeE+UlT6LvK9rxZjN9
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    FiMVxtvuaWheLrKDNpD80TGnizYXFQlmWBGRQSv1juCIx/c3JWElda3AWLf9KomB
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    JBr5DP/2RTmkKFtc53xoSYXQCmg61T8vMycvrdxWX6eAa8VSDszAtl//QFJIrwY8
    -----END CERTIFICATE-----
  sslCertificateKey: |
    -----BEGIN PRIVATE KEY-----
    FuYjetiq9zQppgQuplkZMRQaLisExifFjPY9+5zIegzFZKE3bvjZg+DDWkj++R3p
    -----END PRIVATE KEY-----
```

In the example Nginx configuration below, you can see that there is 2 virtual servers, one for the Enterprise App Store and one for the Testing Distribution.

Check out the `server_name`, `ssl_certificate`, `ssl_certificate_key`, `proxy_pass`, `proxy_set_header Host` values.

- `server_name`: Domain name for the Enterprise App Store and Testing Distribution users coming from the internet.

- `ssl_certificate` and `ssl_certificate_key`: SSL certificate files for `HTTPS` connection between the users and the reverse proxy.

- `proxy_pass`: The IPV4 address or the domain name of the Appcircle server with `HTTPS` schema. We are configuring with `HTTPS` because both of Enterprise App Store and the Testing Distribution work with `HTTPS`.

- `proxy_set_header Host`: The domain names that we have configured on the Appcircle server `global.yaml`.

```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {

    server_names_hash_bucket_size 64;

    server {
        listen 443 ssl;
        server_name store.spacetech.com;

        ssl_certificate /etc/nginx/ssl/appcircle.crt;
        ssl_certificate_key /etc/nginx/ssl/appcircle.key;

        location / {
            proxy_pass https://10.10.20.130;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host store.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }

    server {
        listen 443 ssl;
        server_name dist.appcircle.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass https://10.10.20.130;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host dist.appcircle.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }
}
```

With this `global.yaml` and the `Nginx` configuration, the users can access the Appcircle Enterprise App Store and Testing Distribution from the internet safely.

  </TabItem>

  <TabItem value="usecase2" label="Use-Case 2">

#### Use-Case 2

You may have installed the Appcircle server with an SSL certificate and configured the Enterprise App Store with a custom domain but not with an SSL certificate.

In this use-case;

- The reverse proxy will connect the Enterprise App Store with a custom domain and with `HTTP`.
- The reverse proxy will connect the Testing Distribution with the default domain and with `HTTPS`.
- The Testing Distribution and the Enterprise App Store users will connect the reverse proxy with `HTTPS`.

The `global.yaml` file of your Appcircle server should be as follows for this use-case. See the `storeWeb.customDomain`, `testerWeb.external`, `nginx` and `external.scheme` keys.

```yaml
external:
  scheme: https
  mainDomain: '.appcircle.spacetech.com'
  ca: |
    -----BEGIN CERTIFICATE-----
    6mfNX340o8+jyOTbQN/mTEOWS5eTqzQ/HjxlxNknnF8oxaXRMkdvMXAnrBAexi2S
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    wW1aDz1sjGyAp5Ttal3vY1aJ5RmLTuUuxJ+6+fkTHhLUQCQoEUNatrbKKtzxf0it
    -----END CERTIFICATE-----
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: store.spacetech.com
nginx:
  sslCertificate: |
    -----BEGIN CERTIFICATE-----
    4pXWp0Zmf79+sjCvtm5fYMHKVUpVdxQRfihQjCSYl/WzaXLeE+UlT6LvK9rxZjN9
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    FiMVxtvuaWheLrKDNpD80TGnizYXFQlmWBGRQSv1juCIx/c3JWElda3AWLf9KomB
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    JBr5DP/2RTmkKFtc53xoSYXQCmg61T8vMycvrdxWX6eAa8VSDszAtl//QFJIrwY8
    -----END CERTIFICATE-----
  sslCertificateKey: |
    -----BEGIN PRIVATE KEY-----
    FuYjetiq9zQppgQuplkZMRQaLisExifFjPY9+5zIegzFZKE3bvjZg+DDWkj++R3p
    -----END PRIVATE KEY-----
```

In the example Nginx configuration below, you can see that there is 2 virtual servers, one for the Enterprise App Store and one for the Testing Distribution.

Check out the `server_name`, `ssl_certificate`, `ssl_certificate_key`, `proxy_pass`, `proxy_set_header Host` values.

- `server_name`: Domain name for the Enterprise App Store and Testing Distribution users coming from the internet.

- `ssl_certificate` and `ssl_certificate_key`: SSL certificate files for `HTTPS` connection between the users and the reverse proxy.

- `proxy_pass`: The IPV4 address or the domain name of the Appcircle server with `HTTPS` schema. We are configuring the Testing Distribution with `HTTPS`, but we are configuring `HTTP` for the Enterprise App Store.

- `proxy_set_header Host`: The domain names that we have configured on the Appcircle server `global.yaml`.

```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {

    server_names_hash_bucket_size 64;

    server {
        listen 443 ssl;
        server_name store.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass http://10.10.20.130;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host store.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }

    server {
        listen 443 ssl;
        server_name dist.appcircle.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass https://10.10.20.130;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host dist.appcircle.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }
}
```

  </TabItem>

  <TabItem value="usecase3" label="Use-Case 3">

#### Use-Case 3

You may have installed the Appcircle server with an SSL certificate and not configured the Enterprise App Store with a custom domain.

In this use-case;

- The reverse proxy will connect the Enterprise App Store with the default domain and with `HTTPS`.
- The reverse proxy will connect the Testing Distribution with the default domain and with `HTTPS`.
- The Testing Distribution and the Enterprise App Store users will connect the reverse proxy with `HTTPS`.

The `global.yaml` file of your Appcircle server should be as follows for this use-case. See the `storeWeb.customDomain`, `testerWeb.external`, `nginx` and `external.scheme` keys.

```yaml
external:
  scheme: https
  mainDomain: '.appcircle.spacetech.com'
  ca: |
    -----BEGIN CERTIFICATE-----
    6mfNX340o8+jyOTbQN/mTEOWS5eTqzQ/HjxlxNknnF8oxaXRMkdvMXAnrBAexi2S
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    wW1aDz1sjGyAp5Ttal3vY1aJ5RmLTuUuxJ+6+fkTHhLUQCQoEUNatrbKKtzxf0it
    -----END CERTIFICATE-----
storeWeb:
  external:
    subdomain: store
    domain: store.spacetech.com
  customDomain:
    enabled: false
    domain: store.example.com
nginx:
  sslCertificate: |
    -----BEGIN CERTIFICATE-----
    4pXWp0Zmf79+sjCvtm5fYMHKVUpVdxQRfihQjCSYl/WzaXLeE+UlT6LvK9rxZjN9
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    FiMVxtvuaWheLrKDNpD80TGnizYXFQlmWBGRQSv1juCIx/c3JWElda3AWLf9KomB
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    JBr5DP/2RTmkKFtc53xoSYXQCmg61T8vMycvrdxWX6eAa8VSDszAtl//QFJIrwY8
    -----END CERTIFICATE-----
  sslCertificateKey: |
    -----BEGIN PRIVATE KEY-----
    FuYjetiq9zQppgQuplkZMRQaLisExifFjPY9+5zIegzFZKE3bvjZg+DDWkj++R3p
    -----END PRIVATE KEY-----
```

In the example Nginx configuration below, you can see that there is 2 virtual servers, one for the Enterprise App Store and one for the Testing Distribution.

Check out the `server_name`, `ssl_certificate`, `ssl_certificate_key`, `proxy_pass`, `proxy_set_header Host` values.

- `server_name`: Domain name for the Enterprise App Store and Testing Distribution users coming from the internet.

- `ssl_certificate` and `ssl_certificate_key`: SSL certificate files for `HTTPS` connection between the users and the reverse proxy.

- `proxy_pass`: The IPV4 address or the domain name of the Appcircle server with `HTTPS` schema. We are configuring with `HTTPS` because both of Enterprise App Store and the Testing Distribution work with `HTTPS`.

- `proxy_set_header Host`: The domain names that we have configured on the Appcircle server `global.yaml`.

```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {

    server_names_hash_bucket_size 64;

    server {
        listen 443 ssl;
        server_name store.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass https://10.10.20.130;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host store.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }

    server {
        listen 443 ssl;
        server_name dist.appcircle.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass https://10.10.20.130;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host dist.appcircle.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }
}
```

  </TabItem>

  <TabItem value="usecase4" label="Use-Case 4">

#### Use-Case 4

You may have installed the Appcircle server with an SSL certificate and not configured the Enterprise App Store with a custom domain.

In this use-case;

- The reverse proxy will connect the Enterprise App Store with a custom domain and with `HTTP`.
- The reverse proxy will connect the Testing Distribution with the default domain and with `HTTP`.
- The Testing Distribution and the Enterprise App Store users will connect the reverse proxy with `HTTPS`.

The `global.yaml` file of your Appcircle server should be as follows for this use-case. See the `storeWeb.customDomain`, `testerWeb.external`, `nginx` and `external.scheme` keys.

```yaml
external:
  scheme: http
  mainDomain: '.appcircle.spacetech.com'
  ca: |
    -----BEGIN CERTIFICATE-----
    6mfNX340o8+jyOTbQN/mTEOWS5eTqzQ/HjxlxNknnF8oxaXRMkdvMXAnrBAexi2S
    -----END CERTIFICATE-----
    -----BEGIN CERTIFICATE-----
    wW1aDz1sjGyAp5Ttal3vY1aJ5RmLTuUuxJ+6+fkTHhLUQCQoEUNatrbKKtzxf0it
    -----END CERTIFICATE-----
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: store.spacetech.com
testerWeb:
  external:
    url: https://dist.appcircle.spacetech.com
```

In the example Nginx configuration below, you can see that there is 2 virtual servers, one for the Enterprise App Store and one for the Testing Distribution.

Check out the `server_name`, `ssl_certificate`, `ssl_certificate_key`, `proxy_pass`, `proxy_set_header Host` values.

- `server_name`: Domain name for the Enterprise App Store and Testing Distribution users coming from the internet.

- `ssl_certificate` and `ssl_certificate_key`: SSL certificate files for `HTTPS` connection between the users and the reverse proxy.

- `proxy_pass`: The IPV4 address or the domain name of the Appcircle server with `HTTP` schema. We are configuring with `HTTP` because both of Enterprise App Store and the Testing Distribution work with `HTTPS`.

- `proxy_set_header Host`: The domain names that we have configured on the Appcircle server `global.yaml`.

```nginx
worker_processes auto;

events {
    worker_connections 1024;
}

http {

    server_names_hash_bucket_size 64;

    server {
        listen 443 ssl;
        server_name store.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass http://10.10.20.130;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host store.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }

    server {
        listen 443 ssl;
        server_name dist.appcircle.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass http://10.10.20.130;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host dist.appcircle.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }
}
```

  </TabItem>

</Tabs>

## Restart Appcircle Server

After you have configured the Appcircle server `global.yaml`, you can restart the server with the new configuration.

<RestartAppcircleServer />

Now you can access to the Testing Distribution and Enterprise App Store contents from the internet safely!
