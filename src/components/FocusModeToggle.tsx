import React, { useEffect, useState } from 'react';
import clsx from 'clsx';
import { FaExpand, FaCompress } from 'react-icons/fa';

export default function FocusModeToggle() {
    const [isFocusMode, setFocusMode] = useState(false);

    useEffect(() => {
        if (isFocusMode) {
            document.body.classList.add('focus-mode');
        } else {
            document.body.classList.remove('focus-mode');
        }
    }, [isFocusMode]);

    return (
        <button
            className={clsx('button button--secondary button--sm', 'focus-toggle')}
            onClick={() => setFocusMode(!isFocusMode)}
            title={isFocusMode ? "Exit Focus Mode" : "Enter Focus Mode"}
            style={{
                position: 'fixed',
                bottom: '80px', // Above chat widget
                right: '20px',
                zIndex: 200,
                borderRadius: '50%',
                width: '40px',
                height: '40px',
                border: 'none',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                boxShadow: '0 4px 12px rgba(0,0,0,0.2)'
            }}
        >
            {isFocusMode ? <FaCompress /> : <FaExpand />}
        </button>
    );
}
