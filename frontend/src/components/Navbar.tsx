import { Link } from 'react-router-dom'
import useAuth from '../hooks/useAuth'
import './Navbar.css'


function Navbar() {
  const { isAuthenticated } = useAuth()
  return (
    <>
      <nav>
      <div className="nav-left">
        {/* Иконка сайта слева */}
        <Link to="/">
          <img src= "/imgs/icon.png" className="site-icon" />
        </Link>
      </div>
      <div className="nav-right">
        <Link to="/admin">
          <img src="/imgs/admin-icon.png" className="icon" /> Admin
        </Link>
        {isAuthenticated ? (
          <Link to="/logout">
            <img src="/imgs/logout-icon.png" className="icon" /> Logout
          </Link>
        ) : (
          <Link to="/login">
            <img  src="imgs/login-icon.png" className="icon" /> Login
          </Link>
        )}
        </div>
      </nav>
    </>
  )
}

export default Navbar
