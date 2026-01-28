/**
 * API Service - Centralized backend API calls
 */

const API_URL = typeof window !== 'undefined' 
  ? (window as any).__API_URL__ || 'http://localhost:8000'
  : 'http://localhost:8000';

// Helper to get auth token
export const getAuthToken = (): string | null => {
    if (typeof window === 'undefined') return null;
    return localStorage.getItem('auth_token');
};

// Helper to get user preferences
export const getUserPreferences = () => {
    if (typeof window === 'undefined') return null;
    const prefs = localStorage.getItem('user_preferences');
    return prefs ? JSON.parse(prefs) : null;
};

// Chat API
export const sendChatMessage = async (query: string, history: any[] = []) => {
    const response = await fetch(`${API_URL}/chat/message`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getAuthToken() || 'anonymous'}`,
        },
        body: JSON.stringify({ query, history }),
    });
    
    if (!response.ok) {
        throw new Error('Chat request failed');
    }
    
    return response;
};

// Translation API
export const translateContent = async (content: string, targetLanguage = 'urdu') => {
    const response = await fetch(`${API_URL}/content/translate`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getAuthToken() || 'anonymous'}`,
        },
        body: JSON.stringify({ content, target_language: targetLanguage }),
    });
    
    if (!response.ok) {
        throw new Error('Translation failed');
    }
    
    return response.json();
};

// Personalization API
export const personalizeContent = async (content: string, userLevel?: string, interests?: string[]) => {
    const prefs = getUserPreferences();
    
    const response = await fetch(`${API_URL}/content/personalize`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${getAuthToken() || 'anonymous'}`,
        },
        body: JSON.stringify({
            content,
            user_level: userLevel || prefs?.software_skill || 'intermediate',
            interests: interests || ['robotics', 'AI'],
        }),
    });
    
    if (!response.ok) {
        throw new Error('Personalization failed');
    }
    
    return response.json();
};

// Auth API
export const signIn = async (email: string, password: string) => {
    const response = await fetch(`${API_URL}/auth/signin`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
    });
    
    if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || 'Sign in failed');
    }
    
    return response.json();
};

export const signUp = async (name: string, email: string, password: string) => {
    const response = await fetch(`${API_URL}/auth/signup`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, email, password }),
    });
    
    if (!response.ok) {
        const data = await response.json();
        throw new Error(data.detail || 'Sign up failed');
    }
    
    return response.json();
};

// Health check
export const checkBackendHealth = async (): Promise<boolean> => {
    try {
        const response = await fetch(`${API_URL}/`);
        return response.ok;
    } catch {
        return false;
    }
};

export default {
    sendChatMessage,
    translateContent,
    personalizeContent,
    signIn,
    signUp,
    checkBackendHealth,
    getAuthToken,
    getUserPreferences,
};
