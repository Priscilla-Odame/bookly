import axios from "axios";
// import dynamic from "next/dynamic";



// const userdata = JSON.parse(window.localStorage.getItem('user'));


export default axios.create({
  baseURL: "http://localhost:8000",
  headers: {
    "Content-type": "application/json",
    // 'Authorization': `Bearer ${userdata.tokens.access}`
  }
});