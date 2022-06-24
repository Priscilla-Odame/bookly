import Head from "next/head";
import styles from "../../styles/dashboard/home.module.css";
import { useEffect, useState } from "react";
import SideNav from "../dashboard/sidenav";
import Navigation from "../dashboard/navigation";

export default function DashboardHome() {
  const [firstname, setUsername] = useState("");
  const [othernames, setLastname] = useState("");

  //check user login status
  useEffect(() => {
    const userdata = localStorage.getItem("user");

    if (userdata) {
      const foundUser = JSON.parse(userdata);
      setUsername(foundUser.firstname);
      setLastname(foundUser.othernames);
      console.log("User is logged in");
    } else {
      alert("Your session timed out, Kindly sign in to continue")
      // window.location = "#";
    }
  }, []);

  return (
    <>
      <Head>
        <title>Dashboard: Home</title>
      </Head>

      <body>
        <div className={styles.dashboard}>
          <SideNav />
          <Navigation />

          <div className={styles.dashboardcontent}>
            <div>
              <div className={styles.search_acIcon}>
                <div>
                  <span>
                    <img
                      style={{ position: "absolute", left: "1%", top: "37%" }}
                      src="/search_img.png"
                      alt="search icon"
                    />
                    <input
                      className={styles.searchbox}
                      type="text"
                      placeholder="Search"
                      id="searchbar"
                    />
                  </span>
                  <img
                    style={{
                      position: "absolute",
                      left: "74.5%",
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
              <br></br>
              <br></br>
              <br></br>
              <br></br>

              <div className={styles.home}>
                <div>
                  <h1>
                    Welcome, {firstname} {othernames}
                  </h1>
                  <b>Overview</b>
                  <br></br>

                  <img className={styles.homeimg} src="/home.png" alt="home" />
                </div>

                <div className={styles.report1}>
                  {/* Report 1 */}
                  {/* {renderReportOne()} */}
                </div>

                <div className={styles.report2}>{/* Report 2 */}</div>

                <div className={styles.notification1}>
                  {/* notification1 */}
                </div>

                <div className={styles.notification2}>
                  {/* notification2 */}
                </div>

                <div className={styles.notification3}>
                  {/* notification3 */}
                </div>

                <div className={styles.notification4}>
                  {/* notification4 */}
                </div>
              </div>
              <div>
                <div></div>

                <div></div>

                <div></div>
              </div>
            </div>
          </div>
        </div>
      </body>
    </>
  );
}
