import React, { useState, useContext, useEffect } from "react";
// import { Store } from "../contextStore";
import Head from "next/head";
import { useForm } from "react-hook-form";
import styles from "../styles/login.module.css";
import Link from "next/link";
import { useRouter } from "next/router";
import isEmail from "validator/lib/isEmail";
import classNames from "classnames/bind";
import axios from "axios";
import { Redirect } from "react-router-dom";
import { FiUser } from "react-icons/fi";
import { FiEye } from "react-icons/fi";
import { API_PORT_HOSTED, API_MANAGEMENT_CONSOLE_HOSTED, ORGANIZATIONS } from "../config";

export default function LoginForm() {
  const {container, card, title, input, group, button, link, logo, usericon, passicon, errorInput}=styles
  const [response, setResponse] = useState([]);
  const [emailAddress, setEmailAddress] = useState("");
  const [password, setPassword] = useState("");
  const router = useRouter();
  //Endpoints and urls

  // const endpoint = "api/user/login";

  const management_endpoint = "api/organizations/login";
  const url = `${API_PORT_HOSTED}:${API_MANAGEMENT_CONSOLE_HOSTED}/${management_endpoint}/`;

  //Password visibiltity function using "eye" icon

  const passwordvisibility = () => {
    var x = document.getElementById("password");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  };

  const {
    register,
    handleSubmit = async (e) => {
      {e.preventDefault;}
    },watch,errors,
  } = useForm();

  //handle form data

  const onSubmit = async () => {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({
      email: emailAddress,
      password: password,
    });

    var requestOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw
    };
  

    await fetch(
      `${API_PORT_HOSTED}/${ORGANIZATIONS}/login/`,
      requestOptions
    )
      .then((response) => response.json())
      .then((result) => {
        setResponse(result),
        console.log(result);
        if (result.status == 200) {
                //store user logged in credentials
                setResponse(resp), router.push("/dashboard/adminpanel/");
                window.alert("Login Successful");
      
                localStorage.setItem("user", JSON.stringify(response));
              } else {
                router.push("/");
              }
      })
      .catch((error) => console.log("error", error));
  };

  useEffect(() => {
    if (response.access_token) {
      router.push('/dashboard/adminpanel/')
      window.localStorage.setItem('access-token', response.access_token);
      window.localStorage.setItem('user', JSON.stringify(response));
    }
  }, [onSubmit]);

  // react router redirect to homepage

  const [redirect] = useState(false);

  if (redirect == true) {
    return <Redirect to="/dashboard/homepage" />;
  } else {
    //Login form component returned

    return (
      <body>
        <div>
          <Head>
            <title>Push Insights</title>

            {/*Font import*/}

            <link
              rel="preload"
              href="/fonts/Work_Sans/static/WorkSans-Regular.ttf"
              as="Font"
              crossOrigin=""
            />
          </Head>

          <div className={container}>
            <div className={card}>
              <div className={group}>
                <div className={title}>
                  <img className={logo} src="/logo.png" alt="logo" />
                  <h1>Login</h1>
                </div>

                <div>
                  <form onSubmit={handleSubmit(onSubmit)}>
                    <div>
                      <div>
                        <FiUser
                          className={styles.usericon}
                          aria-label="User icon"
                          id="usericon"
                        />
                        {/* <img className={styles.usericon} src="/user-icon.png" alt="user icon" id= "usericon"/> */}
                        <input
                          type="text"
                          className={
                            errors && errorInput,
                            input
                          }
                          placeholder="Enter Email"
                          name="email"
                          id="email"
                          value={emailAddress}
                          // ref={register({
                          //   required: true,
                          //   validate: (input) => isEmail(input),
                          // })}
                          onChange={(e) => setEmailAddress(e.target.value)}
                        />
                        {/* {errors.emailAddress && (
                          <span className={styles.link}>
                            Kindly enter a valid email
                          </span>
                        )}{" "} */}
                      </div>

                      <div>
                        <FiEye
                          className={styles.passicon}
                          aria-label="Password icon"
                          id="togglepassword"
                          onClick={passwordvisibility}
                        />
                        {/* <img className={styles.passicon} src="/password-icon.png" alt="toggle password icon" id="togglepassword" onClick={passwordvisibility}/> */}

                        <input
                          type="password"
                          className={
                            errors && errorInput,
                            input
                          }
                          placeholder="Enter Password"
                          name="password"
                          id="password"
                          value={password}
                          // ref={register({
                          //   required: true,
                          //   minLength: 8,
                          //   //pattern:/^([a-zA-Z0-9@*#]{8,15})$/})}/>
                          // })}
                          onChange={(e) => setPassword(e.target.value)}
                        />
                        {/* {errors.password && (
                          <span className={styles.link}>
                            Kindly enter a valid password
                          </span>
                        )} */}
                      </div>

                      {/*Empty div*/}
                      <div></div>

                      <button
                        type="submit"
                        className={styles.button}
                        value="submit"
                      >
                        Login
                      </button>

                      <center>
                        <Link href="/">
                          <a className={styles.link}>Forgot Password?</a>
                        </Link>
                        <br />

                        {/* <Link href="/signup"><a className={styles.link} >Don't have an Account? Sign up Here</a></Link> */}
                      </center>
                    </div>
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </body>
    );
  }
}
