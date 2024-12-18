import React, { useState, FormEvent } from "react"; 
import { useLocation, useNavigate } from "react-router-dom"; 
import useAuth from "../hooks/useAuth"; 
import { AuthService } from "../context/AuthServis"; 
import "./Login.css"; 
 
const Login: React.FC = () => { 
 const { setAuth } = useAuth(); 
 const navigate = useNavigate(); 
 const location = useLocation(); 
 const [username, setUsername] = useState<string>(""); 
 const [password, setPassword] = useState<string>(""); 
 const [email, setEmail] = useState<string>(""); 
 const [isRegistering, setIsRegistering] = useState<boolean>(false); 
 const [error, setError] = useState<string>(""); 
 const from = location.state?.from?.pathname || "/"; 
 
 const handleLogin = async (e: FormEvent) => { 
 e.preventDefault(); 
 setError(""); 
 
 if (isRegistering) { 
 const result = await AuthService.register(username, password, email); 
 if (result.success) { 
 setIsRegistering(false); 
 } else { 
 setError(result.error || "Ошибка регистрации"); 
      }
 } else { 
 const result = await AuthService.login(username, password); 
 if (result.success) { 
 setAuth(true); 
 localStorage.setItem("authToken", result.token || ""); 
 navigate(from, { replace: true }); 
 } else { 
 setError(result.error || "Ошибка логина"); 
      }
    }
  };
 
 const handleRegisterClick = () => { 
 setIsRegistering(!isRegistering); 
  };
 
 return ( 
 <div className="LoginBase"> 
 <form className="LoginWindow" onSubmit={handleLogin}> 
 <div className="LoginText">{isRegistering ? "Регистрация" : "Войти на сайт"}</div> 
 <input 
 className="LoginInput" 
 type="text" 
 placeholder="Логин" 
 value={username} 
 onChange={(e) => setUsername(e.target.value)} 
 required 
        />
 <input 
 className="LoginInput" 
 type="password" 
 placeholder="Пароль" 
 value={password} 
 onChange={(e) => setPassword(e.target.value)} 
 required 
        />
 {isRegistering && ( 
 <input 
 className="LoginInput" 
 type="email" 
 placeholder="Электронная почта" 
 value={email} 
 onChange={(e) => setEmail(e.target.value)} 
            required
          />
        )}
 <button className="LoginBtn" type="submit"> 
 {isRegistering ? "Зарегистрироваться" : "Войти"} 
 </button> 
 <button 
 type="button" 
 className="RegisterBtn" 
 onClick={handleRegisterClick} 
        >
          {isRegistering ? "Уже есть аккаунт? Войти" : "Регистрация"}
        </button>
      </form>
    </div>
  );
};
 
export default Login;
 