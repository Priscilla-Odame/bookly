import { useState, useEffect } from "react";
import styles from "../../../../styles/dashboard/settings.module.css";
import "bootstrap/dist/css/bootstrap.min.css";
import Modal from "../projects/modal";
import ProjectList from "../projects/projectList";

export default function AddProject() {
  //user authentication check
  const [email, setEmail] = useState("");
  const [tokens, setToken] = useState("");

  useEffect(() => {
    const userdata = localStorage.getItem("user");

    if (userdata) {
      const foundUser = JSON.parse(userdata);
      setEmail(foundUser.email);
      setToken(foundUser.access_token);
      console.log("User email found for project addition");
    } else {
      (window.location.href = "/"),
        console.log(
          "You happen to be having authentication problems, kindly login again."
        );
    }
  }, []);

  //Css Style ClassNames
  const { button, note, project } = styles;

  // Pop up modal
  const [showmodal, setshowmodal] = useState(false);

  const openModal = () => {
    setshowmodal(prev => !prev);
  };

  return (
    <>
      <body>
        <div className={project}>
          <h1>Project Management</h1>

          <b>
            Welcome to the projects configuration page, <br></br>you can
            customize your settings and perform additional operations here.
          </b>

          <br></br>
          <br></br>

          <button
            className={button}
            id="modalpopup"
            name="modalpopup"
            onClick={openModal}
          >
            Add Project
          </button>

          <br></br>
          <br></br>

          <Modal showmodal={showmodal} setshowmodal={setshowmodal} />

          <br></br>
          <div className={note}>
            <div className="card">
              <div className="card-header" style={{ textAlign: "center" }}>
                <h3>List of Projects Added</h3>
              </div>
              <ProjectList />
            </div>
          </div>
        </div>
      </body>
    </>
  );
}
