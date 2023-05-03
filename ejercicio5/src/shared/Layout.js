import React from 'react';
import Navegacion from '.Navegacion'
import { Outlet } from 'react-router-dom';

export default function layout(){
    return(
        <>
        <Navegacion/>
        <Outlet/>
        </>
    )
}