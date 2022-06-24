module.exports = {
  env: {
    AZURE_ACTIVE_DIRECTORY_APP_CLIENT_ID:
      "feea8b4f-b349-4653-93d8-60e77c89d9cf",
    API_URL: "https://be-dev.scalework.net",
    REDIRECT_URI: "https://fe-dev.scalework.net/auth/login",
  },
  env_local: {
    AZURE_ACTIVE_DIRECTORY_APP_CLIENT_ID:
      "feea8b4f-b349-4653-93d8-60e77c89d9cf",
    API_URL: "http://localhost:8000",
    REDIRECT_URI: "http://localhost:3000/auth/login",
  },
};
