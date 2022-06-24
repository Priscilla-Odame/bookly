import Head from "next/head";
import styles from "../../../styles/dashboard/settings.module.css";
import Link from "next/link";
import FileUploader from "../../../src/components/Upload";
import AddProject from "./projects/projects";
import { HOMEPAGE, PERFORMANCE, ENGAGEMENTS, API_PORT_FRONTEND, SETTINGS } from "../../../config";

export default function Settings() {
  //Define styles
  const {
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
    push_mail,
    search_icon,
    user_icon,
    users
  } = styles;

  //Endpoints and url's

  const dashboardhome_route = `/${HOMEPAGE}`;
  const performance_route = `/${PERFORMANCE}`;
  const engagements_route = `/${ENGAGEMENTS}`;
  const settings_route = '/dashboard/settings';
  const frontend_url = `${API_PORT_FRONTEND}`;

  //user identity check
  // const [email, setEmail] = useState("")

  //     useEffect(()=>{
  //       const userdata = localStorage.getItem('user');

  //       if(userdata) {
  //           const foundUser = JSON.parse(userdata)
  //           setEmail(foundUser.email)
  //           setToken(foundUser.tokens.access)
  //           console.log('User email found for project addition')
  //       } else {
  //           window.location="/"
  //       }

  //   }, [])

  return (
    <>
      <Head>
        <title>Dashboard: Configuration</title>
      </Head>

      <body>
        <div className={styles.dashboard}>
          <div className={styles.navigationpane}>
            <center>
              <div className={styles.logo}>
                <img className={styles.logo} src="/logo.png" alt="logo" />
              </div>

              <div className={styles.dasboardnavigation}>
                <Link href={dashboardhome_route}>
                  <a className={styles.link}>
                    <img
                      className={styles.homeicon}
                      src="/home_icon.png"
                      alt="home icon"
                    />
                  </a>
                </Link>
                <br></br>
                <br></br>
                <br></br>

                <Link href={performance_route}>
                  <a className={styles.link}>
                    <img
                      className={styles.performanceicon}
                      src="/performance_icon.png"
                      alt="performance icon"
                    />
                  </a>
                </Link>
                <br></br>
                <br></br>
                <br></br>

                <Link href={engagements_route}>
                  <a className={styles.link}>
                    <img
                      className={styles.enagementsicon}
                      src="/engagements_icon.png"
                      alt="engagements icon"
                    />
                  </a>
                </Link>
                <br></br>
                <br></br>
                <br></br>

                <Link href={settings_route}>
                  <a className={styles.link}>
                    <img
                      className={styles.settingsicon}
                      src="/settings_icon.png"
                      alt="settings icon"
                    />
                  </a>
                </Link>
              </div>

              <div className={styles.logout}>
                <Link href={frontend_url}>
                  <a className={styles.link}>
                    <img
                      className={styles.logouticon}
                      src="/logout_icon.png"
                      alt="settings icon"
                    />
                  </a>
                </Link>
              </div>
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
              <AddProject />
            </div>
          </div>
        </div>
      </body>
    </>
  );
}
