import React, { useState, useEffect, useRef } from 'react';
import './AdminRoom.css';
import { useNavigate } from 'react-router-dom';

type Participant = {
  id: number;
  name: string;
  isReady: boolean;
};

 type AdminRoomProps = {
   testId: string; // Идентификатор теста
   wsUrl: string; // URL WebSocket сервера
 };


const AdminRoom: React.FC = () => { //  React.FC<AdminRoomProps> = ({ testId, wsUrl })
  const navigate = useNavigate();
  const [participants, setParticipants] = useState<Participant[]>([]);
  const [testLink, setTestLink] = useState('');
  const wsRef = useRef<WebSocket | null>(null);
 

  //затычка
  const testId =1;
  const wsUrl = "Hello";


  useEffect(() => {
    const link = `${window.location.origin}/test/${testId}`;  // тут ссылку менять если что
    setTestLink(link);

    wsRef.current = new WebSocket(wsUrl);

    wsRef.current.onopen = () => {
      console.log('WebSocket connection established');
      wsRef.current?.send(JSON.stringify({ action: 'joinAdminRoom', testId }));
    };

    wsRef.current.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.action === 'updateParticipants') {
        setParticipants(data.participants);
      }
    };

    wsRef.current.onerror = (error) => {
      console.error('WebSocket error:', error);
    };

    wsRef.current.onclose = () => {
      console.log('WebSocket connection closed');
    };

    return () => {
      wsRef.current?.close();
    };
  }, [wsUrl, testId]);

  const copyLinkToClipboard = () => {
    navigator.clipboard.writeText(testLink).then(() => {
      alert('Ссылка скопирована!');
    });
  };

  const toggleReady = (id: number) => {
    const updatedParticipants = participants.map((p) =>
      p.id === id ? { ...p, isReady: !p.isReady } : p
    );
    setParticipants(updatedParticipants);

    wsRef.current?.send(
      JSON.stringify({
        action: 'toggleReady',
        participantId: id,
        isReady: updatedParticipants.find((p) => p.id === id)?.isReady,
      })
    );
  };

  const startTest = () => {
    //wsRef.current?.send(JSON.stringify({ action: 'startTest', testId })); --это веб сокет ---
    alert('Тест начался!');
    navigate(`/test`);  /// добавить если что${testId}
    window.location.href = `/test`; // --это веб сокет ---  добавить если что${testId}
  };

  const allReady = participants.length > 0 && participants.every((p) => p.isReady);

  return (
    <div className="admin-room">
      <h1>Комната ожидания</h1>
      <p>Тест ID: {testId}</p>
      <div className="link-container">
        <input
          type="text"
          value={testLink}
          readOnly
          className="test-link"
          onClick={() => navigator.clipboard.writeText(testLink)}
        />
        <button className="copy-link-btn" onClick={copyLinkToClipboard}>
          Скопировать ссылку
        </button>
      </div>
      <h2>Участники:</h2>
      <ul>
        {participants.map((participant) => (
          <li key={participant.id}>
            {participant.name} - {participant.isReady ? 'Готов' : 'Не готов'}
            <button
              className="toggle-ready-btn"
              onClick={() => toggleReady(participant.id)}
            >
              {participant.isReady ? 'Снять готовность' : 'Поставить готовность'}
            </button>
          </li>
        ))}
      </ul>
      <button
        className="start-test-btn"
        onClick={startTest}
        //disabled={!allReady} для того, чтобы не начать тест пока все не готовы
      >
        Начать тест
      </button>
    </div>
  );
};

export default AdminRoom;
