import { useRouter } from "next/router";
import { localStorageToJson } from "../../utils/shared";
import isTokenExpired from "../../utils/expiredToken";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer, toast } from "react-toastify";
//Toastify config
toast.configure();

const withAuth = (Component) => {
  // if (!Component) return null;

  return (props) => {
    if (typeof window !== "undefined") {
      const router = useRouter();
      const accessToken = localStorageToJson();
      //   console.log(JSON.stringify(accessToken));

      // If there is no access token we redirect to "/" page.
      if (
        !accessToken ||
        !accessToken.token ||
        isTokenExpired(accessToken.token)
      ) {
        toast.error("Login required");
        router.push("/auth/login");
      }
      // If user is logged in, return original component
      return <Component {...props} />;
    }

    return null;

    // Copy getInitial props so it will run as well
    // if (Component.getInitialProps) {
    //   Auth.getInitialProps = Component.getInitialProps;
    // }
  };
};

export default withAuth;
