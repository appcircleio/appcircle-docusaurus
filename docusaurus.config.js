// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const {themes} = require('prism-react-renderer');

const lightCodeTheme = themes.github;
const darkCodeTheme = themes.dracula;

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
          remarkPlugins: [],
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
            to: '/',
            position: 'left',
            label: 'Documentation',
          },
          {
            to: 'updates/release-notes',
            position: 'left',
            label: 'Release Notes',
          },
          {
            href: 'https://blog.appcircle.io',
            label: 'Blog',
            position: 'right',
          },
          {
            href: 'https://appcircle.io/start',
            label: 'Dashboard',
            position: 'right',
          },
          {
            type: 'dropdown',
            items: [
              {
                label: 'Slack',
                href: 'https://join.slack.com/t/appcircleio/signup',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/appcircleio',
              },
              {
                label: 'LinkedIn',
                href: 'https://www.linkedin.com/company/appcircleio',
              },
            ],
            label: 'Community',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        logo: {
          src: 'https://cdn.appcircle.io/docs/footer-logo-full.png',
          alt: 'Appcircle Logo',
          href: 'https://appcircle.io',
          width: 160,
          height: 33,
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
                href: 'https://join.slack.com/t/appcircleio/signup',
              },
              {
                label: 'Twitter',
                href: 'https://twitter.com/appcircleio',
              },
              {
                label: 'LinkedIn',
                href: 'https://www.linkedin.com/company/appcircleio',
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
        additionalLanguages: ['ruby', 'groovy', 'java','kotlin', 'bash', 'diff', 'json'],
      },
      algolia: {
        apiKey: '0664a9795ced4a4b187cd8b010ec9f5d',
        indexName: 'appcircle',
        appId: 'MLYVQZS3BY',
        contextualSearch: false,
      },
    }),
    plugins: [
      [
        '@docusaurus/plugin-google-analytics',
        {
          trackingID: 'UA-40954643-12',
          anonymizeIP: true,
        },
      ],
      'docusaurus-plugin-sass'
    ],
  
};

module.exports = config;
