import { createContext, useState, useEffect } from "react";

type AuthContextType = {
  isAuthenticated: boolean;
  setAuth: (auth: boolean) => void;
  logout: () => void;
  loading: boolean;
};

const AuthContext = createContext<AuthContextType>({
  isAuthenticated: false,
  setAuth: () => {},
  logout: () => {},
  loading: true
});

export const AuthProvider = ({ children }: { children: React.ReactNode }) => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(true);

  // Восстанавливаем авторизацию из localStorage при загрузке
  useEffect(() => {
    const token = localStorage.getItem("authToken");
    if (token) {
      setIsAuthenticated(true);
    }
    setLoading(false); // Когда проверка завершилась, меняем loading на false
  }, []);

  const setAuth = (auth: boolean) => {
    if (auth) {
      // Сохраняем токен, если есть необходимость, уже сделано где-то в логине
    } else {
      localStorage.removeItem("authToken");
    }
    setIsAuthenticated(auth);
  };

  const logout = () => {
    localStorage.removeItem("authToken");
    setIsAuthenticated(false);
  };

  return (
    <AuthContext.Provider value={{ isAuthenticated, setAuth, logout, loading }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;