// import axios from "axios";
// import Head from "next/head";
// import Link from "next/link";
// import classNames from "classnames/bind";
// import { useForm } from "react-hook-form";
// import isEmail from "validator/lib/isEmail";
// import React, { useState, useEffect } from "react";
// import styles from "../styles/signup.module.css";
// import { API_BASE_URL, API_PORT } from "../config";

// export default function SIgnUpform() {
//   //Endpoints and urls

//   const signup_endpoint = "api/user/signup";
//   const signup_url = `${API_BASE_URL}:${API_PORT}/${signup_endpoint}`;

//   const companies_endpoint = "api/companies";
//   const companies_url = `${API_BASE_URL}:${API_PORT}/${companies_endpoint}`;

//   //Object states
//   const [company, setCompany] = useState([]);

//   //fetch companies for user signup/registration function 1

//   useEffect(() => {
//     async function getCompanies() {
//       const response = await axios.get(companies_url);
//       // const body = await response.json();
//       setCompany(response.data.map(({ name }) => ({ id: name, name: name })));
//     }
//     getCompanies();
//   }, []);

//   // useEffect(() => {
//   //   async function getCompanies() {
//   //     const response = await axios.get(companies_url);
//   //     // const body = await response.json();
//   //     setCompany(response.data.map(({ name }) => ({ id: name, name: name })));
//   //   }
//   //   getCompanies();
//   // }, []);

//   //register method for binding inout field

//   const {
//     register,
//     handleSubmit = e => {
//       e.preventDefault;
//     },
//     watch,
//     errors
//   } = useForm();

//   console.log(watch("firstname", "othernames", "email", "company", "password"));
//   console.log(
//     errors.firstname,
//     errors.othernames,
//     errors.email,
//     errors.company,
//     errors.password
//   );

//   //On Submit function to send form data to backend API

//   const onSubmit = (
//     data = { firstname, othernames, email, company, password }
//   ) => {
//     console.log("data is", data);
//     axios
//       .post(signup_url, {
//         firstname: data.firstname,
//         othernames: data.othernames,
//         email: data.email,
//         company: 1,
//         password: data.password
//       })
//       .then(resp => {
//         //on successful singup

//         if (resp.status == 200) {
//           localStorage.setItem("user", JSON.stringify(resp.data));
//           window.alert(
//             "Sign up successful, kindly check your mail for a confirmation link and login"
//           );
//           window.location.href = "/";
//           localStorage.setItem("user", JSON.stringify(resp.data));

//           //signup unsuccessful
//         } else {
//           console.log(resp.data);
//         }
//       })
//       .catch(err => {
//         window.alert("Kindly enter valid credentials to sign up", err),
//           console.log("There was an error", err);
//       });
//     console.log(data);
//   };

//   //watch input fields for entered data change

//   console.log(
//     watch("firstname", "othernames", "email", "password", "company", "password")
//   );

//   console.log(
//     errors.firstname,
//     errors.othernames,
//     errors.email,
//     errors.company,
//     errors.password
//   );

//   return (
//     <>
//       <Head>
//         <title>Push Insights</title>
//       </Head>

//       <body>
//         <div className={styles.container}>
//           <center>
//             <div className={styles.card}>
//               <div className={styles.group}>
//                 <div className={styles.title}>
//                   <img className={styles.logo} src="/logo.png" alt="logo" />
//                   <h1>Almost ready ...</h1>
//                   <p>
//                     Please leave us your contact details to activate your
//                     account.
//                   </p>
//                 </div>
//                 <div>
//                   <form onSubmit={handleSubmit(onSubmit)}>
//                     <div>
//                       <div>
//                         <input
//                           type="email"
//                           className={classNames(
//                             errors.email && styles.errorInput,
//                             styles.input
//                           )}
//                           placeholder="Email *"
//                           name="email"
//                           id="email"
//                           // value={email} onChange={(e)=>setEmail(e.target.value)}
//                           ref={register({
//                             required: true,
//                             validate: input => isEmail(input)
//                           })}
//                         />
//                       </div>

//                       <div>
//                         {/* <div className={styles.passicon} onClick={this.passwordvisibility}>
//                                 <FontAwesomeIcon icon={faEye}/>
//                             </div> */}
//                         <input
//                           type="password"
//                           className={classNames(
//                             errors.password && styles.errorInput,
//                             styles.input
//                           )}
//                           placeholder="Password *"
//                           name="password"
//                           id="password"
//                           // value={password} onChange={(e)=>setPassword(e.target.value)}
//                           ref={register({
//                             required: true,
//                             minLength: 8
//                             // pattern:/^([a-zA-Z0-9@*#]{8,15})$/
//                           })}
//                         />
//                         {/* {errors.email && <span className={styles.error}>Should be at least 8 characters, include Uppercase, lowercase, a number and a symbol</span> } */}
//                       </div>

//                       <div>
//                         <input
//                           type="text"
//                           className={classNames(
//                             errors.firstname && styles.errorInput,
//                             styles.input
//                           )}
//                           // value={firstname} onChange={(e) =>setFirstname(e.target.value)}
//                           placeholder="First name *"
//                           name="firstname"
//                           id="firstname"
//                           ref={register({
//                             required: true,
//                             maxLength: 20,
//                             pattern: /^[A-Za-z]+$/i
//                           })}
//                         />
//                         {/* {errors.firstname && <span className={styles.error}>Letters only</span> } */}
//                       </div>

//                       <div>
//                         <input
//                           type="text"
//                           className={classNames(
//                             errors.othernames && styles.errorInput,
//                             styles.input
//                           )}
//                           // value={lastname} onChange={(e) =>setLastname(e.target.value)}
//                           placeholder="Other names *"
//                           name="othernames"
//                           id="othernames"
//                           ref={register({
//                             required: true,
//                             maxLength: 20,
//                             pattern: /^[A-Za-z]+$/i
//                           })}
//                         />
//                         {/* {errors.firstname && <span className={styles.error}>Letters only</span> } */}
//                       </div>

//                       <div>
//                         <select
//                           type="text"
//                           className={
//                             (errors.company && styles.errorInput,
//                             styles.inputcompany)
//                           }
//                           placeholder="Company *"
//                           name="company"
//                           id="company"
//                           // value ={company}

//                           //  value={company} onChange={(e)=>setCompany(e.target.value)}
//                           ref={register({
//                             required: true
//                             // pattern: /^[A-Za-z]+$/i,
//                           })}
//                         >
//                           {company.map(({ id, name }) => (
//                             <option key={id} name={id}>
//                               {name}
//                             </option>
//                           ))}
//                         </select>
//                       </div>

//                       <center></center>

//                       <button
//                         type="submit"
//                         className={styles.button}
//                         value="submit"
//                         disabled={errors.watch}
//                       >
//                         Sign Up
//                       </button>
//                     </div>
//                   </form>

//                   <Link href="/">
//                     <a className={styles.signin}>
//                       Already have an account? Sign in here
//                     </a>
//                   </Link>
//                 </div>
//               </div>
//             </div>
//           </center>
//         </div>
//       </body>
//     </>
//   );
// }
