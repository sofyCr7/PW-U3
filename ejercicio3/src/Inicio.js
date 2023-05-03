import React from 'react'
import Navegacion from './Navegacion'
import Encabezado from './Encabezado'
import Destacados from './Destacados'
import Testimonios from './Testimonios'
import Blog from './Blog'
import Pie from './Pie'

export default function Inicio() {
  return (
    <div>
        <Navegacion/>
        <Encabezado/>
        <Destacados/>
        <Testimonios/>
        <Blog/>
        <Pie/>
    </div>
  )
}
