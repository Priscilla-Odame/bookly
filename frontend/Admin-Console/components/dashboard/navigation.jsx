import styles from "../../styles/dashboard/engagements.module.css";
import { API_BASE_URL, API_PORT, API_PORT_FRONTEND } from "../../config";
import { HOMEPAGE, PERFORMANCE, ENGAGEMENTS, SETTINGS } from "../../config";
import Link from "next/link";

export default function Navigation() {
    
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
    upload,
    engageicon,
    helpdesk,
    red,
    blue,
    search,
    button,
    survey,
    progress,
    card,
    bold,
    next_icon,
    push_mail,
    note,
    search_icon,
    user_icon,
    dataupload
  } = styles;

  const frontend_url = `${API_BASE_URL}:${API_PORT_FRONTEND}`;

  return (
    <>
      <div className={dashboardoptions}>
        <div className={homelogo}>LOGO</div>
        <div>
          <img className={engageicon} src="/home_icon.png" alt="home icon" />
          <b className={engagement}>Dashboard</b>
        </div>

        <button className={pushs} id="pushs">
          {" "}
          Overview{" "}
        </button>


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
    </>
  );
}
