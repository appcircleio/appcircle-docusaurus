// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const { themes } = require("prism-react-renderer");
const remarkExternalUrlRef = require("./src/plugins/remark-externalUrlRef");

const lightCodeTheme = themes.github;
const darkCodeTheme = themes.dracula;

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "Appcircle Docs",
  tagline: "Guides and Docs for Appcircle.io",
  url: "https://docs.appcircle.io",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  onBrokenAnchors: "throw",
  onDuplicateRoutes: "warn",
  favicon: "img/favicon.ico",
  organizationName: "appcircleio", // Usually your GitHub org/user name.
  projectName: "appcircle-docusaurus", // Usually your repo name.
  trailingSlash: false,

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          remarkPlugins: [remarkExternalUrlRef],
          // Please change this to your repo.
          editUrl:
            "https://github.com/appcircleio/appcircle-docusaurus/tree/master/",
          routeBasePath: "/",
        },
        blog: false,
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      docs: {
        sidebar: {
          autoCollapseCategories: true,
        },
      },
      navbar: {
        title: "",
        logo: undefined,
        items: [
          {
            type: "html",
            position: "left",
            className: " navbar__logo navbar__item_logo_container",
            value: `
            <a href="https://appcircle.io" target="_blank">
              <svg width="100%" height="100%" viewBox="0 0 281 58" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M88.9329 24.4482C88.9329 21.4846 86.9479 19.8277 83.2025 19.8277C81.2226 19.8277 79.1046 20.3776 76.9282 21.4579C76.8495 21.497 76.7604 21.5427 76.6611 21.595C75.8961 21.9979 74.9484 21.7063 74.5443 20.9437L74.5416 20.9386L73.4839 18.925C73.0832 18.162 73.3777 17.2197 74.1423 16.8187C74.4932 16.6347 74.7824 16.4874 75.01 16.3768C78.1634 14.8449 80.8927 14.1955 84.6295 14.1955C91.5781 14.1955 95.6285 17.7107 95.6792 23.7137L95.7246 39.4952C95.727 40.3576 95.0277 41.0587 94.1625 41.0612H94.158H90.5486C89.6835 41.0612 88.9821 40.3621 88.9821 39.4996V38.2641C87.1101 40.2993 84.2606 41.3547 80.6929 41.3547C75.0522 41.3547 71.2671 37.9111 71.2671 33.0101C71.2671 27.9755 75.0387 24.9593 81.4802 24.9101H88.9329V24.4482ZM82.5136 29.6127C79.1706 29.6127 77.7673 30.5044 77.7673 32.6187C77.7673 34.7006 79.4501 36.0161 82.2183 36.0161C85.7679 36.0161 88.6036 34.1553 88.9329 31.738V29.6127H82.5136ZM114.282 14.2444C121.848 14.2444 126.956 19.7378 126.956 27.873C126.956 35.9134 121.947 41.3058 114.381 41.3058C110.645 41.3058 107.65 39.9063 105.648 37.281V48.9911C105.648 49.8535 104.947 50.5527 104.082 50.5527H100.37C99.5049 50.5527 98.8036 49.8535 98.8036 48.9911V16.0016C98.8036 15.1392 99.5049 14.4401 100.37 14.4401H104.082C104.947 14.4401 105.648 15.1392 105.648 16.0016V18.2568C107.604 15.6475 110.588 14.2444 114.282 14.2444ZM112.855 35.38C117.057 35.38 120.013 32.2062 120.013 27.6773C120.013 23.1903 117.051 20.0234 112.855 20.0234C108.617 20.0234 105.648 23.1828 105.648 27.6773C105.648 32.245 108.594 35.38 112.855 35.38ZM145.675 14.2444C153.24 14.2444 158.348 19.7378 158.348 27.873C158.348 35.9134 153.34 41.3058 145.773 41.3058C142.038 41.3058 139.043 39.9063 137.041 37.281V48.9911C137.041 49.8535 136.34 50.5527 135.474 50.5527H131.763C130.898 50.5527 130.196 49.8535 130.196 48.9911V16.0016C130.196 15.1392 130.898 14.4401 131.763 14.4401H135.474C136.34 14.4401 137.041 15.1392 137.041 16.0016V18.2568C138.997 15.6475 141.98 14.2444 145.675 14.2444ZM144.248 35.38C148.45 35.38 151.405 32.2062 151.405 27.6773C151.405 23.1903 148.443 20.0234 144.248 20.0234C140.01 20.0234 137.041 23.1828 137.041 27.6773C137.041 32.245 139.987 35.38 144.248 35.38ZM180.801 22.197C179.235 20.9344 177.285 20.268 175.023 20.268C170.903 20.268 168.062 23.312 168.062 27.7751C168.062 32.3222 170.891 35.38 175.023 35.38C177.143 35.38 178.952 34.8757 180.364 33.888C180.576 33.7397 180.83 33.5213 181.125 33.2334C181.697 32.6742 182.6 32.6356 183.218 33.1439L185.201 34.7747C185.869 35.3235 185.963 36.3077 185.413 36.9729C185.399 36.9889 185.399 36.9889 185.386 37.0045C184.956 37.4963 184.585 37.8759 184.27 38.1442C181.85 40.2083 178.566 41.3058 174.679 41.3058C166.674 41.3058 161.168 35.8171 161.168 27.824C161.168 19.7504 166.706 14.2444 174.777 14.2444C179.078 14.2444 182.69 15.6326 185.162 18.1879C185.711 18.7552 185.695 19.6586 185.125 20.2057L185.116 20.2147L182.99 22.2215C182.408 22.7704 181.505 22.7937 180.896 22.2753C180.862 22.247 180.831 22.2209 180.801 22.197ZM193.085 3.43195C195.224 3.43195 196.753 4.99795 196.753 7.17763C196.753 9.35731 195.224 10.9233 193.085 10.9233C190.945 10.9233 189.416 9.35731 189.416 7.17763C189.416 4.99795 190.945 3.43195 193.085 3.43195ZM191.229 14.4401H194.94C195.806 14.4401 196.507 15.1392 196.507 16.0016V39.4996C196.507 40.3621 195.806 41.0612 194.94 41.0612H191.229C190.364 41.0612 189.662 40.3621 189.662 39.4996V16.0016C189.662 15.1392 190.364 14.4401 191.229 14.4401ZM214.153 14.3608C214.277 14.3404 214.421 14.3213 214.585 14.3033C215.445 14.2093 216.219 14.8281 216.313 15.6853C216.319 15.7419 216.322 15.7987 216.322 15.8556V19.2395C216.322 20.0864 215.645 20.779 214.795 20.8005C214.575 20.8061 214.391 20.816 214.242 20.83C209.98 21.2302 207.366 24.0845 207.366 28.2154V39.4996C207.366 40.3621 206.665 41.0612 205.8 41.0612H202.088C201.223 41.0612 200.522 40.3621 200.522 39.4996V16.0016C200.522 15.1392 201.223 14.4401 202.088 14.4401H205.8C206.665 14.4401 207.366 15.1392 207.366 16.0016V18.8528C208.896 16.3742 211.209 14.8442 214.153 14.3608ZM236.872 22.2927C236.512 21.9858 236.206 21.7542 235.955 21.5984C234.549 20.7239 232.891 20.268 231.02 20.268C226.9 20.268 224.059 23.312 224.059 27.7751C224.059 32.3222 226.887 35.38 231.02 35.38C233.004 35.38 234.717 34.9382 236.086 34.0709C236.371 33.8902 236.717 33.6055 237.119 33.2173C237.693 32.6653 238.59 32.6301 239.205 33.1357L241.193 34.7704C241.86 35.3192 241.955 36.3034 241.404 36.9687C241.389 36.9871 241.389 36.9871 241.373 37.0052C240.873 37.5722 240.443 38.0041 240.078 38.3019C237.676 40.2648 234.461 41.3058 230.675 41.3058C222.671 41.3058 217.165 35.8171 217.165 27.824C217.165 19.7504 222.703 14.2444 230.774 14.2444C234.662 14.2444 237.992 15.3784 240.427 17.4941C240.608 17.6521 240.819 17.8568 241.06 18.1087C241.656 18.7335 241.632 19.7219 241.005 20.3164L241.002 20.319L238.967 22.2398C238.385 22.7892 237.481 22.812 236.872 22.2927ZM246.129 4.3126H249.841C250.706 4.3126 251.408 5.01172 251.408 5.87414V39.4996C251.408 40.3621 250.706 41.0612 249.841 41.0612H246.129C245.264 41.0612 244.563 40.3621 244.563 39.4996V5.87414C244.563 5.01172 245.264 4.3126 246.129 4.3126ZM268.498 35.7225C270.596 35.7225 272.572 35.0922 274.211 33.9015C274.3 33.837 274.402 33.7578 274.515 33.6639C275.147 33.1436 276.075 33.1965 276.643 33.7855L278.243 35.4443C278.842 36.066 278.823 37.0545 278.199 37.6522C278.184 37.6667 278.168 37.6809 278.153 37.6948C277.534 38.2418 277.011 38.6532 276.581 38.9298C274.168 40.4844 271.224 41.3058 267.957 41.3058C259.711 41.3058 254.201 35.87 254.201 27.824C254.201 19.7676 259.771 14.2444 267.809 14.2444C276.212 14.2444 280.646 19.1798 280.696 27.9159C280.697 28.1219 280.694 28.378 280.684 28.6845C280.659 29.5286 279.966 30.1998 279.119 30.1998H261.253C262.141 33.648 264.854 35.7225 268.498 35.7225ZM274.365 25.4972C274.129 21.8863 271.643 19.632 267.859 19.632C264.291 19.632 261.74 21.8635 261.086 25.4972H274.365Z" fill="white"/>
              <path fill-rule="evenodd" clip-rule="evenodd" d="M21.1088 41.2707C25.5492 44.8808 26.2967 48.7165 23.3514 52.7777C19.7207 57.6676 13.0006 59.4438 7.31228 56.6929L7.26463 56.6698C7.25088 56.6632 7.23714 56.6565 7.22341 56.6498C0.828968 53.5294 -1.81504 45.8366 1.31785 39.4676L8.40874 25.0521L12.3933 16.9517L17.182 7.21641C19.5091 2.48562 24.3626 -0.191959 29.3311 0.0107344C34.1306 -0.00738716 38.75 2.64805 41.0024 7.22705L56.8665 39.4782C59.9994 45.8473 57.3554 53.54 50.961 56.6605C50.9472 56.6672 50.9335 56.6738 50.9197 56.6805L50.8721 56.7035C44.5169 59.7769 36.874 57.1996 33.6902 50.9426C32.04 47.4859 33.1405 44.2231 36.9919 41.1543H36.9906C39.8871 38.8238 41.7395 35.2573 41.7395 31.2598C41.7395 24.2389 36.0252 18.5472 28.9763 18.5472C21.9273 18.5472 16.213 24.2389 16.213 31.2598C16.213 35.3244 18.1282 38.9435 21.1088 41.2707ZM28.9878 37.9223C25.2841 37.9223 22.2817 34.9317 22.2817 31.2428C22.2817 27.5538 25.2841 24.5633 28.9878 24.5633C32.6915 24.5633 35.6939 27.5538 35.6939 31.2428C35.6939 34.9317 32.6915 37.9223 28.9878 37.9223Z" fill="#FF8F34"/>
            </a>
            </svg>
            <svg width="2" height="60%" viewBox="0 0 2 33" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd" clip-rule="evenodd" d="M0 33V0H2V33H0Z" fill="white"/>
            </svg>
            <a href="/">
              <svg width="50" height="100%" viewBox="0 0 114 27" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9.03687 26C16.7929 26 21.2789 21.19 21.2789 13.2354C21.2789 5.31819 16.7929 0.545487 9.29788 0.545487H0.796875V26H9.03687ZM4.63687 22.6442V3.90129H9.06189C14.6299 3.90129 17.5009 7.23219 17.5009 13.2354C17.5009 19.2635 14.6299 22.6442 8.82587 22.6442H4.63687ZM53.7659 13.2727C53.7659 5.13169 48.8939 0.197388 42.3069 0.197388C35.6949 0.197388 30.8349 5.13169 30.8349 13.2727C30.8349 21.4013 35.6949 26.348 42.3069 26.348C48.8939 26.348 53.7659 21.4137 53.7659 13.2727ZM49.9629 13.2727C49.9629 19.4748 46.6819 22.843 42.3069 22.843C37.9199 22.843 34.6509 19.4748 34.6509 13.2727C34.6509 7.07069 37.9199 3.70239 42.3069 3.70239C46.6819 3.70239 49.9629 7.07069 49.9629 13.2727ZM85.2959 8.82319C84.4259 3.37929 80.1629 0.197388 74.7819 0.197388C68.1939 0.197388 63.3339 5.13169 63.3339 13.2727C63.3339 21.4137 68.1689 26.348 74.7819 26.348C80.3749 26.348 84.4639 22.843 85.2959 17.8093L81.4189 17.7969C80.7599 21.0533 78.0249 22.843 74.8059 22.843C70.4439 22.843 67.1499 19.4996 67.1499 13.2727C67.1499 7.09549 70.4309 3.70239 74.8189 3.70239C78.0629 3.70239 80.7849 5.52949 81.4189 8.82319H85.2959ZM109.375 7.23219H113.079C112.967 3.15549 109.363 0.197388 104.192 0.197388C99.0839 0.197388 95.1689 3.11829 95.1689 7.50569C95.1689 11.0479 97.7039 13.1236 101.794 14.2298L104.801 15.0501C107.523 15.771 109.624 16.6658 109.624 18.9279C109.624 21.4137 107.25 23.0543 103.981 23.0543C101.023 23.0543 98.5619 21.7369 98.3379 18.9652H94.4849C94.7339 23.5763 98.3009 26.4226 104.006 26.4226C109.984 26.4226 113.427 23.2781 113.427 18.9652C113.427 14.3789 109.338 12.6016 106.106 11.8061L103.621 11.1598C101.632 10.6502 98.9849 9.71799 98.9969 7.28199C98.9969 5.11929 100.973 3.51599 104.105 3.51599C107.026 3.51599 109.102 4.88319 109.375 7.23219Z" fill="white"/>
              </svg>
            </a>
            `,
          },
          {
            to: "/release-notes",
            position: "left",
            label: "Release Notes",
          },
          {
            href: "https://appcircle.io/features",
            label: "Features",
            position: "right",
          },
          {
            href: "https://appcircle.io/start",
            label: "Dashboard",
            position: "right",
          },
          {
            type: "dropdown",
            items: [
              {
                label: "Slack",
                href: "https://join.slack.com/t/appcircleio/signup",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/appcircleio",
              },
              {
                label: "LinkedIn",
                href: "https://www.linkedin.com/company/appcircleio",
              },
            ],
            label: "Community",
            position: "right",
          },
        ],
      },
      footer: {
        style: "dark",
        logo: {
          src: "https://cdn.appcircle.io/docs/footer-logo-full.png",
          alt: "Appcircle Logo",
          href: "https://appcircle.io",
          width: 160,
          height: 33,
        },
        links: [
          {
            title: "Docs",
            items: [
              {
                label: "Getting Started",
                type: "doc",
                to: "/build/manage-the-connections/adding-a-build-profile",
              },
              {
                label: "Best Practices",
                to: "/best-practices",
              },
              {
                label: "Integrations",
                to: "/workflows",
              },
              {
                label: "Appcircle CLI",
                to: "/appcircle-api",
              },
              {
                label: "Release Notes",
                type: "doc",
                to: "/release-notes",
              },
            ],
          },
          {
            title: "Community",
            items: [
              {
                label: "How-To Videos",
                href: "https://www.youtube.com/appcircle",
              },
              {
                label: "Slack",
                href: "https://slack.appcircle.io/",
              },
              {
                label: "Customer Stories",
                href: "https://appcircle.io/customer-stories",
              },
            ],
          },
          {
            title: "Find Us",
            items: [
              {
                label: "Slack",
                href: "https://join.slack.com/t/appcircleio/signup",
              },
              {
                label: "Twitter",
                href: "https://twitter.com/appcircleio",
              },
              {
                label: "LinkedIn",
                href: "https://www.linkedin.com/company/appcircleio",
              },
            ],
          },
          {
            title: "Explore More",
            items: [
              {
                label: "GitHub",
                href: "https://github.com/appcircleio/appcircle-docusaurus",
              },
              {
                label: "Blog",
                href: "https://appcircle.io/blog",
              },
              {
                label: "Features",
                href: "https://appcircle.io/features",
              },
              {
                label: "Contact Us",
                href: "https://appcircle.io/contact",
              },
              {
                label: "Privacy Policy",
                href: "https://appcircle.io/privacy-policy",
              },
              {
                label: "Terms of Service",
                href: "https://appcircle.io/terms-of-service",
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Appcircle, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        additionalLanguages: [
          "ruby",
          "groovy",
          "java",
          "kotlin",
          "bash",
          "diff",
          "json",
          "markdown",
          "shell-session",
          "yaml",
        ],
      },
      algolia: {
        apiKey: "b56a5dc4e52ec9e97ad93981cc668c4a",
        indexName: "appcircle",
        appId: "4U9FKQJ034",
        contextualSearch: true,
      },
      imageZoom: {
        selector: ".screenshot, .image-narrow",
        options: {
          // medium-zoom options
          margin: 24,
          scrollOffset: 0,
        },
      },
    }),
  plugins: [
    [
      "@docusaurus/plugin-google-analytics",
      {
        trackingID: "UA-40954643-12",
        anonymizeIP: true,
      },
    ],
    "docusaurus-plugin-sass",
    "plugin-image-zoom",
  ],
};

module.exports = config;
