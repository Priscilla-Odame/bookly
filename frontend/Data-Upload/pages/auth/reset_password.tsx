import Link from "next/link";
import MainLayout from "../../components/Layout/MainLayout";
import { MdKeyboardArrowLeft } from "react-icons/md";
import styles from "../../styles/PasswordReset/passwordreset.module.css";
import CreatePassword from "../../components/PasswordReset/createPassword";
import PasswordChanged from "../../components/PasswordReset/passwordChanged";
import { useState } from "react";

export default function resetPassword() {
  const [passwordChanged, setPasswordChanged] = useState(false);

  return (
    <MainLayout title="Reset Password">
      <div className={styles.container}>
        <div className={styles.content_left}>
          <img src="/assets/images/logo.png"></img>
        </div>
        <div className={styles.content_right}>
          {passwordChanged ? (
            <PasswordChanged />
          ) : (
            <CreatePassword setPasswordChanged={setPasswordChanged} />
          )}
          {/* Conditionally render PasswordChanged component when password has been reset successfully */}
        </div>
      </div>
    </MainLayout>
  );
}
