import Navbar from './components/Navbar';
import Footer from './components/Footer';
import useRoutes from './routes/routes';
import './App.css'

const App = () => {
  const routes = useRoutes()

  return (
    <div className='Page'>
      <Navbar />
      <main className='main-content'>
      {routes}
      </main>
      <Footer  />
    </div>
  )
};

export default App;
