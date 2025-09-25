import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const PeerChat: React.FC = () => {
  const [message, setMessage] = useState('');
  const [messages, setMessages] = useState<string[]>([]);
  const [socket, setSocket] = useState<any>(null);

  useEffect(() => {
    const newSocket = io('http://127.0.0.1:4000', {
      reconnection: true,
      reconnectionAttempts: 5,
      reconnectionDelay: 1000,
      transports: ['websocket'],
      timeout: 10000
    });
    setSocket(newSocket);

    newSocket.on('connect', () => {
      console.log('Connected to WebSocket:', newSocket.id);
    });
    newSocket.on('connect_error', (err) => {
      console.error('Connection error:', err.message);
    });
    newSocket.on('message', (msg) => {
      console.log('Received message:', msg);
      setMessages((prev) => [...prev, `${msg.user}: ${msg.text}`]);
    });
    newSocket.on('error', (err) => {
      console.error('Socket error:', err.message);
    });

    return () => {
      newSocket.disconnect();
    };
  }, []);

  const sendMessage = () => {
    if (socket && message.trim()) {
      socket.emit('message', { text: message });
      setMessage('');
    } else {
      console.error('Socket not connected or empty message');
    }
  };

  return (
    <div className="p-4 border rounded-lg">
      <h2 className="text-2xl font-bold mb-2">Peer Chat</h2>
      <div className="h-40 overflow-y-auto border p-2 mb-2">
        {messages.map((msg, index) => (
          <p key={index}>{msg}</p>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        className="border p-2 w-full mb-2"
        placeholder="Type a message"
      />
      <button
        onClick={sendMessage}
        className="bg-blue-600 text-white p-2 rounded"
      >
        Send
      </button>
    </div>
  );
};

export default PeerChat;