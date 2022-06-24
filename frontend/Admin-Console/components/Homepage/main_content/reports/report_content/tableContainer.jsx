import React, {useState, useEffect} from "react";
// import TestList from './table';
import ReportList from "./table";
import styles from "../../../../../styles/Homepage/MainContent/reports/tablecontainer.module.css";
import { FiFilter } from "react-icons/fi";

export default function TableContainer() {
  //Define styles

  const { container, details_btn, history_btn, search, filter, table } = styles;

  // Search state State object
  const [searchInput, setSearchInput] = useState("");

  // Update the state when input changes
  const handleSearchChange = e => {
    const value = e.target.value || undefined;
    setSearchInput(value);
  };

  return (
    <div>
      <div className={container}>
        <div className={details_btn}>
          <b>Details</b>
        </div>

        <div className={history_btn}>History</div>

        <input type="text" placeholder=" 🔍search here" 
        className={search} 
        value={searchInput} onChange={handleSearchChange}
        />
        <div className={filter}>
          <FiFilter />
          <b>Filter</b>
        </div>
      </div>

      <div className={table}>
        <ReportList />
      </div>
    </div>
  );
}
