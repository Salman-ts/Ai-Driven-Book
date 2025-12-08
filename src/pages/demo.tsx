import React from 'react';
import Layout from '@theme/Layout';
import ChatWidget from '../components/ChatWidget';
import ChapterControls from '../components/ChapterControls';

export default function DemoPage() {
    return (
        <Layout
            title="AI Features Demo"
            description="Testing the AI components">
            <main className="container margin-vert--xl">
                <h1>🤖 AI Features Playground</h1>
                <p>This page demonstrates the interactive AI components built for the book.</p>

                <section className="margin-top--lg">
                    <h2>1. Chapter Personalization & Translation</h2>
                    <p>
                        The controls below mimic what appears at the top of a chapter.
                        Clicking them will trigger a request to the backend (ensure backend is running).
                    </p>
                    <div style={{ border: '1px solid #ddd', padding: '2rem', borderRadius: '8px', background: 'white' }}>
                        <article>
                            <h3>Sample Chapter: Introduction to Robotics</h3>
                            <p>
                                Robotics is an interdisciplinary branch of computer science and engineering.
                                Robotics involves design, construction, operation, and use of robots.
                                The goal of robotics is to design machines that can help and assist humans.
                            </p>
                            <p>
                                Robotics integrates fields of mechanical engineering, electrical engineering,
                                information engineering, mechatronics, electronics, bioengineering,
                                computer engineering, control engineering, software engineering, mathematics, etc.
                            </p>
                        </article>
                        <hr style={{ margin: '1rem 0' }} />
                        <ChapterControls />
                    </div>
                </section>

                <section className="margin-top--xl">
                    <h2>2. RAG Chatbot</h2>
                    <p>
                        The chatbot widget should be floating in the bottom right corner of this page.
                        Open it to test the RAG functionality.
                    </p>
                </section>

                {/* Floating Widget */}
                <ChatWidget />

            </main>
        </Layout>
    );
}
