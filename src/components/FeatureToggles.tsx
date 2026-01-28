import React, { useState, useEffect } from 'react';
import './FeatureToggles.css';
import { translateContent, personalizeContent } from '../services/api';

interface FeatureTogglesProps {
    chapterId?: string;
    currentContent?: string;
    onContentChange?: (content: string) => void;
}

const FeatureToggles: React.FC<FeatureTogglesProps> = ({
    chapterId = '',
    currentContent = '',
    onContentChange
}) => {
    const [focusMode, setFocusMode] = useState(false);
    const [isTranslating, setIsTranslating] = useState(false);
    const [isPersonalizing, setIsPersonalizing] = useState(false);
    const [translatedContent, setTranslatedContent] = useState<string | null>(null);
    const [personalizedContent, setPersonalizedContent] = useState<string | null>(null);
    const [showPanel, setShowPanel] = useState(false);
    const [notification, setNotification] = useState<string | null>(null);

    // Focus Mode: Hide sidebars
    useEffect(() => {
        if (focusMode) {
            document.body.classList.add('focus-mode');
        } else {
            document.body.classList.remove('focus-mode');
        }
        return () => document.body.classList.remove('focus-mode');
    }, [focusMode]);

    const showNotification = (msg: string) => {
        setNotification(msg);
        setTimeout(() => setNotification(null), 3000);
    };

    // Translation API call
    const handleTranslate = async () => {
        if (translatedContent) {
            // Toggle off - restore original
            setTranslatedContent(null);
            onContentChange?.(currentContent);
            showNotification('Restored original content');
            return;
        }

        setIsTranslating(true);
        try {
            const data = await translateContent(
                currentContent || document.querySelector('article')?.textContent?.slice(0, 2000) || '',
                'urdu'
            );


            setTranslatedContent(data.translated_content);
            onContentChange?.(data.translated_content);
            showNotification('✨ Translated to Urdu');
        } catch (error) {
            console.error('Translation error:', error);
            showNotification('❌ Translation failed - check if backend is running');
        } finally {
            setIsTranslating(false);
        }
    };

    // Personalization API call
    const handlePersonalize = async () => {
        if (personalizedContent) {
            // Toggle off - restore original
            setPersonalizedContent(null);
            onContentChange?.(currentContent);
            showNotification('Restored original content');
            return;
        }

        setIsPersonalizing(true);
        try {
            const data = await personalizeContent(
                currentContent || document.querySelector('article')?.textContent?.slice(0, 2000) || '',
                'intermediate',
                ['robotics', 'AI']
            );


            setPersonalizedContent(data.personalized_content);
            onContentChange?.(data.personalized_content);
            showNotification('✨ Content personalized for you');
        } catch (error) {
            console.error('Personalization error:', error);
            showNotification('❌ Personalization failed - check if backend is running');
        } finally {
            setIsPersonalizing(false);
        }
    };

    return (
        <>
            {/* Notification Toast */}
            {notification && (
                <div className="feature-notification">
                    {notification}
                </div>
            )}

            {/* Toggle Panel Button */}
            <button
                className="feature-panel-toggle"
                onClick={() => setShowPanel(!showPanel)}
                title="Reading Features"
            >
                ⚙️
            </button>

            {/* Feature Panel */}
            <div className={`feature-panel ${showPanel ? 'open' : ''}`}>
                <div className="feature-panel-header">
                    <span>Reading Features</span>
                    <button onClick={() => setShowPanel(false)}>✕</button>
                </div>

                <div className="feature-toggles">
                    {/* Focus Mode */}
                    <div className="feature-toggle-item">
                        <div className="feature-info">
                            <span className="feature-icon">🎯</span>
                            <div>
                                <div className="feature-name">Focus Mode</div>
                                <div className="feature-desc">Hide sidebars for distraction-free reading</div>
                            </div>
                        </div>
                        <button
                            className={`toggle-btn ${focusMode ? 'active' : ''}`}
                            onClick={() => setFocusMode(!focusMode)}
                        >
                            <span className="toggle-slider"></span>
                        </button>
                    </div>

                    {/* Translation */}
                    <div className="feature-toggle-item">
                        <div className="feature-info">
                            <span className="feature-icon">🌐</span>
                            <div>
                                <div className="feature-name">Urdu Translation</div>
                                <div className="feature-desc">Translate content to Urdu</div>
                            </div>
                        </div>
                        <button
                            className={`toggle-btn ${translatedContent ? 'active' : ''} ${isTranslating ? 'loading' : ''}`}
                            onClick={handleTranslate}
                            disabled={isTranslating}
                        >
                            <span className="toggle-slider"></span>
                        </button>
                    </div>

                    {/* Personalization */}
                    <div className="feature-toggle-item">
                        <div className="feature-info">
                            <span className="feature-icon">✨</span>
                            <div>
                                <div className="feature-name">Personalize</div>
                                <div className="feature-desc">Adapt content to your level</div>
                            </div>
                        </div>
                        <button
                            className={`toggle-btn ${personalizedContent ? 'active' : ''} ${isPersonalizing ? 'loading' : ''}`}
                            onClick={handlePersonalize}
                            disabled={isPersonalizing}
                        >
                            <span className="toggle-slider"></span>
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
};

export default FeatureToggles;
