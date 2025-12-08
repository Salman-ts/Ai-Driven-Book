import React from 'react';
import Root from '@theme/Root';
import ChatWidget from '../components/ChatWidget';
import ChapterControls from '../components/ChapterControls';
import { useLocation } from '@docusaurus/router';

export default function RootWrapper({ children }) {
    const location = useLocation();
    const isDocsPage = location.pathname.startsWith('/ai-book/docs/'); // Check base url

    return (
        <>
            {children}
            {/* 
        Inject Chapter Controls at the top of content? 
        Root wraps the whole app, so injecting inside the doc article is hard here.
        Instead, we will swarm the DocItem via swizzle or just place ChatWidget here globally.
      */}
            <ChatWidget />
        </>
    );
}
