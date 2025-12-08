import React, { useState } from 'react';

const ChapterControls = () => {
    const [isPersonalized, setIsPersonalized] = useState(false);
    const [isUrdu, setIsUrdu] = useState(false);
    const [loading, setLoading] = useState(false);
    const [content, setContent] = useState<string | null>(null);

    const handlePersonalize = async () => {
        setLoading(true);
        // Get current page content logic (simplified: user needs to pass context or we select dom)
        // For Docusaurus, often we operate on the MDX content passed as props or via context.
        // Here we'll simulate fetching/sending.

        try {
            const currentContent = document.querySelector('article')?.innerText || "Chapter Content";

            const res = await fetch('http://localhost:8000/content/personalize', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ content: currentContent })
            });
            const data = await res.json();
            setContent(data.content);
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

            const res = await fetch('http://localhost:8000/content/translate', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ content: currentContent })
            });
            const data = await res.json();
            setContent(data.content);
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
