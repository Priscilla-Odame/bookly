import { useState, useEffect } from "react";
import styles from "../../../../styles/Homepage/MainContent/reports/table.module.css";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { API_BASE_URL, API_PORT } from "../../../../config";

export default function InvitesList() {
    
  //Define styles

  const { Table } = styles;

  //Enpoints and urls
  const dummy_endpoint = "http://localhost:7000/projinvites_endpoint";
  const projinvites_endpoint = "projects/api/pending_invites";
  const list_invites_url = `${API_BASE_URL}:${API_PORT}/${projinvites_endpoint}`;

  //  State objects

  const [invites, setInvites] = useState([]);
  const [tokens, setToken] = useState([]);
  const [email, setEmail] = useState("");
  const access = useState("");
  const accesToken = useState(tokens.access);

  //useEffect function to get userdetails token and other data
  useEffect(() => {
    const userdata = localStorage.getItem("user");
    if (userdata) {
      const foundUser = JSON.parse(userdata);
      setEmail(foundUser.email);
      setToken(foundUser.tokens);
      console.log("Email for user is:", email);
      console.log("access token for the user is: ", tokens.access);
      getTable(tokens);
    } else {
      console.log("User token could not be fetched");
    }
  }, []);

  //function to fetch reports
  const getTable = async () => {
    const userdata = localStorage.getItem("user");
    await axios
      .get(dummy_endpoint, {
        headers: {
          "Content-Type": "application/json",
          // 'Application': 'application/json',
          Authorization: `Bearer ${tokens.access}`
        }
      })
      .then(response => {
        // On successful load of pending reports
        if (response.status == 200) {
          console.log(response.data);
          setInvites(response.data);
          localStorage.setItem("report list", JSON.stringify(response));
          window.alert("Pending project invites fetched successfully");
        } else if (response.status == 401) {
          console.log(response);
        }
      })
      .catch(err => {
        console.log("An occured while loading the project invite list", err);
        window.alert(
          "Authentication credentials were not provided, your session must have expired. Kindly login again"
        );
      });
    // setInvites(response.data)
  };

  //Header function for report list

  const renderHeader = () => {
    let headerElement = [
      "Invites ID",
      "Project Name",
      "Description",
      "Date of Invite",
      "Status"
    ];

    return headerElement.map((key, index) => {
      return <th key={index}>{key.toUpperCase()}</th>;
    });
  };

  return (
    <>
      <table className={Table}>
        <thead>
          <tr>{renderHeader()}</tr>
        </thead>
        <tbody>
          {invites.map((invites, index) => {
            return (
              <tr key={index}>
                <td>{invites.id}</td>
                <td>{invites.name} </td>
                <td>{invites.description}</td>
                <td>{invites.invited_at}</td>
                <td>{invites.status}</td>
              </tr>
            );
          })}
          {/* : <tr><td colSpan="5">Loading...</td></tr>}     */}
        </tbody>
      </table>
    </>
  );
}
