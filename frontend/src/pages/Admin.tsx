import React from 'react';
import './Admin.css';

type Test = {
  id: number;
  title: string;
  createdAt: string;
};

type UserProfileProps = {
  username: string;
  registrationDate: string;
  createdTests: Test[];
};

const Admin: React.FC<UserProfileProps> = ({ username, registrationDate, createdTests }) => {
  return (
    <div className="profile-container">
      <h1 className="profile-header">Профиль пользователя</h1>
      <div className="profile-info">
        <h2>Имя пользователя: {username}</h2>
        <p>Дата регистрации: {registrationDate}</p>
      </div>
      <div>
        <h2>История созданных тестов</h2>
        {createdTests.length > 0 ? (
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
    createdTests: [
      { id: 1, title: 'Тест по ТимПрог', createdAt: '2023-12-17' },
      { id: 2, title: 'Тест по Аниме', createdAt: '2023-12-18' },
    ],
  };

  return <Admin {...mockUserData} />;
};


export default App;