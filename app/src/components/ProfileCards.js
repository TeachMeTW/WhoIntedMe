import React from 'react';
import PT from './ProfileTemplate';
import Img1 from "app/src/assets/test.png"

const Profile = () => {
  const profile = [
    {
      imgUrl: "",
      Username: "Kizumi",
      LadderRank: "Diamond 3",
    }
  ];

  return (
    <section className="profile" id="profile">
      <PT
        imgUrl= ""
        Username={profile[0].Username}
        LadderRank={profile[0].LadderRank}
      />
    </section>
  );
};

export default Profile;
