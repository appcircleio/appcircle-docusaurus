---
title: Check Network Access
description: Check the network access with external sources for the Appcircle build module.
tags: [network, build tools, external services, curl, network access, proxy, ssl]
---

import Screenshot from '@site/src/components/Screenshot';

# Check Network Access

This component checks network access to common build endpoints used in Appcircle workflows. It validates connectivity to package managers, build services, APIs, and custom-defined URLs during build time.

This component uses the URLs listed in the [Network section](/self-hosted-appcircle/install-server/linux-package/configure-server/integrations-and-access/network-access) to validate access to external resources during the build on the Appcircle runner

The code checks predefined or custom URLs using `curl`, allows adding extra URLs via step inputs, logs details for non-2xx HTTP responses, and fails only on network or server errors.

:::info

- `2xx` responses indicate successful requests.

- `3xx` responses are logged as WARN (network is reachable, but the service may not respond as expected).

- `4xx`/`5xx`  responses and curl transport errors (exit codes, timeouts, DNS issues, SSL errors) are treated as FAIL and stop the build.

The curl exit code is also used to determine whether the connection was established. If HTTP responses are received, their headers and bodies are logged (truncated) for further details.

:::

### Prerequisites

There are no prerequisites required before using the **Check Network Accessibility** step.

:::tip

Note that you can put the **Check Network Accessibility** component anywhere you want in the workflow. This code is used to check the accessibility of predefined endpoints and report their status.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6281-wf2.png' />

### Input Variables

This step contains some input variable(s). It needs these variable(s) to work. The table below gives explanation for this variable(s).

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6281-comp2.png' />

| Variable Name                                              | Description                                                                                                                                                           | Status   |
| ---------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_CHECK_NETWORK_GITHUB_APPCIRCLE`                       | If enabled, checks if the runner can access to `https://github.com/appcircleio/`. Default: `true`.                                                                    | Optional |
| `$AC_CHECK_NETWORK_RUBYGEMS`                               | If enabled, checks if the runner can access to `https://rubygems.org`. Default: `true`.                                                                               | Optional |
| `$AC_CHECK_NETWORK_INDEX_RUBYGEMS`                         | If enabled, checks if the runner can access to `https://index.rubygems.org`. Default: `true`.                                                                         | Optional |
| `$AC_CHECK_NETWORK_SERVICES_GRADLE_ORG`                    | If enabled, checks if the runner can access to `https://services.gradle.org`. Default: `true`.                                                                        | Optional |
| `$AC_CHECK_NETWORK_DL_GOOGLE_COM_ANDROID_REPOSITORY`       | If enabled, checks if the runner can access to `https://dl.google.com/android/repository/repository2-1.xml`. Default: `true`.                                         | Optional |
| `$AC_CHECK_NETWORK_DL_SSL_GOOGLE_COM_ANDROID_REPOSITORY`   | If enabled, checks if the runner can access to `https://dl-ssl.google.com/android/repository/repository2-1.xml`. Default: `true`.                                     | Optional |
| `$AC_CHECK_NETWORK_MAVEN_GOOGLE_COM`                       | If enabled, checks if the runner can access to `https://maven.google.com/web/index.html`. Default: `true`.                                                            | Optional |
| `$AC_CHECK_NETWORK_REPO1_MAVEN_ORG_MAVEN2`                 | If enabled, checks if the runner can access to `https://repo1.maven.org/maven2/`. Default: `true`.                                                                    | Optional |
| `$AC_CHECK_NETWORK_CDCOAPODS_ORG`                          | If enabled, checks if the runner can access to `https://cdn.cocoapods.org`. Default: `true`.                                                                          | Optional |
| `$AC_CHECK_NETWORK_GITHUB_COCOAPODS_SPECS`                 | If enabled, checks if the runner can access to `https://github.com/CocoaPods/Specs`. Default: `true`.                                                                 | Optional |
| `$AC_CHECK_NETWORK_FIREBASEAPPDISTRIBUTION_GOOGLEAPIS_COM` | If enabled, checks if the runner can access to `https://firebaseappdistribution.googleapis.com/$discovery/rest?version=v1`. Default: `true`.                          | Optional |
| `$AC_CHECK_CONNECTION_TIMEOUT`                             | Specifies the maximum time (**integer**, in seconds) allowed for establishing a connection to the server before the request is aborted. Default: `8` seconds.         | Optional |
| `$AC_CHECK_CONNECTION_MAX_TIMEOUT`                         | Specifies the maximum total time (**integer**, in seconds) allowed for the entire request (including connection, data transfer, and response). Default: `20` seconds. | Optional |
| `$AC_CHECK_NETWORK_EXTRA_URL_PARAMETERS`                   | Additional URLs to check, defined as a comma-separated list (e.g. `https://url1.com`, `https://url2.com`).                                                            | Optional |

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-check-network-access-component

---
