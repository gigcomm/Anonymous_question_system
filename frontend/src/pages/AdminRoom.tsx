import React, { useState, useEffect } from 'react';
import './AdminRoom.css';
import { Link } from 'react-router-dom';

type Participant = {
  id: number;
  name: string;
  isReady: boolean;
};

const AdminRoom: React.FC = () => {
  const [participants, setParticipants] = useState<Participant[]>([]);
  const [testStarted, setTestStarted] = useState(false);
  const socket = new WebSocket('ws://localhost:8080');

  useEffect(() => {
    socket.onopen = () => {
      console.log('Connected to server as admin');
    };

    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'update') {
        setParticipants(data.participants);
      } else if (data.type === 'startTest') {
        setTestStarted(true);
      }
    };

    return () => {
      socket.close();
    };
  }, [socket]);

  const startTest = () => {
    socket.send(JSON.stringify({ type: 'startTest', isAdmin: true }));
  };

  return (
    <div className="admin-room">
      <h1>Комната ожидания администратора</h1>
      {testStarted ? (
        <p>Тест начался!</p>
      ) : (
        <>
          <p>Количество участников: {participants.length}</p>
          <ul className="participant-list">
            {participants.map((participant) => (
              <li
                key={participant.id}
                className={`participant ${participant.isReady ? 'ready' : 'not-ready'}`}
              >
                {participant.name} — {participant.isReady ? 'Готов' : 'Не готов'}
              </li>
            ))}
          </ul>
          <button className="btn-start-test" onClick={startTest}>
           <Link to="questions"> Начать тест</Link>
          </button>
        </>
      )}
    </div>
  );
};

export default AdminRoom;
