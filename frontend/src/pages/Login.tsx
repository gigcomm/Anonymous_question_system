import { Link } from "react-router-dom"
import './Login.css'

const Login = () => {

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

        }}>Войти</button>

        <div className='LoginText1'>Ни разу не посещал нас?</div>
        <Link to={"/registr"}>
          <button className='RegBtn' type={'button'} onClick={() => {
          }}>Зарегестрироваться</button>
        </Link>
      </div>
    </div >
  )
}
export default Login
