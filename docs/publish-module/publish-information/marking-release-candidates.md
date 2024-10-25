---
title: Marking Release Candidates
description: Learn how to mark a version as a release candidate in Appcircle
tags: [publish information, release candidate, mark as rc]
sidebar_position: 3
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

### Mark Version as Release Candidate

Appcircle allows you to mark your app version as RC and designate any version as a **Release Candidate** with ease by simply selecting the desired app version and clicking on the **Mark as RC** button.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3857-pub2.png' />

:::caution
In order to execute a flow, it must be marked as a Release Candidate (RC). If it is not marked as RC, it cannot be executed.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3103-norc.png' />

The chosen version will be visibly distinguished, allowing users to easily identify it as a `Release Candidate`.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-release-candidate.png' />

:::tip

If you configure an app version with `Auto Publish=On` in its build configurations within the build module before distribution to the Publish profile, Appcircle will automatically mark the app version as a `Release Candidate` and execute the Publish Flow operation directly.

Please note that this is valid for auto-published app versions. Any app version that was uploaded manually via UI or API can not be marked as `Release Candidate` automatically.

:::
