import React, { Suspense } from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import BrowserOnly from '@docusaurus/BrowserOnly';
import styles from './index.module.css';

// Lazy load ThreeScene to avoid SSR issues
const ThreeScene = React.lazy(() => import('../components/ThreeScene'));

// Error boundary for 3D scene
class ThreeErrorBoundary extends React.Component<{ children: React.ReactNode }, { hasError: boolean }> {
  constructor(props: { children: React.ReactNode }) {
    super(props);
    this.state = { hasError: false };
  }
  static getDerivedStateFromError() {
    return { hasError: true };
  }
  render() {
    if (this.state.hasError) {
      return <div style={{ height: '100%', background: 'linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%)' }} />;
    }
    return this.props.children;
  }
}

// Feature data
const features = [
  { icon: '🤖', title: 'Agent-Native Architecture', desc: 'Build systems where AI agents are first-class citizens.' },
  { icon: '🧠', title: 'Cognitive RAG', desc: 'Advanced Retrieval Augmented Generation for robotics.' },
  { icon: '🦾', title: 'Physical Deployment', desc: 'Deploy to Raspberry Pi, Jetson, and real robots.' },
  { icon: '🌐', title: 'Digital Twins', desc: 'Simulate robots in Gazebo and Isaac Sim.' },
  { icon: '🎯', title: 'Voice Control', desc: 'LLM-powered voice commands for humanoids.' },
  { icon: '📚', title: '18+ Chapters', desc: 'Comprehensive curriculum from basics to advanced.' },
];

// Modules data
const modules = [
  { num: '01', title: 'ROS 2 Fundamentals', color: '#4285F4' },
  { num: '02', title: 'Digital Twin Simulation', color: '#EA4335' },
  { num: '03', title: 'NVIDIA Isaac Platform', color: '#76B900' },
  { num: '04', title: 'VLA & Humanoids', color: '#9C27B0' },
];

function HeroSection() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <header style={{
      position: 'relative',
      minHeight: '90vh',
      display: 'flex',
      alignItems: 'center',
      overflow: 'hidden',
      background: '#0f172a',
    }}>
      {/* 3D Background */}
      <div style={{
        position: 'absolute',
        inset: 0,
        zIndex: 0,
        opacity: 0.8,
      }}>
        <BrowserOnly fallback={<div style={{ height: '100%', background: '#0f172a' }} />}>
          {() => (
            <ThreeErrorBoundary>
              <Suspense fallback={<div style={{ height: '100%', background: '#0f172a' }} />}>
                <ThreeScene />
              </Suspense>
            </ThreeErrorBoundary>
          )}
        </BrowserOnly>
      </div>

      {/* Content */}
      <div className="container" style={{ position: 'relative', zIndex: 1 }}>
        <div style={{ maxWidth: '800px', margin: '0 auto', textAlign: 'center' }}>
          {/* Badge */}
          <div style={{
            display: 'inline-block',
            padding: '0.5rem 1rem',
            background: 'rgba(139, 92, 246, 0.2)',
            border: '1px solid rgba(139, 92, 246, 0.4)',
            borderRadius: '50px',
            color: '#c4b5fd',
            fontSize: '0.875rem',
            marginBottom: '1.5rem',
          }}>
            ✨ AI-Native Learning Experience
          </div>

          {/* Title */}
          <h1 style={{
            fontSize: 'clamp(2.5rem, 5vw, 4rem)',
            fontWeight: 800,
            lineHeight: 1.1,
            marginBottom: '1.5rem',
            background: 'linear-gradient(135deg, #fff 0%, #a78bfa 100%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
          }}>
            Physical AI &<br />Humanoid Robotics
          </h1>

          {/* Subtitle */}
          <p style={{
            fontSize: '1.25rem',
            color: '#94a3b8',
            marginBottom: '2rem',
            maxWidth: '600px',
            margin: '0 auto 2rem',
          }}>
            {siteConfig.tagline}
          </p>

          {/* CTAs */}
          <div style={{ display: 'flex', justifyContent: 'center', gap: '1rem', flexWrap: 'wrap' }}>
            <Link
              to="/docs/intro"
              style={{
                padding: '1rem 2rem',
                background: 'linear-gradient(135deg, #7c3aed 0%, #a78bfa 100%)',
                color: 'white',
                borderRadius: '50px',
                fontWeight: 600,
                boxShadow: '0 4px 20px rgba(139, 92, 246, 0.4)',
                textDecoration: 'none',
              }}>
              Start Learning 🚀
            </Link>
            <Link
              to="/demo"
              style={{
                padding: '1rem 2rem',
                background: 'rgba(255, 255, 255, 0.1)',
                color: 'white',
                borderRadius: '50px',
                fontWeight: 600,
                border: '1px solid rgba(255, 255, 255, 0.2)',
                textDecoration: 'none',
              }}>
              Try AI Features
            </Link>
          </div>

          {/* Stats */}
          <div style={{
            display: 'flex',
            justifyContent: 'center',
            gap: '3rem',
            marginTop: '3rem',
            flexWrap: 'wrap',
          }}>
            {[
              { val: '4', label: 'Modules' },
              { val: '18+', label: 'Chapters' },
              { val: '50+', label: 'Labs' },
            ].map((s, i) => (
              <div key={i} style={{ textAlign: 'center' }}>
                <div style={{ fontSize: '2rem', fontWeight: 800, color: '#a78bfa' }}>{s.val}</div>
                <div style={{ fontSize: '0.875rem', color: '#64748b' }}>{s.label}</div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </header>
  );
}

function FeaturesSection() {
  return (
    <section style={{ padding: '5rem 0', background: 'var(--ifm-background-color)' }}>
      <div className="container">
        <h2 style={{ textAlign: 'center', marginBottom: '3rem', fontSize: '2rem' }}>
          Why Learn With Us?
        </h2>
        <div className="row">
          {features.map((f, i) => (
            <div key={i} className="col col--4" style={{ marginBottom: '2rem' }}>
              <div style={{
                padding: '1.5rem',
                borderRadius: '12px',
                border: '1px solid var(--ifm-color-emphasis-200)',
                height: '100%',
              }}>
                <span style={{ fontSize: '2rem' }}>{f.icon}</span>
                <h3 style={{ marginTop: '1rem', marginBottom: '0.5rem' }}>{f.title}</h3>
                <p style={{ color: 'var(--ifm-font-color-secondary)', margin: 0 }}>{f.desc}</p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function ModulesSection() {
  return (
    <section style={{ padding: '5rem 0', background: 'var(--ifm-background-surface-color)' }}>
      <div className="container">
        <h2 style={{ textAlign: 'center', marginBottom: '3rem', fontSize: '2rem' }}>
          Course Curriculum
        </h2>
        <div className="row">
          {modules.map((m, i) => (
            <div key={i} className="col col--3" style={{ marginBottom: '1.5rem' }}>
              <div style={{
                padding: '1.5rem',
                borderRadius: '12px',
                border: '1px solid var(--ifm-color-emphasis-200)',
                textAlign: 'center',
              }}>
                <div style={{
                  fontSize: '0.75rem',
                  fontWeight: 700,
                  color: m.color,
                  marginBottom: '0.5rem',
                }}>
                  MODULE {m.num}
                </div>
                <h3 style={{ fontSize: '1rem', margin: 0 }}>{m.title}</h3>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

function CTASection() {
  return (
    <section style={{
      padding: '5rem 0',
      background: 'linear-gradient(135deg, #1e1b4b 0%, #0f172a 100%)',
      textAlign: 'center',
    }}>
      <div className="container">
        <h2 style={{ color: 'white', marginBottom: '1rem' }}>Ready to Build the Future?</h2>
        <p style={{ color: '#94a3b8', marginBottom: '2rem' }}>
          Join developers learning to build intelligent robots.
        </p>
        <Link
          to="/docs/intro"
          style={{
            padding: '1rem 2.5rem',
            background: 'linear-gradient(135deg, #7c3aed 0%, #a78bfa 100%)',
            color: 'white',
            borderRadius: '50px',
            fontWeight: 700,
            textDecoration: 'none',
            boxShadow: '0 4px 20px rgba(139, 92, 246, 0.4)',
          }}>
          Get Started Free 🎯
        </Link>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  const { siteConfig } = useDocusaurusContext();
  return (
    <Layout
      title="Learn Physical AI & Robotics"
      description="AI-native book for learning robotics from fundamentals to voice-controlled humanoids">
      <HeroSection />
      <FeaturesSection />
      <ModulesSection />
      <CTASection />
    </Layout>
  );
}
