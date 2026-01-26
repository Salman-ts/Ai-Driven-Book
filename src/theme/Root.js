import React from 'react';
import Root from '@theme/Root';
import ChatWidget from '../components/ChatWidget';
import FeatureToggles from '../components/FeatureToggles';
import ChapterControls from '../components/ChapterControls';
import { useLocation } from '@docusaurus/router';

export default function RootWrapper({ children }) {
    const location = useLocation();
    const isDocsPage = location.pathname.includes('/docs/');

    return (
        <>
            {children}
            <ChatWidget />
            {isDocsPage && <FeatureToggles />}
        </>
    );
}

