import React, { useState } from 'react';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';

export default function SignUp() {
    const [formData, setFormData] = useState({
        name: '',
        email: '',
        password: '',
        software_skill: 'beginner',
        hardware_skill: 'none'
    });

    const handleSubmit = (e) => {
        e.preventDefault();
        // Simulate Signup
        alert(`Signing up ${formData.name}. Would verify with Backend.`);
    };

    return (
        <Layout title="Sign Up" description="Create your account">
            <div className="container margin-vert--xl" style={{ maxWidth: '500px' }}>
                <div className="card shadow--md">
                    <div className="card__header">
                        <h2>Create Account</h2>
                    </div>
                    <div className="card__body">
                        <form onSubmit={handleSubmit}>
                            <div className="margin-bottom--md">
                                <label className="display-block">Full Name</label>
                                <input
                                    className="input-field"
                                    style={{ width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #ccc' }}
                                    required
                                    value={formData.name}
                                    onChange={e => setFormData({ ...formData, name: e.target.value })}
                                />
                            </div>
                            <div className="margin-bottom--md">
                                <label className="display-block">Email</label>
                                <input
                                    type="email"
                                    style={{ width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #ccc' }}
                                    required
                                    value={formData.email}
                                    onChange={e => setFormData({ ...formData, email: e.target.value })}
                                />
                            </div>
                            <div className="margin-bottom--md">
                                <label className="display-block">Password</label>
                                <input
                                    type="password"
                                    style={{ width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #ccc' }}
                                    required
                                    value={formData.password}
                                    onChange={e => setFormData({ ...formData, password: e.target.value })}
                                />
                            </div>

                            {/* Profile Fields */}
                            <div className="margin-bottom--md">
                                <label className="display-block">Coding Experience</label>
                                <select
                                    style={{ width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #ccc' }}
                                    value={formData.software_skill}
                                    onChange={e => setFormData({ ...formData, software_skill: e.target.value })}
                                >
                                    <option value="beginner">Beginner</option>
                                    <option value="intermediate">Intermediate</option>
                                    <option value="expert">Expert</option>
                                </select>
                            </div>

                            <div className="margin-bottom--lg">
                                <label className="display-block">Hardware Interest</label>
                                <select
                                    style={{ width: '100%', padding: '10px', borderRadius: '8px', border: '1px solid #ccc' }}
                                    value={formData.hardware_skill}
                                    onChange={e => setFormData({ ...formData, hardware_skill: e.target.value })}
                                >
                                    <option value="none">None / Simulation Only</option>
                                    <option value="raspberry_pi">Raspberry Pi</option>
                                    <option value="arduino">Arduino / ESP32</option>
                                    <option value="robotics_kit">Robotics Kit</option>
                                </select>
                            </div>

                            <button className="button button--primary button--block" type="submit">
                                Create Profile
                            </button>
                        </form>
                    </div>
                    <div className="card__footer text--center">
                        <p>Already have an account? <Link to="/signin">Sign In</Link></p>
                    </div>
                </div>
            </div>
        </Layout>
    );
}
