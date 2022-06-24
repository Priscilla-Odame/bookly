import MainLayout from "../components/Layout/MainLayout";
import Link from "next/link";
import { SignOutButton } from "../components/Auth/SignOutButton";
import { MsalProvider } from "@azure/msal-react";
import {
  FaUserCircle,
  FaCloud,
  FaFileUpload,
  FaUpload,
  FaCloudscale,
  FaCloudsmith,
  FaCloudversify,
  FaMixcloud,
  FaCloudDownloadAlt,
} from "react-icons/fa";
import { PublicClientApplication } from "@azure/msal-browser";
import { msalConfig } from "../components/Auth/Azure/AuthConfig";

export default function Home() {
  const msalInstance = new PublicClientApplication(msalConfig);
  return (
    <MsalProvider instance={msalInstance}>
      <MainLayout title="HomePage">
        <div className="home-navigation">
          <p>Proceed to...</p>
          <Link href="/auth/login">
            <a className="auth">
              Login
              <FaUserCircle />
            </a>
          </Link>
          <Link href="/upload">
            <a className="upload">
              Upload <FaFileUpload />
            </a>
          </Link>
          <SignOutButton />
        </div>
      </MainLayout>
    </MsalProvider>
  );
}
