import React from "react";
import styles from "../../styles/Homepage/header.module.css";
import { FiMenu } from "react-icons/fi";
import { MdNotifications, MdSettings } from "react-icons/md";
import { AiFillQuestionCircle } from "react-icons/ai";
import { FaUserCircle } from "react-icons/fa";

export default function Header() {
    
  //Define styles

  const {
    header,
    logo,
    navigation_icon,
    header_center,
    header_right,
    header_right_icon,
    user_icon
  } = styles;

  return (
    <div>
      <section className={header}>
        <img className={logo} src="/logo.png" alt="logo" />

        <b className={header_center}>
          <FiMenu className={navigation_icon} /> Dashboard
        </b>
        <div className={header_right}>
          <MdNotifications className={header_right_icon} />
          <MdSettings className={header_right_icon} />
          <AiFillQuestionCircle className={header_right_icon} />
          <FaUserCircle className={user_icon} />

          <div>
            <b>Passum</b> <br />
            Admin
          </div>
        </div>
      </section>
    </div>
  );
}
