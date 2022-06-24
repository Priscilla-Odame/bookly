export const getAccessKey = () => {
  if (typeof window !== "undefined") {
    const user = window.localStorage.getItem("access-token");
    return user;
  }
};

export const getOrgKey = () => {
  if (typeof window !== "undefined") {
    const orgKey = window.localStorage.getItem("orgKey");
    return orgKey;
  }
};

export const getClientAdminDetails = () => {
    if (typeof window !== "undefined") {
      const clientAdmin = window.localStorage.getItem("Client-Admin");
      return JSON.parse(clientAdmin);
    }
  };

const API_BASE_URL = process.env.API_BASE_URL;
const API_PORT = process.env.API_PORT;
const API_PORT_HOSTED = process.env.NEXT_PUBLIC_API_PORT_HOSTED;
const API_MANAGEMENT_CONSOLE = process.env.API_MANAGEMENT_CONSOLE;
const API_MANAGEMENT_CONSOLE_HOSTED = process.env.API_MANAGEMENT_CONSOLE_HOSTED;
const API_PORT_FRONTEND = process.env.API_PORT_FRONTEND;

const ORGANIZATIONS = "api/organizations";
const ACCOUNTS = "api/accounts";
const HOMEPAGE = "dashboard";
const PERFORMANCE = "dashboard/performance";
const ENGAGEMENTS = "dashboard/engagement";
const SETTINGS = "dashboard/settings";
const ADMIN_PANEL = "dashboard/adminpanel";
const ACCESS_KEY = getAccessKey();
const ORGKEY = getOrgKey();
const CLIENT_ADMIN_DETAILS = getClientAdminDetails()

export {
  API_BASE_URL,
  API_PORT,
  API_PORT_HOSTED,
  API_MANAGEMENT_CONSOLE,
  API_MANAGEMENT_CONSOLE_HOSTED,
  ORGANIZATIONS,
  ACCOUNTS,
  API_PORT_FRONTEND,
  HOMEPAGE,
  PERFORMANCE,
  ENGAGEMENTS,
  SETTINGS,
  ADMIN_PANEL,
  ACCESS_KEY,
  ORGKEY,
  CLIENT_ADMIN_DETAILS
};
