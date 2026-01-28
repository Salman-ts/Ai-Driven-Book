import React, { useState } from 'react';
import { translateContent, personalizeContent } from '../services/api';

const ChapterControls = () => {
    const [isPersonalized, setIsPersonalized] = useState(false);
    const [isUrdu, setIsUrdu] = useState(false);
    const [loading, setLoading] = useState(false);
    const [content, setContent] = useState<string | null>(null);

    const handlePersonalize = async () => {
        setLoading(true);
        try {
            const currentContent = document.querySelector('article')?.innerText || "Chapter Content";
            const data = await personalizeContent(currentContent);

            setContent(data.personalized_content || data.content);
            setIsPersonalized(true);
            setIsUrdu(false);
        } catch (e) {
            console.error(e);
        } finally {
            setLoading(false);
        }
    };

    const handleTranslate = async () => {
        setLoading(true);
        try {
            const currentContent = document.querySelector('article')?.innerText || "Chapter Content";
            const data = await translateContent(currentContent, 'urdu');

            setContent(data.translated_content || data.content);
            setIsUrdu(true);
            setIsPersonalized(false);
        } catch (e) {
            console.error(e);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="chapter-controls mb-4 p-4 bg-gray-100 rounded-lg flex gap-4">
            <button
                onClick={handlePersonalize}
                className={`px-4 py-2 rounded ${isPersonalized ? 'bg-green-500 text-white' : 'bg-blue-500 text-white'}`}
                disabled={loading}
            >
                {loading && !isUrdu ? 'Generating...' : '➡️ Personalize'}
            </button>

            <button
                onClick={handleTranslate}
                className={`px-4 py-2 rounded ${isUrdu ? 'bg-green-500 text-white' : 'bg-green-600 text-white'}`}
                disabled={loading}
            >
                {loading && isUrdu ? 'Translating...' : '➡️ Translate to Urdu'}
            </button>

            {content && (
                <div className="mt-4 p-4 border rounded bg-white shadow" style={{ direction: isUrdu ? 'rtl' : 'ltr' }}>
                    <h3 className="font-bold mb-2">{isUrdu ? 'Translated Content' : 'Personalized Content'}</h3>
                    <div dangerouslySetInnerHTML={{ __html: content.replace(/\n/g, '<br/>') }} />
                    {/* Note: In real docusaurus, render markdown properly using a Markdown renderer component */}
                </div>
            )}
        </div>
    );
};

export default ChapterControls;
