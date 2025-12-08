-- Production Schema for AI Book System (Neon Postgres)
-- Run this in your Neon Console SQL Editor

-- Enable UUID extension if planning to use UUIDs (optional but recommended)
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Users Table (synced with Better-Auth)
CREATE TABLE IF NOT EXISTS users (
    id TEXT PRIMARY KEY, -- Provided by Better-Auth
    email TEXT UNIQUE NOT NULL,
    name TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- User Profiles (Gamification & Personalization)
CREATE TABLE IF NOT EXISTS user_profiles (
    id SERIAL PRIMARY KEY,
    user_id TEXT UNIQUE NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    software_skill TEXT DEFAULT 'beginner', -- beginner, intermediate, expert
    hardware_skill TEXT DEFAULT 'none',    -- none, rpi, arduino, etc
    learning_goal TEXT DEFAULT 'general',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Point Logs (Gamification History)
CREATE TABLE IF NOT EXISTS point_logs (
    id SERIAL PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    points INTEGER NOT NULL,
    reason TEXT,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Chat Logs (RAG History & Analytics)
CREATE TABLE IF NOT EXISTS chat_logs (
    id SERIAL PRIMARY KEY,
    user_id TEXT REFERENCES users(id) ON DELETE SET NULL,
    query TEXT NOT NULL,
    response TEXT,
    context_used JSONB, -- Stores metadata of chunks used
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for Performance
CREATE INDEX IF NOT EXISTS idx_user_email ON users(email);
CREATE INDEX IF NOT EXISTS idx_profile_user ON user_profiles(user_id);
CREATE INDEX IF NOT EXISTS idx_points_user ON point_logs(user_id);
CREATE INDEX IF NOT EXISTS idx_chat_user ON chat_logs(user_id);
