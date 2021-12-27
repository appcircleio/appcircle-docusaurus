---
title: 'Custom Script Samples'
metaTitle: 'Custom Script Samples'
metaDescription: 'Custom Script Samples'
---

# Custom Script Samples

### Deploying Apps to Firebase App Distribution

Appcircle Distribute module provides an integrated and automated enterprise-grade solution for distributing apps to the testers, but if you want to use other solutions for app distribution, you can do so with custom scripts. You can use the following script below to deploy apps to Firebase App Distribution automatically from the Appcircle Build module.

- The binary to be deployed can be obtained with the related environment variable. `AC_EXPORT_DIR` and the binary path.
- `FIREBASE_TOKEN` must be obtained through a local console. Please follow the [instructions here](https://firebase.google.com/docs/cli#cli-ci-systems) to set up the Firebase CLI locally and then you can request a token with the `firebase login:ci `command.
- `FIREBASE_APP_ID` can be obtained from the Firebase Dashboard under the settings screen:

![](<https://cdn.appcircle.io/docs/assets/image (133).png>)

The sample script is as follows:

{% tabs %}
{% tab title="Bash" %}

```bash
#!/usr/bin/env bash
#
# Deploy a binary to Firebase App Distribution
#
npm install -g firebase-tools

firebase appdistribution:distribute $AC_EXPORT_DIR/Runner.ipa --app $FIREBASE_APP_ID --release-notes "Release Notes..." --token $FIREBASE_TOKEN --groups "testers"
```

{% endtab %}
{% endtabs %}

### Send email notification when a build is complete

You can send notification emails when your build is complete so that you or your teammates will know the build status.

Here's a sample Bash script to send emails from a custom script step:

{% tabs %}
{% tab title="Bash" %}

```bash
#!/usr/bin/env bash
#
# Send an email when a build is completed in Appcircle.
#

# Email address for the receipent
RCP_ADDRESS="receipent@example.com"
CC_ADDRESS="cc_receipent@example.com"

# Subject line for email
EMAIL_SUBJECT="Appcircle Build"

# Send a corresponding email for successful builds.

echo "Build completed successfully, sending email notification."
echo -e "Your build in Appcircle is completed successfully." | mail -s "Build completed with success." ${RCP_ADDRESS} -c ${CC_ADDRESS}
echo "Email notification sent."
```

{% endtab %}
{% endtabs %}

###

### Send Slack notification when a build is complete

Appcircle supports a wide range of options for sending notifications to Slack, but you can also send any custom messages to Slack with custom scripts.

If you have a Slack webhook created, you can send a message to your Slack channel with a single line of Bash script.

You can refer to Slack's webhook documentation here: :link: [**Creating Slack webhooks**](https://api.slack.com/tutorials/slack-apps-hello-world)\*\*\*\*

{% tabs %}
{% tab title="Bash" %}

```bash
#!/usr/bin/env bash
#
# Send a Slack notification when a build is completed in Appcircle.
#

curl -X POST -H 'Content-type: application/json' --data '{"text":"Appcircle build is completed successfully!"}' SLACK_WEBHOOK_URL
```

{% endtab %}
{% endtabs %}
