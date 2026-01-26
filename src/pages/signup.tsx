import React, { useState } from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import { useHistory } from '@docusaurus/router';

const API_URL = 'http://localhost:8000';

export default function SignUp() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        software_skill: 'beginner',
        hardware_skill: 'none'
    });
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const history = useHistory();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setLoading(true);
        setError(null);

        try {
            const response = await fetch(`${API_URL}/auth/signup`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    name: formData.name,
                    email: formData.email,
                    password: formData.password,
                }),
            });

            if (!response.ok) {
                const data = await response.json();
                throw new Error(data.detail || 'Sign up failed');
            }

            const data = await response.json();

            // Store token and user info
            localStorage.setItem('auth_token', data.access_token);
            localStorage.setItem('user_email', formData.email);
            localStorage.setItem('user_name', formData.name);
            localStorage.setItem('user_preferences', JSON.stringify({
                software_skill: formData.software_skill,
                hardware_skill: formData.hardware_skill,
            }));

            // Redirect to docs
            history.push('/docs/intro');
        } catch (err: any) {
            setError(err.message || 'Failed to sign up. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    const inputStyle = {
        width: '100%',
        padding: '0.75rem',
        borderRadius: '8px',
        border: '1px solid var(--ifm-color-emphasis-300)',
        fontSize: '1rem',
        background: 'var(--ifm-background-color)',
        color: 'var(--ifm-font-color-base)',
    };

    return (
        <Layout title="Sign Up" description="Create your account">
            <div className="container margin-vert--xl" style={{ maxWidth: '480px' }}>
                <div style={{
                    padding: '2rem',
                    borderRadius: '16px',
                    background: 'var(--ifm-background-surface-color)',
                    border: '1px solid var(--ifm-color-emphasis-200)',
                    boxShadow: '0 8px 32px rgba(0, 0, 0, 0.1)',
                }}>
                    <h2 style={{ textAlign: 'center', marginBottom: '1.5rem' }}>Create Account</h2>

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
                                Full Name
                            </label>
                            <input
                                required
                                value={formData.name}
                                onChange={e => setFormData({ ...formData, name: e.target.value })}
                                style={inputStyle}
                                placeholder="John Doe"
                            />
                        </div>

                        <div style={{ marginBottom: '1rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500 }}>
                                Email
                            </label>
                            <input
                                type="email"
                                required
                                value={formData.email}
                                onChange={e => setFormData({ ...formData, email: e.target.value })}
                                style={inputStyle}
                                placeholder="you@example.com"
                            />
                        </div>

                        <div style={{ marginBottom: '1rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500 }}>
                                Password
                            </label>
                            <input
                                type="password"
                                required
                                value={formData.password}
                                onChange={e => setFormData({ ...formData, password: e.target.value })}
                                style={inputStyle}
                                placeholder="••••••••"
                                minLength={6}
                            />
                        </div>

                        <div style={{ marginBottom: '1rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500 }}>
                                Coding Experience
                            </label>
                            <select
                                value={formData.software_skill}
                                onChange={e => setFormData({ ...formData, software_skill: e.target.value })}
                                style={inputStyle}
                            >
                                <option value="beginner">Beginner - Just starting</option>
                                <option value="intermediate">Intermediate - Some experience</option>
                                <option value="expert">Expert - Professional developer</option>
                            </select>
                        </div>

                        <div style={{ marginBottom: '1.5rem' }}>
                            <label style={{ display: 'block', marginBottom: '0.5rem', fontWeight: 500 }}>
                                Hardware Interest
                            </label>
                            <select
                                value={formData.hardware_skill}
                                onChange={e => setFormData({ ...formData, hardware_skill: e.target.value })}
                                style={inputStyle}
                            >
                                <option value="none">Simulation Only</option>
                                <option value="raspberry_pi">Raspberry Pi</option>
                                <option value="arduino">Arduino / ESP32</option>
                                <option value="robotics_kit">Robotics Kit</option>
                            </select>
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
                            {loading ? 'Creating account...' : 'Create Account'}
                        </button>
                    </form>

                    <p style={{ textAlign: 'center', marginTop: '1.5rem', color: 'var(--ifm-font-color-secondary)' }}>
                        Already have an account? <Link to="/signin">Sign In</Link>
                    </p>
                </div>
            </div>
        </Layout>
    );
}
