import axios from "axios";
import { useState, useEffect } from "react";
import Link from "next/link";
// import 'bootstrap/dist/css/bootstrap.min.css';
import { API_BASE_URL, API_PORT, API_PORT_HOSTED, ORGANIZATIONS } from '../../../../config';
import styles from "../../../../styles/dashboard/AdminPanel/clientorganizationlist.module.css";

export default function ClientList() {
  //Define styles
  const { search, searchbar, Table, btnMore, dropdownMenu } = styles;

  //Enpoints and urls
  const clientlist = "api/...";
  const clientlisturl = `${API_BASE_URL}:${API_PORT}/${clientlist}`;
  const client_ID = "id";

  //  State objects
  const [organizations, setOrganizations] = useState([]);
  const [tokens, setToken] = useState([]);
  const [email, setEmail] = useState("");

  // const access = useState("");
  const [access, setAccess] = useState("");
  const [searchInput, setSearchInput] = useState("");

  // Search funtion to update to update state changes
  const handleSearchChange = (e) => {
    const value = e.target.value || undefined;
    setSearchInput(value);
  };

  const api = API_PORT_HOSTED

  // useEffect(()=>{
  //   const access = window.localStorage.getItem("access");
  //   setAccess(access);
  // })

    //Fetch client list
    const fetchClient = ( data = {organizations, setOrganizations}) =>{
      axios.get(`${api}/${ORGANIZATIONS}/organization`, {headers:{
          'Content-Type': 'application/json',
          'Accept': 'application/json',
          // 'Authorization': `Bearer ${access}`
      }
      }).then(response => {
          if (response.status==200){
              console.log("Cleint organization data fetched successfully", response.data)
              window.alert("Client Organization list fetched successfully")
              localStorage.setItem('Client-Organization-list', response.data)
              setOrganizations(response.data)
          }
          else{
              console.log(response.data)
          }
      }).catch(err=>{
          console.log("There seems to be an issue fetching data", err)
          window.alert("Could not load the client organization list. Please try again later")
      })

  };

  //callback function
  useEffect(() => {
      fetchClient()
  }, [])



const [id, setOrganizationID] = useState("") ;

useEffect(()=>{
  const clientOrganizationList = localStorage.getItem('Client-Organization-list')

  if (clientOrganizationList) {
    setOrganizationID(clientOrganizationList.id);
    console.log("organization found");
  } else {
    console.log("organization details not fetched")
  }
}, [])




async function remOrganization (id){

    await axios.delete(`${API_PORT_HOSTED}/${ORGANIZATIONS}/organization/${id}`, {
        headers: {
          "Content-Type": "application/json",
          // "Authorization": `Bearer ${access}`
        }}
      )
      .then((response) => {
        const newClients = clients.filter((clients) => clients.id !== id);
        setClients(newClients);
        if (response.status == 200) {
          console.log(response.data);
          setClients(response.data);
          localStorage.setItem("client list", JSON.stringify(response.data));
          window.alert("Deleted successfully");
        } else if (response.status == 503) {
          console.log(response);
        }
      })
      .catch((err) => {
        console.log(
          "Could not delete the list item. Kindly try again later.",
          err
        );
        window.alert("Could not delete a list item. Kindly try again later.");
      });
  }

  //Render table header/heading
  const renderTableHeading = () => {
    var headingElement = ["Client Name", "Created By", "Date", "More"];

    return headingElement.map((key, index) => {
      return <th key={index}>{key.toUpperCase()}</th>;
    });
  };

  return (
    <div>
        
      <div className={searchbar} >
        <input
          type="text"
          placeholder=" 🔍search"
          className={search}
          id="search-clients"
          value={searchInput}
          onChange={handleSearchChange}
        />
      </div>
      <table className={Table} id="client-organizaton-list">
        <thead>
          <tr>{renderTableHeading()}</tr>
        </thead>
        <tbody>
          {organizations.map((organizations, id) => {
            return (
              <tr key={organizations.id}>
                {/* <td>{clients.id}</td> */}
                <td>{organizations.name} </td>
                <td>{organizations.updated_by}</td>
                <td>{organizations.updated_at}</td>
                <td>
                  <div>
                    <ul className={dropdownMenu} role="menu" id="more-dropdown">
                      <Link
                        id="view-organization-link"
                        href="/dashboard/adminpanel/clientOrganization/[id]" as={`/dashboard/adminpanel/clientOrganization/${organizations.id}`}
                      ><a>
                        View
                        </a>
                      </Link>
                      <button
                        className={btnMore}
                        id="delete-btn"
                        onClick={remOrganization}
                      >
                        Delete
                      </button>
                    </ul>
                  </div>
                </td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
