---
title: Setting Up Appcircle Enterprise Store Action
sidebar_label: Enterprise App Store
description: Enhance powerful action to publish your builds to appcircle app store
tags:
  [
    testing-distribution,
    overview,
    concepts,
    app store,
    internal testing,
    beta testing,
    binary distribution,
    ipa distribution,
    apk distribution,
  ]
sidebar_position: 2
---

The Appcircle Enterprise Store action allows users to publish their apps to appcircle app store

### Discover Action

You can discover more about this action and install it by:
https://github.com/marketplace/actions/appcircle-enterprise-store

To install the Appcircle Enterprise Store action, add the following step to your pipeline at the end:

```yml
- name: Publish App to Appcircle
  id: appcircle-store-publishment
  uses: ./
  with:
    accessToken: ${{ secrets.AC_ACCESS_TOKEN }} # Appcircle Access Token
    entProfileId: ${{ secrets.AC_PROFILE_ID }} # Enterprise Profile Id
    appPath: "APP_PATH" # Your App Path
    summary: "SUMMARY" # Your Summary
    releaseNotes: "RELEASE_NOTE" # Your Release Note
    publishType: "1" # 0: None, 1: Beta, 2: Live
```

:::caution Build Steps Order
You should add this task extension after completing your build steps.
:::

## Leveraging Environment Variables

Utilize environment variables seamlessly by substituting the parameters with **secrets.NAME** in your task inputs. The action automatically retrieves values from the specified environment variables within your pipeline.

## References

- For details on generating an Appcircle Personal Access Token, visit [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens)

- To create or learn more about Appcircle testing and distribution profiles, please refer to [Creating or Selecting a Distribution Profile](/distribute/create-or-select-a-distribution-profile)
