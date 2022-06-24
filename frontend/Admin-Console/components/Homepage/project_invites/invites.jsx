import React from "react";
import RecentProjects from "./invite_content/recents";
import TableContainer from "./invite_content/tableContainer";
import styles from "../../../styles/Homepage/MainContent/reports/report.module.css";

export default function Invites() {
    
  //Define styles

  const { recents, table } = styles;

  return (
    <div>
      <div className={recents}>
        <RecentProjects />
      </div>

      <div className={table}>
        <TableContainer />
      </div>
    </div>
  );
}
