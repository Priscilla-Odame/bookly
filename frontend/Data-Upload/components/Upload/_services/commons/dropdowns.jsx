import Link from "next/link";
import React, { useState, useEffect } from "react";
import { CSSTransition } from 'react-transition-group'

import {FaUserCircle} from 'react-icons/fa'
import {FiLogOut} from 'react-icons/fi'


//Dropdown navigation items

function NavItem(props) {
    const [show, setShow] = useState(false);

    return(
      <li className="nav-item">
        <button style={{
            textDecoration: "none",
            display: "inline-block",
            background: "none",
            color: "black",
            border: "none",
            cursor: "pointer",
            position: "fixed",
           }} className="icon-button" onClick={()=>setShow(!show)}>
          {props.icon}
        </button>
        {show && props.children}
      </li>

    )
  }

  function DropdownMenu (){
    function DropdownItem(props){
      return(
        <button style={{
          textDecoration: "none",
          display: "inline-block",
          background: "none",
          color: "black",
          border: "none",
          cursor: "pointer",
         }} className="menu-item">
          <span className="icon-button">{props.leftIcon}</span>
          {props.children}
          <span className="icon-right">{props.rightIcon}</span>
        </button>
      )
    }
    return(
      <div className="dropwdown">
        <DropdownItem >
          <button style={{
            textDecoration: "none",
            display: "inline-block",
            background: "none",
            color: "crimson",
            border: "none",
            cursor: "pointer",
            position: "fixed",
            marginTop: "5px",
           }}>Date
          </button>
        </DropdownItem>
        <DropdownItem><button 
          style={{
            textDecoration: "none",
            display: "inline-block",
            background: "none",
            color: "crimson",
            border: "none",
            cursor: "pointer",
            position: "fixed",
            marginTop: "20px"
          }}>Name</button>
        </DropdownItem>
        <DropdownItem ><button 
          style={{
            textDecoration: "none",
            display: "inline-block",
            background: "none",
            color: "crimson",
            border: "none",
            cursor: "pointer",
            position: "fixed",
            marginTop: "35px"
          }}
        >Size</button>
      </DropdownItem>
      </div>
    )
  }
export {NavItem, DropdownMenu}
