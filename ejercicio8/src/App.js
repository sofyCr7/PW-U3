import axios from 'axios';

import { useState, useEffect } from 'react';

function App() {
  const [elementosLista, setElementosLista]=useState();
  useEffect(( )=>{
    const obtenListaPorHacer =async()=>{
      try{
        const respuesta =await axios.get('https://jsonplaceholder.typicode.com/todos');
        setElementosLista(respuesta.data);


      }
      catch(error){
       
         console.log(`error al llamar la lista${error}`);
       
      }

    }
    obtenListaPorHacer();
},[]);

if(! elementosLista){
  return (
    <p>carga elementos de la lsita ...</p>
  )
}
  return (
     <div className="App">
        <ul class="list-group">
            {elementosLista.map((elemento)=>(
              <li class="list-group-item">
                {elemento.title}
              </li>


            ))}
             
          
        </ul>
    </div>
   
  );
}

export default App;
