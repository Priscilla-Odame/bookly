export const STORETYPES = {
  LOGIN: "SET_LOGIN",
};

export const localStorageToJson = () => {
  const data = window.localStorage.getItem("user-data");

  return JSON.parse(data);
};
