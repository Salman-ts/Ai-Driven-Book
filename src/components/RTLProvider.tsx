import React from 'react';

interface Props {
    children: React.ReactNode;
    isRTL: boolean;
}

export const RTLProvider: React.FC<Props> = ({ children, isRTL }) => {
    return (
        <div
            dir={isRTL ? 'rtl' : 'ltr'}
            className={isRTL ? 'rtl-content' : 'ltr-content'}
            style={{
                fontFamily: isRTL ? "'Noto Nastaliq Urdu', serif" : 'inherit',
                direction: isRTL ? 'rtl' : 'ltr',
                textAlign: isRTL ? 'right' : 'left'
            }}
        >
            {children}
        </div>
    );
};
