import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

import styles from './index.module.css';

function HomepageHeader() {
  const { siteConfig } = useDocusaurusContext();
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <h1 className="hero__title">
          <span style={{ color: 'var(--ifm-color-primary)' }}>Physical AI</span> & <br />
          Humanoid Robotics
        </h1>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/intro">
            Start Reading
          </Link>
          <Link
            className="button button--secondary button--lg"
            style={{ marginLeft: '1rem' }}
            to="/demo">
            Try AI Features
          </Link>
        </div>
      </div>
    </header>
  );
}

function FeatureSection() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          <div className={clsx('col col--4')}>
            <div className="text--center">
              <span style={{ fontSize: '3rem' }}>🤖</span>
            </div>
            <div className="text--center padding-horiz--md">
              <h3>Agent-Native Architecture</h3>
              <p>Learn how to build systems where AI agents are first-class citizens.</p>
            </div>
          </div>
          <div className={clsx('col col--4')}>
            <div className="text--center">
              <span style={{ fontSize: '3rem' }}>🧠</span>
            </div>
            <div className="text--center padding-horiz--md">
              <h3>Cognitive RAG</h3>
              <p>Implement advanced Retrieval Augmented Generation for robotics context.</p>
            </div>
          </div>
          <div className={clsx('col col--4')}>
            <div className="text--center">
              <span style={{ fontSize: '3rem' }}>🦾</span>
            </div>
            <div className="text--center padding-horiz--md">
              <h3>Physical Deployment</h3>
              <p>Deploy your models to edge devices, Raspberry Pi, and Jetson Nano.</p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <FeatureSection />
      </main>
    </Layout>
  );
}
