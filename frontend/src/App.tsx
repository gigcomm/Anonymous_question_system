import Navbar from './components/Navbar';
import Footer from './components/Footer';
import useRoutes from './routes/routes';
import { AuthProvider } from './context/AuthProvider';
import './App.css'

const App = () => {
  const routes = useRoutes()

  return (
    <AuthProvider>
      <div className='Page'>
        <Navbar />
        {routes}
        <main className='main-content'>
        </main>
        <Footer />
      </div>
    </AuthProvider>
  )
};

export default App;
