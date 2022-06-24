import Modal from "../../../../../Layout/Modal";
import styles from "../../../../../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";
import React, { useEffect, useState } from "react";
import { API_PORT_HOSTED, ORGANIZATIONS } from "../../../../../../config";

export default function EditClientAdmin({
  getAdmin,
  clientDetail,
  setUpdated,
  orgkey,
}) {
  const { label, input, btn, btn2 } = styles;
  // const [admin, setAdmin] = useState([]);

  const [roleList, setRoleList] = useState([]);
  const [fullName, setFullName] = useState("");
  const [emailAddress, setEmailAddress] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [role, setRole] = useState("");
  const [access, setAccess] = useState("");

  useEffect(() => {
    const user = window.localStorage.getItem("access-token");
    console.log("access-token", user);
    setAccess(user);
  }, []);

  const updateClientAdmin = async (id) => {
    try {
      const myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      myHeaders.append("Authorization", `Bearer ${access}`);

      const raw = JSON.stringify({
        name: fullName,
        email: emailAddress,
        phone_number: phoneNumber,
        role: role,
        organization: `${API_PORT_HOSTED}/${ORGANIZATIONS}/organization/${orgkey}/`,
        status: "2260d2f8-ce59-484a-8da6-5460b8c731f6",
      });

      const reqOptions = {
        method: "PUT",
        headers: myHeaders,
        body: raw,
      };

      fetch(
        `${API_PORT_HOSTED}/${ORGANIZATIONS}/administrator/${id}/`,
        reqOptions
      )
        .then((resp) => resp.json())
        .then((res) => {
          console.log("edit res", res), getAdmin, setUpdated(true);
        })
        .catch((err) => console.log("error", err));
    } catch (err) {
      console.log(err);
    }
  };

  useEffect(() => {
    async function setStates() {
      setFullName(clientDetail.name);
      setEmailAddress(clientDetail.email);
      setPhoneNumber(clientDetail.phone_number);
      setRole(clientDetail.role);
    }
    setStates();

    const getRoles = async () => {
      const myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      const requestOptions = {
        method: "GET",
        headers: myHeaders,
      };
      await fetch(
        `${API_PORT_HOSTED}/${ORGANIZATIONS}/contact-role/`,
        requestOptions
      )
        .then((resp) => resp.json())
        .then((res) => setRoleList(res))
        .catch((err) => console.log(err));
    };
    getRoles();
  }, [clientDetail]);

  return (
    <Modal id="edit-client-admin" title="Profile Information">
      {/* <div>{admin.profile ? <img src={profileImage} /> : <></>}</div> */}
      <div className="m-4" id="eca-nm-sec">
        <label id="nmlab-eca" className={label}>
          Name
        </label>
        <div id="nm-inp-eca">
          <input
            id="eca-nm-inp"
            type="text"
            name="text"
            className={input}
            defaultValue={clientDetail.name}
            onChange={(e) => setFullName(e.target.value)}
          ></input>
        </div>
      </div>
      <div className="m-4" id="eca-ema-sec">
        <label id="emlab-eca" className={label}>
          Email Address
        </label>
        <div id="ema-inp-eca">
          <input
            id="eca-ema-inp"
            className={input}
            defaultValue={clientDetail.email}
            onChange={(e) => setEmailAddress(e.target.value)}
          ></input>
        </div>
      </div>
      <div className="m-4" id="eca-phone-sec">
        <label className={label} id="phnlab-eca">
          Phone Number
        </label>
        <div id="phn-inp-eca">
          <input
            id="eca-ema-inp"
            className={input}
            defaultValue={clientDetail.phone_number}
            onChange={(e) => setPhoneNumber(e.target.value)}
          ></input>
        </div>
      </div>
      <div className="m-4" id="eca-role-sec">
        <label className={label}>Role</label>
        <div id="eca-role-input">
          <select
            id="eca-sel-input"
            className={input}
            value={clientDetail.role}
            onChange={(e) => setRole(e.target.value)}
          >
            <option id="sel-role-eca">Select Role</option>
            {roleList.map((role) => (
              <option id={role.id} key={role.id} value={clientDetail.role}>
                {role.name}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div id="ecabtn" className="buttons">
        <button
          id="dismiss-ecabtn"
          className={`${btn} m-4`}
          data-dismiss="modal"
        >
          Cancel
        </button>
        <button
          className={`${btn2} text-light float-right`}
          id="upd-clabtn"
          type="submit"
          data-dismiss="modal"
          onClick={() => updateClientAdmin(clientDetail.id)}
        >
          Update
        </button>
      </div>
    </Modal>
  );
}
