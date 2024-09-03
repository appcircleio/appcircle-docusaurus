---
title: Setting Up Appcircle Enterprise App Store Action
sidebar_label: Enterprise App Store
description: Enhance powerful action to publish your builds to appcircle app store
tags:
  [
    overview,
    concepts,
    app store,
    internal testing,
    beta testing,
    binary distribution,
    ipa distribution,
    apk distribution,
    github-marketplace,
  ]
sidebar_position: 2
---

The Appcircle Enterprise App Store action allows users to publish their apps to appcircle app store.

## System Requirements

**Compatible Agents:**

- macos-14 (arm64)
- Ubuntu-22.04

:::caution
Currently, plugins are only compatible to use with **Appcircle Cloud**. **Self-hosted** support will be available in future releases.
:::

### Discover Action

You can discover more about this action and install it from:
https://github.com/marketplace/actions/appcircle-enterprise-store

### How to Add the Appcircle Enterprise App Store Action to Your Pipeline

To use the Appcircle Enterprise App Store action, add the following step to your pipeline at the end:

```yml
- name: Publish App to Appcircle Enterprise App Store
  id: store-publish-to-appcircle
  uses: appcircleio/appcircle-enterprise-app-store-githubaction
  with:
    personalAPIToken: ${{ secrets.AC_PERSONAL_API_TOKEN }}
    appPath: APP_PATH
    summary: SUMMARY
    releaseNotes: RELEASE_NOTES
    publishType: PUBLISH_TYPE # "0": None, "1": Beta, "2": Live
```

- `personalAPIToken`: The Appcircle Personal API token is utilized to authenticate and secure access to Appcircle services, ensuring that only authorized users can perform actions within the platform.
- `appPath`: Indicates the file path to the application package that will be uploaded to Appcircle Testing Distribution Profile.
- `releaseNotes`: Contains the details of changes, updates, and improvements made in the current version of the app being published.
- `summary`: Used to provide a brief overview of the version of the app that is about to be published.
- `publishType`: Specifies the publishing status as either none, beta, or live, and must be assigned the values "0", "1", or "2" accordingly.

:::caution
If two workflows start simultaneously, the last workflow to reach the publish step will be the up-to-date version on the Enterprise App Store. If these workflows building the same package version, the first publish will be successful, while later deployments with the same version will fail.
:::

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with **secrets.NAME** in your task inputs. The action automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal API Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

- For more detailed instructions and support, visit the [Appcircle Enterprise App Store documentation](/enterprise-app-store).
