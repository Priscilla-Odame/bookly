import { useState } from "react";

export const useToken = () => {
  const [token, setTokenInternal] = useState<string>(() => {
    return localStorage.getItem("token");
  });

  const setToken = (newToken) => {
    localStorage.setItem("token", newToken);
    setTokenInternal(newToken);
  };

  return [token, setToken];
};
