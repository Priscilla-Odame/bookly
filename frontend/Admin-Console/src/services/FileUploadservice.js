import axios from 'axios';
import { API_BASE_URL, API_PORT} from '../../config';

//Endpoints and urls

const upload_files_endpoint = 'api/fileUpload/create';
const upload_files_url = `${API_BASE_URL}:${API_PORT}/${upload_files_endpoint}`

const get_uploaded_files_endpoint ='api/fileUploads';
const uploaded_files_url = `${API_BASE_URL}:${API_PORT}/${get_uploaded_files_endpoint}`

//Upload functionality
const upload = (file, onUploadProgress, token) => {
  let formData = new FormData();

  formData.append("file", file);

  return axios.post(upload_files_url, JSON.stringify(formData), JSON.stringify([
    {
      tittle: data.tittle,
      data_file: data.status,
      project: 1,
      user: data.user,
      // created_by: userdata.email
  }
  ]), {
    headers: {
      "Content-Type": "multipart/form-data",
      "Authorization": `Bearer ${token}`
    },  
    onUploadProgress,
  });
};

//Checking for user auth State objects

// const [tokens, setToken] = useState("")
// const [email, setEmail] = useState([])

const tokens = ""
const setToken = ""
const email = ""
const setEmail =""

//fetching user data for authorization

const thisfunction=(() => {
  const userdata = localStorage.getItem('user');

if(userdata) {
    const foundUser = JSON.parse(userdata)
    setEmail(foundUser.email)
    setToken(foundUser.tokens.access)
    console.log('User is authenticated to view uploaded files');

  getFiles()
}

}, [])

//fetch list of files in database

const getFiles = async (thisfunction) => {
  const userdata = JSON.parse(localStorage.getItem("user"))

  const response = await axios.get(uploaded_files_url, {headers: {
      "Content-Type": "multipart/form-data",
      "Authorization": `Bearer ${userdata.tokens.access}`
    },  
    // onUploadProgress,
  })


};

export default {
  upload,
  getFiles,
};