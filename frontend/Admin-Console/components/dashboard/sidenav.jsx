import styles from "../../styles/dashboard/engagements.module.css";
import {FaNetworkWired} from 'react-icons/fa'
import { HOMEPAGE, PERFORMANCE, ENGAGEMENTS, API_PORT_FRONTEND, SETTINGS, ADMIN_PANEL } from "../../config";
import Link from "next/link";

export default function SideNav() {
  const logoutuser = () =>
    useEffect(() => {
      const userdata = localStorage.getItem("user");

      if (userdata) {
        localStorage.clear("user");
        console.log("User is logged out");
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
    adminicon,
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

  //Routes / endpoints for navigation

  const dashboardhome_route = `/${HOMEPAGE}`;
  const performance_route = `/${PERFORMANCE}`;
  const engagements_route = `/${ENGAGEMENTS}`;
  const admin_route = `/${ADMIN_PANEL}`
  const settings_route = '/dashboard/settings';
  const frontend_url = "/";

  return (
    <>
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

            <div className={link}>
              <Link href={admin_route}>
                <a className={adminicon}>
                <FaNetworkWired/>?
                  <img
                    className={adminicon}
                    src="/admin_icon.png"
                    alt="settings icon"
                  />
                </a>
              </Link>
            </div>
          </div>

          <div className={logout}>
            <Link href={frontend_url} onclick={logoutuser}>
              <a>
                <img
                  className={logouticon}
                  src="/logout_icon.png"
                  alt="logout icon"
                />
              </a>
            </Link>
          </div>
        </center>
      </div>
    </>
  );
}
