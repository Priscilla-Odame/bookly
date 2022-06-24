import { useState, useEffect } from "react";
import Header from "../../components/Upload/Header";
import Uploads from "../../components/Upload/Uploads";
import FileUpload from "../../components/Upload/Upload";
import MainLayout from "../../components/Layout/MainLayout";
import styles from "../../styles/upload/main.module.css";

export default function UploadFile() {
  const [access, setAccess] = useState("");
  const [firstname, setFirstname]: any = useState("");
  const [user, setUser]: any = useState<Number>();

  useEffect(() => {
    async function getLocalStorage() {
      if (typeof window !== "undefined") {
        const userData = window.localStorage.getItem("user-data");
        const foundUser = JSON.parse(userData);
        if (foundUser) {
          setAccess(foundUser.tokens.access);
          setFirstname(foundUser.firstname);
          setUser(foundUser.id);
          // console.log("access", access);
        }
      }
    }
    getLocalStorage();
  });

  return (
    <MainLayout title="Upload">
      <div className={styles.container}>
        <div id="header-section" className={styles.header}>
          <Header firstname={firstname} />
        </div>

        <div id="upload-section" className={styles.upload}>
          <Uploads access={access} />
        </div>
        <div id="files-section" className={styles.fileupload}>
          <FileUpload access={access} user={user} />
        </div>
      </div>
    </MainLayout>
  );
}
