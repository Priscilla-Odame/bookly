import React from "react";
import dynamic from "next/dynamic";
import { useState, useEffect } from "react";
import Reports from "./reports/report";
import styles from "../../../styles/Homepage/MainContent/tileNavigation.module.css";

//dynamic rendering for reports
//don't need this

// const ReportElements = dynamic (
//     () => {
//         import('./reports/report');
//     }, {ssr: false}
// )

export default function TileNavigation() {
    
  //Define styles
  const {
    horizon_division,
    container,
    report_avatars,
    invites_avatars,
    survey_avatars,
    UnreadReports,
    PendingInvites,
    IncompleteSurveys,
    btn_ReportTile,
    btn_InviteTile,
    btn_SurveyTile
  } = styles;

  const [loadReportElements, setLoadReportElements] = useState(false);

  //function to render reports
  const renderReportElements = () => {
    console.log("about to render report");
    return <Reports />;
  };

  return (
    <div>
      <div className={container}>
        <div className={UnreadReports}>
          <button className={btn_ReportTile} onClick={renderReportElements}>
            <div className={report_avatars}>
              <div>1</div>
              <div> 2</div>
              <div>3</div>
            </div>
            {/* <hr className={horizon_division}></hr> */}
            Unread Reports
          </button>
        </div>

        <div className={PendingInvites}>
          <button className={btn_InviteTile}>
            <div className={invites_avatars}>
              <div>1</div>
              <div>2</div>
            </div>
            {/* <hr className={horizon_division}></hr> */}
            Pending Invites
          </button>
        </div>

        <div className={IncompleteSurveys}>
          <button className={btn_SurveyTile}>
            <div className={survey_avatars}>
              <div>1</div>
              <div>2</div>
              <div>3</div>
            </div>
            {/* <hr className={horizon_division}></hr> */}
            Incomplete Survey
          </button>
        </div>
      </div>
    </div>
  );
}
