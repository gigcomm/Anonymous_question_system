import React from 'react';
import { Container, Navbar, Nav } from 'react-bootstrap';
import logo from './logo.png'
import login from './login-icon.png'
import admin from './admin-icon.png'
import { Route, Routes, Link } from 'react-router-dom';
import './Header.css'

import { Login } from '../Pages/Login'
import { Home } from '../Pages/Home'
import { Admin } from '../Pages/Admin'


export default function header() {
    return (
        <div className='head'><Navbar  collapseOnSelect expand="md" bg='dark' variant='dark'>
            <Container>
                <Navbar.Brand to='/'>
                    <img
                        src={logo}
                        height="30"
                        width="30"
                        className='i-head'
                        alt='logo'
                    />
                    Anonymous question
                </Navbar.Brand>
                <Navbar.Toggle aria-controls='responsive-navbar-nav' />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="nav">
                        <Link to="/">
                            Home
                        </Link>
                        <Link to="/admin">
                            <img
                                src={admin}
                                height="30"
                                width="30"
                                className='i-head'
                            />
                            admin
                        </Link>
                        <Link to="/login">
                            <img
                                src={login}
                                height="30"
                                width="30"
                                className='i-head'
                            />
                            login
                        </Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
            <Routes>
                <Route path='/' element={<Home />} />
                <Route path='/login' element={<Login />} />
                <Route path='/admin' element={<Admin />} />
            </Routes>
        </Navbar>


        </div>
    )
}

