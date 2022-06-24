import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import isEmail from "validator/lib/isEmail";
import axios from "axios";
import { API_BASE_URL, API_PORT } from "../../../../config";
import "bootstrap/dist/css/bootstrap.min.css";
import styles from "../../../../styles/dashboard/configuration/usermanagement.module.css";
import Head from "next/head";
import { Form, FormGroup, Button } from "reactstrap";
import MemberList from "./memberlist";

export default function AddUser() {
  //handling user management, add user data
  const { register, handleSubmit, watch, errors } = useForm();

  //Define styles
  const {
    usermgmtinput,
    useradmin,
    usermember,
    projects,
    submitbutton,
    label,
    userlist
  } = styles;

  //api data fields for data submission/retrieval

  const project_id = "1";

  //define backend api endpoint and url
  const addproject_memeber_endpoint = "api/project/members/create";
  const addproject_member_url = `${API_BASE_URL}:${API_PORT}/${addproject_memeber_endpoint}`;

  // //companies object state
  // const [member, setMember] = useState([]);

  // //function to get list of companies from api

  // useEffect (() => {
  //     async function getCompanies() {
  //     const response = await axios.get(companies_url);
  //     // const body = await response.json();
  //     setCompany(response.data.map(({ name }) => ({ id: name, name: name })));
  //     }
  //     getCompanies();
  // }, []);

  // //project state objects

  // const [projects, setProjects] = useState([])

  // //function to fetch projects
  // const getData = async () => {
  //     const userdata = JSON.parse(localStorage.getItem("user"))
  //     const response = await axios.get(list_projects_url, {headers: {
  //         'Content-Type': 'application/json',
  //         'Authorization': `Bearer ${userdata.tokens.access}`
  //         }})
  //         //.then(response =>{
  //         //     if (response.status == 200){
  //         //         console.log(response.data)
  //         //     }else{

  //         //     }
  //         // }).catch(err=>{
  //         //     console.log("error fetching data", err)
  //         //     window.alert("Projects could not be fetched at this time. Kindly check your internet, refresh the page or try again later")
  //         // })
  //     setProjects(response.data)
  // }

  //function for submitting user addition data
  const onSubmit = data => {
    // {e.preventDefault}

    console.log("data is ", data);
    axios
      .post(addproject_member_url, {
        project_id,
        firstname: data.firstname,
        othernames: data.othernames,
        email: data.email,
        role: data.role
      })
      .then(resp => {
        // On successful addition of user

        if (resp.status == 201) {
          //store added user details

          localStorage.setItem("members", resp.data);
          console.log(resp.data);
          window.alert(
            "Project member/user added successfully, a confirmation mail has been sent to the user."
          );

          localStorage.setItem("members", JSON.stringify(resp.data));
        } else {
          console.log(resp.data);
        }
      })
      .catch(err => {
        // alert('Kindly enter valid credentials ', err)
        console.log("User addition failed. Kindly try again later", err);
        window.alert("User addition failed. Kindly try again later");
      });

    console.log(data);
  };

  console.log(watch("email"));
  console.log(errors.email);

  return (
    <>
      <Head></Head>

      <body id="body">
        <div>
          <h5>Kindly add a user or project member below</h5>
        </div>

        <hr style={{ backgroundColor: "black" }}></hr>

        <div>
          <Form alt="user management form" onSubmit={handleSubmit(onSubmit)}>
            <FormGroup>
              {/* <label for="project-id" id="label" className={label} alt="label for project id">
                                Project ID
                        </label>
                            <select id="project-id" ref={register} name="project-id" required= {true} className={projectID} alt="select a project">
                                <option id ="project-id" value= "" name= "project-id" className={projectID} alt="selected project"></option>
                            </select>
                            <br/> */}

              <label
                for="firstname"
                id="label"
                className={label}
                alt="label for user firstname"
              >
                First Name
              </label>

              <input
                id="firstname"
                ref={register}
                name="firstname"
                className={usermgmtinput}
                alt="user firstname"
                required={true}
                placeholder="Project member or user's firstname"
              ></input>
              <br />

              <label
                for="othernames"
                id="label"
                className={label}
                alt="label for user other name "
              >
                Other Names
              </label>

              <input
                id="othernames"
                ref={register}
                name="othernames"
                className={usermgmtinput}
                alt="user othernames"
                required={true}
                placeholder="Project member or user's othernames"
              ></input>
              <br />

              <label
                for="email"
                id="label"
                className={label}
                alt="label for user email"
              >
                Email
              </label>

              <input
                id="email"
                name="email"
                type="email"
                className={usermgmtinput}
                alt="user email"
                placeholder="Project member or user's email address"
                ref={register({
                  required: true,
                  validate: input => isEmail(input)
                })}
              ></input>
              <br />
              {errors.email && (
                <span style={{ color: "red", fontSize: "11px" }}>
                  Kindly enter a valid email
                </span>
              )}
              <br />

              <label
                for="role"
                id="label"
                className={label}
                alt="label for user role"
              >
                User Role
              </label>
              <select
                id="role"
                ref={register}
                name="role"
                required={true}
                className={usermgmtinput}
                alt="select user role"
              >
                <option
                  id="role"
                  value="admin "
                  name="role"
                  className={useradmin}
                  alt="user admin role selected"
                >
                  Administrator
                </option>
                <option
                  id="role"
                  value="member"
                  name="role"
                  className={usermember}
                  alt="user member role selected"
                >
                  Member
                </option>
              </select>
            </FormGroup>

            <Button type="submit" id="submitbtn" className={submitbutton}>
              Submit
            </Button>
          </Form>
          <hr style={{ backgroundColor: "black" }}></hr>
          <hr style={{ backgroundColor: "black" }}></hr>

          <div id="user-list" name="user-list" className={userlist}>
            <div>
              <MemberList />
            </div>
          </div>
        </div>
      </body>
    </>
  );
}
