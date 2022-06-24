import { useState, useEffect } from "react";
import { useForm } from "react-hook-form";
import isEmail from "validator/lib/isEmail";
import axios from "axios";

import "bootstrap/dist/css/bootstrap.min.css";
import styles from "../../../../styles/dashboard/configuration/usermanagement.module.css";
import Head from "next/head";
import { Form, FormGroup, Button } from "reactstrap";

export default function EditUser() {
  //handling user management, add user data
  const {
    register,
    handleSubmit = async e => {
      {
        e.preventDefault;
      }
    },
    watch,
    errors
  } = useForm();

  //Define styles
  const {
    useremail,
    userrole,
    useradmin,
    usermember,
    projects,
    submitbtn,
    label,
    cancelbtn
  } = styles;

  //function for submitting user addition data
  const onSubmit = async (e, data = { email, role, project }) => {
    {
      e.preventDefault;
    }

    console.log("data is ", data);
    axios
      .post("http://localhost:8000/", {
        email: data.email,
        role: data.role,
        project: data.project
      })
      .then(resp => {
        // On successful addition of user

        if (resp.status == 200) {
          //store added user details

          localStorage.setItem("users", resp.data);
          console.log(resp.data);
          window.alert(
            "User updated successfully, a confirmation mail has been sent to the user."
          );

          localStorage.setItem("users", JSON.stringify(resp.data));
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

      <body>
        <div>
          <h1>User Management</h1>
        </div>

        <div>
          <h3>Kindly update a User below</h3>
        </div>

        <hr></hr>

        <div>
          <Form alt="user management form">
            <FormGroup>
              <label id="label" className={label} alt="label for user email">
                User email
              </label>
              <input
                id="user-email"
                name="email"
                type="email"
                className={useremail}
                alt="user email"
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

              <label id="label" className={label} alt="label for user role">
                User Role
              </label>
              <select
                id="user-role-dropdown"
                name="role"
                required="true"
                className={userrole}
                alt="select user role"
              >
                <option
                  id="1"
                  name="user-admin-role"
                  className={useradmin}
                  alt="user admin role selected"
                >
                  Administrator
                </option>
                <option
                  id="2"
                  name="user-member-role"
                  className={usermember}
                  alt="user member role selected"
                >
                  Member
                </option>
              </select>

              <label id="label" className={label} alt="label for user project">
                Project
              </label>
              <select
                id="project-id"
                name="project"
                required="true"
                className={projects}
                alt="select user role"
              >
                <option
                  id="1"
                  name="projects"
                  className={projects}
                  alt="user project to be assigned"
                >
                  Project A
                </option>
                <option
                  id="2"
                  name="projects"
                  className={projects}
                  alt="user project to be assigned"
                >
                  Project B
                </option>
              </select>
            </FormGroup>

            <Button
              id="submitbtn"
              className={submitbtn}
              onClick={handleSubmit(onSubmit)}
            >
              Update User
            </Button>
            <Button id="cancelbtn" className={cancelbtn}>
              Cancel
            </Button>
          </Form>
        </div>
      </body>
    </>
  );
}
