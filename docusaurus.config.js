import { themes as prismThemes } from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'From Foundational Concepts to Voice-Controlled Humanoid Robots',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  // Set the production url of your site here
  url: 'https://ai-driven-book.vercel.app',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For Vercel/Netlify/Root domain, use '/'
  baseUrl: '/',

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
          editUrl: 'https://github.com/Salman-ts/ai-book/tree/main/',
        },
        blog: false, // Disabled blog
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  // Search plugin removed due to compatibility issues
  // themes: [],

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
        {
          href: 'https://github.com/Salman-ts/ai-book',
          label: 'GitHub',
          position: 'right',
        },
        {
          to: '/signin',
          label: 'Sign In',
          position: 'right',
          className: 'navbar-signin-btn',
        },
        {
          to: '/signup',
          label: 'Sign Up',
          position: 'right',
          className: 'navbar-signup-btn',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Learn',
          items: [
            {
              label: '📚 Start Reading',
              to: '/docs/intro',
            },
            {
              label: '🤖 ROS 2 Fundamentals',
              to: '/docs/module-1-ros2/M1-C1-ROS-2-Fundamentals',
            },
            {
              label: '🎮 Digital Twins',
              to: '/docs/module-2-digital-twin/M2-C1-Why-Digital-Twins-Matter',
            },
          ],
        },
        {
          title: 'Resources',
          items: [
            {
              label: '📦 NVIDIA Isaac',
              to: '/docs/module-3-isaac/M3-C1-Isaac-Sim-Foundations',
            },
            {
              label: '🦾 VLA & Humanoids',
              to: '/docs/module-4-vla-humanoids/M4-C1-VLA-Foundations',
            },
          ],
        },
        {
          title: 'Connect',
          items: [
            {
              label: '⭐ GitHub',
              href: 'https://github.com/Salman-ts/ai-book',
            },
            {
              label: '🐦 Twitter',
              href: 'https://twitter.com',
            },
            {
              label: '💬 Discord',
              href: 'https://discord.gg',
            },
            {
              label: '📺 YouTube',
              href: 'https://youtube.com',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Physical AI & Humanoid Robotics. Built with ❤️ using Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['powershell'],
    },
  },
};

export default config;
