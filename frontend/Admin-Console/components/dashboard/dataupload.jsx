import Head from "next/head";
import styles from "../../styles/dashboard/dataupload.module.css";
import Link from "next/link";
import "bootstrap/dist/css/bootstrap.min.css";
import FileUploader from "../../src/components/Upload";
import { HOMEPAGE, PERFORMANCE, ENGAGEMENTS, API_PORT_FRONTEND, SETTINGS } from "../../config";
import { useEffect, useState } from "react";

export default function DataUpload_Area() {
  const [email, setUser] = useState("");
  //check user login

  useEffect(() => {
    const userdata = localStorage.getItem("user");

    if (userdata) {
      const foundUser = JSON.parse(userdata);
      setUser(foundUser.email);
      console.log("User is logged in and can add/view projects");
    } else {
      window.location.href = "/";
    }
  }, []);

  //Define styles
  const {
    dashboard,
    navigationpane,
    logo,
    dasboardnavigation,
    link,
    homeicon,
    performanceicon,
    engagementsicon,
    settingsicon,
    logout,
    logouticon,
    dashboardoptions,
    dashboardcontent,
    homelogo,
    pushs,
    engagement,
    notify,
    engageicon,
    helpdesk,
    red,
    blue,
    search,
    button,
    survey,
    push_mail,
    note,
    search_icon,
    user_icon,
    dataupload,
    push_link
  } = styles;

  //Routes / endpoints for navigation

  const dashboardhome_route = `/${HOMEPAGE}`;
  const performance_route = `/${PERFORMANCE}`;
  const engagements_route = `/${ENGAGEMENTS}`;
  const settings_route = '/dashboard/settings';
  const frontend_url = `${API_PORT_FRONTEND}`;

  return (
    <>
      <Head>
        <title>Dashboard: Engagements</title>
      </Head>

      <body>
        <div className={dashboard}>
          <div className={navigationpane}>
            <center>
              <div className={logo}>
                <img className={logo} src="/logo.png" alt="logo" />
              </div>

              <div className={dasboardnavigation}>
                <div className={link}>
                  <Link href={dashboardhome_route}>
                    <a>
                      <img
                        className={homeicon}
                        src="/home_icon.png"
                        alt="home icon"
                      />
                    </a>
                  </Link>
                </div>

                <div className={link}>
                  <Link href={performance_route}>
                    <a>
                      <img
                        className={performanceicon}
                        src="/performance_icon.png"
                        alt="performance icon"
                      />
                    </a>
                  </Link>
                </div>

                <div className={link}>
                  <Link href={engagements_route}>
                    <a>
                      <img
                        className={engagementsicon}
                        src="/engagements_icon.png"
                        alt="engagements icon"
                      />
                    </a>
                  </Link>
                </div>

                <div className={link}>
                  <Link href={settings_route}>
                    <a>
                      <img
                        className={settingsicon}
                        src="/settings_icon.png"
                        alt="settings icon"
                      />
                    </a>
                  </Link>
                </div>
              </div>

              <footer className={logout}>
                <Link href={frontend_url}>
                  <a>
                    <img
                      className={logouticon}
                      src="/logout_icon.png"
                      alt="logout icon"
                    />
                  </a>
                </Link>
              </footer>
            </center>
          </div>

          <div className={dashboardoptions}>
            <div className={homelogo}>LOGO</div>
            <div>
              <img
                className={engageicon}
                src="/engagements_icon.png"
                alt="engagements icon"
              />
              <b className={engagement}>Engagement</b>
            </div>

            <button className={pushs} id="pushs">
              <Link href="/dashboard/engagement">
                <a className={push_link} id="dataupload">
                  Pushs
                </a>
              </Link>
              <span className={blue}>12</span>
            </button>

            <button className={notify} id="notifications">
              {" "}
              Notifications
            </button>

            <Link href="#">
              <a className={dataupload} id="dataupload">
                Data Upload
              </a>
            </Link>

            {/* <div className={notify}>
                                <p>Notifications</p>
                            </div>
                            <div className={upload}>
                                <p>Data Upload</p>
                                <input type="file" />
                            </div> */}

            <footer>
              <center className={helpdesk}>
                <p>
                  If you have any questions, the Scalework team is here for you.
                </p>
                <p className={red}>
                  <Link href={frontend_url}>
                    <a className={styles.link}>Helpdesk</a>
                  </Link>
                </p>
              </center>
            </footer>
          </div>

          <div className={dashboardcontent}>
            <div>
              <input
                className={search}
                type="text"
                name="search"
                id="search"
                placeholder="Search"
              />
              <img className={search_icon} src="/search.png" alt="next icon" />
              <img className={user_icon} src="/user_icon.png" alt="user icon" />
            </div>
            <div className={survey}>
              <h1>
                Data Upload
                <button type="button" className={button} value="submit">
                  Add Survey
                </button>
              </h1>
            </div>

            {/* file upload functionality */}

            <div className={push_mail}>
              <b>Kindly select a file/multiple files to upload</b>

              <div className={note}>
                <div>
                  {/* <FileUploader /> */}
                </div>
              </div>
            </div>
          </div>
        </div>
      </body>
    </>
  );
}
