import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
// import styles from "../../../../styles/dashboard/AdminPanel/clientmodals.module.css";
import Modal from "../../../Layout/Modal";
import {
  API_BASE_URL,
  API_MANAGEMENT_CONSOLE,
  ORGANIZATIONS,
} from "../../../../config";
import styles from "../../../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";
import GlobalClientAdmin from "./AddGlobalClientAdmin";

export default function AddOrganizationForm() {
  const {
    textArea,
    label,
    input,
    btn,
    btn2,
  } = styles;


  
  return (
    <div>
      <Modal title="Add Organization" id="add-organization">
        <form>
          <div className="m-4">
            <label htmlFor="name" className={label}>
              Organization Name
            </label>
            {/* <br></br> */}
            <div>
              <input>
              </input>
            </div>
          </div>

          {/* <br></br> */}

          {/*Email*/}
          <div className="m-4">
            <label htmlFor="email" className={label}>
              Description
            </label>
            {/* <br></br> */}
            <div>
              <textarea
                rows="10"
                cols="50"
                type="text"
              >
              </textarea>
            </div>
          </div>

          <div className="buttons">
            <button className={`${btn} text-light m-4 text-capitalize`}>
              close
            </button>
            <button
              className={`${btn2} text-light float-right text-capitalize`}
              type="submit"
              value="submit"
              // data-dismiss="modal"
              data-target={"#add-global-client-admin"}>
              next
            </button>
          </div>
        </form>
      </Modal>
      <GlobalClientAdmin />
    </div>
  );
}
