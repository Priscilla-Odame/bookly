import Head from "next/head";
import styles from "../../styles/dashboard/AdminPanel/adminpanel.module.css";
import SideNav from "../dashboard/sidenav";
import Navigation from "../dashboard/navigation";

export default function Admin({ children, title }) {
  const { dashboard, dashboardcontent } = styles;

  return (
    <>
      <Head>
        <link
          rel="preload"
          href="/fonts/Work_Sans/static/WorkSans-Regular.ttf"
          as="Font"
          crossOrigin=""
        />
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/css/bootstrap.min.css"
          integrity="sha384-B0vP5xmATw1+K9KRQjQERJvTumQW0nPEzvF6L/Z6nronJ3oUOFUFpCjEUQouq2+l"
          crossOrigin="anonymous"
        />

        <title>{title}</title>
      </Head>
      <div className={dashboard}>
        <div>
          <SideNav />
        </div>
        <div>
          <Navigation />
        </div>
        <div className="container mr-5">{children}</div>
      </div>
      <script
        src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
        integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
        crossOrigin="anonymous"
      ></script>
      <script
        src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
        integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN"
        crossOrigin="anonymous"
      ></script>
      <script
        src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.min.js"
        integrity="sha384-+YQ4JLhjyBLPDQt//I+STsc9iw4uQqACwlvpslubQzn4u2UU2UFM80nGisd026JF"
        crossOrigin="anonymous"
      ></script>
    </>
  );
}
