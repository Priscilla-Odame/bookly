import React from "react";
import Reports from "./reports/report";
import Invites from "../project_invites/invites";
import Surveys from "./survey/survey";
import { useState, useEffect } from "react";
import Recents from "./reports/report";
import TileNavigation from "./tile_navigation";
// import TableContainer from './table_container';
import RecentReports from "./reports/report_content/recents";
import RecentsDescription from "../main_content/recents_description";
import styles from "../../../styles/Homepage/MainContent/mainContent.module.css";
import { FaUserCheck } from "react-icons/fa";
import { MdPieChart, MdInsertChart } from "react-icons/md";

export default function MainContent() {
  //Define styles

  const {
    tiles,
    recents,
    container,
    report_avatars,
    invites_avatars,
    survey_avatars,
    UnreadReports,
    PendingInvites,
    IncompleteSurveys,
    btn_ReportTile,
    btn_InviteTile,
    btn_SurveyTile,
    tile_title,
    tile_content,
    tile_icon
  } = styles;

  //function to load report
  // const loadReportElements = ()=>{
  //     return<Reports/>
  // }

  //------------------------------------------
  //all elements to be rendered state object
  const [renderAllReportsElements, setrenderAllReportsElements] = useState(
    true
  );
  const [renderAllInviteElements, setrenderAllInviteElements] = useState(false);
  const [renderAllSurveyElements, setrenderAllSurveyElements] = useState(false);

  const showReportElements = () => {
    setrenderAllReportsElements(true);
    setrenderAllInviteElements(false);
    setrenderAllSurveyElements(false);
  };

  const showInviteElements = () => {
    setrenderAllReportsElements(false);
    setrenderAllInviteElements(true);
    setrenderAllSurveyElements(false);
  };

  const showSurveyElements = () => {
    setrenderAllReportsElements(false);
    setrenderAllInviteElements(false);
    setrenderAllSurveyElements(true);
  };

  //Logged in user token state object
  const [token, setToken] = useState("");
  const [firstname, setFirstname] = useState("");

  //check user login status
  useEffect(() => {
    const userdata = localStorage.getItem("user");

    if (userdata) {
      const foundUser = JSON.parse(userdata);
      setToken(foundUser.token);
      setFirstname(foundUser.firstname);
      console.log("User found", token, firstname);
    } else {
      //    window.location="/"
    }
  }, []);

  return (
    <div>
      <div className={tiles}>
        {/* <TileNavigation/> */}
        <div className={container}>
          <div className={UnreadReports}>
            <div className={btn_ReportTile} onClick={showReportElements}>
              <div className={tile_title}>
                <span>TF</span>
                <span style={{ background: "#FDC132", color: "#ffffff" }}>
                  LF
                </span>
                <span style={{ background: "#0FCDF6", color: "#ffffff" }}>
                  TK
                </span>
              </div>
              <div className={tile_content}>
                <div>
                  <span>10</span> <br />
                  <span>Unread Reports</span>
                </div>

                <div>
                  <MdPieChart className={tile_icon} />
                </div>
              </div>
            </div>
          </div>

          <div className={PendingInvites}>
            <div className={btn_InviteTile} onClick={showInviteElements}>
              <div className={tile_title}>
                <span>CP</span>
                <span style={{ background: "#FDC132", color: "#ffffff" }}>
                  RO
                </span>
              </div>
              <div className={tile_content}>
                <div>
                  <span>2</span> <br />
                  <span>Pending Invites</span>
                </div>
                <div>
                  <FaUserCheck className={tile_icon} />
                </div>
              </div>
            </div>
          </div>

          <div className={IncompleteSurveys}>
            <div className={btn_SurveyTile} onClick={showSurveyElements}>
              <div className={tile_title}>
                <span>TF</span>
                <span style={{ background: "#FDC132", color: "#ffffff" }}>
                  LF
                </span>
                <span style={{ background: "#0FCDF6", color: "#ffffff" }}>
                  TK
                </span>
              </div>
              <div className={tile_content}>
                <div>
                  <span>10</span> <br />
                  <span>Incomplete Survey</span>
                </div>

                <div>
                  <MdInsertChart
                    className={tile_icon}
                    style={{ marginLeft: "80px" }}
                  />
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div className={recents}>
        <RecentsDescription />
      </div>

      <div>
        {renderAllReportsElements && <Reports />}​​
        {renderAllInviteElements && <Invites />}
        {renderAllSurveyElements && <Surveys />}​​
        {/* {loadReportElements} */}
        {/* <Reports/> */}
      </div>

      {/* <div className={recentReports}>
                <RecentReports/>
            </div>
            <div className={listing}>
                <TableContainer/>
            </div> */}
    </div>
  );
}
