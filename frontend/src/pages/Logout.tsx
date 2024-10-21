import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import useAuth from "../hooks/useAuth";

function Logout() {
  const { setAuth } = useAuth()
  const navigate = useNavigate();
  
  useEffect(() => {
    setAuth(false)
    navigate('/');
  }, [setAuth, navigate])

  return (
    <div>Logout</div>
  )
}

export default Logout
