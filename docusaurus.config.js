// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');
const remarkoembed = require('@agentofuser/remark-oembed');
const rlc = require('remark-link-card');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Appcircle Docs',
  tagline: 'Guides and Docs for Appcircle.io',
  url: 'https://docs.appcircle.io',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'appcircleio', // Usually your GitHub org/user name.
  projectName: 'appcircle-docusaurus', // Usually your repo name.

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          remarkPlugins: [remarkoembed.default, rlc],
          // Please change this to your repo.
          editUrl: 'https://github.com/appcircleio/appcircle-docusaurus/tree/master/',
          routeBasePath: '/',
        },
        blog: false,
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: '',
        logo: {
          alt: 'Appcircle Docs',
          src: 'https://cdn.appcircle.io/docs/logo.svg',
        },
        items: [
          {
            type: 'doc',
            docId: 'intro',
            position: 'left',
            label: 'Documentation',
          },
          {
            type: 'doc',
            docId: 'updates/release-notes',
            position: 'left',
            label: 'Release Notes',
          },
          {
            href: 'https://appcircle.io',
            label: 'Appcircle.io',
            position: 'right',
          },
          {
            href: 'https://github.com/appcircleio/appcircle-docusaurus',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        logo: {
          src: 'https://cdn.appcircle.io/docs/docs-footer-logo.png',
          alt: 'Facebook Open Source Logo',
          href: 'https://appcircle.io',
          width: 40,
          height: 40,
        },
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Documentation',
                type: 'doc',
                to: '/',
              },
              {
                label: 'Release Notes',
                type: 'doc',
                to: 'updates/release-notes',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Slack',
                href: 'https://slack.appcircle.io',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/appcircleio',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/appcircleio/appcircle-docusaurus',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Appcircle, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        additionalLanguages: ['ruby'],
      },
      algolia: {
        apiKey: '0664a9795ced4a4b187cd8b010ec9f5d',
        indexName: 'appcircle',
        appId: 'MLYVQZS3BY',
      },
    }),
};

module.exports = config;
