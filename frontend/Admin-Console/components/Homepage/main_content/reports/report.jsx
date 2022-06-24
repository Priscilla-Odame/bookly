import React from "react";
import RecentReports from "../reports/report_content/recents";
import TableContainer from "./report_content/tableContainer";
import styles from "../../../../styles/Homepage/MainContent/reports/report.module.css";

export default function Reports() {
  //Define styles

  const { recents, list, table } = styles;

  return (
    <div>
      <div className={recents}>
        <RecentReports />
      </div>

      <div className={table}>
        <TableContainer />
      </div>
    </div>
  );
}
