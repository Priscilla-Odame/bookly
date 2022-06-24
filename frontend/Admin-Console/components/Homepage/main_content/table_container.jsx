import React from "react";
import ReportList from "./reports/report_content/table";
import styles from "../../../styles/Homepage/MainContent/reports/tablecontainer.module.css";

export default function TableContainer() {
  //Define styles

  const { container, details_btn, history_btn, search, filter, table } = styles;

  return (
    <div>
      <div className={container}>
        <button className={details_btn}>Details</button>

        <button className={history_btn}>History</button>

        <input placeholder="🔍search here..." className={search} />
        <button className={filter}> &#8910; Filter</button>
      </div>

      <div className={table}>
        <ReportList />
      </div>
    </div>
  );
}
