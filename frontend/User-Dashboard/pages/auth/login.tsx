import { useState } from "react";
import AzureLogin from "../../components/Auth/Azure";
import LoginForm from "../../components/Auth/LoginForm";
import SignUpForm from "../../components/Auth/SignUpForm";
import MainLayout from "../../components/Layout/MainLayout";
//import reportWebVitals from './reportWebVitals';

export default function Login() {
  const [toggleAuth, setToggleAuth] = useState("login");

  return (
    <MainLayout title="Login">
      <div className="row" style={{ height: "1vh" }}>
        <img src="/assets/images/bg.svg" className="col-6"></img>
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
              <hr style={{ border: "2px solid #D6D8EF", marginTop: "-11px" }} />
              <div className="p-5">
                <AzureLogin />
              </div>
              <span style={{ border: "2px solid #D6D8E7" }}></span>
              or better yet...
              <span style={{ border: "2px solid #D6D8E7" }}></span>
              {toggleAuth == "login" ? <LoginForm /> : <SignUpForm />}
            </section>
          </div>
        </div>
      </div>
    </MainLayout>
  );
}
