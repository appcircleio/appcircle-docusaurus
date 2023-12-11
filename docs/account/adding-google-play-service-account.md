---
title: Adding a Google Play Service Account
metaTitle: Adding a Google Play Service Account
metaDescription: Adding a Google Play Service Account
sidebar_position: 6
---

import Screenshot from '@site/src/components/Screenshot';

# Adding a Google Play Service Account

Google Service Account is required to upload your binary to Google Play Store. This JSON key must be added to your account to publish apps to Google Play.

1. Please go to [Google Cloud Platform](https://console.cloud.google.com/apis) and create a Google Cloud Project.

2. Enable the Google Play Developer API for your Google Cloud Project. Login with your account, then head over to **Credentials -> Create Credentials**, and then click **Service account**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service01.png' />

3. This screen will forward you to the **Create service account** page. Fill in the details of your service account. According to the service name you set, an automatic **Service account ID** will be created.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service03.png' />

4. Please select `Editor` in the Role dropdown.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service04.png' />

5. Click Done to save this account.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service05.png' />

6. Click **Manage service accounts** to open manage page.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service05-1.png' />

7. Find the account you have just created. Click three dots on the Actions column, and then click **Manage keys**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service06.png' />

8. Click **ADD KEY** and then click **Create new key**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service07.png' />

9. Download your key as JSON and save it.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service08.png' />

10. Switch to the **PERMISSIONS** tab and click on **GRANT ACCESS**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service09.png' />

11. Select the email, generated in step 6 in the **Add principals** field then click **SAVE** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service09-1.png' />

12. Go to [Google Play Console](https://play.google.com/console) and login with your account and then head over to **User and permissions** and then click **Invite new users**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service09-2.png' />

13. Add the email, generated in step 6 in the **E-mail address** field.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service12.png' />

14. Check the permissions of your user and make sure this account has access to **Releases**, **Store presence** and **App access** (for read-only ones) then click **Invite User**.

<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service11-1.png' />
<Screenshot url='https://cdn.appcircle.io/docs/assets/google-service11.png' />

Your account key is ready. To add a key, go to [My Organization](./my-organization.md) and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "Google Play Developer API Keys" item under the Connections section.