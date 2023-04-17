---
title: Self-Signed Certificates
metaTitle: Self-Signed Certificates
metaDescription: Self-Signed Certificates
sidebar_position: 8
---

# Overview

If you're using self-signed certificates for your Self-Hosted Installation, the same certificates must also be added to runners. If you don't add and trust those self-signed certificates, your build may fail.

# Adding Certificates

The following script will allow you to add custom certificates by connecting to the given URL address and extracting the public certificate.

- Stop all runners
- Start your template image
- Transfer below script to the runner. You may use scp to transfer it:

```bash
scp ~/Desktop/install_cert.sh AppcircleVM.local:/Users/appcircle/
```
- Run the script as root

The script connects to the given host and extracts the root CA. Then, it adds this root certificate to the following locations:

- Keychain (macOS)
- ca-certificates,update-ca-trust (Linux)
- Ruby's CERT directory
- Java's cacerts directory

:::info

NodeJS doesn't use the system CA store. If you're using a self-signed certificate, you have two options:

1. Add the `NODE_EXTRA_CA_CERTS="rootCA.pem"`  environment variable. It is possible to add multiple certificates in a single file.
2. Add the `NODE_TLS_REJECT_UNAUTHORIZED=0` environment variable. This completely disables SSL verification (not recommended).

:::

```bash
#!/bin/bash
set +x

UNAME=$(uname)
echo "[+] OS: $UNAME"
if [ "$(id -u)" -ne 0 ]; then echo "Please run as root." >&2; exit 1; fi

# Add certificate to macOS Keychain
function add_cert_macos() {
    CERT=$1
    echo "[-] Adding '$CERT' to Keychain"
    # Allow additiong of root certificate without GUI
    sudo security authorizationdb write com.apple.trust-settings.admin allow
    # trustAsRoot and trustRoot are different
    sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain old.crt
    # Set the old rule back
    sudo security authorizationdb remove com.apple.trust-settings.admin
}

# Add certificate to Linux Distros
function add_cert_linux() {
    CERT=$1
    echo "[-] Adding '$CERT' to Keychain"

    if [[ -f /etc/redhat-release ]]; then
        # Redhat or Fedora
        sudo cp $CERT /etc/pki/ca-trust/source/anchors/
        sudo update-ca-trust
    elif [[ -f /etc/SuSE-release ]]; then
        # Suse
        sudo cp $CERT /etc/pki/trust/anchors/
        sudo update-ca-certificates
    elif [[ -f /etc/lsb-release ]]; then
        # Ubuntu or Debian
        sudo cp $CERT /usr/local/share/ca-certificates/
        sudo update-ca-certificates
    else
        echo "[!] Unsupported operating system"
    fi
}

# Add certificate to Java Keystore
function add_cert_keystore() {
  CERT=$1
  echo "[-] Adding '$CERT' to Java Keystore"
  DESC=$(openssl x509 -in "$CERT" -noout -subject | sed -n '/^subject/s/^.*CN=//p')
  filename="${CERT%.*}"
  # if the cert doesn't have subject, we will set its alias to filename
  $JAVA_HOME/bin/keytool -import -noprompt -trustcacerts \
          -keystore  $JAVA_HOME/jre/lib/security/cacerts \
          -storepass changeit -keypass changeit \
          -alias "${DESC:-$filename}" \
          -file $CERT
}

# Add certificate to Ruby
function add_cert_ruby() {
    CERT=$1
    echo "[-] Adding '$CERT' to Ruby"
    CERT_DIR=$(ruby -ropenssl -e 'puts OpenSSL::X509::DEFAULT_CERT_DIR')
    CHASH_PATH="$(dirname "$(dirname "$CERT_DIR")")/bin/c_rehash"
    echo " [+] Copying '$CERT' to '$CERT_DIR'"
    cp "$CERT" "$CERT_DIR"
    echo " [+] Rehashing '$CERT' via $CHASH_PATH"
    $CHASH_PATH
}

# Verify certificate against host
function verify_cert() {
    HOST=$1
    echo "[-] Verifying connection to '$HOST'"
    result=$(security verify-cert -v "https://$HOST" 2>&1)
    if echo "$result" | grep -q "certificate verification successful"; then
        echo " [+] Verification successful!'"
    else
        echo " [!] Verification failed!"
        echo "$result"
    fi
}

# Get certificate for given host
function get_cert() {
    HOST=$1
    PORT=${2:-443}
    if [ -z "$HOST" ]
    then
        echo "[!] Invalid syntax"
        echo "Syntax: get_cert host port"
        exit 1
    fi
    # Remove https if it exists
    HOST=$(echo "$1" | sed -E -e 's/https?:\/\///' -e 's/\/.*//')
    echo "[-] Allowing addition of root certificates"
    echo "[-] Getting root certificate of '$HOST'"
    openssl s_client -showcerts -connect "$HOST:$PORT" </dev/null 2>/dev/null|openssl x509 -outform PEM > "$HOST.crt"
    echo " [+] Subject: $(openssl x509 -in "$HOST.crt" -noout -subject | sed -n '/^subject/s/^.*CN=//p')"
    echo " [+] Expires on: $(openssl x509 -in "$HOST.crt" -noout -enddate | cut -d= -f 2)"
    echo " [+] Certificate written to '$HOST.crt'"
    if [[ $UNAME == 'Darwin' ]]; then
      add_cert_macos "$HOST.crt"
    elif  [[ $UNAME == 'Linux' ]]; then
      add_cert_linux "$HOST.crt"
    else
      echo " [!] Unsupported OS: $UNAME"
      exit 1
    fi
    add_cert_ruby "$HOST.crt"
    add_cert_keystore "$HOST.crt"
    verify_cert "$HOST"
}

while true; do
  read -rp "Enter a URL or 'q' to quit: " url
  if [[ $url == q || $url == Q ]]; then
    exit 0
  elif curl --output /dev/null --silent --head --fail "$url"; then
    echo "Valid URL entered: $url"
    get_cert "$url"
  else
    echo "Invalid URL. Please try again."
  fi
done

```