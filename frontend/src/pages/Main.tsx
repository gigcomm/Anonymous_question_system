import { Link } from "react-router-dom"
import "./Main.css"

const Login = () => {

    return (
        <div className="base">
            <Link to="/create">
                <div className="button" id="button-3">
                    <div id="circle"></div>
                    <a>Создать тест</a>
                </div>

            </Link>

            <div className="button" id="button-3">
                <div id="circle"></div>
                <a>Выбрать тест</a>
            </div>
        </div>
    )
}
export default Login
