import React, { useState, useRef, useEffect } from 'react';
import clsx from 'clsx';
import './ChatWidget.css';
import { sendChatMessage } from '../services/api';

interface Message {
    role: 'user' | 'assistant';
    content: string;
    citations?: { id: number; chapter: string; section: string }[];
}

const ChatWidget = () => {
    const [isOpen, setIsOpen] = useState(false);
    const [messages, setMessages] = useState<Message[]>([]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const [selectedText, setSelectedText] = useState('');
    const [showAskBtn, setShowAskBtn] = useState(false);
    const [btnPos, setBtnPos] = useState({ x: 0, y: 0 });

    const chatEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(scrollToBottom, [messages]);

    // Highlight-to-Ask Logic
    useEffect(() => {
        const handleSelection = () => {
            const selection = window.getSelection();
            const text = selection?.toString().trim();

            if (text && text.length > 5) {
                const range = selection?.getRangeAt(0);
                const rect = range?.getBoundingClientRect();
                if (rect) {
                    setSelectedText(text);
                    setBtnPos({
                        x: rect.right + window.scrollX,
                        y: rect.top + window.scrollY - 40
                    });
                    setShowAskBtn(true);
                }
            } else {
                setShowAskBtn(false);
            }
        };

        document.addEventListener('mouseup', handleSelection);
        return () => document.removeEventListener('mouseup', handleSelection);
    }, []);

    const askSelection = (e: React.MouseEvent) => {
        e.stopPropagation();
        setIsOpen(true);
        setInput(`Explain this: "${selectedText}"`);
        setShowAskBtn(false);
        // Optional: clear selection
        window.getSelection()?.removeAllRanges();
    };

    const sendMessage = async () => {
        if (!input.trim()) return;

        const userMsg = input;
        setMessages(prev => [...prev, { role: 'user', content: userMsg }]);
        setInput('');
        setLoading(true);

        try {
            const response = await sendChatMessage(userMsg, messages);

            if (!response.ok) throw new Error('Network response was not ok');

            const reader = response.body?.getReader();
            const decoder = new TextDecoder();
            let assistantMsg = '';

            setMessages(prev => [...prev, { role: 'assistant', content: '' }]);

            if (reader) {
                while (true) {
                    const { done, value } = await reader.read();
                    if (done) break;
                    const chunk = decoder.decode(value);
                    assistantMsg += chunk;

                    // Simple streaming update (ignoring citation parsing for stream smoothness)
                    setMessages(prev => {
                        const newMsgs = [...prev];
                        newMsgs[newMsgs.length - 1].content = assistantMsg;
                        return newMsgs;
                    });
                }
            }
        } catch (error) {
            console.error(error);
            setMessages(prev => [...prev, { role: 'assistant', content: "Error connecting to AI." }]);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            {showAskBtn && (
                <button
                    className="highlight-ask-btn"
                    style={{
                        position: 'absolute',
                        top: btnPos.y,
                        left: btnPos.x,
                        zIndex: 1000,
                        background: '#1A73E8',
                        color: 'white',
                        border: 'none',
                        borderRadius: '20px',
                        padding: '5px 15px',
                        cursor: 'pointer',
                        boxShadow: '0 2px 10px rgba(0,0,0,0.2)',
                        fontWeight: 'bold',
                        animation: 'popIn 0.2s ease-out'
                    }}
                    onClick={askSelection}
                >
                    ✨ Ask AI
                </button>
            )}

            <div className={clsx('chat-widget', { 'open': isOpen })}>
                {!isOpen && (
                    <button className="chat-toggle" onClick={() => setIsOpen(true)}>
                        💬
                    </button>
                )}
                {isOpen && (
                    <div className="chat-window">
                        <div className="chat-header">
                            <span>AI Assistant</span>
                            <button onClick={() => setIsOpen(false)}>✖</button>
                        </div>
                        <div className="chat-messages">
                            {messages.map((m, i) => (
                                <div key={i} className={`message ${m.role}`}>
                                    {m.content}
                                    {m.citations && (
                                        <div className="citations-box">
                                            <small>Sources:</small>
                                            {m.citations.map(c => (
                                                <span key={c.id}> [{c.id}] {c.chapter} </span>
                                            ))}
                                        </div>
                                    )}
                                </div>
                            ))}
                            {loading && <div className="loading">Thinking...</div>}
                            <div ref={chatEndRef} />
                        </div>
                        <div className="chat-input-area">
                            <input
                                value={input}
                                onChange={e => setInput(e.target.value)}
                                onKeyPress={e => e.key === 'Enter' && sendMessage()}
                                placeholder="Ask about this page..."
                            />
                            <button onClick={sendMessage}>Send</button>
                        </div>
                    </div>
                )}
            </div>
        </>
    );
};

export default ChatWidget;
