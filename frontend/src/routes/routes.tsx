import { Route, Routes } from 'react-router-dom';
import { PrivateRoute } from '../components/PrivateRoute';
import Main from '../pages/Main';
import Login from '../pages/Login';
import Admin from '../pages/Admin';
import Logout from '../pages/Logout';
import Com from '../pages/Coment';
import Create from '../pages/Create';
import Test from '../pages/Test';
import Answer from '../pages/answers';
import WaitingRoom from '../pages/WaitingRoom';
import AdminRoom from '../pages/AdminRoom';

export const useRoutes = () => {

  return (
    <Routes>
      <Route index element={<Main />} />
      <Route path="/" element={<Main />} />
      <Route path="/login" element={<Login />} />
      <Route path="/comment" element={<Com />} />
      <Route path="/test" element={<Test />} />
      <Route path="/answer" element={<Answer />} />
      <Route path="/waitingRoom" element={<WaitingRoom />} />
      <Route path="/adminRoom" element={<AdminRoom />} />
      
      <Route path='/admin' element={<Admin />} />
      <Route path="/create" element={<Create />} />


      <Route element={<PrivateRoute />}>
        {/* <Route path='/admin' element={<Admin />} />
        <Route path="/create" element={<Create />} /> */}
        <Route path="/logout" element={<Logout />} />
      </Route>

    </Routes>
  )
}

export default useRoutes
