import Prompt from "../../../../../Layout/Prompt";
import React, { useState } from "react";
import styles from "../../../../../../styles/dashboard/AdminPanel/Modal/prompt.module.css";

export default function DeleteContactDetail({
  contactDetail,
  setDeleted,
  contactPerson,
}) {
  const { dismissbtn, btn, container, } = styles;

  const deleteContactPerson = async (id) => {
    const reqOptions = {
      method: "DELETE",
    };

    await fetch(
      `https://be01.pitest.xyz/api/organizations/staff-members/${id}`,
      reqOptions
    )
      .then((resp) => resp.json())
      .then((res) => {
        if (res) {
          contactPerson.splice(
            contactPerson.findIndex((contact) => contact.id === id),
            1
          );
          setDeleted(true);
        } else {
        }
      })
      .catch((err) => console.log("error", err));
  };

  return (
    <Prompt id="delete-contact-detail" title="Delete Contact Person">
      <div className={container}>
        <div>
          Are you sure you want to permanently delete {contactDetail.name} ?
        </div>
        <div className="mt-5">
          <button
            className={btn}
            data-dismiss="modal"
            onClick={() => deleteContactPerson(contactDetail.id)}
          >
            Delete
          </button>
          <button className={`${dismissbtn} float-right`} data-dismiss="modal">
            Dismiss
          </button>
        </div>
      </div>
    </Prompt>
  );
}
