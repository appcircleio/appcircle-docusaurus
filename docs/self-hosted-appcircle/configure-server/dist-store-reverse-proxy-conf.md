---
title: Testing Distribution & Store Reverse Proxy
metaTitle: Testing Distribution & Store Reverse Proxy
metaDescription: Testing Distribution & Store Reverse Proxy
sidebar_position: 14
---

import Screenshot from '@site/src/components/Screenshot';

## Overview

In this section, you will see how to configure Nginx as a reverse proxy. At the end, you will be able to access the Appcircle Testing Distribution and Enterprise Appstore from the internet.

In enterprise environments, all incoming requests from the internet to the Appcircle server are blocked by default. If you want to access the Appcircle Testing Distribution and Enterprise Appstore from the internet, you should create a reverse proxy which accepts requests from the internet and forwards requests to the Appcircle server.

As a result, your Testing Distribution users and Enterprise Appstore users can access the resources like `apk` and `ipa` files in the Appcircle server.

If you have any other common loadbalancer, reverse proxy or firewall tool, you don't need to deploy another Nginx as a reverse proxy. You can configure your own tool. Here you can see the main logic to access Appcircle server from the internet.

## Overall Structure

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-2624-common-view.png' />

In the diagram above, you can see the overall structure that you will deploy.

You see the reverse proxy device that accepts requests from the internet and proxies to the Appcircle server. This way, Appcircle server won't be reached from the internet directly but with a reverse proxy.

There is one thing you should consider, the SSL certificates.

1. You may have installed the Appcircle server with a self-signed, untrusted SSL certificate. You can access the Enterprise Appstore with a `HTTPS` connection with a custom domain, and the Testing Distribution with a `HTTPS` connection.

2. You may have installed the Appcircle server with a self-signed, untrusted SSL certificate, and access the Enterprise Appstore as `HTTP` with a custom domain.

3. You may have installed the Appcircle server with a self-signed, untrusted SSL certificate, and access the Enterprise Appstore as `HTTPS` with the default domain.

4. You may have installed the Appcircle server without any SSL certificate, and the Enterprise Appstore as `HTTP`.

Are recommendation is the first option. In this use-case, the traffic between the reverse proxy and the Appcircle server will be encrypted also which is best for security.

## Use-Case 1

```yaml
environment: Production
enableErrorHandling: 'true'
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
smtpServer:
  user: smtpuser@spacetech.com
  password: smtpPassword
  from: appcircle@spacetech.com
  host: smtp.spacetech.com
  fromDisplayName: Appcircle
  port: 465
  ssl: false
  auth: true
  starttls: true
keycloak:
  initialUsername: appcircle-admin@spacetech.com
  initialPassword: superSecretPassword
  enabledRegistration: true
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
testerWeb:
  external:
    url: https://dist.spacetech.com
    domain: dist.spacetech.com
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
            proxy_pass https://100.106.223.87;
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
        server_name dist.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass https://100.106.223.87;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host dist.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }
}
```

## Use-Case 2

In this use-case;

- The Appcircle server will use a self-signed certificate,
- The Enterprise Appstore will be accessed with a custom domain and with `HTTP`,
- The Testing Distribution will be accessed with the default domain and with `HTTPS`.

```yaml
environment: Production
enableErrorHandling: 'true'
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
smtpServer:
  user: smtpuser@spacetech.com
  password: smtpPassword
  from: appcircle@spacetech.com
  host: smtp.spacetech.com
  fromDisplayName: Appcircle
  port: 465
  ssl: false
  auth: true
  starttls: true
keycloak:
  initialUsername: appcircle-admin@spacetech.com
  initialPassword: superSecretPassword
  enabledRegistration: true
storeWeb:
  external:
    subdomain: store
  customDomain:
    enabled: true
    domain: store.spacetech.com
testerWeb:
  external:
    url: https://dist.spacetech.com
    domain: dist.spacetech.com
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
            proxy_pass http://100.106.223.87;
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
        server_name dist.spacetech.com;

        ssl_certificate /etc/nginx/ssl/store.crt;
        ssl_certificate_key /etc/nginx/ssl/store.key;

        location / {
            proxy_pass https://100.106.223.87;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header Host dist.spacetech.com;
            proxy_busy_buffers_size 512k;
            proxy_buffers 4 512k;
            proxy_buffer_size 256k;
        }
    }
}
```
