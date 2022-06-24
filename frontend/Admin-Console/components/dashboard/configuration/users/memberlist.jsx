import React from "react";
import axios from "axios";
import Head from "next/head";
import { MdDelete } from "react-icons/md";
import "bootstrap/dist/css/bootstrap.min.css";
// import {members} from '../../../../data/db.json'
import { useForm, useState, useEffect } from "react";
import { API_BASE_URL, API_PORT } from "../../../../config";
// import {ListGroup, ListGroupItem, Button } from 'reactstrap';
import styles from "../../../../styles/dashboard/settings.module.css";

export default function MemberList() {
  //Define styles
  const { Addbutton, MemberList, opration } = styles;

  //Enpoints and urls

  const list_projectmembers_endpoint = "api/project/members";
  const list_projectmembers_url = `${API_BASE_URL}:${API_PORT}/${list_projectmembers_endpoint}`;

  const accessproject_by_id_endpoint = "api/project/member";
  const accesproject_by_id_url = `${API_BASE_URL}:${API_PORT}/${accessproject_by_id_endpoint}`;

  // const URL = 'http://localhost:7000/members'

  // List Project Code
  const [members, setmembers] = useState([]);

  //function to fetch projects
  const getData = async (data = { members, setmembers }) => {
    const userdata = JSON.parse(localStorage.getItem("user"));
    const response = await axios
      .get(list_projectmembers_url, {
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${userdata.access_token}`
        }
      })
      .then(response => {
        // On successful addition of Project

        if (response.status == 200) {
          console.log(response);
          window.alert("Members on projects fetched successfully");
          localStorage.setItem("member list", JSON.stringify(response.data));
        } else {
          console.log(response);
        }
      })
      .catch(err => {
        console.log("Could not fetch members on projects", err);
        window.alert(
          "Could not fetch members on projects, Please check your network connection"
        );
      });
    setmembers(response);
  };

  //call back function for fetch members on projects
  useEffect(() => {
    getData();
  }, []);

  //function to delete projects
  const removeData = id => {
    const update_endpoint = "members/update";

    axios
      .delete(`${accesproject_by_id_url}/${id}/${update_endpoint}`)
      .then(response => {
        const del = members.filter(member => id !== member.id);
        setmembers(del);
      });
  };

  //function to bind fetch project members to table elements
  const renderHeader = () => {
    let headerElement = ["Id", "Firstname", "Othernames", "Email", "Role"];

    return headerElement.map((key, index) => {
      return <th key={index}>{key.toUpperCase()}</th>;
    });
  };

  const renderBody = () => {
    return (
      members &&
      members.map(({ id, firstname, othernames, email, role }) => {
        return (
          <tr key={id}>
            <td>{id}</td>
            <td>{firstname}</td>
            <td>{othernames}</td>
            <td>{email}</td>
            <td>{role}</td>
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
      <table className={MemberList}>
        <thead>
          <tr>{renderHeader()}</tr>
        </thead>
        <tbody>{renderBody()}</tbody>
      </table>
    </>
  );
}
