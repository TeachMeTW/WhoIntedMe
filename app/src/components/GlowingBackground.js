import React from 'react'
import './GlowingBackground.css'
export default function GlowingBackground() {
    return (
        <div className='glowingBackground'>
          <div className="glowing">
            <span style={{'--i': 1}}></span>
            <span style={{'--i': 2}}></span>
            <span style={{'--i': 3}}></span>
          </div>
          <div className="glowing">
            <span style={{'--i': 1}}></span>
            <span style={{'--i': 2}}></span>
            <span style={{'--i': 3}}></span>
          </div>
          <div className="glowing">
            <span style={{'--i': 1}}></span>
            <span style={{'--i': 2}}></span>
            <span style={{'--i': 3}}></span>
          </div>
          <div className="glowing">
            <span style={{'--i': 1}}></span>
            <span style={{'--i': 2}}></span>
            <span style={{'--i': 3}}></span>
          </div>
        </div>
      )
}
