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
- Node.js `NODE_EXTRA_CA_CERTS`

## Adding Certificates

The self-hosted runner has a command-line tool to help you install the required certificates. When called, it connects to the given host via the URL and extracts the root CA. It adds the root CA to the locations listed above.

If your runner version `1.3.12` or later, you can find it in the `scripts` directory inside the Appcircle runner directory.

If your runner version is older than `1.3.12`, then you can follow one of the steps below:

- [Upgrade](../update.md#1-update-runner) the Appcircle runner to `1.3.12` or later

- If you can't upgrade the Appcircle runner, you can [download the latest](../update.md#1-update-runner) runner package and get the script from there after you extract the archive.

Execute the bash script like below.

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

After the script is complete, the operating system, default Java (`11`), Ruby, and Node.js trust the root certificate.

:::caution
Please exit from the current terminal session and start a new one for changes to take effect.
:::

### Adding Certificates Manually

In situations where automatic root certificate detection may not work, the bash script provides a user-friendly manual trust method.

Users can supply the root certificates themselves locally to the tool and import them.

Once imported, the operating system and other tools listed above will trust the certificate, ensuring secure connections to the server, just like getting them from a URL.

If `install_cert.sh` can't auto-detect the root CA from URL, follow the steps below to import it from disk:

- Get your organization's root CA and copy its content.

- Go to the `scripts` directory, which is in the `appcircle-runner` directory.

- Create a file named `rootca.crt` and paste the root CA content inside it.

```bash
vi rootca.crt
```

:::info
Alternatively, you can push the certificate files to the runner disk and use them directly as certificate arguments.
:::

- To use the `install_cert.sh` in manual mode, you should provide the root CA and a URL to test the connection.

```bash
./install_cert.sh <path to the CA cert> <url to test connection>
```

For example, if you saved the root CA in the `rootca.crt` file and want to import and test the connection to the Appcircle server, see the example below:

```bash
./install_cert.sh rootca.crt api.appcircle.spacetech.com
```

After the script completes successfully, the certificate will be trusted in your system.
