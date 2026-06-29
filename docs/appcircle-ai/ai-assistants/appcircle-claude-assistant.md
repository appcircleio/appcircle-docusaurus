---
title: Appcircle Claude Assistant
description: Use the Appcircle Claude Plugin to connect Claude to the Appcircle platform with MCP tools and Appcircle-aware skills.
tags: [appcircle ai, claude, assistant]
sidebar_position: 3
---

# Appcircle Claude Assistant

Appcircle provides an **Appcircle Claude Plugin** that connects Claude to the Appcircle platform, bundling the [Appcircle MCP Server](/appcircle-ai/appcircle-mcp-server) with Appcircle-aware skills so you can ask Claude about your Appcircle organization or about how to use Appcircle.

https://github.com/appcircleio/appcircle-claude-plugin

## What's Included

- **MCP Server**: registers `mcp.appcircle.io` as an MCP server named `appcircle`, exposing build, signing, distribution, publish, and reporting tools so Claude can query your organization. See [Appcircle MCP Server](/appcircle-ai/appcircle-mcp-server) for the full list of tools.
- **Skills**: Appcircle-aware skills that extend Claude's capabilities. More skills are added over time and are automatically namespaced under `appcircle:`.

| Skill | Purpose |
|-------|---------|
| `appcircle:doc-assistant` | Answers Appcircle questions using official sources (`docs.appcircle.io` and `appcircle.io`) |
| `appcircle:build-insights-report` | Renders a visual Build Insights Report (health & trends, root cause, workflow quality, artifact health, queue time, and CI maturity) from the `get_build_insights_report` MCP tool |

## How to Use Appcircle Claude Assistant

Claude Code and claude.ai install the plugin differently, so follow the steps for the surface you use. MCP tools are only available in Claude Code for now; installing the plugin in claude.ai gets you the `doc-assistant` skill, not the MCP tools.

### In Claude Code

1. *(Optional, for MCP tools)* Before starting Claude Code, set your [Appcircle Access Token](https://github.com/appcircleio/appcircle-mcp/blob/main/docs/appcircle_access_token.md) in your shell so the MCP server can authenticate:
   ```bash
   export APPCIRCLE_ACCESS_TOKEN=<your-access-token>
   ```
   The MCP server reads this from the process environment, so it must be set before you launch `claude`; exporting it later in an already-running session has no effect until you restart.
2. Add the Appcircle marketplace:
   ```shell
   /plugin marketplace add appcircleio/appcircle-claude-plugin
   ```
3. Install the plugin:
   ```shell
   /plugin install appcircle@appcircle
   ```
4. Reload:
   ```shell
   /reload-plugins
   ```
5. Ask Claude an Appcircle question. For "how do I" or troubleshooting questions, for example "How do I set up automatic code signing for my iOS builds," Claude uses the `doc-assistant` skill. For questions about your own organization, for example "List my build profiles," Claude uses the Appcircle MCP tools, which requires step 1.

### In claude.ai

You can install this plugin's skills in claude.ai too. MCP tools remain Claude Code-only for now.

1. Open **Customize**.
2. Click **Add plugin**.
3. Choose **Create plugin**, then **Add marketplace**.
4. Enter the repository URL: `https://github.com/appcircleio/appcircle-claude-plugin`.
5. Ask Claude an Appcircle question, for example "How do I set up automatic code signing for my iOS builds," and Claude will use the `doc-assistant` skill to answer.
