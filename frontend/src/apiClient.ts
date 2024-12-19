import axios from 'axios'; 
 
 
const apiClient = axios.create({ 
 baseURL: 'http://localhost:8000/api/',  
 headers: { 
 'Content-Type': 'application/json',  
  },
});
 
apiClient.interceptors.request.use( 
 (config) => { 
 const token = localStorage.getItem('authToken'); 
 if (token) { 
 config.headers.Authorization = `Token ${token}`; 
    }
 return config; 
  },
 (error) => { 
 return Promise.reject(error); 
  }
);
 
apiClient.interceptors.response.use( 
 (response) => response, 
    (error) => {
 if (error.response) { 
 console.error(`Ошибка ${error.response.status}:`, error.response.data); 
 } else { 
 console.error('Ошибка сети:', error.message); 
      }
      return Promise.reject(error);
    }
  );  
export default apiClient; 