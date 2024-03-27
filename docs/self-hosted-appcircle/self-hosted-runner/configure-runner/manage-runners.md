---
title: Managing Runners
metaTitle: Managing Runners
metaDescription: Managing Runners
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';

### Monitoring Self-hosted Runners

When you add a new self-hosted runner to your organization, it appears at "Self-hosted Runners" list with `Offline` state. You can see your runner in list with given name and pool from CLI.

After configuring and starting runner service, it becomes `Online` on list.

Self-hosted runners list has also other quick details which give your overview for your runners.

- "Version" is your self-hosted runner's version, you got from CLI.

```bash
./ac-runner --version
```

- "Last Contact" shows when Appcircle cloud has last contact with your self-hosted runner.

- "State" shows your self-hosted runner's current build status. For example, it can be `idle` when runner is waiting for a build job and `running` when it's executing build job.

<Screenshot url='https://cdn.appcircle.io/docs/assets/self-hosted-runner-runners-01.png' />

You can **disable** self-hosted runner from list, using toggle button on right-hand side. When runner is disabled, it won't accept build job anymore. Disabling runner, doesn't affect currently running build pipeline on runner. It will complete its executing job. When complete, it won't take any new build job from queue until you **enable** it again. Using same toggle button you can enable self-hosted runner.

With quick enable/disable feature, you can remove self-hosted runner from pool temporarily and make some maintenance or debugging. When ready, you can add the self-hosted runner to pool again without any CLI operation.

:::warning

Your pool should have at least one active (ready-to-build) runner for build pipeline continuity.

If your pool is assigned to an active build profile but doesn't have any active runners, started build jobs from that profile will wait in queue until timeout.

For this reason, you should think about your pool organization and build profile settings while removing or disabling self-hosted runners.

:::

### Move Self-hosted Runner Between Pools

For some reason, you may need to move your runner from one pool to another. For this purpose, use below command:

```bash
./ac-runner install -p ${Runner Pool}
```

Runner pool argument must be new target pool to move self-hosted runner.

If there is no runner left in old pool, it will be deleted automatically and disappear from build profile pool selection list.

If new target pool doesn't exist, it will be created automatically.

:::info

Moving self-hosted runner from one pool to another doesn't require service restart. Change will be activated immediately without any manual intervention.

:::

### Delete Self-hosted Runner

If you want to remove your self-hosted runner for any reason, click on runner name to open details view. Here you can see details of your runner. (its pool, create and update times etc.)

<Screenshot url='https://cdn.appcircle.io/docs/assets/self-hosted-runner-runner-detail-01.png' />

Click on delete button at the bottom of the page. A confirmation dialog will be visible for your approval. Type runner name into textbox and click on delete.

Deleting runner removes it from pool and it's unreachable from Appcircle cloud. If you want to add same runner again to the same pool or another pool, you need to register and configure it again. See, [add self-hosted runner](../installation.md) page for details.

:::info

Removing or deleting runner from pool doesn't affect running build job on that runner. On-going build job will be completed but that runner won't get any new build job from queue.

:::

:::info

If there is no runner left in self-hosted pool, it will be deleted automatically and disappear from build profile pool selection list.

:::

:::warning

When a self-hosted pool is deleted from organization for any reason, its related build profiles will return to `default` pool automatically which is Appcircle cloud. So, build jobs will go on with Appcircle-hosted runners automatically.

:::

### Adding Xcode After Install

You can add more Xcode versions side-by-side or more up-to-date Xcode any time after installation.

```bash
./ac-runner xcode -v ${Xcode Version}
```

Xcode version argument is similar to xcode argument on [installation](../installation.md#3-configure). You can give one or more versions comma-separated.

For example, below command will install Xcode 13.1.x:

```bash
./ac-runner xcode -v 13.1
```

For example, below command will install both Xcode 13.1.x and 12.5.x side-by-side:

```bash
./ac-runner xcode -v 13.1,12.5
```

:::info

Adding Xcode to self-hosted runner doesn't require service restart. Newly added Xcode versions will be enabled immediately without any manual intervention.

:::
