---
title: Build Cache
description: Learn how to manage the build cache in Appcircle
tags: [cache, my organization, build cache]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

The Artifacts section also allows you to manually clear cached files created during the build process. This helps resolve unexpected caching issues or reduce storage usage.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE7404-10.png' />

:::danger Cache Deletion Scope

Clearing caches from a main organization also removes all associated caches from its sub-organizations.

If you only want to remove caches for a specific sub-organization, make sure to perform the action within that sub-organization.
This helps prevent unintended data removal across related organizations.

:::

Clearing the cache only removes temporary build data. It does not affect build artifacts, logs, or published applications.

:::info Permission Required

Only users with **Manager** or **Owner** roles in the build can use the Clean Build Caches feature. For more information, please refer to the [Role Management](/account/my-organization/profile-and-team/role-management#build-permissions) documentation.

:::

:::tip Cache Limit by Plan

The build cache limit shown on the screen is determined by your subscription plan. For example:

- **Starter**: 5GB
- **Developer**: 10GB
- **Professional**: 20GB
- **Enterprise**: 30GB
- **Self-hosted**: Customizable (see the [documentation](https://docs.appcircle.io/self-hosted-appcircle/install-server/linux-package/configure-server/advanced-configuration/cache-size-configuration))

:::

For more detailed information on how to use **Cache Pull** and **Cache Push** in Appcircle builds, please refer to the following documentation:
- [Cache Pull](/workflows/common-workflow-steps/build-cache/cache-pull)
- [Cache Push](/workflows/common-workflow-steps/build-cache/cache-push)

Regularly clearing your build cache can help maintain a healthy and efficient build environment.

## FAQ

### Why am I seeing a "cache limit exceeded" error even though my cache usage is not full?

Even if your sub-organization has not used the entire cache limit, other sub-organizations or the main organization may have. The cache limit is shared across the entire organization.

To view the full cache usage and identify which part of the organization is consuming the cache, please visit the **main organization**.

#### Example:

- Your sub-organization may show low usage:
  <Screenshot url='https://cdn.appcircle.io/docs/assets/BE7404-12.png' />

- But the main organization may show that the overall limit has been reached:
  <Screenshot url='https://cdn.appcircle.io/docs/assets/BE7404-11.png' />