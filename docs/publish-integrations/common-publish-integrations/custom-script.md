---
title: Custom Script (Publish Flow)
sidebar_label: Custom Script
description: Allows you to create custom Publish flows that are not available in the default steps.
tags: [custom script, publish, customized publish flow]
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Screenshot from '@site/src/components/Screenshot';
import RunnerUsage from '@site/docs/\_publish-steps-runner-usage-caution.mdx';

# Custom Script

You can use the **Custom Script** steps to add extra functionalities in your [Publish flow](/publish-module/publish-flow). Appcircle will execute the commands specified in your custom scripts, allowing you to perform custom actions. These scripts will run on the runner, giving you access to all the capabilities of the publish environment.

The guidelines detailed in the **Custom Script** documentation for [Build Workflow](/workflows) also apply to the Custom Script in [Publish](/publish-module). Therefore, this document will not repeat those details. For comprehensive information about the Custom Script step, please visit the link below:

<RunnerUsage />

<ContentRef url="/workflows/common-workflow-steps/custom-script">
Custom Script Step in Build Workflow
</ContentRef>

## FAQ

### How can I print the status of publish steps with detailed information?

If you want to track or share the status of your publish steps during a publish flow, you can use the following environment variable:  

- **`$AC_PUBLISH_STEPS_STATUS`**: Displays detailed information about each executed publish step.  

:::caution

Please ensure that when writing scripts, you only include conditions for existing statuses, considering the possibility of new statuses being added in the future. For example, while supporting a condition like `if step_status == 'Success'`, avoid using a generic negation such as `if step_status != 'Success'` for handling other statuses.

:::

However, the output of `$AC_PUBLISH_STEPS_STATUS` is in raw JSON format, which may not be easy to read directly. To make it more readable, you can use the following Ruby script to format and print the information in a user-friendly way:

```ruby
require 'json'

# Read the environment variable
json_data = ENV['AC_PUBLISH_STEPS_STATUS']

begin
  # Parse and beautify the JSON
  parsed_data = JSON.parse(json_data)
  pretty_json = JSON.pretty_generate(parsed_data)
  
  # Output the formatted JSON
  puts "AC_PUBLISH_STEPS_STATUS:"
  puts pretty_json
rescue JSON::ParserError => e
  puts "Failed to parse JSON: #{e.message}"
end
```

:::info

The script above is written in Ruby. To execute it, select `Ruby` as the `Execute with` option in the **Custom Script** step.

<Screenshot url="https://cdn.appcircle.io/docs/assets/publishflow-custom-script-faq-0.png" />

:::

If you add a **Custom Script** step in your publish flow, the script will generate an output similar to this:

```json
AC_PUBLISH_STEPS_STATUS:
[
  {
    "StepName": "Get Approvel via Email",
    "StepId": "qwertyu-iopa-sdfg-hjkl-zxcvbnm",
    "StepStatus": "NotStarted",
    "Duration": 0.133102,
    "StartDate": "2024-12-30T16:48:47.919386Z",
    "FinishDate": "2024-12-30T16:48:48.052488Z"
  },
  {
    "StepName": "Distribute to Track",
    "StepId": "qwertyu-iopa-sdfg-hjkl-zxcvbnn",
    "StepStatus": "Success",
    "Duration": 1.90708,
    "StartDate": "2024-12-30T16:48:48.186532Z",
    "FinishDate": "2024-12-30T16:48:50.093612Z"
  }
]
```

:::info

Steps that are disabled in the publish flow will not appear in the above output. The `NotStarted` status is assigned to enabled steps that were not executed when running only specific steps instead of the entire publish flow.

:::

Simply include this script in your publish flow to better understand and monitor the status of your publish steps.