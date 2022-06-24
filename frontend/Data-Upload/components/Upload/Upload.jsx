import axios from "axios";

import { MdAddCircle } from "react-icons/md";

// import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import CircularProgress from "@material-ui/core/CircularProgress";
import { Container, Row, Col, Form, Button, ProgressBar } from "react-bootstrap"


import "bootstrap/dist/css/bootstrap.min.css";
import "react-circular-progressbar/dist/styles.css";
import "react-toastify/dist/ReactToastify.css";
import { ToastContainer, toast } from "react-toastify";

import styles from "../../styles/upload/upload.module.css";

import React, { useState, useEffect, useRef } from "react";

// Circular upload imports

var classNames = require("classnames");
toast.configure();

const FileUpload = ({ access, user }) => {
  //#####-- DATA URLs --#####//
  const endpointcreatefiles = "api/fileupload/create";
  const CreatefilesURL = `${process.env.API_URL}/${endpointcreatefiles}`;

  //#####-- react-hooks state variables -#####//
  const [multipleFiles, setMultiplefiles] = useState([]);
  const [moreFiles, setmoreFiles] = useState([]);
  const [selectedFilesInfos, setselectedFilesInfos] = useState([]);
  const [moreselectedFilesInfos, setmoreselectedFilesInfos] = useState([]);

  const [finalFileList, setfinalFileList] = useState([]);
  const [morefinalFileList, setmorefinalFileList] = useState([]);

  const [comment, setComments] = useState("");
  // const [MultipleProgress, setMultipleProgress] = useState(0);
  const [uploadingNotif, setUploadingNotif] = useState(false);

  //progress state for upload complete
  const [showProgress, setShowprogress] = useState(false);

  //#####-- Upload progress --#####//
  const multipleFileOptions = {
    onUploadProgress: (progressEvent) => {
      const { loaded, total } = progressEvent;
      const percentage = Math.floor(((loaded / 1000) * 100) / (total / 1000));
      setMultipleProgress(percentage);
    },
  };

  //Onchange events

  //Multiple files selected on change event
  const MultipleFileChange = (e) => {
    //set files
    let filestoUpload = e.target.files;
    setMultiplefiles(filestoUpload);
    setfinalFileList(filestoUpload);
    console.log("files to upload", filestoUpload);

    //get information about selected files
    let _selectedFilesInfo = [];
    //loop through fileList for properties, i.e file names
    for (let i = 0; i < filestoUpload.length; i++) {
      _selectedFilesInfo.push({ fileName: filestoUpload[i].name });
    }
    setselectedFilesInfos(_selectedFilesInfo);
    console.log("selected file Infos: ", _selectedFilesInfo);
    // console.log("files to be uploaded :", multipleFiles);
  };

  //adding more files.
  const MorefilesChange = (e) => {
    let filestoAppend = e.target.files;
    setmoreFiles(filestoAppend);
    setmorefinalFileList(filestoAppend);
    console.log("files to be appended", filestoAppend);

    //get information about selected files
    let _moreselectedFilesInfo = [];
    //loop through fileList for properties, i.e file names
    for (let i = 0; i < filestoAppend.length; i++) {
      _moreselectedFilesInfo.push({ fileName: filestoAppend[i].name });
    }
    setmoreselectedFilesInfos(_moreselectedFilesInfo);
    console.log("files to append Infos: ", _moreselectedFilesInfo);
  };

  //------>Remove file from list<------//

  //Remove an item from the 1st set of files selected
  const RemovelistFile = (index) => {
    const NewFileList = [...multipleFiles];

    console.log("index to remove", index);
    console.log("some new list:", NewFileList);

    //finally remove file
    const AfterRemoved = [...NewFileList];
    AfterRemoved.splice(index, 1);
    setfinalFileList(AfterRemoved);
    setMultiplefiles(AfterRemoved);
    console.log("After splice:", AfterRemoved);

    const newInfo = [...selectedFilesInfos];
    const NewInfoRemoved = [...newInfo];
    NewInfoRemoved.splice(index, 1);
    setselectedFilesInfos(NewInfoRemoved);
  };

  //Remove an item from the 2nd set of files selected
  const RemoveMoreFiles = (index) => {
    const NewFileList = [...moreFiles];

    console.log("index to remove", index);
    console.log("some new list:", NewFileList);

    //finally remove file
    const AfterRemoved = [...NewFileList];
    AfterRemoved.splice(index, 1);
    setmorefinalFileList(AfterRemoved);
    setmoreFiles(AfterRemoved);
    console.log("After splice:", AfterRemoved);

    const newInfo = [...moreselectedFilesInfos];
    const NewInfoRemoved = [...newInfo];
    NewInfoRemoved.splice(index, 1);
    setmoreselectedFilesInfos(NewInfoRemoved);
  };

  //Upload progress
  const [progress, setProgress] = useState()


  // Upload service -------> API Calls//
  const UploadService = (data) => {
    setUploadingNotif(true);
    axios
      .post(CreatefilesURL, data, {
        headers: {
          "Content-Type": "multipart/form-data",
          Authorization: `Token ${access}`,
        },
        onUploadProgress: data => {
          //Set the progress value to show the progress bar
          setProgress(Math.round((100 * data.loaded) / data.total))
        },
      })
      .then(() => {
        if (response.status == 201) {
          setUploadingNotif(false);
          setShowprogress(true);
        }
      })
      .catch((err) => {
        setUploadingNotif(false);
        setShowprogress(false);
        window.location.href = "#";
        toast.error("Upload unsuccessful. Please try again");
      });
  };

  //Upload Files ------> function//
  const uploadMultipleFiles = () => {
    const formData = new FormData();

    const FileUploadList = [...finalFileList, ...morefinalFileList];

    for (let i = 0; i < FileUploadList.length; i++) {
      formData.append("data_file", FileUploadList[i]);
    }

    formData.append("comment", comment);
    formData.append("user", user);

    UploadService(formData);

    console.log("files to be uploaded :", FileUploadList);
  };

  //#####--------- Spinners etc -------#####//

  //File upload circular progress
  function UploadSpinner() {
    return (
      <>
        {progress && <ProgressBar now={progress} label={`${progress}%`} style={{width: "80%"}}/>}

        {/* <CircularProgress color="secondary" variant="indeterminate" /> */}
        <p>Your file is Uploading...</p>
      </>
    );
  }

  function UploadDoneNotif() {
    return (
      <>
        <img
          src="/assets/images/upload-done.svg"
          alt="upload-done"
          id="upload-done-img"
          className="uploads-done"
        />
        <p style={{ fontFamily: "WorkSans", fontWeight: "bolder" }}>
          You are all done
        </p>
      </>
    );
  }

  //add files button on page load
  function Addfilesbtn() {
    return (
      <>
        <div
          style={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            backgroundColor: "white",
          }}
        >
          <label id="btn_selectlbl">
            <MdAddCircle
              className="stroke_add"
              id="stroke_add_btn"
              style={{
                fontSize: "50px",
                color: "#DF265E",
                cursor: "pointer",
              }}
            />
            <input
              className="select-file-input"
              id="select-file-in"
              type="file"
              webkitdirectory
              directory
              multiple
              onChange={(e) => MultipleFileChange(e)}
              className={styles.file_input}
            />
          </label>
          <p>Add your files</p>
        </div>
      </>
    );
  }

  function Morefilesbtn() {
    return (
      <>
        <div className={styles.btn_selectfiles}>
          <label id="btn_selectlbl">
            <MdAddCircle
              className="stroke_add"
              id="stroke_add_btn"
              style={{
                fontSize: "30px",
                color: "#DF265E",
                cursor: "pointer",
              }}
            />
            <input
              className="select-file-input"
              id="select-file-in"
              type="file"
              multiple
              onChange={(e) => MorefilesChange(e)}
              className={styles.file_input}
            />
            Add more files
          </label>
        </div>
      </>
    );
  }

  return (
    <>
      <div className={styles.container}>
        <div className={styles.uploadContainer}>
          <div className={styles.upload_content}>
            <div className={styles.files_to_upload} id="files-selected">
              {multipleFiles.length === 0 ? (
                <div>
                  <div
                    style={{ padding: "10px 10px 10px 10px" }}
                    className="no-file-selected"
                    id="no-file-selected"
                  >
                    No files selected
                  </div>
                  <Addfilesbtn />
                </div>
              ) : (
                <div className="selected-files" id="selected-files">
                  {selectedFilesInfos &&
                    selectedFilesInfos.map((file, index) => (
                      <div
                        className={styles.files_to_upload}
                        id="files-selected"
                        key={index}
                      >
                        <div className={styles.fileWrapper}>
                          <li>
                            <button
                              title="Remove from list"
                              className="modal-close"
                              onClick={() => {
                                RemovelistFile(index);
                              }}
                            >
                              &times;
                            </button>
                            <a
                              href="#"
                              id="file-instance"
                              className={styles.fileInstance}
                            >
                              {file.fileName}
                            </a>
                          </li>
                        </div>
                      </div>
                    ))}

                  {moreFiles.length === 0 ? (
                    <div>
                      <Morefilesbtn />
                    </div>
                  ) : (
                    <div className="selected-files" id="selected-files">
                      {moreselectedFilesInfos &&
                        moreselectedFilesInfos.map((file, index) => (
                          <div
                            className={styles.files_to_upload}
                            id="files-selected"
                          >
                            <div className={styles.fileWrapper}>
                              <li>
                                <button
                                  title="Remove from list"
                                  className="modal-close"
                                  onClick={() => {
                                    RemoveMoreFiles(index);
                                  }}
                                >
                                  &times;
                                </button>
                                <a
                                  href="#"
                                  id="file-instance"
                                  className={styles.fileInstance}
                                >
                                  {file.fileName}
                                </a>
                              </li>
                            </div>
                          </div>
                        ))}
                    </div>
                  )}
                </div>
              )}
            </div>

            <div className="upload-progress">
              {showProgress && <UploadDoneNotif />}
              <div className={styles.circular_upload}>
                {uploadingNotif && <UploadSpinner />}
              </div>
            </div>

            <div>
              <textarea
                id="upload_comment"
                cols="5"
                rows="3"
                placeholder="comments"
                className={styles.comment}
                onChange={(e) => setComments(e.target.value)}
              />
            </div>

            <div id="upload-btn-container">
              <button
                type="button"
                className={styles.btn_upload}
                disabled={!multipleFiles}
                onClick={() => uploadMultipleFiles()}
              >
                Upload
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default FileUpload;
