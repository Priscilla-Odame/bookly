import Head from "next/head";
import styles from "../../styles/dashboard/performance.module.css";
import Link from "next/link";
import dynamic from "next/dynamic";
import { useState } from "react";
import { API_BASE_URL, API_PORT, API_PORT_FRONTEND } from "../../config";
import axios from "axios";
import SideNav from "../dashboard/sidenav";

const PushInsightsReport = dynamic(
  () => {
    return import("./reports/samplereport");
  },
  { ssr: false }
);

export default function Performance() {
  const [accessToken, setAccessToken] = useState("");
  const [embedUrl, setEmbedUrl] = useState("");
  const [reportName, setReportName] = useState("");
  const [reportId, setReportId] = useState("");
  const [reportDataReady, setReportDataReady] = useState(false);

  //Report to be rendered
  const renderReportOne = () => {
    return (
      reportDataReady && (
        <PushInsightsReport
          accessToken={accessToken}
          embedUrl={embedUrl}
          reportId={reportId}
          reportName={reportName}
        />
      )
    );
  };

  //load report function

  const loadReport = () => {
    //retrieving logged in user details from localStorage

    const userdata = JSON.parse(localStorage.getItem("user"));

    //backend api enpoint and url to fetch reports
    const endpoint = "api/report";
    const url = `${API_BASE_URL}:${API_PORT}/${endpoint}`;

    console.log(`token ${userdata.tokens.access}`);

    // Make request to endpoints for embedded reports
    axios
      .get(url, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${userdata.access_token}`
        }
      })
      .then(resp => {
        const { data } = resp;
        console.log("Data from fetch", data);
        setAccessToken(data.access_token);
        setEmbedUrl(data.report_config[0].embedUrl);
        setReportName(data.report_config[0].reportName);
        setReportId(data.report_config[0].reportId);
        setReportDataReady(true);
      })
      .catch(err => {
        console.log(err);
      });
  };

  //frontend url
  const frontend_url = `${API_BASE_URL}:${API_PORT_FRONTEND}`;

  //report generation in process notification

  // setTimeout(() => {
  //     alert('Kindly wait as the report is being generated');
  //     clearInterval()
  // }, 3000);

  return (
    <>
      <Head>
        <title>Dashboard: Performance</title>
      </Head>

      <body>
        <div className={styles.dashboard}>
          <SideNav />

          {/* Dashboard Options section : : Second/Midle Section of dashboard*/}

          <div className={styles.dashboardoptions}>
            <center>
              <br></br>

              <div className={styles.performancelogo}>LOGO</div>

              <br></br>

              <div className={styles.performanceheading}>
                {/* <div className={styles.home_top_logo}> */}
                <img
                  style={{ height: "24px", width: "24px" }}
                  src="/performance_icon.png"
                  alt="performance logo"
                />
                {/* </div> */}

                {/* <div className={styles.dashboardtext}> */}
                <b style={{ fontSize: "18px", paddingLeft: "10px" }}>
                  Performance
                </b>

                {/* </div> */}
              </div>

              <button
                onClick={loadReport}
                className={styles.portfolioanalytics}
                id="portfolioanalytics"
              >
                {" "}
                Portfolio Analytics
              </button>

              <br></br>

              <button
                onClcik={loadReport}
                className={styles.shopanalytics}
                id="shopanalytics"
              >
                Shop Analytics
              </button>

              <center>
                <div className={styles.Helpdesk}>
                  <p>
                    If you have any questions, the Scalework team is here for
                    you.
                  </p>
                  <p>
                    <Link href={frontend_url}>
                      <a className={styles.link}>Helpdesk</a>
                    </Link>
                  </p>
                </div>
              </center>

              <div></div>
            </center>
          </div>

          {/* Dashboard Content section : : Third/Rightmost Section of dashboard*/}

          <div className={styles.dashboardcontent}>
            <div>
              <div className={styles.search_acIcon}>
                <div>
                  <span>
                    <input
                      style={{
                        position: "absolute",
                        left: "3%",
                        top: "7px",
                        width: "20%",
                        height: "43px"
                      }}
                      className={styles.searchbox}
                      type="text"
                      placeholder="Search"
                      id="searchbar"
                    />
                    <img
                      style={{
                        position: "absolute",
                        left: "50px",
                        top: "42px"
                      }}
                      src="/search_img.png"
                      alt="search icon"
                    />
                  </span>
                  <img
                    style={{
                      position: "absolute",
                      left: "70%",
                      top: "30px",
                      width: "42px",
                      height: "42px"
                    }}
                    src="/user_icon.png"
                    alt="user icon"
                  />
                </div>

                <div className={styles.user_icon}></div>
              </div>
            </div>

            <br></br>

            {/*Empty div*/}

            <div></div>

            <br></br>
            <br></br>
            <br></br>

            <div className={styles.reports}>
              <h1>Performance</h1>
              <div>
                {/* Report 1 */}
                {renderReportOne()}
              </div>
            </div>
          </div>
        </div>
      </body>
    </>
  );
}
