import React from "react";
import styles from "../../../styles/Homepage/MainContent/reports/recents.module.css";

export default function RecentsDescription() {
  //Define styles

  const {
    bub_1,
    bub_2,
    bub_3,
    rHeading,
    color_code_description,
    report_bubble,
    invites_bubble,
    survey_bubble
  } = styles;

  return (
    <div>
      <div className={color_code_description}>
        <div className={rHeading}>Recents</div>

        <div className={bub_1}></div>

        <div className={report_bubble}>Report</div>

        <div className={bub_2}></div>

        <div className={invites_bubble}>Invites</div>

        <div className={bub_3}></div>

        <div className={survey_bubble}>Surveys</div>
      </div>
    </div>
  );
}
