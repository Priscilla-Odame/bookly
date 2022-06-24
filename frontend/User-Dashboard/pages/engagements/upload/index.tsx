import { useState } from "react";
import FileUpload from '../../../components/Engagements/Upload/Upload';
import MainLayout from "../../../components/Layout/MainLayout";
import Header from '../../../components/Engagements/Upload/Header';
import Uploads from '../../../components/Engagements/Upload/Uploads';

export default function UploadFile() {

  return (
    <MainLayout title="Upload">
      <div>
        <div id="header-section">
          <Header/>
        </div>

        <div id="upload-section">
          <Uploads/>
        </div>
        <div id="files-section">
          <FileUpload/>
        </div>
      </div>
    </MainLayout>
  );
}
