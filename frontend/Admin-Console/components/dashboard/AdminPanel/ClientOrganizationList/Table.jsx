import Head from 'next/head';
import Link from "next/link";
import {FaCartPlus} from "react-icons/fa"

import { useState, useEffect } from "react";
import {Dropdown, Toggle, Menu} from 'react-bootstrap'
import { API_BASE_URL, API_PORT, API_PORT_HOSTED, ORGANIZATIONS } from "../../../../config";
import styles from "../../../../styles/dashboard/AdminPanel/clientorganizationlist.module.css";


const OrganizationsTable =({organizations})=>{

    //Define styles
    const { search, searchbar, Table, dropdownLink, dropdownDel, dropdownMenu } = styles;

    //State objects
    const [searchInput, setSearchInput] = useState("");

    // Search funtion to update to update state changes
    const handleSearchChange = (e) => {
        const value = e.target.value || undefined;
        setSearchInput(value);
    };

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
    
    //Table header/heading
    const renderTableHeading = () => {
        var headingElement = ["Client Name", "Created By", "Date", "More"];

        return headingElement.map((key, index) => {
        return <th key={index}>{key.toUpperCase()}</th>;
        });
    };
    
    return(
        
        <div>
            <Head>
            </Head>
            <div className={searchbar}>
                <input
                    type="text"
                    placeholder= "&#128269; search"
                    className={search}
                    id="search-table-input"
                    value={searchInput}
                    onChange={handleSearchChange}
                />
            </div>

            <table className={Table} id="client-organization-list">
                <thead>
                    <tr>{renderTableHeading()}</tr>
                </thead>
                <tbody>
                {organizations.map((organizations) => {
                    return (
                    <tr key={organizations.id}>
                        <td>{organizations.name} </td>
                        <td>{organizations.updated_by}</td>
                        <td>{organizations.updated_at}</td>
                        <td>
                        <div>
                            <Dropdown className={dropdownMenu} role="menuitem" id="options-drop-down">
                                <Dropdown.Toggle className={dropdownMenu} id="options-drop-down-toggle">
                                    . . .
                                </Dropdown.Toggle>

                                <Dropdown.Menu id="options-drop-down-menu">
                                    <Dropdown.Item id="options-drop-down-item">
                                        <Link
                                            className={dropdownLink}
                                            id="client-organization-instance-option"
                                            href={`/dashboard/adminpanel/clientOrganization/${encodeURIComponent(organizations.id)}`}>
                                                View
                                        </Link>
                                    </Dropdown.Item>
                                    <Dropdown.Item id="options-drop-down-item">
                                        <button
                                            className={dropdownDel}
                                            id="del-client-organization-instance-option"
                                            onClick={remOrganization}
                                        > Delete </button>
                                    </Dropdown.Item>
                                </Dropdown.Menu>
                            </Dropdown>
                        </div>
                        </td>
                    </tr>
                    );
                })}
                </tbody>
            </table>

        </div>
    )
}

export default OrganizationsTable;