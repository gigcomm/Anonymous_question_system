import { Link } from "react-router-dom"
import "./Main.css"

const Login = () => {

    return (
        <div className="base">
            <Link to="/create">
                <div className="button" id="button-3">
                    <div id="circle"></div>
                    <a>Создание теста</a>
                </div>
            </Link>
        </div>
    )
}
export default Login
