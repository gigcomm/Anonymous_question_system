import React, { useState } from 'react';
import './Coments.css'

const Com: React.FC = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    feedback: '',
    options: '',
  });

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Form Data Submitted:', formData);
    alert('Form submitted successfully!');
  };

  return (
    <div className='base'>
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1 style={{ textAlign: 'center' }}>Форма обратной связи</h1>
      <p style={{ textAlign: 'center' }}>Пожалуйста, заполните форму ниже, чтобы оставить отзыв.</p>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px' }}>Имя:</label>
          <input
            type="text"
            name="name"
            value={formData.name}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px', fontSize: '16px' }}
            required
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px' }}>Email:</label>
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px', fontSize: '16px' }}
            required
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px' }}>Ваш отзыв:</label>
          <textarea
            name="feedback"
            value={formData.feedback}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px', fontSize: '16px', height: '100px' }}
            required
          />
        </div>
        <div style={{ marginBottom: '15px' }}>
          <label style={{ display: 'block', marginBottom: '5px' }}>Выберите категорию:</label>
          <select
            name="options"
            value={formData.options}
            onChange={handleChange}
            style={{ width: '100%', padding: '8px', fontSize: '16px' }}
            required
          >
            <option value="">Выберите...</option>
            <option value="feedback">Отзыв</option>
            <option value="question">Вопрос</option>
            <option value="other">Другое</option>
          </select>
        </div>
        <button
          type="submit"
          style={{
            backgroundColor: '#6200ea',
            color: 'white',
            padding: '10px 20px',
            fontSize: '16px',
            border: 'none',
            borderRadius: '5px',
            cursor: 'pointer',
          }}
        >
          Отправить
        </button>
      </form>
    </div>
    </div>
  );
};

export default Com
  