---
title: Custom Script
description: Use Custom Script steps for additional functionalities in your builds.
tags: [custom scripts, build, test, workflow, step]
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Screenshot from '@site/src/components/Screenshot';

# Custom Script

You can use **Custom Script** steps for additional functionalities in your builds. Appcircle will run the commands in your custom scripts and perform the specified actions. These scripts will be run on the runner and you can use any functionality of the build environment as you need.

:::tip
Note that you can put the **Custom Script** component anywhere you want in the workflow. This step is used to add different capabilities to the existing workflow.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customScript.png' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customInput.png' />

| Variable Name | Description                                                                                                                                                                                                         | Status   |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `Execute`     | You can run your script as **`Bash`** or **`Ruby`** with two different language environments in the **Execute With** input value.                                                                                   | Required |
| `Script`      | With the **Script** input variable, you can add the script you want to run and run it directly in the selected language. If you leave this input blank, it will proceed to the next step without taking any action. | Optional |

:::caution
Note that the **Script** area works according to the selected language variable. If you want to run a script in any language, make sure that you select the language correctly.
:::

## Custom Script FAQ

### How to change Java version

This feature has been introduced as a component, so there is no need to use **Custom Script** for this task. For more details, see:

- [Change Java Version](/workflows/common-workflow-steps/change-java-version)

However, if you prefer to update or improve it manually on **Custom Script**, the source code is available here:

- [Change Java Version - Source Code](https://github.com/appcircleio/appcircle-change-java-version-component)

### How to install a new package to the build machine?

You can use the compatible package managers to install packages.

For the macOS build machines for iOS builds, \_brew \_is a commonly used package manager with commands like `brew install maven`

For the Linux (Debian) build machines for Android builds, _apt-get_ can be used for 3rd party packages such as `apt-get -y install maven`

### How to change the package name/application ID dynamically?

With custom scripts, you can edit the Info.plist and the build.gradle files.

<Tabs>
  <TabItem value="ios" label="iOS" default>

```bash title="iOS sample for Info.plist"
cd $AC_REPOSITORY_DIR/Your-Target-Folder
/usr/libexec/PlistBuddy -c "Set :CFBundleIdentifier io.myapp" "./Info.plist"
```

  </TabItem>
  <TabItem value="android" label="Android">

```bash title="Android sample for build.gradle"
cd $AC_REPOSITORY_DIR/app
sed -i '' 's/old-value/new-value/g' build.gradle
```

  </TabItem>
</Tabs>

### How to access a file in the repository directory?

For each step in the workflow, you can view the input and output variables in the step configuration.

The repository directory is an output of the Git Clone step and its patch can be accessed with the `AC_REPOSITORY_PATH` environment variable by any step added after the Git Clone step. An example is as follows:

```bash
cd $AC_REPOSITORY_DIR
cat README
```

### How to a add a file as a downloadable build artifact?

You can add any file to the output directory that contain the build artifacts using the `AC_OUTPUT_DIR` environment variable. An example is as follows:

```bash
cd $AC_REPOSITORY_DIR/app/build/reports/
mv lint-results* $AC_OUTPUT_DIR/
```

### How to break pipeline on low test coverage

This document provides a sample custom script written in Ruby that can be integrated into your CI/CD pipeline to enforce a minimum test coverage threshold. The script is designed to break the pipeline if the covered test result falls below a specified percentage.

:::danger
Please note that this custom script must be placed after the [**Test Reports**](https://docs.appcircle.io/continuous-testing/android-testing/running-android-unit-tests#generating-test-report) step in the workflow.
:::

```ruby
require 'json'

def env_has_key(key)
    !ENV[key].nil? && ENV[key] != '' ? ENV[key] : abort("Missing #{key}.")
end

output_dir = env_has_key('AC_OUTPUT_DIR')

def read_json_file(test_result_file_path)
  JSON.parse(File.read(test_result_file_path))
end

def extract_line_coverage(json_data)
  json_data['coverage']['lineCoverage']
end

begin
test_result_file_path = "#{output_dir}/test_results.json"
json_data = read_json_file(test_result_file_path)
line_coverage = extract_line_coverage(json_data)

puts "Current Line Coverage: % #{line_coverage * 100}"

min_coverage = 2.0
puts "Minimum coverage percentage: #{min_coverage}"

if (line_coverage * 100) < min_coverage
    puts "Coverage is #{line_coverage} and below minimum coverage percentage given #{min_coverage}. \nExiting."
    exit (1)
else
    puts "Coverage is above the threshold. It is clear."
end

rescue StandardError => e
  puts "An error occurred: #{e.message}"
end
```

:::info

Please feel free to edit the following variables according to your own requirements:

- `test_result_file_path`: The file path of the test result file from which to retrieve the covered percentage value.
- `min_coverage`: The minimum percentage required for the pipeline to continue without breaking.

:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-custom-script-component/

### How to use environment variables along with the `sudo` command?

Both user-created and Appcircle-reserved [environment variables](/environment-variables/managing-variables) can be used within a custom script with any required command. But, by default, commands that are triggered with `sudo` will not reach them since the user scope is changed.

In order to use all user environment variables with `sudo`, you should add the `-E` argument to the `sudo` command. The `-E` (preserve environment) option indicates to the security policy that the user wishes to preserve their existing environment variables.

For instance, you can check the list of environment variables in the build pipeline using the command below.

```bash
sudo -E printenv
```

### How can I send a custom email?

Appcircle provides a **ready-to-use email** structure in the [**Testing Distribution**](/testing-distribution/create-or-select-a-distribution-profile#share-binary) and [**Publish**](/publish-integrations/common-publish-integrations/get-approval-via-email) modules. This structure varies across the two modules. If desired, the user can customize this structure by using the [**Custom Script**](/workflows/common-workflow-steps/custom-script) below to send their own custom email.

The following Bash script is set to use a **Gmail SMTP Server**. For more information, please visit [**Gmail SMTP Server**](https://support.google.com/a/answer/176600?hl=en) documentation. 

```bash

# Set SMTP server 
CS_HOST="smtp.gmail.com"
CS_PORT="587"
CS_ACCOUNT="gmail"

# Make sure to replace CS_EMAIL, CS_USERNAME, and CS_PASSWORD with your account details
CS_EMAIL="your-email-address@gmail.com"
CS_USERNAME="your-email-address@gmail.com"
CS_PASSWORD="your-email-password"

# Set email details
CS_EMAIL_SUBJECT="Test Email Subject"
CS_EMAIL_TO="recipient-address@mail.com,recipient-2-address@mail.com"
# This part will be used for visualization
CS_EMAIL_FROM="Sender Name <sender-address@gmail.com>"
CS_EMAIL_BODY="This is the body of the sent email."
# Set TLS and SSL usage
CS_USE_TLS="True"
CS_USE_SSL="False"

# Detect operating system
os=""
if uname -a | grep -iq "darwin"; then
    os="darwin"
elif uname -a | grep -iq "linux"; then
    os="linux"
fi

# Create the .msmtprc file with appropriate permissions
cat <<EOF > ~/.msmtprc
defaults
auth on
tls on
EOF

# Check if OS is supported and install necessary packages
if [ "$os" == "darwin" ]; then
    if ! command -v brew > /dev/null 2>&1; then
        echo "Can't find brew installation; make brew command visible or install homebrew and try again."
        exit 1
    fi
    brew install mailutils
    brew install msmtp
    echo "set sendmail=/usr/local/bin/msmtp" | sudo tee -a /etc/mail.rc
    { echo -n "tls_fingerprint " && msmtp --serverinfo --tls --tls-certcheck=off --host=$CS_HOST --port=$CS_PORT | egrep -o "([0-9A-Za-z]{2}:){31}[0-9A-Za-z]{2}"; } >> ~/.msmtprc
elif [ "$os" == "linux" ]; then
    if ! command -v apt > /dev/null 2>&1; then
        echo "Apt is not installed; install apt and try again."
        exit 1
    fi
    apt-get update
    apt-get install -y mailutils msmtp msmtp-mta
    echo "tls_trust_file /etc/ssl/certs/ca-certificates.crt" >> ~/.msmtprc
else
    echo "Unsupported OS: $os. Darwin or Linux was expected."
    exit 1
fi

cat <<EOF >> ~/.msmtprc
logfile ~/.msmtp.log
account $CS_ACCOUNT
host $CS_HOST
port $CS_PORT
from $CS_EMAIL
user $CS_USERNAME
password $CS_PASSWORD
account default: $CS_ACCOUNT
EOF

# Restrict permissions for the .msmtprc file to avoid security issues
chmod 600 ~/.msmtprc

# Cleanup .msmtprc whether script ends with success or failure
function cleanup {
  cat /dev/null > ~/.msmtprc
}
trap cleanup EXIT

# Send email
echo "From: $CS_EMAIL_FROM
To: $CS_EMAIL_TO
Subject: $CS_EMAIL_SUBJECT
$CS_EMAIL_BODY" | msmtp --debug --from=$CS_EMAIL -t $CS_EMAIL_TO

```

:::info Script Execution

This script is written in `Bash`. When running with **Custom Script**, you need to set the `Execute With` parameter as `Bash`. For more information, please visit the [**Custom Script Input Variables**](/workflows/common-workflow-steps/custom-script#input-variables) documentation section.

:::

:::note Input Variables
When using your own SMTP server credentials for the three variables below, using **Environment Variables** is strongly suggested since this prevents sensitive information, such as passwords, from being exposed to unauthorized individuals.

For more detailed information, please refer to the [**Environment Variables**](/environment-variables/managing-variables) documentation.

- **$CS_EMAIL**: SMTP Server email address.
- **$CS_USERNAME**: Sender email address.
- **$CS_PASSWORD**: Sender email address password.

Otherwise, to send an email, you need to have some information, such as the email subject, sender email, and recipient email. You can use these parameters to:

- **$CS_EMAIL_SUBJECT**: Subject of sending email
- **$CS_EMAIL_TO**: Recipient email address.
- **$CS_EMAIL_FROM**: Sender email address.
- **$CS_EMAIL_BODY**: Content of sending email.

:::

:::tip Recipient Email Address

If you want to send an email to multiple email addresses instead of a single email address, in the `$CS_EMAIL_TO` parameter, it will be enough to write all the addresses to send an email separated by commas. For example, `$CS_EMAIL_TO=example@email.com,example2@email.com`

:::

:::danger Sensitive Informations

Since the variables mentioned above, which need to be provided by the user, contain **sensitive** information like **passwords**, please use [**Environment Variables**](/environment-variables/managing-variables#adding-key-and-text-based-value-pairs) for these types of values.

To do this, comment out or remove the sensitive variables such as `$CS_EMAIL`, `$CS_USERNAME`, and `$CS_PASSWORD` defined at the top of the script, and add them as environment variables instead.

For other variables that need to be defined, you can also make use of environment variables.

:::

:::caution Self-hosted Runners

If you're using self-hosted runners and they're not starting to build pipelines with clean states as in Appcircle Cloud, this custom script can be insecure to use since the consecutive pipelines are using the same build environment, and it might have last sent email sensitive configuration in some cases.

In order to send email, the script persists SMTP configuration to the `~/.msmtprc` file. Although the script has a cleanup mechanism that works for success or failure cases, it cannot work on all conditions. For example, the "cancel build" case should be considered. In this case, the `~/.msmtprc` might not be cleaned, and it can be read in the next pipeline.

If you have configured runners similar to the Appcircle Cloud pools and they are wiped off after a build is executed to provide a fresh environment for every build, then there is nothing to consider; it's safe.

:::

:::info Username and Password for Google SMTP Users

When you want to send an email with your Gmail account using **Google's SMTP** server, you must first **authenticate** to the Google SMTP server. For this process, you need to enter your **App Password** in the password field.

In order to generate this password, **2FA authentication** must be turned on in your **Google account**. You can generate and retrieve this password from the **App Passwords** section under **Google Account management**. For detailed information about **App Passwords**, please visit the [**Google App Password**](https://support.google.com/accounts/answer/185833?hl=en) documentation.

:::

:::tip Protocols and SMTP Host

This script uses the TLS protocol for SMTP server usage. Since the **Gmail SMTP** server is used in the script, the required protocols are pulled from **Google's SMTP** server using the `$CS_HOST` parameter. If you are using your own SMTP server, don't forget to change the `$CS_HOST` value here.

On the other hand, to change **TLS or SSL** usage, you can change the protocol by setting the `$CS_USE_TLS` or `$CS_USE_SSL` parameters in the script to `true` or `false`. Note that you need to change the `$CS_PORT` parameter when using **SSL** and **TLS**.

For more information about protocols, please visit the [**Google's TLS and SSL**](https://support.google.com/a/answer/100181) documentation.

:::

:::danger Sender Email and Spoofing

To use an SMTP server, this script first installs the necessary certificates, then authenticates to the server with the required credentials and sends the prepared email content to the recipient's email address. In order to change the sender's email address, the SMTP server must allow it by providing the necessary permissions. Otherwise, SMTP servers will send the email using the authenticated email address to prevent spoofing (impersonating someone else).

:::

### How can I send the Appcircle build log to another platform?

To send your build log to another platform using an API, you can access the log in your workflow through `$AC_LOGFILE`.

Here is an example using Dropbox's [file-upload](https://www.dropbox.com/developers/documentation/http/documentation#files-upload) API. Replace it with the appropriate API for your platform. If you are going to use DropBox, you can follow the document below to obtain the access token:
- [Generate an access token for your own account](https://dropbox.tech/developers/generate-an-access-token-for-your-own-account)

:::danger

Ensure sensitive data, like access tokens, are defined as private environment variables. Learn more:
- [Adding key and text-based value pairs](/environment-variables/managing-variables#adding-key-and-text-based-value-pairs)

:::

```bash
current_datetime=$(date +"%Y-%m-%d-%H-%M")
dropbox_log_filename="/home/appcircle-logs/ac-log-$current_datetime.txt"

curl -X POST https://content.dropboxapi.com/2/files/upload \
    --header "Authorization: Bearer $DROPBOX_ACCESS_TOKEN" \
    --header "Dropbox-API-Arg: {\"autorename\":false,\"mode\":\"add\",\"mute\":false,\"path\":\"$dropbox_log_filename\",\"strict_conflict\":false}" \
    --header "Content-Type: application/octet-stream" \
    --data-binary @"$AC_LOGFILE"

```
This script generates a timestamped log file (e.g., `ac-log-2024-10-01-14-55.txt`) in the `/home/appcircle-logs` in Dropbox.

<Screenshot url="https://cdn.appcircle.io/docs/assets/workflow-custom-script-faq-1.png" />

:::caution

Ensure that the **Custom Script** step runs after the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step to capture the full log.

:::