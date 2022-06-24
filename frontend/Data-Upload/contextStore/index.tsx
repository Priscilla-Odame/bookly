import { createContext, useReducer } from "react";
import { STORETYPES } from "../utils/shared";

export const Store = createContext<string | any>("");

type TTokens = {
  accessToken: string;
  refreshToken: string;
};

interface IGState {
  tokens: TTokens;
  loggedin: boolean;
}

//Defining the initial states
const initState: IGState = {
  tokens: { accessToken: "", refreshToken: "" },
  loggedin: false,
};

const reducer = (state, action) => {
  switch (action.type) {
    case STORETYPES.LOGIN: //
      return { ...state, loggedin: action.payload };

    default:
      break;
  }
};

export const StoreProvider = ({ children }) => {
  const [state, dispatch] = useReducer(reducer, initState);
  return (
    <Store.Provider value={{ state, dispatch }}>{children}</Store.Provider>
  );
};
