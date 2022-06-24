import Link from "next/link";
import React, { useState, useEffect } from "react";
import styles from "../../styles/upload/header.module.css";
import { Offline } from "react-detect-offline";

// import {MdArrowDropDownCircle} from 'react-icons/md'
import {FiLogOut} from 'react-icons/fi'
// import { CSSTransition } from 'react-transition-group'
import "react-toastify/dist/ReactToastify.css";
import { toast } from "react-toastify";
import {InternetOffline} from './_services/commons/_internetconnectivity.js'

import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';



toast.configure();
const Header = ({ firstname }) => {

  //User profile dropdown menu
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);

  //Event handlers
  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };
  
  //Get first character from user firstname
  const username_firstChar = firstname.charAt(0);

 //Logout user
  function Logout (){
    if (typeof window !== 'undefined'){
      window.localStorage.removeItem('user-data');
      window.location.href="/";
      toast.success(
        "Logout successful",
      );

    }
  }

  //Navigate to profile page
  function UserProfile(){
    window.location.href="#";
    toast.info(
      "Profile section is underway. Kindly cantact your administrator.",
    );
  }

  function profileAction(){
    handleClose();
    UserProfile();
  }

  function logoutAction(){
    handleClose();
    Logout();
  }

  return (
    <div>
      <div>
        {/* Header elements */}
        <div className={styles.header}>
            <Offline><InternetOffline/></Offline>
          <div className={styles.header_left}>
            <Link href="/">
              <a className={styles.logo}>
                <img
                  src="/assets/images/logo/logo.svg"
                  alt="Push insights logo"
                />
              </a>
            </Link>
            <div className={styles.title}>Uploads</div>
          </div>

          <div className={styles.profile}>
            <div>{firstname}</div>
            
            <div className={styles.profile_img}>

              <Button aria-controls="simple-menu" aria-haspopup="true" onClick={handleClick} title="Click for menu">
                <div style={{color:"white"}}>{username_firstChar} </div>
              </Button>
              <Menu
                id="simple-menu"
                anchorEl={anchorEl}
                keepMounted
                open={Boolean(anchorEl)}
                onClose={handleClose}
              >
                <MenuItem onClick={profileAction}>Profile</MenuItem>
                <MenuItem><FiLogOut/><button onClick={logoutAction} style={{border:"none", background:"inherit"}}>Logout</button></MenuItem>
              </Menu> 
            </div>
            
            
            
          </div>

        </div>
      </div>
    </div>
  );
};

    
export default Header;
