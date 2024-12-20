import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import './Admin.css';

type Test = {
  id: number;
  title: string;
  createdAt: string;
  creator: number;
};

type UserProfileProps = {
  username: string;
  registrationDate: string;
};

const Admin: React.FC<UserProfileProps> = ({ username, registrationDate }) => {
  const [createdTests, setCreatedTests] = useState<Test[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchUserAndTests = async () => {
      try {
        // Получение данных о текущем пользователе через токен
        const token = localStorage.getItem('authToken'); // Замените на способ хранения токена в вашем приложении
        if (!token) {
          setError('Токен авторизации отсутствует');
          setLoading(false);
          return;
        }

        const userResponse = await axios.get('http://127.0.0.1:8000/api/auth/users/me/', {
          headers: { Authorization: `Token ${token}` },
        });

        const currentUser = userResponse.data;
        const userId = currentUser.id;

        // Получение и фильтрация тестов
        const testsResponse = await axios.get('http://127.0.0.1:8000/api/test/', {
          headers: { Authorization: `Token ${token}` },
        });

        const filteredTests = testsResponse.data
          .filter((test: any) => test.creator === userId)
          .map((item: any) => ({
            id: item.id,
            title: item.title,
            createdAt: item.created_at,
            creator: item.creator,
          }));

        setCreatedTests(filteredTests);
        setLoading(false);
      } catch (err) {
        setError('Ошибка загрузки данных');
        setLoading(false);
      }
    };

    fetchUserAndTests();
  }, []);

  return (
    <div className="profile-container">
      <h1 className="profile-header">Профиль пользователя</h1>
      <div>
        <div className="profile-info">
          <h2>Имя пользователя: {username}</h2>
          <p>Дата регистрации: {registrationDate}</p>
          <button><Link to="/testResults">TEST</Link></button>
        </div>
        <h2>История созданных тестов</h2>
        {loading ? (
          <p>Загрузка...</p>
        ) : error ? (
          <p>{error}</p>
        ) : createdTests.length > 0 ? (
          <ul className="tests-list">
            {createdTests.map((test) => (
              <li key={test.id} className="test-item">
                <h3>{test.title}</h3>
                <p>Дата создания: {test.createdAt}</p>
                <button className="button-test" id={test.title}><Link to="/testResults">TEST</Link></button>
              </li>
            ))}
          </ul>
        ) : (
          <p>Вы еще не создали ни одного теста.</p>
        )}
      </div>
    </div>
  );
};

const App: React.FC = () => {
  const mockUserData = {
    username: 'Кущенко Влад',
    registrationDate: '2023-12-16',
  };

  return <Admin {...mockUserData} />;
};

export default App;
