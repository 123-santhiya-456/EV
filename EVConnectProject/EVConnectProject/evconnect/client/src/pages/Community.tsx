import React from 'react';
  import ChatBot from '../components/Community/ChatBot';
  import PeerChat from '../components/Community/PeerChat';

  const Community: React.FC = () => {
    return (
      <div className="container mx-auto p-4">
        <h1 className="text-3xl font-bold mb-4">Community</h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <ChatBot />
          <PeerChat />
        </div>
      </div>
    );
  };

  export default Community;