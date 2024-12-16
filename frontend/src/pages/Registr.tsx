import { Link } from "react-router-dom"
import './Registr.css'

const Registr = () => {

    return (
        <div className='LoginBase'>
            <div className='LoginWindow'>
                <div className='LoginText'>Зарегистрироваться на сайте</div>
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
                <input
                    className='LoginInput'
                    type='password'
                    placeholder='Повторите пароль'
                />

                <button className='RegBtn1' type={'button'} onClick={() => {

                }}>Зарегестрироваться</button>

                <div className='LoginText1'>Уже были у нас?</div>
                <Link to={"/login"}>
                    <button className='LoginBtn1' type={'button'} onClick={() => {
                    }}>Войти</button>
                </Link>

            </div>
        </div>
    )
}
export default Registr
