import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'From Foundational Concepts to Voice-Controlled Humanoid Robots',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://uni-tech.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub Pages deployment, it is often '/<projectName>/'
  baseUrl: '/ai-book/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Salman-ts', // Usually your GitHub org/user name.
  projectName: 'ai-book', // Usually your repo name.
  deploymentBranch: 'gh-pages',

  onBrokenLinks: 'ignore',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace 'en' with 'zh-Hans'.
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./src/sidebar.ts'),
          // Please change this to your repo. For example: `https://github.com/facebook/docusaurus/edit/main/website/docs/
          editUrl: 'https://github.com/Salman-ts/ai-book/tree/main/',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo. For example: `https://github.com/facebook/docusaurus/edit/main/website/blog/
          editUrl: 'https://github.com/Salman-ts/ai-book/tree/main/',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Physical AI & Humanoid Robotics',
      logo: {
        alt: 'My Site Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Book',
        },
        // Blog removed as requested
        {
          href: 'https://github.com/Salman-ts/ai-book',
          label: 'GitHub',
          position: 'right',
        },
        {
          type: 'html',
          position: 'right',
          value: '<a href="/signin" class="button button--secondary button--sm" style="margin-left: 10px; border-radius: 50px; font-weight: 600;">Sign In</a>',
        },
        {
          type: 'html',
          position: 'right',
          value: '<a href="/signup" class="button button--primary button--sm" style="margin-left: 10px; border-radius: 50px; font-weight: 600;">Sign Up</a>',
        },
      ],
    },
    algolia: {
      // The application ID provided by Algolia
      appId: 'YOUR_APP_ID',
      // Public API key: it is safe to commit it
      apiKey: 'YOUR_SEARCH_API_KEY',
      indexName: 'YOUR_INDEX_NAME',
      // Optional: Algolia search parameters
      searchParameters: {},
      // Optional: path for search page that e.g. Docusaurus uses to display the results.
      // E.g. /docs/search/
      // contextualSearch: true,
      // You can further tune the dictionary in client-algolia.config.js
      // ...
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Book',
              to: '/docs/M1-ROS-2-The-Robotic-Nervous-System/M1-C1-ROS-2-Fundamentals',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Blog',
              to: '/blog',
            },
            {
              label: 'GitHub',
              href: 'https://github.com/Salman-ts/ai-book',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['powershell'],
      // Optional: Add `showLineNumbers` to all code blocks by default
      // showLineNumbers: true, 
    },
  },
};

export default config;
