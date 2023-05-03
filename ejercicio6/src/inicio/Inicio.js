import React, {useEffect,useState} from 'react';
import axios from 'axios';

export default function Inicio() {
  const [blogs,setBlogs] = useState()

  useEffect(()=> {
    const obtenerBlogs = async () => {
      try{
        const response = await
        axios.get('https://jsonplaceholder.typicode.com/posts');
        setBlogs((blogs)=> response.data);
      }
      catch{
        console.error("Error al busscar posts.")
      }
    };
    obtenerBlogs();
  }, []);
  if (blogs){
    return(
      <>
        <div>Inicio</div>
        {
          blogs.map((blog)=>{
            return(
            <div class="mb-4">
              <div class="small text-muted">{blog.id}</div>
              <a class="link-dark" href="#!"><h3>{blog.title}</h3></a>
            </div>
            )
            /*<>
              <p>{blog.body}</p>
              <br/>
            </>*/
          })}
        <p>{blogs[0].body}</p>
      </>
    );
  }
  else{
    return (<div>Cargando....</div>)
  }
  
}
