import { useState } from "react";
import { BsDash } from "react-icons/bs";
import { AzureLogin } from "../../components/Auth/Azure";
import LoginForm from "../../components/Auth/LoginForm";
import SignUpForm from "../../components/Auth/SignUpForm";
import MainLayout from "../../components/Layout/MainLayout";
import { PublicClientApplication } from "@azure/msal-browser";
import { MsalProvider } from "@azure/msal-react";
import { msalConfig } from "../../components/Auth/Azure/AuthConfig";
import styles from "../../styles/PasswordReset/passwordreset.module.css";

export default function Login() {
  const msalInstance = new PublicClientApplication(msalConfig);
  const [toggleAuth, setToggleAuth] = useState("login");

  return (
    <MsalProvider instance={msalInstance}>
      <MainLayout title="Login">
        <div className={styles.container}>
          <div className={styles.content_left}>
            <img src="/assets/images/logo.png"></img>
          </div>
          <section className={styles.content_right}>
            <div className={styles.content}>
              <h3>Scalework</h3>
              <div className={styles.row}>
                <div
                  className={styles.btn_logacc}
                  onClick={() => setToggleAuth("login")}
                  style={
                    toggleAuth == "login"
                      ? {
                          cursor: "pointer",
                          borderBottom: "2px solid #DF265E",
                        }
                      : { cursor: "pointer" }
                  }
                >
                  <h6>Log in</h6>
                </div>
                <div
                  className={styles.btn_logacc}
                  onClick={() => setToggleAuth("signup")}
                  style={
                    toggleAuth !== "login"
                      ? {
                          cursor: "pointer",
                          borderBottom: "2px solid #DF265E",
                        }
                      : { cursor: "pointer" }
                  }
                >
                  <h6>Create Account</h6>
                </div>
              </div>
              <div className={styles.btn_azure}>
                <AzureLogin />
              </div>
              <div className={styles.dash_row}>
                <span>
                  <BsDash
                    className={styles.dash_icon}
                    style={{
                      margin: "0 20px 0 0",
                    }}
                  />
                </span>
                or better yet...
                <span>
                  <BsDash
                    className={styles.dash_icon}
                    style={{
                      margin: "0 0 0 20px",
                    }}
                  />
                </span>
              </div>{" "}
              {toggleAuth == "login" ? <LoginForm /> : <SignUpForm />}
            </div>
          </section>
        </div>
        {/* <div className="row">
          <div
            className="col-6"
            style={{
              background: "#F7F7FC",
              backgroundImage: "url(" + " /assets/images/bg-image.jpg" + ")",
              margin: "0px",
              backgroundPosition: "center center",
              backgroundSize: "cover",
              backgroundRepeat: "no-repeat",
            }}
          >
            <img
              src="/assets/images/logo.png"
              style={{
                height: "62px",
                width: "#62px",
                zIndex: 1,
                margin: "50px 0 0 50px",
              }}
            ></img>
          </div>

          <div className="col-6">
            <div className="row justify-content-center">
              <section className="col-9 text-center p-5">
                <h1
                  className="pb-5"
                  style={{ fontWeight: "bolder", fontSize: "48px" }}
                >
                  Scalework
                </h1>
                <div className="row justify-content-center p-2">
                  <div
                    className="col-6"
                    onClick={() => setToggleAuth("login")}
                    style={
                      toggleAuth == "login"
                        ? {
                            cursor: "pointer",
                            borderBottom: "2px solid #DF265E",
                          }
                        : { cursor: "pointer" }
                    }
                  >
                    <h6 className="mb-4">Login</h6>
                  </div>
                  <div
                    className="col-6"
                    onClick={() => setToggleAuth("signup")}
                    style={
                      toggleAuth !== "login"
                        ? {
                            cursor: "pointer",
                            borderBottom: "2px solid #DF265E",
                          }
                        : { cursor: "pointer" }
                    }
                  >
                    <h6>Create Account</h6>
                  </div>
                </div>
                <hr
                  style={{ border: "2px solid #D6D8EF", marginTop: "-11px" }}
                />
                <div className="p-5">
                  <AzureLogin />
                </div>
                <span>
                  <BsDash
                    style={{
                      width: "50px",
                      height: "2px",
                      color: "#D6D8E7",
                      fontSize: "16px",
                      background: "#D6D8E7",
                      margin: "0 20px 0 0",
                    }}
                  />
                </span>
                or better yet...
                <span>
                  <BsDash
                    style={{
                      width: "50px",
                      height: "2px",
                      color: "#D6D8E7",
                      fontSize: "16px",
                      background: "#D6D8E7",
                      margin: "0 0 0 20px",
                    }}
                  />
                </span>{" "}
                {toggleAuth == "login" ? <LoginForm /> : <SignUpForm />}
              </section>
            </div>
          </div>
        </div> */}
      </MainLayout>
    </MsalProvider>
  );
}
