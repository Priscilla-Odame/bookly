import Head from "next/head";
import "bootstrap/dist/css/bootstrap.css";

export default function MainHead({ title }) {
  return (
    //Head Section
    <Head>
      <title>{`Push Insights | ${title}` || "Push Insights"}</title>
      <meta name="viewport" content="width=device-width, initial-scale=1.0" />
      <link rel="shortcut icon" href="/assets/images/logo/logo.svg" />
      <link rel="preconnect" href="https://fonts.gstatic.com" />
      <link
        href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@700&display=swap"
        rel="stylesheet"
      />
    </Head>
  );
}
