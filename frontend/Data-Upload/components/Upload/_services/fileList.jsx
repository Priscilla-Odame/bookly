import axios from "axios";

import useInterval from 'react-useinterval';
import "react-toastify/dist/ReactToastify.css";
import { toast } from "react-toastify";
import Loading from './commons/LoadingSpinner';

import React, { useState, useEffect } from "react";
import styles from "../../../styles/upload/filelist.module.css";
import {MdFolder, MdDelete, MdFileDownload} from 'react-icons/md';
import { RiArrowDownSFill, RiArrowUpSFill } from "react-icons/ri";
import {FiFilter} from "react-icons/fi";


// DATA----URLS
const endpointfetchfiles = "api/fileuploads";
const fetchfilesURL = `${process.env.API_URL}/${endpointfetchfiles}`;

const endpointaccessFile = "api/fileupload/delete";
const accessFileURL = `${process.env.API_URL}/${endpointaccessFile}`;

  //Function to order files
  const orderBy = (files, value, direction) => {
    if (direction === "asc") {
        return [...files].sort((a, b) =>
            a[value] > b[value] ? 1 : -1
        );
    }
 
    if (direction === "desc") {
        return [...files].sort((a, b) =>
            a[value] > b[value] ? -1 : 1
        );
    }
 
    return files
  } 

  //function to sort files
  const SortArrow = ({direction}) => {
    if (!direction) {
        return (
          <div className={styles.filterIcons} id="normal-order" title="Normal sort">
            <FiFilter/>
          </div>
        )
    }

    if (direction === "desc") {
        return (
            <div className={styles.filterIcons} id="descending-order" title="Descending order" className={styles.heading_arrow}>
                <RiArrowDownSFill/>
            </div>
        );
        
    } else {
        return (
            <div className={styles.filterIcons} id="descending-order" title="Ascending order" className={styles.heading_arrow}>
                <RiArrowUpSFill/>
            </div>
        );
    }
  }

toast.configure();
const FileList = ({ access }, props) => {

  //#########################----------Type decalarations/State objects------------##################//

  const [load, setLoading] = useState(false);
  const [files, setFiles] = useState([]);

  const [direction, setDirection] = useState()
  const [value, setValue] = useState()

  const orderedFiles = orderBy(files, value, direction)

  const switchDirection = () => {
    if (!direction) {
        setDirection("desc")
    } else if (direction === "desc") {
        setDirection("asc")
    } else {
        setDirection(null)
    }
  }

  const setvalueAndDirection = (value) => {
      switchDirection()
      setValue(value)
  };


  //#########################----------Get user files------------##################//

  const getFiles = async () => {
    await axios.get(fetchfilesURL, {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          Authorization: `Token ${access}`,
        },
      })
      .then((response) => {
        setLoading(false);
        if (response.status == 200) {
          console.log("User files fetched successfully");
          setFiles(response.data);
        }
      }).catch((err) => {
        console.log("There seems to be an issue fetching data", err);
        // toast.error(
        //   "We could not get your files at this time... Please check your connection",
        //   err
        // );
      });
  };

  useInterval(getFiles, 30000);

  // if(typeof window == 'defined' || 'undefined'){
  // window.setInterval(function(){getFiles()}, 50000)}

  // if (access !== "") getFiles();


  //##############-- user actions --#######################//

  // delete service
  const delFile =  (id) => {
    axios.delete(`${accessFileURL}/${id}`, {
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
        Authorization: `Token ${access}`,
      },
    }).then((response) => {
      if (response.status == 200 ) {
        setFiles(response.data);
        console.log("File deleted");
        toast.success("File deleted successfully...");
      } 
    }).catch((err) => {
      console.log("There seems to be an issue deleting the data", err);
      toast.error(
        "We could not delete the file at this time... Please try again"
      );
    });
    
    //return new file list
    const newfileList = files.filter((file)=>{
      return file.id !== id;
    })
    setFiles(newfileList);
  };


  return (
    <>
        {files.length <= 0 ? 
          <div className={styles.noFiles}>
            <img src="/assets/images/no-files.svg" alt="no-files" />
            <h3>No files here yet</h3>
            <p>Upload a file to get started</p>
          </div>
         : 

          /*Styles in global stylesheet*/          
          <table
            styles={{fontFamily: 'Work Sans',
                  }}
                  id="uploads-table">
            <thead id="table-head" className="tb-head">
              {/* <tr  id="table-head-row" className="tb-head-row">{RenderHeader()}</tr> */}
              <tr  id="table-head-row" className="tb-head-row">
                <td>
                  Name
                  <button id="sortbyName" className={styles.sortButton} onClick={() => setvalueAndDirection("name")}><SortArrow direction={direction}/></button>
                </td>
                <td>
                  Size
                  <button id="sortbSize" className={styles.sortButton} onClick={() => setvalueAndDirection("file_size")}><SortArrow direction={direction}/></button>
                </td>
                <td>
                  Date
                  <button id="sortbyDate" className={styles.sortButton} onClick={() => setvalueAndDirection("timestamp")}><SortArrow direction={direction}/></button>
                </td>
                <td>
                  Actions
                </td>
              </tr>

            </thead>

          {/*Body*/}
            
            {orderedFiles.map((files) => {
              // {load && <Loading/>}
              return (
              <tbody id="tb-bdy" className="tb-bdy">
                <tr key={files.id}  id="tb-bd-row" className="tb-bd-row">
                  {/* <MdFolder/> */}
                    {files.name ? (<a href={`${files.data_file}`} id="anc-file-link" className="anc-file-link"><td id="td-file-name" className="td-file-name"><MdFolder style={{marginRight: "10px"}}/>{files.name}</td></a>) : (<td id="td-no-files" className="td-no-files"><MdFolder/>{' '} No name</td>)}
                    {files.file_size ? (<td id="td-file-size" className="td-file-size">{files.file_size}</td>) : (<td id="td-no-size" className="td-no-size">-</td>)}
                    <td id="td-file-date" className="td-file-date">{files.timestamp}</td>
                    {/* {files.comment ? (<td>{files.comment}</td>) :(<td>_______________</td>)} */}
                    
                    <td style={{ display: "flex", justifyContent: "center"}} className="user-file-actions" id="user-file-actions">
                      <a id="download-file" href={`${files.data_file}`} download={files.id} target="_blank">
                        <MdFileDownload id="download-file-btn" title="Download File" style={{margin: '0px 5px 0px 5px'}} className={styles.user_action}/>
                      </a>
                      <div id="del-file-d" className="del-file-div">
                        <button 
                          id="del-file" 
                          title="Delete File" style={{margin: '0px 5px 0px 5px'}}
                          className={styles.user_action} 
                          onClick={()=>{delFile(files.id)}}
                        >
                          <MdDelete/>
                        </button>
                      </div>
                    </td>
                </tr>
              </tbody>
              )
            })}
          </table> 
        }

    </>
  );
};

export default FileList;
