---
title: Troubleshooting & FAQ
description: Troubleshooting & FAQ
tags: [api, authentication, personal api token, api token, session token, troubleshooting, faq]
sidebar_position: 5
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Overview

This section is designed to help you quickly find answers to common questions and provide you with a better understanding of Appcircle server API.

## Appcircle Server API FAQ

### How can I check the versions of an app published in the Enterprise App Store and download it?

After you have successfully [created the Personal API Token](/appcircle-api/api-authentication.md#generatingmanaging-the-personal-api-tokens) from the **root organization**, you can check the versions of an application and download them, like in the following example code blocks.

:::caution
You must create the PAT (Personal API Token) on the root organization. Requests will fail if you create the PAT from a sub-organization.
:::

<Tabs
defaultValue="bash"
groupId="language"
values={[
{label: 'Bash', value: 'bash'},
{label: 'Python', value: 'python'},
]}>

<TabItem value="bash">

<details>
  <summary>Click to see the code block.</summary>
  <p>

```bash
#!/usr/bin/env bash

set -uo pipefail

PERSONAL_API_TOKEN="SuperSecretPatTakenFromRootOrganization=="
# Please be cautious, URLs shouldn't end with '/'.
API_URL="https://api.appcircle.io" # API URL for Appcircle cloud
AUTH_URL="https://auth.appcircle.io" # AUTH URL for Appcircle cloud
STORE_URL="https://mycustomstoredomain.appcircle.io" # Your default or custom store URL on Appcircle cloud.

echo -e "Authenticating to the $AUTH_URL \n"
TOKEN_JSON_RESPONSE=$(curl -fs -X POST "${AUTH_URL}/auth/v1/token" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "pat=$PERSONAL_API_TOKEN")
if [[ "$?" != "0" ]]; then
  echo "Couldn't authenticate to the $API_URL with the PAT."
  echo "Please check your PAT."
  echo "If you are a self-hosted Appcircle user, please change the 'API_URL', 'AUTH_URL' and 'STORE_URL'"
  exit 1
fi

ACCESS_TOKEN=$(echo "$TOKEN_JSON_RESPONSE" | jq -j '.access_token')

echo -e 'Getting profiles... \n'

PROFILE_RESPONSE=$( curl -fs "${API_URL}/store/v1/profiles" \
  -H "authorization: Bearer $ACCESS_TOKEN"
)
if [[ "$?" != "0" ]]; then
  echo "Couldn't get the Enterprise App Store profiles."
  echo "Please check your connection."
  exit 1
fi

PROFILE_ID=$(echo "$PROFILE_RESPONSE" | jq -r '.[0].id') # Get the first element for test responses. You should filter by ids here for your needs.
echo "Enterprise App Store profile id:  $PROFILE_ID"
echo -e "Getting app versions... \n"

APP_VERSION_RESPONSE=$( curl -fs "$API_URL/store/v1/profiles/$PROFILE_ID/app-versions?suborg=all" \
  -H "authorization: Bearer $ACCESS_TOKEN"
)
if [[ "$?" != "0" ]]; then
  echo "Couldn't get versions of the selected Enterprise App Store application."
  echo "Please check your connection."
  exit 1
fi

APP_VERSION_ID=$(echo "$APP_VERSION_RESPONSE" | jq -r '.[0].id') # Get the first element for test responses. You should filter by ids here for your needs.
APP_OS_TYPE=$(echo "$APP_VERSION_RESPONSE" | jq -r '.[0].platformType') # Get the first element for test responses. You should filter by ids here for your needs.
APP_OS=""
APP_OUTPUT_FILE=""
echo "App version id:  $APP_VERSION_ID"
if [[ "$APP_OS_TYPE" == "1" ]]; then
  APP_OS="ios"
  APP_OUTPUT_FILE="app.plist"
else
  APP_OS="android"
  APP_OUTPUT_FILE="app.apk"
fi
echo "App OS:  $APP_OS" # 1 for iOS, 2 for Android.
echo -e "Getting app download link... \n"

echo "Downloading the app to the $APP_OUTPUT_FILE file."
  curl -fs --location "$STORE_URL/api/profile/$PROFILE_ID/appversions/$APP_VERSION_ID/download-update" \
    --header "Authorization: Bearer $ACCESS_TOKEN" \
    -o "$APP_OUTPUT_FILE"
```

  </p>
</details>

</TabItem>

<TabItem value="python">

<details>
  <summary>Click to see the code block.</summary>
  <p>

```python
import requests
import sys
import json

PERSONAL_API_TOKEN = "SuperSecretPatTakenFromRootOrganization=="
# Please be cautious, URLs shouldn't end with '/'.
API_URL = "https://api.appcircle.io" # API URL for Appcircle cloud
AUTH_URL = "https://auth.appcircle.io" # AUTH URL for Appcircle cloud
STORE_URL = "https://mycustomstoredomain.appcircle.io" # Your default or custom store URL on Appcircle cloud.

def main():
    print(f"Authenticating to {AUTH_URL}\n")
    try:
        token_response = requests.post(
            f"{AUTH_URL}/auth/v1/token",
            headers={"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"},
            data={"pat": PERSONAL_API_TOKEN}
        )
        token_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Couldn't authenticate to {API_URL} with the PAT.")
        print("Please check your PAT.")
        print("If you are a self-hosted Appcircle user, please change the 'API_URL', 'AUTH_URL', and 'STORE_URL'")
        sys.exit(1)

    access_token = token_response.json().get("access_token")

    print('Getting profiles...\n')
    try:
        profile_response = requests.get(
            f"{API_URL}/store/v1/profiles",
            headers={"authorization": f"Bearer {access_token}"}
        )
        profile_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Couldn't get the Enterprise App Store profiles.")
        print("Please check your connection.")
        sys.exit(1)

    profiles = profile_response.json()
    if not profiles:
        print("No profiles found.")
        sys.exit(1)

    profile_id = profiles[0].get("id")
    print(f"Enterprise App Store profile id: {profile_id}")

    print("Getting app versions...\n")
    try:
        app_version_response = requests.get(
            f"{API_URL}/store/v1/profiles/{profile_id}/app-versions?suborg=all",
            headers={"authorization": f"Bearer {access_token}"}
        )
        app_version_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print("Couldn't get versions of the selected Enterprise App Store application.")
        print("Please check your connection.")
        sys.exit(1)

    app_versions = app_version_response.json()
    if not app_versions:
        print("No app versions found.")
        sys.exit(1)

    app_version_id = app_versions[0].get("id")
    app_os_type = app_versions[0].get("platformType")
    app_os = "ios" if app_os_type == "1" else "android"
    app_output_file = "app.plist" if app_os == "ios" else "app.apk"

    print(f"App version id: {app_version_id}")
    print(f"App OS: {app_os}")  # 1 for iOS, 2 for Android.
    print("Getting app download link...\n")

    print(f"Downloading the app to the {app_output_file} file.")
    try:
        download_response = requests.get(
            f"{STORE_URL}/api/profile/{profile_id}/appversions/{app_version_id}/download-update",
            headers={"Authorization": f"Bearer {access_token}"},
            stream=True
        )
        download_response.raise_for_status()
        with open(app_output_file, "wb") as f:
            for chunk in download_response.iter_content(chunk_size=8192):
                f.write(chunk)
    except requests.exceptions.RequestException as e:
        print(f"Couldn't download the app: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

```

  </p>
</details>

</TabItem>

</Tabs>

:::tip
If you are a self-hosted Appcircle server user, you can change the required URL variables for your own needs and use the same method.
:::

:::caution
Please create the PAT from the root organization. If you do not create it from the sub-organization, you will not be able to download the app versions available in the Enterprise App Store profiles of either the root organization or the organization where you created the PAT.
:::
