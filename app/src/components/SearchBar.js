import React from 'react';
import './SearchBar.css'; // Import the CSS file for styling

function SearchBar() {
  return (
    <div>
<div className="search-container">
<img
        className='land-img'
        src="https://meta-static.op.gg/logo/image/fc9a4aeddcf438c0b4faa8556253fadc.png?image=q_auto,f_webp,w_auto&v=1692943905742"
        alt=""
      />
      <input type="text" className="search-input" placeholder="Search..." />
      <button className="search-button">
      <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
  <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"/>
</svg>
      </button>
    </div>
    </div>

  );
}

export default SearchBar;
