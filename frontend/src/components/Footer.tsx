import React from 'react';
import './Footer.css';

const Footer: React.FC = () => {
  return (
    <footer className="footer">
      <div className="footer-container">
        <div className="footer-section creator">
          <h3>Создатель сайта</h3>
          <p>Кущенко Владислав</p>
          <p>Гулый Игорь</p>
          <p>Гумен Максим</p>
          <p className="niz">Коржова Мария</p>
        </div>
        <div className="footer-section contacts">
          <h3>Наши контакты</h3>
          <ul>
            <li>Email: <a href="mailto:test@mail.ru">test@mail.ru</a></li>
            <li>Телефон: <a href="tel:+1234567890">+7 929 000 ** **</a></li>
            <li>Адрес: Белгород, ул. Костюкова, д. 5</li>
          </ul>
        </div>
        <div className="footer-section standard-phrases">
          <h3>Информация</h3>
          <p>Все права защищены © {new Date().getFullYear()}</p>
          <p>Спасибо за посещение нашего сайта!</p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
