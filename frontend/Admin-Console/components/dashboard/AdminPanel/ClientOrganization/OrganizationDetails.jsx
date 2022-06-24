import axios from "axios";
import Head from "next/head";
import { useState, useEffect } from "react";
import styles from "../../../../styles/dashboard/AdminPanel/ClientDetails.module.css";
import { MdDelete, MdModeEdit } from "react-icons/md";
import { API_PORT_HOSTED, API_PORT, ORGANIZATIONS, } from "../../../../config";
import EditOrganization from "./Modal/EditOrganization";
import DeleteOrganization from "./Modal/DeleteOrganization";


export default function ClientDetails({orgId}) {

    //Css Classnames
    const {
            container, logo, details, action, edit_button, delete_button, data,
    } = styles

    // State Objects
    const [organization, setOrganization] = useState([]);
    const [access, setAccess] = useState("");

    useEffect(() => {
      const user = window.localStorage.getItem("access-token");
      console.log("access-token", user);
      setAccess(user);
    }, []);

    //Endpoints and URLs

    const endpoint_organization = `organization/${orgId}`;
    const url = `${API_PORT_HOSTED}/${ORGANIZATIONS}/${endpoint_organization}`;

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
            console.log("There seems to be an issue fetching data", err)
            // window.alert("Could not load the client organization data. Please try again later")
        })
    }
  
    //callback function
    useEffect(() => {
        fetchOrganizationData()
    }, [])


    return(
        <div>
            <Head>
                <link
            rel="preload"
            href="/fonts/Work_Sans/static/WorkSans-Regular.ttf"
            as="Font"
            crossOrigin=""
            />

            </Head>
            <body onLoad = {fetchOrganizationData}>
                <div className={container}>
                    <div className={details}>
                        <div className={logo}>
                            <b>{organization.logo}</b>
                        </div>

                        <div className={data}>
                            <b>{organization.name}</b>
                            <p> {organization.updated_at} </p>
                            <p> {organization.description} </p>
                        </div>

                    </div>
                    <div className={action}>
                        <span className={edit_button} id="orgEdit_button">
                            <MdModeEdit 
                            data-toggle="modal"
                            data-target="#edit-organization" />
                        </span>                    
                        <span className={delete_button} id="orgDelete_button">
                            <MdDelete 
                            data-toggle="modal"
                            data-target="#delete-organization"
                            orgId= {orgId}/>
                        </span>
                        
                    </div>
                </div>
                <DeleteOrganization orgId={orgId} />
                <EditOrganization orgId={orgId} /> 

            </body>
        </div>
    )
    
}