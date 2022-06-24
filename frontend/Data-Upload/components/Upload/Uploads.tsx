import Link from "next/link";
import axios from "axios";
import FileList from "./_services/fileList";
import styles from "../../styles/upload/uploads.module.css";
import React, { useState } from "react";

import { MdSearch, MdFolder, MdDelete, MdClose } from "react-icons/md";
import { toast } from "react-toastify";

toast.configure();
const Uploads = ({ access }) => {
  // DATA----URLS
  const endpointfetchfiles = "api/fileuploads";
  const fetchfilesURL = `${process.env.API_URL}/${endpointfetchfiles}`;

  const endpointaccessFile = "api/fileupload/delete";
  const accessFileURL = `${process.env.API_URL}/${endpointaccessFile}`;

  //Type declarations / state objects
  const [searchFiles, setsearchFiles]: any = useState([]);
  const [searchTxt, setsearchTxt]: any = useState("");

  //Get user fetched files from storage
  const [files, setFiles]: any = useState([]);

  //--> Change event for search input <--//
  const handlesearchChange = (event) => {
    const searchText = event.target.value;
    setsearchTxt(searchText);
    const newSearchData = files.filter((value) => {
      return value.name.toLowerCase().includes(searchText.toLowerCase());
    });
    if (searchText === "") {
      setsearchFiles([]);
    } else {
      setsearchFiles(newSearchData);
    }
  };

  //--> Get user fetched files from storage <--//
  const searchFunc = async () => {
    await axios
      .get(fetchfilesURL, {
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
          Authorization: `Token ${access}`,
        },
      })
      .then((response) => {
        if (response.status == 200) {
          console.log("Files fetched for search");
          setFiles(response.data);
        }
      })
      .catch((err) => {
        console.log("There seems to be an issue fetching data", err);
      });
  };

  //--> Clear search text <--//
  const clearSearchText = () => {
    setsearchFiles([]);
    setsearchTxt("");
  };

  //--> Call back functions after search text is cleared <--///
  function ClearSearch() {
    clearSearchText();
    !searchFunc();
  }

  return (
    <div>
      <div>
        {/* Files / Uploads elements */}
        <div className={styles.container}>
          <div style={{ borderBottom: "1px solid #D6D8E7" }}>
            <section className={styles.top}>
              {/* <h2 className={styles.title}>Uploads</h2> */}
              <button className={styles.subnavBtn}>Files</button>
              <div className={styles.searchFilter}>
                <MdSearch />
                <input
                  type="text"
                  placeholder="search by file name"
                  className={styles.search_input}
                  onChange={handlesearchChange}
                  value={searchTxt}
                  onKeyUp={searchFunc}
                />
                {/*Filter button*/}
                {/* <button className={styles.filter_button} title="Start by using the actions on file headers to filter by Date, Name or File Size">
                  Filter By
                  <FiFilter style={{ fontSize: "24px", float: "right" }}/>
                </button> */}
                {searchTxt.length !== 0 ? (
                  <MdClose
                    id="clear-search"
                    onClick={ClearSearch}
                    style={{ cursor: "pointer" }}
                  />
                ) : (
                  <></>
                )}
              </div>
            </section>

            {searchFiles.length != 0 && (
              <div className={styles.searchResult}>
                {searchFiles.slice(0, 5).map((value, key) => {
                  return (
                    <>
                      <a
                        className={styles.searchItem}
                        href={`${files.data_file}`}
                        target="_blank"
                        key={key}
                      >
                        <p>{value.name}</p>
                      </a>
                    </>
                  );
                })}
              </div>
            )}
            <div className={styles.searchResults}></div>
            <div className={styles.content}>
              <div>
                <FileList access={access} />
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Uploads;
