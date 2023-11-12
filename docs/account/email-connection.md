---
title: Email Connection and Notifications Subscription
metaTitle: Email Connection and Notifications Subscription
metaDescription: Email Connection and Notifications Subscription
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Email Connection and Notifications Subscription

This feature allows users with specified email addresses to be notified by email of the actions specified in Appcircle (starting a build, adding an IOS certificate, the store submission process, etc.).

:::info

Appcircle email notification can work independently for each module. For example, you can send notifications to different people for events under the Build module and to different people for store submission operations.

You can also define more than one email address for a module and send notifications.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/email-notify-all-2.png' />

# Email Notifications: Unsubscribe

To cancel email notifications, you can click the unsubscribe button in the notification email, or you can delete the email address for the relevant module by following the steps below:

**My Organization -> Integrations -> Email -> Manage**

<Screenshot url='https://cdn.appcircle.io/docs/assets/email-manage.png' />

:::info
If the user unsubscribes via email, the relevant email will be deleted directly from the module. If you want to send notifications, you will need to add the email address again.
:::
