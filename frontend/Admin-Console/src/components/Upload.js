import axios from "axios";
import { useForm } from "react-hook-form";
import "bootstrap/dist/css/bootstrap.min.css";
import React, { useState, useEffect } from "react";
import { API_BASE_URL, API_PORT } from "../../config";
import styles from "../../styles/dashboard/dataupload.module.css";
import UploadService from "../../src/services/FileUploadservice";

const UploadFiles = () => {
  //Endpoints / urls
  const list_projects_endpoint = "api/projects";
  const list_projects_url = `${API_BASE_URL}:${API_PORT}/${list_projects_endpoint}`;

  //styles
  const { label, uploadInputfields } = styles;

  //handle fields for post requests
  const { register } = useForm();

  //defined/hard coded project

  const [selectedFiles, setSelectedFiles] = useState(undefined);
  const [message, setMessage] = useState("");
  const [progressInfos, setProgressInfos] = useState([]);
  const [fileInfos, setFileInfos] = useState([]);
  const [token, setToken] = useState("");
  const [email, setEmail] = useState("");

  // const userdata = localStorage.getItem('user');
  // console.log(userdata)

  //Using a second useEffect to make company calls to API
  //-----------------------------------------------------

  useEffect(() => {
    const userdata = localStorage.getItem("user");
    if (userdata) {
      const foundUser = JSON.parse(userdata);
      setEmail(foundUser.email);
      setToken(foundUser.tokens);
      console.log("User is authenticated to view projects");
      getProjects();
    }
  }, []);

  async function getProjects() {
    const userdata = localStorage.getItem("user");
    userdata = JSON.parse(userdata);
    const response = await axios
      .get(list_projects_url, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${userdata.access_token}`,
        },
      })
      .then((response) => {
        // On successful addition of Project

        if (response.status == 200) {
          console.log(response);
          localStorage.setItem("member list", JSON.stringify(response.data));
        }

        if (response.status == 401) {
          console.log(response);
          window.alert(
            "You are not authorized to fetch projects for uploading data."
          );
          localStorage.setItem("member list", JSON.stringify(response.data));
        } else {
          console.log(response);
        }
      })
      .catch((err) => {
        console.log("Could not fetch projects", err);
        window.alert(
          "Could not fetch projects to upload data. Please check your network connection and try again"
        );
      });
    // const body = await response.json();
    setProjects(response.data.map(({ name }) => ({ id: name, name: name })));
  }
  getProjects();

  //companies object state

  const [project, setProjects] = useState([]);
  const [ProjValue, setProjValue] = useState();
  const [tokens] = useState("");

  // set the values of selectedFiles after user triggers the file input
  const selectFiles = (event) => {
    setSelectedFiles(event.target.files);
    setProgressInfos([]);
  };

  // handles upload of files
  const uploadFiles = () => {
    let allFilesSelected = selectedFiles;
    // hold and push the fileName and progress of each file upload
    let _progressInfos = progressInfos;

    // populate the fileNames of the progress info together
    // with the initial values of progress 0%
    for (let i = 0; i < allFilesSelected.length; i++) {
      _progressInfos.push({
        percentage: 0,
        nameoffile: allFilesSelected[i].name,
      });
    }

    // set initial values of progress infos
    setProgressInfos([..._progressInfos]);

    // iterate through all the selected files
    let progInfos = [...progressInfos];
    for (let i = 0; i < allFilesSelected.length; i++) {
      let currentFile = allFilesSelected[i];

      // now call the upload serverice for each iter
      UploadService.upload(
        currentFile,
        (event) => {
          console.log("prog infos is ", progInfos);
          const percentage = Math.round((100 * event.loaded) / event.total);
          // during upload, just update the percentage part of the progressInfo of the file
          progInfos[i].percentage = percentage;
          setProgressInfos(progInfos);
        },
        token
      )
        .then((response) => {
          let message = "File's uploaded successfully " + i;
          setMessage(message);
          console.log(message);
        })
        .catch(() => {
          let message = "Could not upload the file! " + i;
          setMessage(message);
          console.log(message);
        });
      // end of upload service
    }
    // after the upload reset selectedFiles to default
    setSelectedFiles(undefined);
  };
  useEffect(() => {
    UploadService.getFiles().then((response) => {
      setFileInfos(response);
    });
  }, []);

  return (
    <div>
      {/* Iterate here and do this */}
      {progressInfos &&
        progressInfos.map((progressInfo, index) => (
          <div className="mb-2" key={index}>
            <span>{progressInfo.nameoffile}</span>
            <div className="progress">
              <div
                className="progress-bar progress-bar-striped progress-bar-animated "
                role="progressbar"
                aria-valuenow={progressInfo.percentage}
                aria-valuemin="0"
                aria-valuemax="100"
                style={{ width: progressInfo.percentage + "%" }}
              >
                {progressInfo.percentage}%
              </div>
            </div>
          </div>
        ))}
      <div></div>

      <label
        for="Project"
        id="Project"
        className={label}
        alt="label for Project"
      >
        Project to which file will be uploaded to:
      </label>
      <select
        type="text"
        className={uploadInputfields}
        placeholder="Projects *"
        name="projects"
        id="projects"
        value={ProjValue}
        onChange={(e) => setProjValue(e.currentTarget.value)}
        ref={register({
          required: true,
          // pattern: /^[A-Za-z]+$/i,
        })}
      >
        {project.map(({ id, name, key }) => (
          <option value={key} key={id} name={name}>
            {name}
          </option>
        ))}
      </select>

      <br></br>
      <br></br>
      <hr></hr>

      <label
        for="filetitle"
        id="filetitle"
        className={label}
        alt="label for file title"
      >
        File title
      </label>
      <input
        id="filename"
        name="tittle"
        type="text"
        className={uploadInputfields}
        alt="title"
        ref={register({ required: true })}
      ></input>

      <br></br>
      <br></br>
      <hr></hr>

      <label for="user" id="user" className={label} alt="user">
        User uploading
      </label>
      <input
        id="user"
        name="user"
        type="read-only"
        className={uploadInputfields}
        alt="user"
        value={email}
        ref={register({ required: true, validate: (input) => isEmail(input) })}
      ></input>

      <br></br>
      <br></br>
      <hr></hr>

      <label
        className="btn btn-default"
        style={{
          border: "solid 2px #D6D8E7",
          marginRight: "28px",
          paddingRight: "90px",
          backgroundColor: "#df265e",
          color: "white",
        }}
      >
        <input
          type="file"
          accept=".doc, .docx,.pdf"
          id="dataupload"
          name="dataupload"
          multiple
          onChange={selectFiles}
        />
        File(s) to be uploaded
      </label>

      <br></br>
      <br></br>
      <hr></hr>

      <button
        className="btn btn-primary "
        disabled={!selectedFiles}
        id="upload"
        onClick={uploadFiles}
        style={{
          padding: "9px 20px",
          marginTop: "-7px",
          backgroundColor: "#df265e",
          color: "white",
        }}
      >
        Upload
      </button>
      <div className="alert alert-light" role="alert">
        {message}
      </div>
      <div className="card">
        <div className="card-header">List of Uploaded Files</div>
        <ul className="list-group list-group-flush">
          {fileInfos &&
            fileInfos.map((file, index) => (
              <li className="list-group-item" key={index}>
                <a href="#">{file.title}</a>
              </li>
            ))}
        </ul>
      </div>
    </div>
  );
};
export default UploadFiles;
