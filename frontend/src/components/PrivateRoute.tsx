// Импортируем необходимые модули из библиотеки react-router-dom и пользовательский хук useAuth
import { Navigate, Outlet, useLocation } from "react-router-dom";
import useAuth from "../hooks/useAuth";

// Определяем функциональный компонент PrivateRoute
export const PrivateRoute = () => {

  // Получаем значение isAuthenticated из пользовательского хука useAuth
  const { isAuthenticated } = useAuth()

  // Получаем текущий маршрут из хука useLocation
  const location = useLocation()

  // Возвращаем условный оператор для рендеринга компонентов на основе состояния isAuthenticated
  return (
    // Если пользователь авторизован, то рендерим дочерние элементы текущего маршрута, используя компонент Outlet
    isAuthenticated === true ?
      <Outlet />
      // Если пользователь не авторизован, то перенаправляем его на маршрут /login с помощью компонента Navigate.
      // Свойство replace указывает, что текущий маршрут будет заменен на новый, чтобы пользователь не мог вернуться обратно, используя кнопку "назад" в браузере.
      :
      <Navigate to="/login" state={{ from: location }} replace />
  )
};
