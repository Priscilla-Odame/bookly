import Modal from "../../../Layout/Modal";
import styles from "../../../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";
import { useState, useEffect } from "react";
import AddClientAdmin from './AddClientAdmin';


export default function AddClientOrganization({ setAdded, orgKey }) {
  const { label, input, btn, fileLabel,fileinput, btn2 } = styles;

  const [logo, setLogo] = useState([]);
  const [name, setName] = useState("")
  const [description, setDescription] = useState("");
  const [access, setAccess] = useState("");

  

  useEffect(() => {
    const user = window.localStorage.getItem("access");
    console.log("access", user);
    setAccess(user);
  }, []);


  const addClientOrganization = async () => {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Authorization", "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3Mjg0NTQxLCJqdGkiOiIyZThhZTRmYTVlODY0ZjhlYTIyNmZjOTBkZmNhMjY2OSIsInVzZXJfaWQiOjJ9.KQLYSC4CFgQLpahbP-u80uRC5Vf_WKgIamSq3Cmk71U");
    const raw = JSON.stringify({
      logo: logo,
      name: name,
      description: description    });

    const reqOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
    };

    await fetch(
      `https://be01.pitest.xyz/api/organizations/organization/`,
      reqOptions
    )
      .then((resp) => resp.text())
      .then((res) => {
        console.log("res", res), setAdded(true);
      })
      .catch((err) => console.log("err", err));
  };
  return (
      <div>
    <Modal id="admin-add-client-organization" title="Add Client Organization">
      <div>
        <form id="admin-clt client-organization-form">
          <div className="m-4">
            <label className={label}>Organization Name</label>
            <div>
              <input
                className={input}
                id="admin-clt-org-name"
                value={name}
                onChange={(e) => setName(e.target.value)}
              ></input>
            </div>
          </div>
          <div className="m-4">
            <label className={label}>Organization Description</label>
            <div>
              <input
                className={input}
                id="admin-clt-org-des"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              ></input>
            </div>
          </div>
          <div className="m-4">
            <div>
            <label className={fileLabel}>            
              <input
                id="admin-clt-org-logo"
                placeholder="Upload Image"
                type="file"
                accept="image"
                className={fileinput}
                value={logo}
                onChange={(e) => setLogo(e.target.value)}
              ></input>
                165 x 165 px (min size)
              </label>
            </div>
          </div>
          <div className="m-4">
            <button
                className={`${btn} text-light `}
                id="admin-dismiss-org-mod-btn"
                type="button"
                data-dismiss="modal"
                >
                Close
            </button>
            <button
                className={`${btn} text-light `}
                id="admin-sub-org-mod-btn"
                type="button"
                data-toggle="modal"
                data-dismiss="modal"
                data-target="#admin-add-client-admin"
            >
              Next
            </button>
          </div>
        </form>
      </div>
    </Modal>
    <AddClientAdmin/>
    </div>
  );
}
