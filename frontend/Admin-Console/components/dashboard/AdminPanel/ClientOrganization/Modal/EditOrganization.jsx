import React from "react";
import axios from "axios";
import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import Modal from "../../../../Layout/Modal";
import styles from "../../../../../styles/dashboard/AdminPanel/Modal/bootstrapmodal.module.css";
import { API_PORT_HOSTED, API_PORT, ORGANIZATIONS, } from "../../../../../config"

export default function EditOrganization( {orgId} ) {
  const [success, setSuccess] = useState(false);

  const {
    // modal,
    // close,
    // header,
    // content,
    // form,
    // input,
    //   actions,
    // button,
    textArea,
    label,
    input,
    btn,
    btn2,
    form_header,
    logo,
    upload,
    status,
    status_field,
  } = styles;

  //useform
  const {
    register,
    errors,
    watch,
    handleSubmit = async (e) => {
      {
        e.preventDefault;
      }
    },
  } = useForm();

  //---------------------check user auth-------------//

  // //state objects
  // const [tokens, setToken] = useState("");
  // const [description, setDescription] = useState([]);
  // const [orgName, setOrgName] = useState([]);

  // // Use effect
  // useEffect(() => {
  //   const userdata = localStorage.getItem("user");

  //   if (userdata) {
  //     const foundUser = JSON.parse(userdata);
  //     // setEmail(foundUser.email);
  //     setToken(foundUser.tokens);
  //     console.log("User is authenticated");
  //   }
  // }, []);

  // Endpoints and urls
  const endpoint_organization = `organization/${orgId}`
  const url = `${API_PORT_HOSTED}/${ORGANIZATIONS}/${endpoint_organization}`


  //Handle form data
  const onSubmit = (data = { orgName, description, status }) => {
    console.log("data is", data);
    axios
      .patch(
        url,
        {
          headers: {
            "Content-Type": "application/json",
            // Authorization: `Bearer ${access}`,
          },
        },
        {
          name: data.orgName,
          description: data.description,
          status:data.status
        }
      )
      .then((resp) => {
        //If Client organization is creation is successful
        if (resp.status == 200 || 201) {
          // window.location="login";
          setSuccess(true);
          // alert("Successfully updated client organization")
          console.log(resp.data);
          localStorage.setItem(
            "client_organization",
            JSON.stringify(resp.data)
          );
        } else {
          //if user credentials are inccorect and signup unsuccessful
          // window.location.href="dashboard/adminpanelup";
          console.log(resp.data)
        }
      })
      .catch((err) => {
        console.log(
          "An error occurred while adding  the client organization",
          err
        );
        // alert("An error occured, kindly check the form and try again later")
      });
    console.log(data)
  };

  // //watch errors in form fields
  // console.log(watch("organizationname", "organizationdescription"));
  // console.log(errors.organizationname, errors.organizationdescription);

 
    // State Objects
    const [organization, setOrganization] = useState([])
    const [access, setAccess] = useState("");
    const [description, setDescription] = useState([])
    const [orgName, setOrgName] = useState([])

    useEffect(() => {
      const user = window.localStorage.getItem("access-token")
      console.log("access-token", user)
      setAccess(user);
    }, []);
  
      
    //Fetching Client organization data
    async function fetchOrganizationData  (data = {organization, setOrganization}) {
        await axios.get( url, {headers:{
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            // 'Authorization': `Bearer ${access}`
        }
        
        }).then(resp => {
            if (resp.status==200){
                console.log("Organization fetched successfully", resp.data)
                localStorage.setItem('Client Organization data', resp.data)
                setOrganization(resp.data)
            }
            else{
                console.log(resp.data)
            }
        }).catch(err=>{
            console.log("There seems to be an issue fetching Org data", err)
            // window.alert("Could not load the client organization data. Please try again later")
        })
    }
  
    //callback function
    useEffect(() => {
        fetchOrganizationData()
    }, [])



  return (
    
    <div>
    <Modal  id="edit-organization">
      <form onSubmit={handleSubmit(onSubmit)}>
        <div className={form_header}>
          <div className={logo}>
            <b>{organization.logo}</b>
          </div>
          <div className={upload}>
            <b>{organization.name}</b>

          </div>
          <div className={status}>
            <select id="organizationstatus" 
              name="status"
              className={status_field}
              // ref={register({ required: true })}
            >
              <option value="Active">Active</option>
              <option value="Inactive">Inactive</option>

            </select>
          </div>

        </div>
        <div className="m-4">
          <label htmlFor="name" className={label}>
            Organization Name
          </label>
         
          <div>
            <input
              type="text"
              className={input}
              placeholder="Organization Name "
              name="organizationame"
              defaultValue={organization.name} onChange ={(e) => setOrgName(e.target.value)}
              id="organizationname"
              // ref={register({
              //   required: true,
              //   maxLength: 20,
              //   pattern: /^[A-Za-z]+$/i,
              //   message: "This field is required",
              // })}
            />
          </div>
        </div>

        <div className="m-4">
          <label htmlFor="email" className={label}>
            Description
          </label>
          <div>
            <textarea
              rows="5"
              cols="50"
              type="text"
              className={textArea}
              placeholder="Organization Description "
              defaultValue={organization.description} onChange ={(e) => setDescription(e.target.value)}
              name="organizationdescription"
              id="organizationdescription"
              // ref={register({
              //   required: true,
              //   minLength: 20,
              //   maxLength: 1500,
              //   message: "This field is required",
              // })}
            />
          </div>
        </div>

        <div className="buttons">
          <button className={`${btn}  m-4 text-capitalize`} id="cancel_button" data-dismiss="modal">
            Cancel
          </button>
          <button
            className={`${btn2} text-light float-right text-capitalize`}
            type="submit"
            value ="submit"
            id="update_button"
            
            >
            Update
          </button>
        </div>
      </form>
    </Modal>
    </div>
  );
}
