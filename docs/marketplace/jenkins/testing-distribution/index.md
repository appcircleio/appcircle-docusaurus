---
title: Setting Up Appcircle Testing Distribution Plugin
sidebar_label: Testing Distribution
description: Enhance powerful plugin to distribute your builds to appcircle
tags:
  [
    testing-distribution,
    ipa distribution,
    apk distribution,
    binary distribution,
  ]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

The Appcircle Testing Distribution plugin allows users to upload their apps and start distribution to test groups or individuals.

### Install Appcircle Testing Distribution Plugin

Go to your Jenkins dashboard and follow, Manage Jenkins > Plugins and search for "Appcircle Testing Distribution"

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-installation_steps.png' />

### Add Plugin in Build Steps

Go to your configuration page of the project add a build step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-add_pannel.png' />

### Configure Plugin

After adding the plugin into your build steps make sure you fulfill required inputs.
Also, do not forget to add the plugin after your build steps. Because you will be asked to provide the build path.

<Screenshot url='https://cdn.appcircle.io/docs/assets/sp-158-configure_pannel.png' />

### Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with `$(VARIABLE_NAME)` in your task inputs. The extension automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal Access Token, visit [Generating/Managing Personal API Tokens](https://docs.appcircle.io/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens)

For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](https://appcircle.io/enterprise-app-store).
