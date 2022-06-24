import {
  API_BASE_URL,
  API_MANAGEMENT_CONSOLE,
  API_PORT, API_PORT_HOSTED,
  ORGANIZATIONS,
} from '../../../config';

import axios from 'axios';
import {useState, useEffect} from 'react';
import OrganizationsTable from './ClientOrganizationList/Table';
import Pagination from './ClientOrganizationList/Pagination';

import Admin from '../../Layout/Admin';
import Navigation from '../navigation';
import styles from '../../../styles/dashboard/AdminPanel/adminpanel.module.css';
import AddClientOrganization from './AddClientOrganization/AddClientOrganization';


export default function AdminPanel() {

  //Enpoints and urls
  const clientlist = "api/...";
  const clientlisturl = `${API_BASE_URL}:${API_PORT}/${clientlist}`;
  const client_ID = "id";

  //Define styles
  const {
    dashboard,
    Heading,
    addclient_btn,
    clientTable } = styles;

    //state objects
    const [organizations, setOrganizations] = useState([]);
    const [currentPage, setcurrentPage] = useState(1);
    const [organizationsPerPage, setOrganizationsPerPage] = useState(5);


    useEffect(() => {
        const fetchData = async ()=>{
            const response = await axios.get('https://be01.pitest.xyz/api/organizations/organization/', 
            {headers:{
              'Content-Type': 'application/json',
              'Accept': 'application/json',
              // 'Authorization': `Bearer ${access}`
          }
          }).then(response => {
            if (response.status==200){
                console.log("Client organization data fetched successfully", response)
                localStorage.setItem('Client-Organization-list', response)
                setOrganizations(response.data)
            }
            else{
                console.log(response.data)
            }
        }).catch(err=>{
          console.log("There seems to be an issue fetching data", err)

        });
      }
        fetchData();
    }, []);


    // change Page
    const paginate = pageNumber => setcurrentPage(pageNumber)

    //current post
    const indexOfLastOrganization = currentPage * organizationsPerPage;
    const indexOfFirstOrganization = indexOfLastOrganization - organizationsPerPage;
    const currentOrganizations = organizations.slice(indexOfFirstOrganization, indexOfLastOrganization);


  return (
    <Admin title="Push Insights :: Admin Panel">
      <div className={dashboard}>
        <div>
          <Navigation />
        </div>
      </div>
      <div className={Heading} id="adminpanel-heading">
        <h2 style={{fontWeight: "600", fontSize:"64px", lineHeight:"75.07px"}}>Client Organizations</h2>
      </div>
      <div>
        <button
          className={addclient_btn}
          id="add-client-btn"
          type="button"
          data-toggle="modal"
          data-target="#admin-add-client-organization"
        >
          Add Client
        </button>
      </div>
        <AddClientOrganization/>
      <div>

      </div>
      <div className={clientTable}  id="client-organization-table">
        <OrganizationsTable organizations={currentOrganizations}/>
        <Pagination organizationsPerPage={organizationsPerPage} totalOrganizations={organizations.length} paginate={paginate}/>

      </div>
    </Admin>
  );
}
