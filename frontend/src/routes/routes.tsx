import { Route, Routes } from 'react-router-dom';
import { PrivateRoute } from '../components/PrivateRoute';
import Main from '../pages/Main';
import Login from '../pages/Login';
import Admin from '../pages/Admin';
import Logout from '../pages/Logout';
import Com from '../pages/Coment';
import Create from '../pages/Create';
import Questions from '../pages/questions';
import Answer from '../pages/answers';

export const useRoutes = () => {

  return (
    <Routes>
      <Route index element={<Main />} />
      <Route path="/" element={<Main />} />
      <Route path="/login" element={<Login />} />
      <Route path="/comment" element={<Com />} />
      <Route path='/admin' element={<Admin />} />
      <Route path="/create" element={<Create />} />
      <Route path="/questions" element={<Questions />} />
      <Route path="/answer" element={<Answer />} />


      <Route element={<PrivateRoute />}>
        {/* <Route path='/admin' element={<Admin />} /> */}
        {/* <Route path="/create" element={<Create />} /> */}
        <Route path="/logout" element={<Logout />} />
      </Route>

    </Routes>
  )
}

export default useRoutes
