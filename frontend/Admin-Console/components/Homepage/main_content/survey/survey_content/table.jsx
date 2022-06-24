import { useState, useEffect } from "react";
import styles from "../../../../../styles/Homepage/MainContent/reports/table.module.css";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import { API_BASE_URL, API_PORT } from "../../../../../config";

export default function SurveyList() {
  //Define styles
  const { Table } = styles;

  //Enpoints and urls
  const dummy_endpoint = "http://localhost:7000/surveys";
  const survey_endpoint = "surveys/project/all";
  const list_survey_url = `${API_BASE_URL}:${API_PORT}/${survey_endpoint}`;

  //  State objects
  const [surveys, setSurveys] = useState([]);
  const [tokens, setToken] = useState([]);
  const [email, setEmail] = useState("");
  const access = useState("");
  const accesToken = useState(access);

  //useEffect function to get userdetails token and other data
  useEffect(() => {
    const userdata = localStorage.getItem("user");
    if (userdata) {
      const foundUser = JSON.parse(userdata);
      setEmail(foundUser.email);
      setToken(foundUser.tokens);
      console.log("Email for user is:", email);
      console.log("access token for the user is: ", tokens.access);
      getTable(tokens.access);
    } else {
      console.log("User token could not be fetched");
    }
  }, []);

  //function to fetch surveys
  const getTable = async () => {
    await axios
      .get(list_survey_url, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${tokens.access}`
        }
      })
      .then(response => {
        // On successful load of pending surveys
        if (response.status == 200) {
          console.log(response.data);
          setSurveys(response.data);
          localStorage.setItem("survey list", JSON.stringify(response));
          window.alert("Pending surveys fetched successfully");
        } else if (response.status == 401) {
          console.log(response.data);
        }
      })
      .catch(err => {
        console.log("An occured while loading the surveys list", err);
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

  //mapping report details to table

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
                <td>{surveys.project}</td>
                <td>{surveys.completion_status}</td>
                <td>{surveys.completion_deadline}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
