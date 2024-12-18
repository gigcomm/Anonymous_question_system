import React, { useState } from 'react';
import './answer.css';

const Answer: React.FC = () => {
  const [selectedAnswer, setSelectedAnswer] = useState<string | null>(null);

  const options = ['Вариант 1', 'Вариант 2', 'Вариант 3', 'Вариант 4'];

  const handleSelect = (option: string) => {
    setSelectedAnswer(option);
  };

  const handleConfirm = () => {
    if (selectedAnswer) {
      
    } else {
      alert('Выберите вариант перед подтверждением!');
    }
  };

  return (
    <div className="answer-page">
      <div className="options-container">
        {options.map((option, index) => (
          <div
            key={index}
            className={`option ${selectedAnswer === option ? 'selected' : ''}`}
            onClick={() => handleSelect(option)}
          >
            {option}
          </div>
        ))}
      </div>
      <button className="confirm-button" onClick={handleConfirm}>
        Готово
      </button>
    </div>
  );
};

export default Answer;

