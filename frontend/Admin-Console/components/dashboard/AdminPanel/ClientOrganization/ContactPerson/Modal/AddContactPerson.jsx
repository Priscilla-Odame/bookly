import Modal from "../../../../../Layout/Modal";
import styles from "../../../../../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";
import { useEffect, useState } from "react";
import { API_PORT_HOSTED, ORGANIZATIONS } from "../../../../../../config";

export default function AddContactPersonModal({ setAdded, orgkey, contactDetail }) {
  const { label, input, btn, btn2 } = styles;
  const [fullName, setFullName] = useState("");
  const [phone, setPhone] = useState();
  const [role, setRole] = useState(contactDetail.role);
  const [access, setAccess] = useState("");
  const [roleList, setRoleList] = useState([]);
  // const [contactList, setContactList] = useState([]);

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
    // fetch(`${API_PORT_HOSTED}/${ORGANIZATIONS}/staff-members/`, requestOptions)
    //   .then((resp) => resp.json())
    //   .then((res) => setContactList(res))
    //   .catch((err) => console.log(err));

    fetch(`${API_PORT_HOSTED}/${ORGANIZATIONS}/contact-role/`, requestOptions)
      .then((resp) => resp.json())
      .then((res) => setRoleList(res))
      .catch((err) => console.log(err));
  }, []);

  const addContactPerson = (e) => {
    e.preventDefault();

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    myHeaders.append(`Bearer ${access}`);

    const raw = JSON.stringify({
      name: fullName,
      phone_number: phone,
      role: role,
      organization: `${API_PORT_HOSTED}/${ORGANIZATIONS}/organization/${orgkey}/`,
      status: "Activated",
    });

    const reqOptions = {
      method: "POST",
      headers: myHeaders,
      body: raw,
    };

    fetch(`${API_PORT_HOSTED}/${ORGANIZATIONS}/staff-members/`, reqOptions)
      .then((resp) => resp.json())
      .then((res) => {
        setContactList, setAdded(true);
      });
  };

  return (
    <Modal id="add-contact-person" title="Add Contact Person">
      <div>
        <form onSubmit={addContactPerson} id="add-contact-person-form">
          <div className="m-4">
            <label className={label}>Name</label>
            <div>
              <select
                className={input}
                id="select-contact-name"
                value={fullName}
                onChange={(e) => setFullName(e.target.value)}
              >
                <option>Select Name</option>
                {/* {contactList.map((contact) => ( */}
                  <option key={contactDetail.id} value={contactDetail.id}>
                    {contactDetail.firstname} {contactDetail.lastname}
                  </option>
                {/* ))} */}
              </select>
            </div>
          </div>

          <div className="m-4">
            <label className={label}>Phone Number</label>
            <div>
              <input
                className={input}
                id="contact-phone"
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
                id="select-contact-role"
                value={role}
                onChange={(e) => setRole(e.target.value)}
              >
                <option>Select Role</option>
                {roleList.map((role) => (
                  <option key={role.id} value={role.id}>{role.name}</option>
                ))}
              </select>
            </div>
          </div>
          <div className="m-4">
            <button className={`${btn2} text-light`} type="submit" id="modal-form-submit">
              Submit
            </button>
          </div>
        </form>
      </div>
    </Modal>
  );
}
