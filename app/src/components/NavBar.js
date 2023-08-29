import React, { useState } from 'react';
import './NavBar.css';

export default function NavBar() {
  const [loginStatus, setLoginStatus] = useState(null);

  const handleLogin = () => {
    
    const username = "Jeff";
    setLoginStatus(username);
  };

  return (
    <nav className="navbar">
      <div className="logo">
        <img src="logo.png" alt="WhoInvitedMeLOGO" />
      </div>
      <div className="tabs">
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Services</a>
        <a href="#">Contact</a>
        {loginStatus ? (
          <span className='welcome-msg'>Welcome, {loginStatus}</span>
        ) : (
          <a href="#">
            <button className='login-btn' onClick={handleLogin}>Login</button>
          </a>
        )}
      </div>
    </nav>
  );
}
