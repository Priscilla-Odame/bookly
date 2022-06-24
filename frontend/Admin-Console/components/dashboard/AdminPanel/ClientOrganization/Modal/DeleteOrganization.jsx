import Prompt from "../../../../Layout/Prompt"
import React, { useState, useEffect } from "react"
import styles from "../../../../../styles/dashboard/AdminPanel/Modal/prompt.module.css"
import { API_PORT_HOSTED, ORGANIZATIONS, } from "../../../../../config"
import axios from "axios"


export default function DeleteOrganization({orgId}) {
  const { dismissbtn, btn, container } = styles


  //Endpoints and URLs
  const endpoint_organization = `organization/${orgId}`;
  const url = `${API_PORT_HOSTED}/${ORGANIZATIONS}/${endpoint_organization}`

  // State Object
  const [access, setAccess] = useState("");

  useEffect(() => {
    const user = window.localStorage.getItem("access-token");
    console.log("access-token", user);
    setAccess(user);
  }, []);


  const deleteOrganization = () => {
    const deleteEndpoint = "delete"

    axios
      .delete(`${url}`, {
        headers: {
          "Content-Type": "application/json",
          // Authorization: `Bearer ${access}`
        }
      })
      .then(res => {
        if (res == 202 || 200 || 204) {

          console.log ("Organization deleted successfully")
          
        } else {
          console.log(resp.data)
        }
      }).catch(err=>{
        console.log("There seems to be an issue deleting data", err)
        
        // window.alert("You are Unauthorized to delete an Organization")
    })
    
  }

  return (
    <Prompt id="delete-organization" title="Delete Organization">
      <div className={container}>
        <div>
          <b>Are you sure you want to permanently delete this organization ?</b>
        </div>

        <div className="mt-5">
          <button
            className={btn}
            data-dismiss="modal"
            id="delete_button"
            onClick={() => deleteOrganization()}
          >
            Delete
          </button>
          <button className={`${dismissbtn} float-right`} id="dismiss_button" data-dismiss="modal">
            Dismiss
          </button>
        </div>
      </div>

    </Prompt>
  );
}
