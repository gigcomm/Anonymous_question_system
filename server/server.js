const WebSocket = require('ws');

const server = new WebSocket.Server({ port: 8080 }); //Выбор порта подключения,  const socket = new WebSocket('ws://your-server-address:8080');
let participants = [];
let testStarted = false;

server.on('connection', (ws) => {
  console.log('New client connected.');

  // Отправляем состояние теста и участников новому клиенту
  ws.send(JSON.stringify({ type: 'update', participants, testStarted }));

  ws.on('message', (message) => {
    const data = JSON.parse(message);

    if (data.type === 'join') {
      // Добавляем нового участника
      participants.push({ id: data.id, name: data.name, isReady: false });
      broadcast({ type: 'update', participants });
    } else if (data.type === 'toggleReady') {
      // Обновляем статус готовности
      participants = participants.map((p) =>
        p.id === data.id ? { ...p, isReady: !p.isReady } : p
      );
      broadcast({ type: 'update', participants });
    } else if (data.type === 'startTest' && data.isAdmin) {
      // Администратор запускает тест
      testStarted = true;
      broadcast({ type: 'startTest' });
    }
  });

  ws.on('close', () => {
    console.log('Client disconnected.');
    participants = participants.filter((p) => p.ws !== ws);
    broadcast({ type: 'update', participants });
  });

  const broadcast = (data) => {
    server.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(JSON.stringify(data));
      }
    });
  };
});

console.log('WebSocket server is running on ws://localhost:8080');
