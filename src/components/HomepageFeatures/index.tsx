import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  link: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Module 1: ROS 2',
    link: '/docs/module-1-ros2/M1-C1-ROS-2-Fundamentals',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Build the nervous system of your robot with the industry-standard Robot Operating System. Master nodes, topics, and services.
      </>
    ),
  },
  {
    title: 'Module 2: Digital Twin',
    link: '/docs/module-2-digital-twin/M2-C1-Why-Digital-Twins-Matter',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Create high-fidelity simulations in Gazebo and Unity. Test your robot in a virtual world before deploying to hardware.
      </>
    ),
  },
  {
    title: 'Module 3: NVIDIA Isaac',
    link: '/docs/module-3-isaac/M3-C1-Isaac-Sim-Foundations',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Dive into GPU-accelerated simulation with Isaac Sim to generate synthetic data and train robust AI models.
      </>
    ),
  },
  {
    title: 'Module 4: VLA & Humanoids',
    link: '/docs/module-4-vla-humanoids/M4-C1-VLA-Foundations',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Integrate Vision-Language-Action models to give your robot a "brain" for reasoning and executing complex, high-level tasks.
      </>
    ),
  },
];

function Feature({title, link, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--3')}>
      <Link className={styles.featureCard} to={link}>
        <div className="text--center">
          <Svg className={styles.featureSvg} role="img" />
        </div>
        <div className="text--center padding-horiz--md">
          <h3>{title}</h3>
          <p>{description}</p>
        </div>
      </Link>
    </div>
  );
}

export default function HomepageFeatures(): JSX.Element {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
