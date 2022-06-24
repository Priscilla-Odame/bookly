import "../styles/globals.css";
import { StoreProvider } from "../contextStore";

function MyApp({ Component, pageProps }) {
  return (
    <StoreProvider>
      <Component {...pageProps} />
    </StoreProvider>
  );
}

export default MyApp;
