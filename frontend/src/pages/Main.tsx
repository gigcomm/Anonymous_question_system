import React, { useState } from 'react';

type Question = {
  id: number;
  type: 'text' | 'multiple-choice';
  questionText: string;
  options?: string[];
};

const Main: React.FC = () => {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');

  const addQuestion = (type: 'text' | 'multiple-choice') => {
    setQuestions([
      ...questions,
      { id: Date.now(), type, questionText: '', options: type === 'multiple-choice' ? [''] : undefined },
    ]);
  };

  const handleQuestionChange = (id: number, field: string, value: string, optionIndex?: number) => {
    setQuestions((prevQuestions) =>
      prevQuestions.map((q) => {
        if (q.id !== id) return q;
        if (field === 'questionText') return { ...q, questionText: value };
        if (field === 'optionText' && q.options && optionIndex !== undefined) {
          const updatedOptions = [...q.options];
          updatedOptions[optionIndex] = value;
          return { ...q, options: updatedOptions };
        }
        return q;
      })
    );
  };

  const addOption = (id: number) => {
    setQuestions((prevQuestions) =>
      prevQuestions.map((q) => {
        if (q.id === id && q.options) {
          return { ...q, options: [...q.options, ''] };
        }
        return q;
      })
    );
  };

  const deleteQuestion = (id: number) => {
    setQuestions((prevQuestions) => prevQuestions.filter((q) => q.id !== id));
  };

  const handleSave = () => {
    console.log({ title, description, questions });
    alert('Тест сохранен!');
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1 style={{ textAlign: 'center' }}>Создание теста</h1>
      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          placeholder="Название теста"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          style={{ width: '100%', padding: '10px', fontSize: '18px', marginBottom: '10px' }}
        />
        <textarea
          placeholder="Описание теста"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          style={{ width: '100%', padding: '10px', fontSize: '16px', height: '80px' }}
        />
      </div>
      <div>
        {questions.map((q) => (
          <div
            key={q.id}
            style={{
              marginBottom: '20px',
              padding: '15px',
              border: '1px solid #ddd',
              borderRadius: '5px',
              backgroundColor: '#f9f9f9',
            }}
          >
            <input
              type="text"
              placeholder="Введите текст вопроса"
              value={q.questionText}
              onChange={(e) => handleQuestionChange(q.id, 'questionText', e.target.value)}
              style={{ width: '100%', padding: '10px', fontSize: '16px', marginBottom: '10px' }}
            />
            {q.type === 'multiple-choice' && q.options && (
              <div>
                {q.options.map((option, index) => (
                  <div key={index} style={{ marginBottom: '5px' }}>
                    <input
                      type="text"
                      placeholder={`Вариант ${index + 1}`}
                      value={option}
                      onChange={(e) => handleQuestionChange(q.id, 'optionText', e.target.value, index)}
                      style={{ width: '80%', padding: '8px', fontSize: '14px' }}
                    />
                  </div>
                ))}
                <button
                  type="button"
                  onClick={() => addOption(q.id)}
                  style={{
                    backgroundColor: '#007bff',
                    color: 'white',
                    padding: '5px 10px',
                    fontSize: '14px',
                    border: 'none',
                    borderRadius: '3px',
                    cursor: 'pointer',
                  }}
                >
                  Добавить вариант
                </button>
              </div>
            )}
            <button
              type="button"
              onClick={() => deleteQuestion(q.id)}
              style={{
                backgroundColor: '#dc3545',
                color: 'white',
                padding: '5px 10px',
                fontSize: '14px',
                border: 'none',
                borderRadius: '3px',
                cursor: 'pointer',
                marginTop: '10px',
              }}
            >
              Удалить вопрос
            </button>
          </div>
        ))}
      </div>
      <div>
        <button
          type="button"
          onClick={() => addQuestion('text')}
          style={{
            backgroundColor: '#28a745',
            color: 'white',
            padding: '10px 20px',
            fontSize: '16px',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
            marginRight: '10px',
          }}
        >
          Добавить текстовый вопрос
        </button>
        <button
          type="button"
          onClick={() => addQuestion('multiple-choice')}
          style={{
            backgroundColor: '#17a2b8',
            color: 'white',
            padding: '10px 20px',
            fontSize: '16px',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
          }}
        >
          Добавить вопрос с вариантами
        </button>
      </div>
      <button
        onClick={handleSave}
        style={{
          marginTop: '20px',
          backgroundColor: '#343a40',
          color: 'white',
          padding: '10px 20px',
          fontSize: '16px',
          border: 'none',
          borderRadius: '5px',
          cursor: 'pointer',
          display: 'block',
          width: '100%',
        }}
      >
        Сохранить тест
      </button>
    </div>
  );
};


export default Main
  