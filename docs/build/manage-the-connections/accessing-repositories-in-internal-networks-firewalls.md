---
title: Accessing Internal Networks
description: Learn how to access repositories within internal networks and behind firewalls in Appcircle
tags: [internal networks, firewalls, repository access]
sidebar_position: 3
---

# Accessing Repositories Within Internal Networks

In certain cases, the source codes of the apps may be stored in internal repositories instead of the cloud providers. If these internal repositories are accessible from the public internet, then you can use Appcircle without any additional configuration.

However, if your repositories are within an internal network/behind a firewall, which is usually the case with enterprises, the network configuration of these repositories must be configured for external access.;

Appcircle requires direct access to the repositories for the following use cases:

- For retrieving the repository information such as the branches and the commits.
- For cloning the repository to the build agent during the build.

If the repositories cannot be exposed to the public internet in general, the following Appcircle platform IP addresses must be allowed through the firewall (whitelisted) to access such repositories:

- 34.147.2.16
- 162.19.204.13
- 77.92.96.46
- 77.92.124.2/27

:::caution

If the provided IP address is a subnet defined in CIDR notation, you need to allow the entire subnet on your network.

For example, 77.92.124.2/27 means all IP addresses between 77.92.124.1 and 77.92.124.30 (`77.92.124.1`, `77.92.124.2`, `77.92.124.3`, and so on, all the way to and including `77.92.124.30`) that must be whitelisted on your firewall.

:::

You can then [connect to the repository](/build/manage-the-connections/adding-a-build-profile#connect-your-repository) with your favorite Git provider.
