import React from 'react';
import Content from '@theme-original/DocItem/Content';
import ChapterControls from '@site/src/components/ChapterControls';

export default function ContentWrapper(props) {
    return (
        <>
            <div style={{ marginBottom: '2rem' }}>
                <ChapterControls />
            </div>
            <Content {...props} />
        </>
    );
}
