---
title: Overview & Concepts
metaTitle: Overview & Concepts
metaDescription: Overview & Concepts
sidebar_position: 1
---

# Overview

Self-hosted runner enables you to use your own systems and infrastructure for running Appcircle build pipelines. By this way, you can build and test your apps on your choice of architectures. You have full control over the build environment especially for hardware and operating system.

Self-hosted runners can be physical (bare-metal) machines or virtual machines. You should choose your hardware configurations that meet your needs with enough processing power and memory to run your build jobs.

To get started:

- Provide your own platform to install Appcircle self-hosted runner
- Install and register self-hosted runner to Appcircle infrastructure

The only requirement for using self-hosted runners is to be in **Enterprise** plan. See [pricing](https://appcircle.io/pricing) and feature comparison table for details.

## Differences Between Appcircle-hosted and Self-hosted Runners

**Appcircle-hosted runners:**

- Receive automatic updates for the operating system
- Has some operating system level optimizations
- Preinstalled packages and tools regularly updated
- Are managed and maintained by Appcircle
- Provide a clean, isolated instance for every build job
- Can take longer to start your build (waiting in queue)

**Self-hosted runners:**

- Can use your own local or cloud machines for build job
- Customizable to your hardware, operating system, and security requirements
- Don't need to have a clean instance for every build job (reusable caches)
- Not waiting in build queue for other users' build jobs (private queue)

## Runner Pools

Runner pools are a way of grouping may runners with similar build capabilities and assigning them to build profiles with a single click. You can group and organize your runners according to installed platform tools, operating systems or architectures. You can use any number of pools for your needs.

You can use any text for your pool naming according to your requirements. Pools are added automatically while adding self-hosted runners. Then you will find your runner and its pool in "Build > Self-hosted Runners" list. When your runner is ready for build, you can choose your runner pool from "Build Profile > Config" section and send build jobs to those group of runners.
