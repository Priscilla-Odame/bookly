import Modal from "../../../Layout/Modal";
import styles from "../../../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";
import { useEffect, useState } from "react";
import AddClientAdmin from "./AddClientAdmin";


export default function AddContactPersonModal({ setAdded, orgKey }) {
  const { label, input, btn, btn2 } = styles;
  const [email, setEmail] = useState("");
  const [fullName, setFullName] = useState("");
  const [phone, setPhone] = useState();
  const [role, setRole] = useState("");
  const [access, setAccess] = useState("");
  const [roleList, setRoleList] = useState([]);
  const [contactList, setContactList] = useState([]);

  useEffect(() => {
    const user = window.localStorage.getItem("access");
    console.log("access", user);
    setAccess(user);

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const requestOptions = {
      method: "GET",
      headers: myHeaders,
    };
    fetch(
      "https://be01.pitest.xyz/api/organizations/staff-members/",
      requestOptions
    )
      .then((resp) => resp.json())
      .then((res) => setContactList(res))
      .catch((err) => console.log(err));
  }, []);

  const getRoles = async () => {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    const requestOptions = {
      method: "GET",
      headers: myHeaders,
    };
    await fetch(
      "https://be01.pitest.xyz/api/organizations/contact-role/",
      requestOptions
    )
      .then((resp) => resp.json())
      .then((res) => setRoleList(res))
      .catch((err) => console.log(err));
  };
  getRoles();

  const addContactPerson = (e) => {
    e.preventDefault();
    try {
      const myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      myHeaders.append(`Bearer ${access}`);

      const raw = JSON.stringify({
        name: fullName,
        phone_number: phone,
        role: role,
        organization: `https://be01.pitest.xyz/api/organizations/contact/`,
        status: "Activated",
      });

      const reqOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
      };

      fetch(
        "https://be01.pitest.xyz:8000/api/organizations/staff-members/",
        reqOptions
      )
        .then((resp) => resp.text())
        .then((res) => {
          console.log(res), setAdded(true);
        });
    } catch (err) {
      alert("error from post", err);
    }
  };

  return (
    <div>
    <Modal id="admin-add-contact-person" title="Add Contact Person">
      <div>
        <form onSubmit={addContactPerson} id="admin-clt-ctc-form">
          <div className="m-4">
            <label className={label}>Name</label>
            <div>
              <select
                className={input}
                id="admin-clt-ctc-name"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
              >
                <option>Select Name</option>
                {contactList.map((contact) => (
                  <option value={contact.id}>
                    {contact.firstname} {contact.lastname}
                  </option>
                ))}
              </select>
            </div>
          </div>

          <div className="m-4">
            <label className={label}>Phone Number</label>
            <div>
              <input
                className={input}
                id="admin-clt-ctc-phone"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
              ></input>
            </div>
          </div>
          <div className="m-4">
            <label className={label}>Role</label>
            <div>
              <select
                className={input}
                id="admin-clt-ctc--role"
                value={role}
                onChange={(e) => setRole(e.target.value)}
              >
                <option>Select Role</option>
                {roleList.map((role) => (
                  <option value={role.id}>{role.name}</option>
                ))}
              </select>
            </div>
          </div>
          <div className="m-4">
          <button
                className={`${btn} text-light `}
                id="admin-clt-ctc-pbtn"
                type="button"
                data-toggle="modal"
                data-dismiss="modal"
                data-target="#admin-add-client-admin"
                >
                Previous
            </button>
            <button className={`${btn} text-light`}
            id="admin-clt-ctc-sbtn"
            type="submit"
            data-dismiss="modal"
            >
              Submit
            </button>
          </div>
        </form>
      </div>
    </Modal>
    {/* <AddClientAdmin/> */}
    </div>
  );
}
