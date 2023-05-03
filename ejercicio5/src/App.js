import Layout from './shared/layout';
import Datos from './inicio/Datos';
import Inicio from './inicio/Inicio';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  return (
    <div className="App">
     <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Inicio />} />
            <Route path='datos' element={<Datos/>} />
            </Route>  
        </Routes> 
      </BrowserRouter>     
    </div>
  );
}

export default App;
