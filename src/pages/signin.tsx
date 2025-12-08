import React, { useState } from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function SignIn() {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = (e) => {
        e.preventDefault();
        // Use Better-Auth or backend API
        alert('Sign in logic would connect to /api/v1/auth/login');
    };

    return (
        <Layout title="Sign In" description="Sign in to your account">
            <div className="container margin-vert--xl" style={{ maxWidth: '400px' }}>
                <div className="card shadow--md">
                    <div className="card__header">
                        <h2>Welcome Back</h2>
                    </div>
                    <div className="card__body">
                        <form onSubmit={handleSubmit}>
                            <div className="margin-bottom--md">
                                <label className="display-block" htmlFor="email">Email</label>
                                <input
                                    className="button--block"
                                    style={{ width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #ccc' }}
                                    type="email"
                                    id="email"
                                    required
                                    value={email}
                                    onChange={e => setEmail(e.target.value)}
                                />
                            </div>
                            <div className="margin-bottom--lg">
                                <label className="display-block" htmlFor="password">Password</label>
                                <input
                                    className="button--block"
                                    style={{ width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #ccc' }}
                                    type="password"
                                    id="password"
                                    required
                                    value={password}
                                    onChange={e => setPassword(e.target.value)}
                                />
                            </div>
                            <button className="button button--primary button--block" type="submit">
                                Sign In
                            </button>
                        </form>
                    </div>
                    <div className="card__footer text--center">
                        <p>Don't have an account? <Link to="/signup">Sign Up</Link></p>
                    </div>
                </div>
            </div>
        </Layout>
    );
}
