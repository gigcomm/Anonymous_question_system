import React, { useState } from 'react';
import './Main.css';
import { Link } from 'react-router-dom';




const Main: React.FC = () => {
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [testLink, setTestLink] = useState('');

    const handleOpenModal = () => {
        setIsModalOpen(true);
    };

    const handleCloseModal = () => {
        setIsModalOpen(false);
        setTestLink(''); // Сбрасываем ссылку при закрытии
    };

    const handleJoinTest = () => {
        if (testLink) {
          if (/^https?:\/\/.+$/.test(testLink)) {
            window.location.href = testLink; // Переход по введенной ссылке
          } else {
            alert('Введите корректную ссылку, начинающуюся с http:// или https://');
          }
        } else {
          alert('Введите ссылку на тест!');
        }
      };
    
    return (
        <div className="main-container">
            {/* Фоновая анимация */}
            <div className="background-animation">
                <div className="circle small" style={{ left: '10%', animationDelay: '0s' }}></div>
                <div className="circle medium" style={{ left: '50%', animationDelay: '3s' }}></div>
                <div className="circle large" style={{ left: '80%', animationDelay: '6s' }}></div>
                <div className="circle small" style={{ left: '70%', animationDelay: '1s' }}></div>
                <div className="circle medium" style={{ left: '20%', animationDelay: '4s' }}></div>
            </div>

            {/* Основной контент */}
            <main className="main-content">
                <header className="main-header">
                    <h1>Создавай и проходи тесты легко</h1>
                    <p>Простой инструмент для создания опросов, тестов и викторин.</p>
                </header>

                <div className="main-buttons">
                    <a className="btn btn-create">
                        <Link to="/create">
                            ➕ Создать тест
                        </Link>
                    </a>
                    <a className="btn btn-view" onClick={handleOpenModal}>
                        🔍 Подключиться к тесту
                    </a>
                </div>
                {isModalOpen && (
                    <div className="modal">
                        <div className="modal-content">
                            <h2>Подключение к тесту</h2>
                            <input
                                type="text"
                                placeholder="Введите ссылку на тест"
                                value={testLink}
                                onChange={(e) => setTestLink(e.target.value)}
                                className="modal-input"
                            />
                            <div className="modal-buttons">
                                <button className="btn modal-btn" onClick={handleJoinTest}>        <Link to="/waitingRoom"> Подключиться </Link></button>
                                <button className="btn modal-btn-cancel" onClick={handleCloseModal}>Отмена</button>
                            </div>
                        </div>
                    </div>
                )}
                <section className="features">
                    <div className="feature-card">
                        <h3>🚀 Быстро и удобно</h3>
                        <p>Создавай тесты за несколько минут с интуитивным интерфейсом.</p>
                    </div>
                    <div className="feature-card">
                        <h3>🛡 Анонимность</h3>
                        <p>Проходи тесты и отправляй результаты.</p>
                    </div>
                    <div className="feature-card">
                        <h3>📊 Статистика</h3>
                        <p>Анализируй результаты тестов с удобной визуализацией.</p>
                    </div>
                </section>

                <section className="stats">
                    <p>📈 Уже создано <strong>1200+</strong> тестов и <strong>8500+</strong> прохождений!</p>
                </section>
            </main>
        </div>
    );
};

export default Main;
