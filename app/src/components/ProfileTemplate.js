import React from 'react';
import './ProfileCard.css';

const PT = ({ imgUrl, Username, LadderRank }) => {
  return (
    <div className="card">
      <img src={imgUrl} alt="Profile" />
      <h4>{Username}</h4>
      <span>{LadderRank}</span>
    </div>
  );
};

export default PT;
