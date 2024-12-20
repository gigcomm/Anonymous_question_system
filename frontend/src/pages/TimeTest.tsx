import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './TimeTest.css';

type Question = {
  id: number;
  text: string;
};

const TimeTest: React.FC = () => {
  const navigate = useNavigate();
  const QUESTION_TIMER = 2; // Время для каждого вопроса в секундах
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState<number>(0);
  const [remainingTime, setRemainingTime] = useState<number>(QUESTION_TIMER);

  const questions: Question[] = [
    { id: 1, text: 'What is the capital of France?' },
    { id: 2, text: 'What is 2 + 2?' },
    { id: 3, text: 'What is the largest planet?' },
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setRemainingTime((prev) => {
        if (prev === 1) {
          handleNextQuestion();
          return QUESTION_TIMER; // Сброс таймера для следующего вопроса
        }
        return prev - 1;
      });
    }, 1000);

    return () => clearInterval(interval); // Очистка интервала при размонтировании компонента
  }, [currentQuestionIndex]);

  const handleNextQuestion = () => {
    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      navigate('/admin'); // Перенаправление в профиль
      alert('Тест завершен!');
    }
  };

  return (
    <div className="timed-question-page-simple">
      <h1>Тест</h1>
      <div className="question-timer">
        <p>Вопрос {currentQuestionIndex + 1} из {questions.length}</p>
        <p>Осталось времени: {remainingTime} секунд</p>
      </div>
      <div className="question-container">
        <p>{questions[currentQuestionIndex].text}</p>
      </div>
    </div>
  );
};

export default TimeTest;
