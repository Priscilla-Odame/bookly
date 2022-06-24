import Modal from "../../../../../Layout/Modal";
import styles from "../../../../../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";
import { useState, useEffect } from "react";
import { API_PORT_HOSTED, ORGANIZATIONS } from "../../../../../../config";

export default function AddClientAdmin({
  setAdded,
  orgkey,
  setClientAdminList,
  clientAdminList,
}) {
  const { label, input, addClientBtn, validation } = styles;
  const [email, setEmail] = useState("");
  const [fullName, setFullName] = useState("");
  const [phone, setPhone] = useState("");
  const [role, setRole] = useState("");
  const [roleList, setRoleList] = useState([]);
  const [access, setAccess] = useState("");
  const [emailError, setEmailError] = useState(false);
  const [nameError, setNameError] = useState(false);
  const [phoneError, setPhoneError] = useState(false);
  const [roleError, setRoleError] = useState(false);
  useEffect(() => {
    const user = window.localStorage.getItem("access-token");
    console.log("access-token", user);
    setAccess(user);

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const requestOptions = {
      method: "GET",
      headers: myHeaders,
    };
    fetch(`${API_PORT_HOSTED}/${ORGANIZATIONS}/contact-role/`, requestOptions)
      .then((resp) => resp.json())
      .then((res) => setRoleList(res))
      .catch((err) => console.log(err));
  }, []);

  const addClientAdmin = async () => {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Authorization", `Bearer ${access}`);
    const raw = JSON.stringify({
      name: fullName,
      email: email,
      phone_number: phone,
      role: role,
      organization: `${API_PORT_HOSTED}/${ORGANIZATIONS}/organization/${orgkey}/`,
      status: "2260d2f8-ce59-484a-8da6-5460b8c731f6",
    });

    const reqOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
    };

    await fetch(
      `${API_PORT_HOSTED}/${ORGANIZATIONS}/administrator/`,
      reqOptions
    )
      .then((resp) => resp.json())
      .then((res) => {
        alert(res.email);
        setClientAdminList([...clientAdminList, res]), setAdded(true);
      })
      .catch((err) => console.log("err", err));
  };
  return (
    <Modal id="add-client-admin" title="Add Client Administrator">
      <div>
        <form id="aca-form">
          <div className="m-4" id="aca-nm-sec">
            <label id="lab-aca-nm" className={label}>Name</label>
            <div id="inp-aca-nm">
              <input
                className={input}
                id="add-client-admin-name"
                value={fullName}
                onChange={(e) => {
                  setFullName(e.target.value);
                  if (fullName == "") {
                    setNameError(true);
                  } else {
                    setNameError(false);
                  }
                }}
              ></input>
            </div>
            {nameError ? (
              <div id="val-aca-nm" className={validation}>
                <p>Enter a valid name</p>
              </div>
            ) : (
              <></>
            )}
          </div>
          <div className="m-4" id="aca-em-sec">
            <label id="lab-aca-em" className={label}>Email Address</label>
            <div id="inp-aca-em">
              <input
                className={input}
                id="add-client-admin-email"
                value={email}
                type="email"
                onChange={(e) => {
                  setEmail(e.target.value);
                  if (
                    email == "" ||
                    !email.match(
                      /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
                    )
                  ) {
                    setEmailError(true);
                  } else {
                    setEmailError(false);
                  }
                }}
              ></input>
            </div>
            {emailError ? (
              <div id="val-aca-em" className={validation}>
                <p>Enter a valid email address</p>
              </div>
            ) : (
              <></>
            )}
          </div>
          <div className="m-4" id="aca-phn-sec">
            <label id="lab-aca-phn" className={label}>Phone Number</label>
            <div id="inp-aca-phn">
              <input
                className={input}
                id="add-client-admin-phone"
                value={phone}
                onChange={(e) => {
                  setPhone(e.target.value);
                  if (phone == "" || !phone.match(/^\+[1-9]{1}[0-9]{3,14}$/)) {
                    setPhoneError(true);
                  } else {
                    setPhoneError(false);
                  }
                }}
              ></input>
            </div>
            {phoneError ? (
              <div className={validation} id="val-aca-phn">
                <p>Enter a phone number</p>
              </div>
            ) : (
              <></>
            )}
          </div>
          <div className="m-4" id="sec-aca-role">
            <label id="lab-aca-role" className={label}>Role</label>
            <div id="inp-aca-role">
              <select
                className={input}
                id="select-client-admin-role"
                value={role.name}
                onChange={(e) => {
                  setRole(e.target.value);
                  if (role.name == "") {
                    setRoleError(true);
                  } else {
                    setRoleError(false);
                  }
                }}
              >
                <option>Select Role</option>
                {roleList.map((role) => (
                  <option key={role.id} value={role.name}>
                    {role.name}
                  </option>
                ))}
              </select>
            </div>
            {roleError ? (
              <div id="val-aca-role" className={validation}>
                <p>Select a role</p>
              </div>
            ) : (
              <></>
            )}
          </div>
          <div className="m-4" id="aca-btn">
            {nameError || emailError || phoneError || roleError ? (
              <button
                className={`${addClientBtn} text-light `}
                id="submit-modal-form-btn"
                type="submit"
                data-dismiss="modal"
                onClick={addClientAdmin}
                disabled
              >
                Submit
              </button>
            ) : (
              <button
                className={`${addClientBtn} text-light `}
                id="close-modal-form-btn"
                type="submit"
                data-dismiss="modal"
                onClick={addClientAdmin}
              >
                Submit
              </button>
            )}
          </div>
        </form>
      </div>
    </Modal>
  );
}
