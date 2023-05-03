import React from 'react'
import Navegation from './Navegation'
import Footer from './Footer'
import { Outlet } from 'react-router-dom'

export default function Layout() {
  return (
    <div className="d-flex flex-column" >
    <main className="flex-shrink-0">
        <Navegation/>
        <section className="py-5 bg-light">
                <div className="container px-5">
                    <div className="row gx-5">
                        <div className="col-xl-8">
                            <h2 className="fw-bolder fs-5 mb-4">Blogs</h2>
                            <Outlet/>
                        </div>
                    </div>
                </div>
        </section>
    </main>
    <Footer/>
    </div>
  )
}
