import React, { useState } from 'react';
import './Create.css';
import { Link } from 'react-router-dom';
import axios from 'axios';

type Question = {
  id: number;
  type: 'text' | 'multiple-choice';
  questionText: string;
  options?: string[];
};

const Create: React.FC = () => {
  const [questions, setQuestions] = useState<Question[]>([]);
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [isAnonymous, setIsAnonymous] = useState(false); // Состояние для чекбокса
  const [selectedTime, setSelectedTime] = useState<string>('not'); // Состояние для выбранного времени
  const [isLoading, setIsLoading] = useState(false);

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

  const deleteOption = (id: number, optionIndex: number) => {
    setQuestions((prevQuestions) =>
      prevQuestions.map((q) => {
        if (q.id === id && q.options) {
          const updatedOptions = q.options.filter((_, index) => index !== optionIndex);
          return { ...q, options: updatedOptions };
        }
        return q;
      })
    );
  };

  const deleteQuestion = (id: number) => {
    setQuestions((prevQuestions) => prevQuestions.filter((q) => q.id !== id));
  };

  const handleSave = async () => {
    const token = localStorage.getItem('authToken');

    if (!token) {
      alert('Пожалуйста, авторизуйтесь');
      return;
    }

    try {
      setIsLoading(true);

      // Шаг 1: Получаем данные текущего пользователя
      const userResponse = await axios.get('http://localhost:8000/api/auth/users/me/', {
        headers: {
          Authorization: `Token ${token}`,
        },
      });

      const userId = userResponse.data.id;

      // Шаг 2: Отправляем запрос на создание теста
      const testResponse = await axios.post(
        'http://localhost:8000/api/test/',
        {
          title,
          description,
          creator: userId,
          is_active: true,
          is_anonymous: isAnonymous,
          default_time_limit: selectedTime === 'not' ? null : parseInt(selectedTime, 10),
        },
        {
          headers: {
            Authorization: `Token ${token}`,
          },
        }
      );

      if (testResponse.status === 201) {
        const testId = testResponse.data.id;

        // Шаг 3: Фильтруем и создаем записи для вопросов
        const filteredQuestions = questions.filter((q) => q.questionText.trim() !== ''); // Убираем пустые вопросы
        const reorderedQuestions = filteredQuestions.map((q, index) => ({
          ...q,
          order: index + 1, // Обновляем порядок вопросов на основе текущего состояния
        }));

        const questionRequests = reorderedQuestions.map((q) =>
          axios.post(
            'http://localhost:8000/api/test/questions/',
            {
              test: testId,
              text: q.questionText,
              type: q.type,
              options: q.options || [],
              order: q.order,
            },
            {
              headers: {
                Authorization: `Token ${token}`,
              },
            }
          )
        );

        await Promise.all(questionRequests);

        alert('Тест и вопросы успешно созданы!');

        // Очистить поля после успешного сохранения
        setTitle('');
        setDescription('');
        setIsAnonymous(false);
        setQuestions([]);
        setSelectedTime('not');
      } else {
        alert('Ошибка при создании теста');
      }
    } catch (error) {
      alert('Произошла ошибка. Попробуйте снова.');
      console.error(error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="base">
      <div className="Test" style={{ maxWidth: '1000px', margin: '0 auto', padding: '20px', fontFamily: 'Arial, sans-serif' }}>
        <h1 style={{ textAlign: 'center', fontSize: '40px' }}>Создание теста</h1>

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

        <div className="Text">
          <label>Таймер: </label>
          <select
            id="time"
            name="time"
            value={selectedTime}
            onChange={(e) => setSelectedTime(e.target.value)}
          >
            <option disabled selected value=""> -- Выберите время -- </option>
            <option value="9999">Без ограничения</option>
            <option value="15">15 сек</option>
            <option value="30">30 сек</option>
            <option value="60">60 сек</option>
          </select> 
        </div>

        <div className="Text">
          <input
            type="checkbox"
            id="Anon"
            checked={isAnonymous}
            onChange={() => setIsAnonymous((prev) => !prev)}
          />
          <label>Анонимность теста</label>
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
                className="text-q"
                type="text"
                placeholder="Введите текст вопроса"
                value={q.questionText}
                onChange={(e) => handleQuestionChange(q.id, 'questionText', e.target.value)}
              />
              {q.type === 'multiple-choice' && q.options && (
                <div>
                  {q.options.map((option, index) => (
                    <div key={index} style={{ display: 'flex', alignItems: 'center', marginBottom: '5px' }}>
                      <input
                        type="text"
                        placeholder={`Вариант ${index + 1}`}
                        value={option}
                        onChange={(e) => handleQuestionChange(q.id, 'optionText', e.target.value, index)}
                        style={{ width: '80%', padding: '8px', fontSize: '14px' }}
                      />
                      <button
                        type="button"
                        className="delete-option"
                        onClick={() => deleteOption(q.id, index)}
                      >
                        Удалить
                      </button>
                    </div>
                  ))}
                  <button className="add-var" type="button" onClick={() => addOption(q.id)}>
                    Добавить вариант
                  </button>
                </div>
              )}
              <button className="delet-q" type="button" onClick={() => deleteQuestion(q.id)}>
                Удалить вопрос
              </button>
            </div>
          ))}
        </div>

        <div>
          <button className="add-var-q" type="button" onClick={() => addQuestion('multiple-choice')}>
            Добавить вопрос с вариантами
          </button>
        </div>

        <Link to="/adminRoom">
          <button className="save-test" onClick={handleSave} disabled={isLoading}>
            {isLoading ? 'Создание...' : 'Создать тест'}
          </button>
        </Link>
      </div>
    </div>
  );
};

export default Create;
