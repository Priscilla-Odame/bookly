import React from "react";
import { useMsal } from "@azure/msal-react";

/**
 * Renders a sign-out button
 */
export const SignOutButton = () => {
  const { instance } = useMsal();

  const handleLogout = () => {
    window.localStorage.removeItem("user-data");
    instance.logoutRedirect({
      postLogoutRedirectUri: "/",
    });
  };
  return (
    <button className="sign-out" onClick={() => handleLogout()}>
      Sign out using Redirect
    </button>
  );
};
