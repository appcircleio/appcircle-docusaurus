---
title: Hardening the macOS Host
description: Use the harden-host.sh script to apply a safe security baseline to the physical macOS machine that runs your Appcircle self-hosted runner VMs.
tags:
  [
    self-hosted runner,
    macos,
    host hardening,
    security,
  ]
sidebar_position: 6
---

# Hardening the macOS Host

When you run iOS builds on a self-hosted runner, the physical macOS machine (the host) runs your build VMs with Tart. The host is long-lived and reachable on your network, so it is the part of the setup worth securing first. The build VMs are disposable and re-created for each build.

The `harden-host.sh` script applies a safe security baseline to that host. It is based on a subset of the CIS macOS Level 1 benchmark and is designed not to break your runner's connectivity.

This page explains what the script does, why it does it, and how to run it.

:::info

The script targets macOS Sequoia and Tahoe (and later) on Apple silicon. Run it on the physical host, not inside a build VM. To harden the build VM image, see the separate guest hardening guidance.

:::

## What the Script Does

The script makes two kinds of changes: settings it can safely apply on its own, and platform protections it only checks and reports.

**Applied automatically:**

- Turns on the macOS application firewall and stealth mode, so the host does not respond to unsolicited network probes.
- Disables sharing services a build host does not need: Remote Management, File Sharing, Printer Sharing, Remote Apple Events, Internet Sharing, and Bluetooth.
- Hardens the login window: disables the guest account, hides the user list (asks for a name and password), removes password hints, and requires a password immediately after sleep.
- Reduces telemetry and tracking: turns off sending analytics and crash reports to Apple, disables the system analytics and diagnostics daemons, limits ad tracking and personalized ads, and disables the Siri, Apple Intelligence, and suggestion agents.
- Blocks known Apple telemetry and analytics domains in `/etc/hosts`. The list is analytics-only and deliberately leaves signing and notarization endpoints untouched, so code signing keeps working.
- Keeps automatic security responses and security data updates enabled, so the host still receives critical protections.

**Checked and reported only:**

- System Integrity Protection (SIP), FileVault, Gatekeeper, and the Secure Boot policy. These cannot be changed safely from a running script, so the script reports their status and warns you if any of them needs attention.

## Why Remote Login Stays Enabled

Appcircle orchestrates builds on the host over SSH, so the script leaves Remote Login (SSH) enabled by default. Disabling it would cut off the runner.

Secure SSH separately instead of turning it off:

- Allow key-based authentication only and disable password login.
- Disallow root login.
- Restrict access to the specific administrator account with `AllowUsers` in `/etc/ssh/sshd_config`.

If your setup does not orchestrate the host over SSH, you can pass `--disable-ssh` to turn Remote Login off.

## Why Screen Sharing Stays Enabled

The script leaves Screen Sharing enabled so you can administer the host remotely. Disabling it would cut off graphical remote access, which is often needed to manage a headless or rack-mounted host.

Restrict it instead of turning it off: limit access to trusted users and reach the host only over a trusted network or VPN. If you do not need remote graphical access, you can disable Screen Sharing manually from System Settings.

## Download the Script

On the host, download `harden-host.sh` from the Appcircle CDN and make it executable:

```bash
curl -fsSL https://cdn.appcircle.io/self-hosted/harden-macos-host.sh -o harden-host.sh && \
  chmod +x harden-host.sh
```

## How to Use It

Run the script as an administrator on the host. It supports three modes.

Review the current security posture without changing anything:

```bash
sudo ./harden-host.sh --audit-only
```

Preview the exact changes the script would make, without applying them:

```bash
sudo ./harden-host.sh --dry-run
```

Apply the baseline:

```bash
sudo ./harden-host.sh
```

To apply the baseline and also disable Remote Login:

```bash
sudo ./harden-host.sh --disable-ssh
```

:::caution

Run `--audit-only` first and review the report. If SIP, FileVault, or Gatekeeper is reported as off, enable it before relying on the host for production builds.

:::

Some changes (limiting ad tracking and disabling the Siri, Apple Intelligence, and suggestion agents) apply to a specific user account. The script uses the account that invoked `sudo`, falling back to the current console user. To target a different account, set `ADMIN_USER`:

```bash
sudo ADMIN_USER=ci-admin ./harden-host.sh
```

## What You Still Need to Do Manually

A few protections cannot be enabled from a script and require your action:

- **SIP:** If reported as disabled, re-enable it from recoveryOS with `csrutil enable`.
- **FileVault:** If reported as off, enable full-disk encryption and store the recovery key safely (ideally through your MDM). For unattended reboots, use `fdesetup authrestart` so the host can come back online without someone entering the password at the screen.

## After Running the Script

Confirm the host is still reachable and the runner still works:

- Verify you can still reach the host over SSH.
- Run a test build to confirm the runner connects and completes a job.

Re-run the script (or at least re-check the audit report) after every macOS update, because updates can reset some of these settings.

## Managing a Fleet with MDM

The script is a good fit for a single host or for preparing a host before it joins a managed fleet. For several hosts, the more durable approach is to enroll them in a Mobile Device Management (MDM) solution and push the security settings as a configuration profile. Profile-based settings are enforced and cannot be removed locally, which keeps every host consistent.

The recommended baseline for this is a CIS Level 1 profile generated with the macOS Security Compliance Project (mSCP), with SSH left enabled for runner access.
