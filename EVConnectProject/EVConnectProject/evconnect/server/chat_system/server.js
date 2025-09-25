const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const app = express();
const server = http.createServer(app);
const io = socketIo(server, {
  cors: {
    origin: 'http://localhost:3001', // Update to match client port
    methods: ['GET', 'POST'],
    credentials: true
  },
  pingTimeout: 60000,
  pingInterval: 25000,
  transports: ['websocket'] // Force WebSocket transport
});

app.use(express.json());

app.get('/', (req, res) => {
  res.send('EVConnect Chat Server');
});

io.on('connection', (socket) => {
  console.log('New client connected:', socket.id);
  socket.on('message', (msg) => {
    console.log('Received:', msg);
    io.emit('message', { user: 'User', text: msg.text });
  });
  socket.on('disconnect', (reason) => {
    console.log('Client disconnected:', socket.id, 'Reason:', reason);
  });
  socket.on('error', (err) => {
    console.error('Socket error:', err.message);
  });
});

server.on('error', (err) => {
  console.error('Server error:', err.message);
});

server.listen(4000, '127.0.0.1', () => {
  console.log('Server running on http://127.0.0.1:4000');
});