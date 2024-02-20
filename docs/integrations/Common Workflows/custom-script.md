---
title: Custom Script
metaTitle: Custom Script
metaDescription: Custom Script
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Custom Script

You can use custom scripts for additional functionalities in your builds. Appcircle will run the commands in your custom scripts and perform the specified actions. These scripts will be run on the build agent and you can use any functionality of the virtual machine as you need.

:::tip
Note that you can put the **Custom Script** component anywhere you want in the workflow. This step is used to add different capabilities to the existing workflow.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customScript.png' />

### Input Variables

- You can run your script as **`Bash`** or **`Ruby`** with 2 different technologies in the Execute With input value. 

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customExecute.png' />

- With the Script input variable you can add the script you want to run and run it directly in the selected language.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customArea.png' />

:::caution
Note that the Script area works according to the selected language variable. If you want to run a script in any language, make sure that you select the language correctly.
:::

https://github.com/appcircleio/appcircle-custom-script-component/