---
title: Accessing Repositories in Internal Networks (Firewalls)
metaTitle: Accessing Repositories in Internal Networks (Firewalls)
metaDescription: Accessing Repositories in Internal Networks (Firewalls)
sidebar_position: 3
---
# Accessing Repositories in Internal Networks (Firewalls)

In certain cases, the source codes of the apps may be stored in internal repositories instead of the cloud providers. If these internal repositories are accessible from the public internet, then you can use Appcircle without any additional configuration.

However, if your repositories are within an internal network/behind a firewall, which is usually the case with enterprises, the network configuration of these repositories must be configured for external access.;

Appcircle requires direct access to the repositories for the following use cases:

* For retrieving the repository information such as the branches and the commits.
* For cloning the repository to the build agent during the build.

If the repositories cannot be exposed to the public internet in general, the following Appcircle platform IP addresses must be allowed through the firewall (whitelisted) to access such repositories:

* 34.147.2.16

You can then [connect to the repository through SSH](../build/adding-a-build-profile/#connect-your-repository) just like connecting to any Git provider.
