import React, { useState } from "react";
import "./TestResults.css";

type Participant = {
  id: number;
  name: string;
  results: { question: string; isCorrect: boolean }[];
};

const TestResults: React.FC = () => {
  const [participants, setParticipants] = useState<Participant[]>([
    {
      id: 1,
      name: "Иван Иванов",
      results: [
        { question: "Вопрос 1", isCorrect: true },
        { question: "Вопрос 2", isCorrect: false },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
        { question: "Вопрос 3", isCorrect: true },
 
      ],
    },
    {
      id: 2,
      name: "Анна Смирнова",
      results: [
        { question: "Вопрос 1", isCorrect: true },
        { question: "Вопрос 2", isCorrect: true },
        { question: "Вопрос 3", isCorrect: false },
      ],
    },
  ]);

  const [hoveredParticipant, setHoveredParticipant] = useState<number | null>(
    null
  );

  return (
    <div className="results-page">
      <h1 className="test-title">Результаты теста: "Название теста"</h1>
      <div className="participants-list">
        {participants.map((participant) => (
          <div
            key={participant.id}
            className="participant-item"
            onMouseEnter={() => setHoveredParticipant(participant.id)}
            onMouseLeave={() => setHoveredParticipant(null)}
          >
            <span className="participant-name">{participant.name}</span>

            {/* Всплывающее окно с результатами */}
            {hoveredParticipant === participant.id && (  //Должно отображаться поверх окон
              <div className="results-popup">
                <h4>Результаты:</h4>
                <ul>
                  {participant.results.map((result, index) => (
                    <li
                      key={index}
                      className={
                        result.isCorrect ? "correct-answer" : "wrong-answer"
                      }
                    >
                      {result.question}:{" "}
                      {result.isCorrect ? "Правильно" : "Неправильно"}
                    </li>
                  ))}
                </ul>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default TestResults;
