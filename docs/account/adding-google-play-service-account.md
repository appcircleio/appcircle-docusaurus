---
title: Adding a Google Play Service Account
metaTitle: Adding a Google Play Service Account
metaDescription: Adding a Google Play Service Account
sidebar_position: 5
---

# Adding a Google Play Service Account

Google Service Account is required to upload your binary to Google Play Store. This JSON key must be added to your account to publish apps to Google Play.

1. Please go to Go to [Google Play Console](https://play.google.com/console) and login with your account and then head over to **Setup -> API Access** and then click **Create new service account**

![](<https://cdn.appcircle.io/docs/assets/google-service01.png>)

2. This screen will forward you to **Google Cloud Platform** Click **Create Service account** to create your account.

![](<https://cdn.appcircle.io/docs/assets/google-service02.png>)

3. Fill in the details of your service account. According to the service name you set, an automatic **Service account ID** will be created.

![](<https://cdn.appcircle.io/docs/assets/google-service03.png>)

4. Please select `Editor` in the Role dropdown.

![](<https://cdn.appcircle.io/docs/assets/google-service04.png>)

5. Click Done to save this account

![](<https://cdn.appcircle.io/docs/assets/google-service05.png>)

6. Find the account you have just created. Click three dots on the Actions column and then click **Manage keys**.

![](<https://cdn.appcircle.io/docs/assets/google-service06.png>)

7. Click **ADD KEY** and then click **Create new key**

![](<https://cdn.appcircle.io/docs/assets/google-service07.png>)

8. Download your key as JSON and save it

![](<https://cdn.appcircle.io/docs/assets/google-service08.png>)

9. Go back to Google Play Console and click **Grant Access** to give access 

![](<https://cdn.appcircle.io/docs/assets/google-service09.png>)

10. Select the app from the list and click **Apply**

![](<https://cdn.appcircle.io/docs/assets/google-service10.png>)

11. Check the permissions of your account key and make sure this account has access to Releases and then click **Invite User**

![](<https://cdn.appcircle.io/docs/assets/google-service11.png>)

Your account key is ready. To add a key, go to [My Organization](./my-organization.md) and press the "Add New" button (or the "Manage" button first if you have saved keys) next to the "Google Play Developer API Keys" item under the Connections section.