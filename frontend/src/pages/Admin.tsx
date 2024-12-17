
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Admin.css';

type Test = {
  id: number;
  title: string;
  createdAt: string;
};

type UserProfileProps = {
  username: string;
  registrationDate: string;
};

const Admin: React.FC<UserProfileProps> = ({ username, registrationDate}) => {
  const [createdTests, setCreatedTests] = useState<Test[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchTests = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/test/');
        const tests = response.data.map((item: any) => ({
          id: item.id,
          title: item.title,
          createdAt: item.created_at,
        }));
        setCreatedTests(tests);
        setLoading(false);
      } catch (err) {
        setError('Ошибка загрузки тестов');
        setLoading(false);
      }
    };

    fetchTests();
  }, []);

  return (
    <div className="profile-container">
      <h1 className="profile-header">Профиль пользователя</h1>
      <div>
      <div className="profile-info">
        <h2>Имя пользователя: {username}</h2>
        <p>Дата регистрации: {registrationDate}</p>
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