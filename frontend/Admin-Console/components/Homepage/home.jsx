import React from "react";
import Head from "next/head";
import Header from "./header";
import Sidenav from "./sidenav";
import { useState, useEffect } from "react";
import MainContent from "./main_content/main_content";
import styles from "../../styles/Homepage/home.module.css";

export default function Home() {
    
  //Define styles
  const { body, dashboard, side_nav, main_content, header } = styles;

  //Logged in user state object

  const [firstname, setFirstname] = useState("");
  const [othernames, setOthernames] = useState("");
  const [tokens, setToken] = useState("");

  //check user login status
  useEffect(() => {
    const userdata = localStorage.getItem("user");

    if (userdata) {
      const foundUser = JSON.parse(userdata);

      setFirstname(foundUser.firstname);
      setOthernames(foundUser.othernames);
      setToken(foundUser.token);

      console.log("User is logged in", othernames, firstname, tokens);
    } else {
      window.location = "#";
      // window.location="/"
    }
  }, []);

  return (
    <>
      <Head>
        <link
          rel="preload"
          href="/fonts/Work_Sans/static/WorkSans-Regular.ttf"
          as="Font"
          crossOrigin=""
        />

        <title>Push Insights</title>
      </Head>

      <body className={body}>
        <div className={dashboard}>
          <section className={header}>
            <Header />
          </section>

          <section className={side_nav}>
            <Sidenav />
          </section>

          <section className={main_content}>
            <MainContent />
          </section>
        </div>
      </body>
    </>
  );
}
