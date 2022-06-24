import React, { useEffect, useState } from "react";
import { useMsal } from "@azure/msal-react";
import { loginRequest } from "./Azure/AuthConfig";
import styles from "./Auth.module.css";
import { useRouter } from "next/router";
import { graphConfig } from "./Azure/AuthConfig";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer, toast } from "react-toastify";

export const AzureLogin = () => {
  const router = useRouter();
  const { instance, accounts } = useMsal();
  //const [handled, setHandled] = useState(accounts?.length > 1 ? true : false);

  async function RequestProfileData() {
    // Silently acquires an access token which is then attached to a request for MS Graph data
    if (accounts?.length > 0) {
      await instance
        .acquireTokenSilent({
          ...loginRequest,
          account: accounts[0],
        })
        .then((response) => {
          callMsGraph(response.accessToken);
        });
    }
  }

  /**
   * Attaches a given access token to a MS Graph API call. Returns information about the user
   * @param accessToken
   */
  async function callMsGraph(accessToken) {
    // console.log("access", accessToken);
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({
      auth_token: accessToken,
      auth_provider: "microsoft",
    });

    const options = {
      method: "POST",
      body: raw,
      headers: myHeaders,
    };

    await fetch(graphConfig.endpoint, options)
      .then((response) => response.json())
      .then((res) => {
        if (res.id)
          window.localStorage.setItem("user-data", JSON.stringify(res));
        toast.success("Login successful");
      })
      .then(() => router.push("/upload"))
      .catch((error) => {
        console.log(error);
        toast.error("Login failed, Please try again");
      });
  }

  useEffect(() => {
    RequestProfileData();
  });

  const handleLogin = () => {
    instance.loginRedirect(loginRequest);
  };

  return (
    <button
      id="authenticationButton"
      className={styles.microsoftbtn}
      onClick={() => handleLogin()}
      title="Sign In"
    >
      <img src="/assets/images/logo/micro.svg" style={{ marginRight: "10%" }} />{" "}
      Continue with Microsoft
    </button>
  );
};
