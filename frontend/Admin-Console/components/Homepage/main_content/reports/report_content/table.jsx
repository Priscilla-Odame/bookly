import axios from "axios";
import Link from 'next/link';
// import React, { useState,  } from 'react';
import { useState, useEffect, useContext } from "react";
import { API_BASE_URL, API_PORT } from "../../../../../config";
import styles from "../../../../../styles/Homepage/MainContent/reports/table.module.css";
// import { Store } from "../../../../../contextStore";import "bootstrap/dist/css/bootstrap.min.css";

export default function ReportList() {
  //Define styles
  const { Table } = styles;

  //Enpoints and urls
  const dummy_endpoint = "http://localhost:7000/report_endpoint";
  const report_endpoint = "api/report";
  const list_reports_url = `${API_BASE_URL}:${API_PORT}/${report_endpoint}`;

  //  State objects
  const [reports, setReports] = useState([]);
  const [tokens, setToken] = useState([]);
  const [email, setEmail] = useState("");
  const access = useState("");
  const accesToken = useState(tokens.access);

//   const { state } = useContext(Store);
//   console.log("state", state);

  //useEffect function to get userdetails token and other data

  useEffect(async () => {
    const userdata = await localStorage.getItem("user");
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
    // var axios = require('axios');
    // // var data = '\r\n';

    // var config = {
    // method: 'get',
    // url: 'http://localhost:8000/api/project',
    // headers: {
    //     'Authorization': `Bearer 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2NDE1NjE3LCJqdGkiOiI3MmUzYjdjNTNmMmE0OWFjOGZlMTk0ZjFkMmQ2ZjMxOCIsInVzZXJfaWQiOjJ9.xLWEz6gS2c_Vzap69H79jRFogIncdWNT6FFuwjXeRnA'`,
    //     'Content-Type': 'application/json'
    // }, 
    // // data : data
    // };

    // await axios(config)
    //     .then(function (response) {
    //     console.log(JSON.stringify(response));
    //     setReports(response);
    //     })
    //     .catch(function (error) {
    //     console.log(error);
    //     });

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
          console.log("unread reports fetched successfully");
          console.log(response.data);
          setReports(response.data);
          localStorage.setItem("report list", JSON.stringify(response));
          // window.alert('unread reports fetched successfully')
        } else if (response.status == 401) {
          console.log(response.data);
        }
      })
      .catch(err => {
        console.log("An occured while loading the report list", err);
        // window.alert('Authentication credentials were not provided, your session must have expired. Kindly login again')
      });
    // setReports(response.data)
  };

  //Header function for report list

  const renderHeader = () => {
    let headerElement = [
      "Report ID",
      "Project",
      "Report Name",
      "Description",
      "Published On",
      "Last Modified"
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
          {reports.map((reports, index) => {
            return (
              <tr key={index}>
                <td>{reports.id}</td>
                <td><Link href={reports.project}>{reports.project}</Link> </td>
                <td>{reports.name}</td>
                <td>{reports.description}</td>
                <td>{reports.published_at}</td>
                <td>{reports.last_modified}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </>
  );
}
