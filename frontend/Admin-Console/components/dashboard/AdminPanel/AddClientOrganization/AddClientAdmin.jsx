import Modal from "../../../Layout/Modal";
import styles from "../../../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";
import { useState, useEffect } from "react";
import AddClientOrganization from './AddClientOrganization';
import AddContactPerson from './AddContactPerson';


export default function AddClientAdmin({ setAdded, orgKey }) {
  const { label, input, btn, btn2 } = styles;
  const [email, setEmail] = useState("");
  const [fullName, setFullName] = useState("");
  const [phone, setPhone] = useState("");
  const [role, setRole] = useState("");
  const [roleList, setRoleList] = useState([]);
  const [access, setAccess] = useState("");

  useEffect(() => {
    const user = window.localStorage.getItem("access");
    console.log("access", user);
    setAccess(user);
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

  const addClientAdmin = async () => {
    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append("Authorization", "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE3Mjg0NTQxLCJqdGkiOiIyZThhZTRmYTVlODY0ZjhlYTIyNmZjOTBkZmNhMjY2OSIsInVzZXJfaWQiOjJ9.KQLYSC4CFgQLpahbP-u80uRC5Vf_WKgIamSq3Cmk71U");
    const raw = JSON.stringify({
      name: fullName,
      email: email,
      phone_number: phone,
      role: "Admin",
      organization: `https://be01.pitest.xyz/api/organizations/administrator/`,
      status: "2260d2f8-ce59-484a-8da6-5460b8c731f6",
    });

    const reqOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
    };

    await fetch(
      `https://be01.pitest.xyz/api/organizations/administrator/`,
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
    <Modal id="admin-add-client-admin" title="Add Client Administrator">
      <div>
        <form id="admin-clt-gadmin-form">
          <div className="m-4">
            <label className={label}>Name</label>
            <div>
              <input
                className={input}
                id="admin-clt-gadmin-name"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
              ></input>
            </div>
          </div>
          <div className="m-4">
            <label className={label}>Email Address</label>
            <div>
              <input
                className={input}
                id="admin-clt-gadmin-email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
              ></input>
            </div>
          </div>
          <div className="m-4">
            <label className={label}>Phone Number</label>
            <div>
              <input
                className={input}
                id="admin-clt-gadmin-phone"
                value={phone}
                onChange={(e) => setPhone(e.target.value)}
              ></input>
            </div>
          </div>
          <div className="m-4">
            <label className={label}>Role</label>
            <div>
              <select 
                className={input} value={role} 
                id="admin-clt-gadmin-role"
                onChange={e => setRole(e.target.value)} 
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
                id="admin-clt-gadmin-mod-pbtn"
                type="button"
                data-toggle="modal"
                data-dismiss="modal"
                data-target="#admin-add-client-organization"
                >
                Previous
            </button>
            <button
              className={`${btn} text-light `}
              id="admin-clt-gadmin-mod-sbtn"
              type="submit"
              data-toggle="modal"
              data-dismiss="modal"
              data-target="#admin-add-contact-person"
              onClick={addClientAdmin}
            >
              Next
            </button>
          </div>
        </form>
      </div>
    </Modal>
    {/* <AddClientOrganization/> */}
    <AddContactPerson/>
    </div>
  );
}
