import Prompt from "../../../../../Layout/Prompt";
import React, { useState } from "react";
import styles from "../../../../../../styles/dashboard/AdminPanel/Modal/prompt.module.css";
import { API_PORT_HOSTED, ORGANIZATIONS } from "../../../../../../config";

export default function DeleteClientAdmin({
  clientDetail,
  setDeleted,
  clientAdminList,
  setClientAdminList,
}) {
  const { dismissbtn, btn, promptText } = styles;

  const deleteClientAdmin = async (id) => {
    const reqOptions = {
      method: "DELETE",
    };

    await fetch(
      `${API_PORT_HOSTED}/${ORGANIZATIONS}/administrator/${id}`,
      reqOptions
    )
      .then((resp) => resp.text())
      .then((res) => {
        if (res) {
          setDeleted(true);
          let removed = clientAdminList.filter((contact) => contact.id !== id);
          setClientAdminList([...removed]);
        }
      })
      .catch((err) => console.log("error", err));
  };

  return (
    <Prompt id="delete-client-admin" title="Delete Contact Person">
      <div id="dclad" className={promptText}>Are you sure you want to permanently delete {clientDetail.name} ?</div>
      <div className="m-5" id="dcabtn">
        <button
          id="delclad"
          className={btn}
          data-dismiss="modal"
          onClick={() => deleteClientAdmin(clientDetail.id)}
        >
          Delete
        </button>
        <button id="dissmiss-delcla" className={`${dismissbtn} float-right`} data-dismiss="modal">
          Dismiss
        </button>
      </div>
    </Prompt>
  );
}
