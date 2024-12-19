import React, { useState } from 'react';
import './Test.css';

const Test = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [showParticipants, setShowParticipants] = useState(false);

  const questions = [
    'Первый вопрос',
    'Второй вопрос',
    'Третий вопрос',
  ];

  const totalQuestions = questions.length;

  const handleNextQuestion = () => {
    if (currentQuestion < totalQuestions - 1) {
      setCurrentQuestion(currentQuestion + 1);
    }
  };

  const handlePreviousQuestion = () => {
    if (currentQuestion > 0) {
      setCurrentQuestion(currentQuestion - 1);
    }
  };

  const toggleParticipants = () => {
    setShowParticipants(!showParticipants);
  };

  return (
    <div className="question-page">
      <div className="question-container">
        <h1>Вопрос {currentQuestion + 1}</h1>
        <p className="question-text">{questions[currentQuestion]}</p>
        <div className="question-info">
          <p>Всего вопросов: {totalQuestions}</p>
          <p>Осталось вопросов: {totalQuestions - currentQuestion - 1}</p>
        </div>
        <div className="navigation-buttons">
          <button 
            className="prev-button" 
            onClick={handlePreviousQuestion} 
            disabled={currentQuestion === 0}
          >
            Назад
          </button>
          <button 
            className="next-button" 
            onClick={handleNextQuestion} 
            disabled={currentQuestion === totalQuestions - 1}
          >
            Вперед
          </button>
        </div>
      </div>

      <button className="participants-button" onClick={toggleParticipants}>
        {showParticipants ? 'Скрыть участников' : 'Показать участников'}
      </button>

      {showParticipants && (
        <div className="participants-list">
          <h2>Список участников</h2>
          <ul>
            <li>Участник 1</li>
            <li>Участник 2</li>
            <li>Участник 3</li>
          </ul>
        </div>
      )}
    </div>
  );
};

export default Test;