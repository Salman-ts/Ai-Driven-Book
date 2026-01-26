import React, { useState } from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import { useHistory } from '@docusaurus/router';

const API_URL = 'http://localhost:8000';

export default function SignIn() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const history = useHistory();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await fetch(`${API_URL}/auth/signin`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ email, password }),
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Sign in failed');
            }

            const data = await response.json();

            // Store token in localStorage
            localStorage.setItem('auth_token', data.access_token);
            localStorage.setItem('user_email', email);

            // Redirect to docs
            history.push('/docs/intro');
        } catch (err: any) {
            setError(err.message || 'Failed to sign in. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout title="Sign In" description="Sign in to your account">
            <div className="container margin-vert--xl" style={{ maxWidth: '420px' }}>
                <div style={{
                    padding: '2rem',
                    borderRadius: '16px',
                    background: 'var(--ifm-background-surface-color)',
                    border: '1px solid var(--ifm-color-emphasis-200)',
                    boxShadow: '0 8px 32px rgba(0, 0, 0, 0.1)',
                }}>
                    <h2 style={{ textAlign: 'center', marginBottom: '1.5rem' }}>Welcome Back</h2>

                    {error && (
                        <div style={{
                            padding: '0.75rem',
                            marginBottom: '1rem',
                            borderRadius: '8px',
                            background: '#fee2e2',
                            color: '#dc2626',
                            fontSize: '0.875rem',
                        }}>
                            {error}
                        </div>
                    )}

                    <form onSubmit={handleSubmit}>
                        <div style={{ marginBottom: '1rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500 }}>
                                Email
                            </label>
                            <input
                                type="email"
                                required
                                value={email}
                                onChange={e => setEmail(e.target.value)}
                                style={{
                                    width: '100%',
                                    padding: '0.75rem',
                                    borderRadius: '8px',
                                    border: '1px solid var(--ifm-color-emphasis-300)',
                                    fontSize: '1rem',
                                    background: 'var(--ifm-background-color)',
                                    color: 'var(--ifm-font-color-base)',
                                }}
                            />
                        </div>

                        <div style={{ marginBottom: '1.5rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500 }}>
                                Password
                            </label>
                            <input
                                type="password"
                                required
                                value={password}
                                onChange={e => setPassword(e.target.value)}
                                style={{
                                    width: '100%',
                                    padding: '0.75rem',
                                    borderRadius: '8px',
                                    border: '1px solid var(--ifm-color-emphasis-300)',
                                    fontSize: '1rem',
                                    background: 'var(--ifm-background-color)',
                                    color: 'var(--ifm-font-color-base)',
                                }}
                            />
                        </div>

                        <button
                            type="submit"
                            disabled={loading}
                            className="button button--primary"
                            style={{
                                width: '100%',
                                padding: '0.875rem',
                                fontSize: '1rem',
                                opacity: loading ? 0.7 : 1,
                            }}
                        >
                            {loading ? 'Signing in...' : 'Sign In'}
                        </button>
                    </form>

                    <p style={{ textAlign: 'center', marginTop: '1.5rem', color: 'var(--ifm-font-color-secondary)' }}>
                        Don't have an account? <Link to="/signup">Sign Up</Link>
                    </p>
                </div>
            </div>
        </Layout>
    );
}
