import React from "react";
import RecentProjects from "./survey_content/recents";
import TableContainer from "./survey_content/tableContainer";
import styles from "../../../../styles/Homepage/MainContent/reports/report.module.css";

export default function Survey() {
  //Define styles

  const { recents, list, table } = styles;

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
