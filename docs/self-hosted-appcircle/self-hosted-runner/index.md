---
title: Overview
metaTitle: Overview
metaDescription: Overview
sidebar_position: 1
---


Self-hosted runner enables you to use your own systems and infrastructure for running Appcircle build pipelines. By this way, you can build and test your apps on your choice of architectures. You have full control over the build environment especially for hardware and operating system.

Self-hosted runners can be physical (bare-metal) machines or virtual machines. You should choose your hardware configurations that meet your needs with enough processing power and memory to run your build jobs.

To get started:

- Provide your own platform to install Appcircle self-hosted runner
- Install and register self-hosted runner to Appcircle infrastructure

:::warning

The only requirement for using self-hosted runners is to be in `enterprise` plan.

See [pricing](https://appcircle.io/pricing) and feature comparison table for details.

:::

### Differences Between Appcircle-hosted and Self-hosted Runners

**Appcircle-hosted runners:**

- Receive automatic updates for the operating system
- Has some operating system level optimizations
- Preinstalled packages and tools regularly updated
- Are managed and maintained by Appcircle
- Provides a clean instance for every build job
- Can take longer to start your build (waiting in queue)

**Self-hosted runners:**

- Can use your own local or private cloud machines for build job
- Customizable to your hardware, operating system, and security requirements
- Don't need to have a clean instance for every build job (reusable caches)
- Not waiting in build queue for other users' build jobs (private queue)

:::info
On self-hosted runners, you can have a clean and isolated instance for each build, just like Appcircle Cloud.

In this case, we recommend running a single runner per (virtual) machine for better isolation if you need concurrency. Using a well established virtualization infrastructure, such as a virtual machine or Docker container, for self-hosted runner helps you to run every build on a clean state.
:::

## Runner Pools

Runner pools are a way of grouping many runners with similar build capabilities and assigning them to build profiles with a single click. You can group and organize your runners according to installed platform tools, operating systems or architectures. You can use any number of pools for your needs.

You can use any text for your pool naming according to your requirements. Pools are added automatically while adding self-hosted runners. Then you will find your runner and its pool in "Build > Self-hosted Runners" list. When your runner is ready for build, you can choose your runner pool from "Build Profile > Config" section and send build jobs to those group of runners.

## Limitations

Self-hosted runner usage is limited with your current plan's monthly quotas. Same hard limits of `enterprise` plan is applied to both self-hosted and Appcircle-hosted runners.

For example, you can not start a new build when you exceeded the number of builds that can be initiated in a month. Your self-hosted runners will be kept in your organization. You can manage them and you can add new runners, but can not use them for build job. When your monthly quotas are renewed, you can go on with self-hosted builds.

When your `enterprise` plan expires or doesn't renew on time, self-hosted runner usage will also be limited with your downgraded plan. In this case, you can not build apps with self-hosted runners although your build quota is sufficient. You can't add new self-hosted runners even if you have runner access token created previously before downgrade. You can see list of existing self-hosted runners but can not see pool or runner details. You can't delete any pool or runner and can't enable or disable any runner.

Your existing self-hosted runners will be kept in system as-is and won't be removed by us. When you upgrade to `enterprise` plan again, you can go on using your self-hosted runners as usual.

If you don't upgrade to `enterprise` plan, you can only use Appcircle-hosted runners which is default pool.
