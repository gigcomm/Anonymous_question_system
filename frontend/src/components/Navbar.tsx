import { Link } from 'react-router-dom'
import useAuth from '../hooks/useAuth'
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
            <img src="/imgs/logo.png" className="site-icon" />
          </Link>
          <h1>Анонимные вопросы</h1>
        </div>
        <div className="nav-right">
          <Link to="/admin">
            <img src="/imgs/admin-icon.png" className="icon" /> Admin
          </Link>
          <Link to="/comment">
             Comments
          </Link>
          {isAuthenticated ? (
            <Link to="/logout">
              <img src="/imgs/logout-icon.png" className="icon" /> Logout
            </Link>
          ) : (
            <Link to="/login">
              <img src="imgs/login-icon.png" className="icon" /> Login
            </Link>
          )}
        </div>
      </nav>
    </>
  )
}


export default Navbar
