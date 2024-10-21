import useAuth from '../hooks/useAuth';
import { useLocation, useNavigate } from 'react-router-dom';
import './Login.css'

const Login = () => {

  const { setAuth } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const from = location.state?.from?.pathname || '/'
  return (
    <div className='LoginBase'>
      <div className='LoginWindow'>
        <div className='LoginText'>Войти на сайт</div>
        <input
          className='LoginInput'
          type='text'
          placeholder='Логин'
        />

        {/* Поле для пароля */}
        <input
          className='LoginInput'
          type='password'
          placeholder='Пароль'
        />
        <button className='LoginBtn' type={'button'} onClick={() => {
          setAuth(true)
          navigate(from, { replace: true });
        }}>Login</button>
        </div>
    </div>
  )
}

export default Login
