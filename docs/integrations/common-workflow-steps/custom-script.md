---
title: Custom Script
metaTitle: Custom Script
metaDescription: Custom Script
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';

# Custom Script

You can use **Custom Script** steps for additional functionalities in your builds. Appcircle will run the commands in your custom scripts and perform the specified actions. These scripts will be run on the build agent and you can use any functionality of the virtual machine as you need.

Please check this document for samples of **Custom Script** that can be used: [**Custom Script Samples**](https://docs.appcircle.io/integrations/working-with-custom-scripts/custom-script-samples/).

For frequently asked questions about **Custom Script**, please visit this page: [**Custom Script FAQ**](https://docs.appcircle.io/integrations/working-with-custom-scripts/custom-script-faq/).

:::tip
Note that you can put the **Custom Script** component anywhere you want in the workflow. This step is used to add different capabilities to the existing workflow.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customScript.png' />

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2793-customInput.png' />


| Variable Name  | Description                                    | Status   |  
|----------------|------------------------------------------------|----------|
| `Execute`      | You can run your script as **`Bash`** or **`Ruby`** with two different technologies in the **Execute With** input value. | Required |
| `Script`       | With the **Script** input variable, you can add the script you want to run and run it directly in the selected language. If you leave this input blank, it will proceed to the next step without taking any action. | Optional |

:::caution
Note that the **Script** area works according to the selected language variable. If you want to run a script in any language, make sure that you select the language correctly.
:::

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-custom-script-component/