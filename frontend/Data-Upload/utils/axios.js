import axios from "axios";

//import { baseUrl } from '../config/env';

const axiosInstance = axios.create({
  baseURL: process.env.API_URL,
  "Content-Type": "application/json",
  Accept: "application/json",
});

export default axiosInstance;

// axiosInstance.defaults.headers.common['Authorization'] = `Bearer ${token}`