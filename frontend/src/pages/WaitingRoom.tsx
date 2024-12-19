import React, { useState, useEffect } from 'react';
import './WaitingRoom.css';

type Participant = {
  id: number;
  name: string;
  isReady: boolean;
};

const WaitingRoom: React.FC = () => {
  const [participants, setParticipants] = useState<Participant[]>([]);
  const [userReady, setUserReady] = useState(false);
  const socket = new WebSocket('ws://localhost:8080');

  const userId = 1; // Идентификатор текущего пользователя присылать с апи
  const userName = 'Текущий пользователь'; // Имя текущего пользователя присылать с апи

  useEffect(() => {
    // При подключении отправляем данные о новом участнике
    socket.onopen = () => {
      socket.send(
        JSON.stringify({ type: 'join', id: userId, name: userName })
      );
    };

    // Обновляем список участников при получении сообщения
    socket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      if (data.type === 'update') {
        setParticipants(data.participants);
      }
    };

    // Чистим соединение при размонтировании
    return () => {
      socket.close();
    };
  }, [socket, userId, userName]);

  const toggleReady = () => {
    setUserReady((prev) => !prev);
    socket.send(
      JSON.stringify({ type: 'toggleReady', id: userId })
    );
  };

  return (
    <div className="waiting-room">
      <h1>Комната ожидания</h1>
      <p>Количество участников: {participants.length}</p>
      <ul className="participant-list">
        {participants.map((participant) => (
          <li key={participant.id} className={`participant ${participant.isReady ? 'ready' : 'not-ready'}`}>
            {participant.name} — {participant.isReady ? 'Готов' : 'Не готов'}
          </li>
        ))}
      </ul>
      <button className={`btn ${userReady ? 'btn-ready' : 'btn-not-ready'}`} onClick={toggleReady}>
        {userReady ? 'Отменить готовность' : 'Готов'}
      </button>
    </div>
  );
};

export default WaitingRoom;
