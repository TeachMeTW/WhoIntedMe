import React from 'react'
import './NavBar.css'
export default function NavBar() {
    return (
        <nav className="navbar">
          <div className="logo">
            <img src="logo.png" alt="WhoIntedMeLOGO" />
          </div>
          <div className="tabs">
            <a href="#">Home</a>
            <a href="#">About</a>
            <a href="#">Services</a>
            <a href="#">Contact</a>
            <a href="#"><button className='login-btn'>Login</button></a>
          </div>
        </nav>
      )
}
