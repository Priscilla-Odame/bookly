import Head from "next/head";
import styles from "../../styles/dashboard/engagements.module.css";
import Link from "next/link";
import { HOMEPAGE, PERFORMANCE, ENGAGEMENTS, API_PORT_FRONTEND , SETTINGS } from "../../config";
// import axios from 'axios';
import SideNav from "../dashboard/sidenav";

export default function Engagements() {
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
    dataupload,
    notify_icon
  } = styles;

  //Routes / endpoints for navigation

  // const dashboardhome_route = `/${HOMEPAGE}`;
  // const performance_route = `/${PERFORMANCE}`;
  // const engagements_route = `/${ENGAGEMENTS}`;
  // const settings_route = '/dashboard/settings';
  const frontend_url = `${API_PORT_FRONTEND}`;

  return (
    <>
      <Head>
        <title>Dashboard: Engagements</title>
      </Head>

      <body>
        <div className={dashboard}>
          <SideNav />

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
              {" "}
              Pushs <span className={blue}>12</span>
            </button>

            <button className={notify} id="notifications">
              {" "}
              Notifications
            </button>

            <Link href="/dashboard/engagement/dataupload">
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
                Pushs
                <button type="button" className={button} value="submit">
                  Add Survey
                </button>
              </h1>
            </div>
            <div className={progress}>
              <b>Title</b>
              <br></br>
              <img className={next_icon} src="/push.png" alt="next icon" />
              {/* <div className={card}>
                                    Title <img className={next_icon} src="/next.png" alt="next icon" />

                                    
                                </div>
                                <div className={card}>
                                    Title <img className={next_icon} src="/next.png" alt="next icon" />
                                </div> */}
            </div>
            <div className={push_mail}>
              <b>Title</b>
              <br></br>
              <img className={notify_icon} src="/notify.png" alt="next icon" />

              {/* <div className={note}>
                                    Notifications
                                    {/* <input type="text" placeholder="number"/> 
                                </div> */}
            </div>
          </div>
        </div>
      </body>
    </>
  );
}
