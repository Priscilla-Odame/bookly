import axios from "axios";
import { MdDelete } from "react-icons/md";
import { useState, useEffect } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import { API_BASE_URL, API_PORT } from "../../../../config";
import styles from "../../../../styles/dashboard/settings.module.css";

export default function ProjectList() {
  //Css Style ClassNames
  const { Addbutton, projectTable, opration } = styles;

  //Enpoints and urls

  const list_projects_endpoint = "api/projects";
  const list_projects_url = `${API_BASE_URL}:${API_PORT}/${list_projects_endpoint}`;

  const accessproject_by_id_endpoint = "api/project";
  const accesproject_by_id_url = `${API_BASE_URL}:${API_PORT}/${accessproject_by_id_endpoint}`;

  //  State objects

  const [tokens, setToken] = useState("");
  const [email, setEmail] = useState([]);

  const [projects, setProjects] = useState([]);

  //check user auth

  useEffect(() => {
    const userdata = localStorage.getItem("user");

    if (userdata) {
      const foundUser = JSON.parse(userdata);
      setEmail(foundUser.email);
      setToken(foundUser.access_token);
      console.log("User is authenticated to view projects");

      getData();
    }
  }, []);

  //function to fetch projects
  const getData = async () => {
    const userdata = JSON.parse(localStorage.getItem("user"));
    const response = await axios.get(list_projects_url, {
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${userdata.access_token}`
      }
    });
    //.then(response =>{
    //     if (response.status == 200){
    //         console.log(response.data)
    //     }else{

    //     }
    // }).catch(err=>{
    //     console.log("error fetching data", err)
    //     window.alert("Projects could not be fetched at this time. Kindly check your internet, refresh the page or try again later")
    // })
    setProjects(response.data);
  };

  //function to remove project from list
  const removeData = id => {
    const userdata = JSON.parse(localStorage.getItem("user"));
    const deletendpoint = "delete";

    axios
      .delete(`${accesproject_by_id_url}/${id}/${deletendpoint}`, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${userdata.access_token}`
        }
      })
      .then(res => {
        const del = projects.filter(project => id !== project.id);
        setProjects(del);
      });
  };

  //Header function for project list

  const renderHeader = () => {
    let headerElement = ["Id", "Project_Name", "Description", "Status"];

    return headerElement.map((key, index) => {
      return <th key={index}>{key.toUpperCase()}</th>;
    });
  };

  //mapping project details to table

  const renderBody = () => {
    return (
      projects &&
      projects.map(({ id, name, description, status }) => {
        return (
          <tr key={id}>
            <td>{id}</td>
            <td>{name}</td>
            <td>{description}</td>
            <td>{status}</td>
            <td className={opration}>
              <MdDelete
                className={Addbutton}
                aria-label="Close modal"
                onClick={() => removeData(id)}
              />
            </td>
          </tr>
        );
      })
    );
  };

  return (
    <>
      <table className={projectTable}>
        <thead>
          <tr>{renderHeader()}</tr>
        </thead>
        <tbody>{renderBody()}</tbody>
      </table>
    </>
  );
}
