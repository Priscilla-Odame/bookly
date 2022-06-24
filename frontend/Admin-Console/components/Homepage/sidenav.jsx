import React from "react";
import styles from "../../styles/Homepage/sidenav.module.css";
import Link from "next/link";
import { FiBox } from "react-icons/fi";
import { MdDashboard } from "react-icons/md";
import { RiArrowRightSLine } from "react-icons/ri";

export default function Sidenav() {
    
  //Define styles

  const { side_nav, navigation_item, navigation_icon, project_icon } = styles;

  return (
    <div>
      <section className={side_nav}>
        <Link href="/homepage">
          <div className={navigation_item}>
            <b>
              <MdDashboard className={navigation_icon} /> Dashboard
            </b>
          </div>
        </Link>

        <Link href="/homepage">
          <div className={navigation_item}>
            <b>
              <FiBox className={navigation_icon} /> Projects{" "}
              <RiArrowRightSLine className={project_icon} />
            </b>
          </div>
        </Link>
      </section>
    </div>
  );
}
