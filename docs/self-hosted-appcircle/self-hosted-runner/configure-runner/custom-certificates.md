---
title: Self-signed Certificates
metaTitle: Self-signed Certificates
metaDescription: Self-signed Certificates
sidebar_position: 5
---

# Overview

If you're using self-signed certificates in your environment, the same certificates must also be added to runners. It can be your self-hosted Appcircle server or your own git repositories.

If you don't add and trust those self-signed certificates, runner will most probably get SSL connection errors while trying to access those resources.

While adding root CAs and sub CAs to host, you should consider the following locations:

- System keychain (macOS)
- `ca-certificates`, `ca-trust` (linux)
- Ruby's `DEFAULT_CERT_DIR`
- Java's keystore `cacerts`

## Adding Certificates

The self-hosted runner has a command-line tool to help you install the required certificates. When called, it connects to the given host via the URL and extracts the root CA. It adds the root CA to the locations listed above.

If your runner version `1.3.12` or later, you can find it in the root directory of the runner installation.

If your runner version is older, then you can get it from Appcircle CDN with the below commands.

```bash
curl -L -O https://storage.googleapis.com/appcircle-dev-common/self-hosted/install_cert.sh
chmod u+x install_cert.sh
```

Simply execute the bash script.

```bash
./install_cert.sh
```

When asked, enter the URL that you need to connect to.

Below is a sample log that was run on macOS.

```txt
% ./install_cert.sh
[+] OS: Darwin
Enter a URL or 'q' to quit: gitlabint.fintek.local
Valid URL entered: gitlabint.fintek.local
[-] Allowing addition of root certificates
[-] Getting root certificate of 'gitlabint.fintek.local'
 [+] Subject: mkcert osboxes@osboxes (osboxes.org)
 [+] Expires on: Feb 11 08:10:48 2033 GMT
 [+] Certificate written to 'gitlabint.fintek.local.crt'
[-] Adding 'gitlabint.fintek.local.crt' to Keychain
YES (0)
YES (0)
[-] Adding 'gitlabint.fintek.local.crt' to Ruby
 [+] Copying 'gitlabint.fintek.local.crt' to '/Users/appcircle/.rbenv/versions/2.7.5/openssl/ssl/certs'
 [+] Rehashing 'gitlabint.fintek.local.crt' via /Users/appcircle/.rbenv/versions/2.7.5/openssl/bin/c_rehash
Doing /Users/appcircle/.rbenv/versions/2.7.5/openssl/ssl/certs
[-] Adding 'gitlabint.fintek.local.crt' to Java Keystore
Certificate was added to keystore
[-] Verifying connection to 'gitlabint.fintek.local'
 [+] Verification successful!'
Enter a URL or 'q' to quit: q
%
```

:::info

NodeJS doesn't use the system CA store so you need to take extra steps.

For self-sigend certificates, you have two options:

1. Add the `NODE_EXTRA_CA_CERTS="rootCA.pem"`  environment variable. It is possible to add multiple certificates in a single file.
2. Add the `NODE_TLS_REJECT_UNAUTHORIZED=0` environment variable. This completely disables SSL verification (not recommended).

:::
