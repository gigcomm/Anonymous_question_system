import Navbar from './components/Navbar';
import useRoutes from './routes/routes';
import './App.css'

const App = () => {
  const routes = useRoutes()

  return (
    <div className='Page'>
      <Navbar />
      {routes}
    </div>
  )
};

export default App;
