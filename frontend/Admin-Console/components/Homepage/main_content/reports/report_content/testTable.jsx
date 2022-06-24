// DEBUG=TRUE

import axios from "axios";
import Link from 'next/link'
import { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { API_BASE_URL, API_PORT } from "../../../../../config";
import styles from "../../../../../styles/Homepage/MainContent/reports/table.module.css";

export default function TestList() {
  //Define styles
  const { Table } = styles;

  //Enpoints and urls
  const dummy_endpoint = "http://localhost:7000/survey_endpoint";
  const Report_endpoint = "api/report";
  const list_reports_url = `${API_BASE_URL}:${API_PORT}/${Report_endpoint}`;

  //  State objects
  const [surveys, setSurveys] = useState([]);
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
  const getTable = async (data = { surveys, setSurveys }) => {
    const userdata = localStorage.getItem("user");
    await axios.get(dummy_endpoint, {
        headers: {
          "Content-Type": "application/json",
          "Application": "application/json",
          surveys: data.surveys,
          setSurveys: data.setSurveys
        }
      })
      .then(response => {
        // On successful load of pending reports
        if (response.status == 200) {
          console.log(response.data);
          setSurveys(response.data);
          localStorage.setItem("report list", JSON.stringify(response));
          window.alert(" List generated  successfully");
        } else if (response.status == 401) {
          console.log(response);
        }
      })
      .catch(err => {
        console.log("An occured while generating the list", err);
        window.alert(
          "Authentication credentials were not provided, your session must have expired. Kindly login again"
        );
      });
    // setSurveys(response.data)
  };

  //Header function for report list

  const renderHeader = () => {
    let headerElement = [
      "Survey ID",
      "Survey Name",
      "Description",
      "Project",
      "Completion Status",
      "Completion Deadline"
    ];

    return headerElement.map((key, index) => {
      return <th key={index}>{key.toUpperCase()}</th>;
    });
  };

  return (
    <div>
      <table className={Table}>
        <thead>
          <tr>{renderHeader()}</tr>
        </thead>
        <tbody>
          {surveys.map((surveys, index) => {
            return (
              <tr key={index}>
                <td>{surveys.id}</td>
                <td>{surveys.name} </td>
                <td>{surveys.description}</td>
                <td><Link href={surveys.project}>{surveys.project}</Link></td>
                <td>{surveys.completion_status}</td>
                <td>{surveys.completion_deadline}</td>
              </tr>
            );
          })}
          {/* : <tr><td colSpan="5">Loading...</td></tr>}     */}
        </tbody>
      </table>
    </div>
  );
}
