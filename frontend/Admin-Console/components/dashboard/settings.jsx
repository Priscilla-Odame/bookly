import Head from "next/head";
import styles from "../../styles/dashboard/settings.module.css";
import Link from "next/link";
import FileUploader from "../../src/components/Upload";
// import SideNav from '../dashboard/sidenav'
import { HOMEPAGE, PERFORMANCE, ENGAGEMENTS, API_PORT_FRONTEND, SETTINGS } from "../../config";

export default function Settings() {
    
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
    company,
    engagement,
    campaign,
    projects,
    seticon,
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
    users
  } = styles;

  const dashboardhome_route = `/${HOMEPAGE}`;
  const performance_route = `/${PERFORMANCE}`;
  const engagements_route = `/${ENGAGEMENTS}`;
  const settings_route = '/dashboard/settings';
  const frontend_url = `${API_PORT_FRONTEND}`;

  //check user login status
  const useEffect = () => {
    const UserLoggedIn = localStorage.getItem("user");

    if (UserLoggedIn) {
      const foundUser = JSON.parse(UserLoggedIn);
      setUser(foundUser);
      console.log("User is logged in");
    } else {
      window.location = "/";
    }
    console.log(props.firstname);
  };

  return (
    <>
      <Head>
        <title>Dashboard: Configuration</title>
      </Head>

      <body>
        <div className={styles.dashboard}>
          {/* <SideNav/> */}
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
                className={seticon}
                src="/settings_icon.png"
                alt="settings icon"
              />
              <b className={engagement}>Configuration</b>
            </div>

            <button className={company} id="pushs">
              {" "}
              Company <span className={blue}>12</span>
            </button>

            <button className={campaign} id="notifications">
              {" "}
              Campaign
            </button>

            <Link href="/dashboard/settings/configuration/projectmanagement">
              <a className={projects} id="dataupload">
                Projects
              </a>
            </Link>

            <Link href="/dashboard/settings/configuration/usermanagement">
              <a className={users} id="dataupload">
                Users
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
                  If you have any questions, the Scalework team is there for
                  you.
                </p>
                <p className={red}>Helpdesk</p>
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

            {/* file upload functionality */}

            <div className={push_mail}>
              <b>
                Welcome to the configuration page, <br></br>you can customize
                your settings and perform additional operations here.
              </b>

              <div className={note}>
                <div>Configuration Page</div>
              </div>
            </div>
          </div>
        </div>
      </body>
    </>
  );
}
