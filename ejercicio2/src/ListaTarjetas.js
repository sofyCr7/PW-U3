import React from 'react';
import Tarjeta from './Tarjeta';
import Encabezado from './Encabezado';
export default function ListaTarjetas(){
    return(
        
        <div className='container'>
              <div className='row'>
                    <Encabezado Titulo="Tarjeta"/>

                </div>
            <div className='row'>
               
                <div className='col-4'>
                <Tarjeta datos={{Titulo:"Nota 1",Text:"t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",Urlimagen:"https://picsum.photos/120/120?random=1"}}/> 

                </div>
                <div className='col-4'>
                <Tarjeta datos={{Titulo:"Nota 2",Text:"t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",Urlimagen:"https://picsum.photos/120/120?random=2"}}/> 


                </div>
                <div className='col-4'>
                <Tarjeta datos={{Titulo:"Nota 3",Text:"t is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).",Urlimagen:"https://picsum.photos/120/120?random=3"}}/> 


                </div>


            </div>
        </div>
    )
}