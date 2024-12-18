import { Link } from 'react-router-dom'
//import useAuth from '../hooks/useAuth'
import useAuth  from "../hooks/useAuth";


import './Navbar.css'
import { Container } from 'react-bootstrap'
import { Component } from 'react'


function Navbar() {
  const { isAuthenticated } = useAuth()
  return (
    <>
      <nav className='Head'>
        <div className="nav-left">
          {/* Иконка сайта слева */}
          <Link to="/">
            <div className="site-icon" />
          </Link>
          <h1 className='retroshadow'>Анонимные Вопросы</h1>
        </div>
        <div className="nav-right">
          <Link to="/admin">
            Профиль
          </Link>
          <Link to="/comment">
             Отзыв
          </Link>
          {isAuthenticated ? (
            <Link to="/logout">
               Выход
            </Link>
          ) : (
            <Link to="/login">
               Вход
            </Link>
          )}
        </div>
      </nav>
    </>
  )
}


export default Navbar
