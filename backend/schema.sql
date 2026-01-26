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

-- Better-Auth Session Management
CREATE TABLE IF NOT EXISTS sessions (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    token TEXT UNIQUE NOT NULL,
    ip_address TEXT,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS accounts (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    provider_id TEXT NOT NULL, -- e.g. 'google', 'github', 'credential'
    account_id TEXT NOT NULL, -- external ID
    access_token TEXT,
    refresh_token TEXT,
    expires_at TIMESTAMP WITH TIME ZONE,
    password_hash TEXT, -- for credential provider
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Content Ingestion Tracking
CREATE TABLE IF NOT EXISTS content_ingestion (
    id SERIAL PRIMARY KEY,
    file_path TEXT UNIQUE NOT NULL,
    file_hash TEXT NOT NULL,
    chunk_count INTEGER NOT NULL,
    embedding_model TEXT NOT NULL,
    ingested_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    status TEXT DEFAULT 'completed' -- pending, completed, failed
);

-- Chapter Metadata
CREATE TABLE IF NOT EXISTS chapters (
    id SERIAL PRIMARY KEY,
    module TEXT NOT NULL,
    chapter_slug TEXT UNIQUE NOT NULL,
    title TEXT NOT NULL,
    description TEXT,
    difficulty TEXT DEFAULT 'intermediate', -- beginner, intermediate, advanced
    prerequisites JSONB DEFAULT '[]',
    learning_outcomes JSONB DEFAULT '[]',
    estimated_time_minutes INTEGER,
    tags TEXT[] DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for New Tables
CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
CREATE INDEX IF NOT EXISTS idx_sessions_token ON sessions(token);
CREATE INDEX IF NOT EXISTS idx_accounts_user ON accounts(user_id);
CREATE INDEX IF NOT EXISTS idx_ingestion_path ON content_ingestion(file_path);
CREATE INDEX IF NOT EXISTS idx_chapters_module ON chapters(module);
