import React, { useState, useEffect } from "react";
import styles from "../../../../styles/dashboard/AdminPanel/ClientOrganization/list.module.css";
import AddClientAdmin from "../ClientOrganization/ClientAdministrator/Modal/AddClientAdmin";
import AddContactPersonModal from "../ClientOrganization/ContactPerson/Modal/AddContactPerson";
import { API_PORT_HOSTED, ORGANIZATIONS, ORGKEY } from "../../../../config";
import ViewClientAdminDetail from "./ClientAdministrator/Modal/ViewClientAdminDetails";
import ViewContactDetail from "./ContactPerson/Modal/ViewContactDetail";
import EditClientAdmin from "./ClientAdministrator/Modal/EditClientAdmin";
import DeleteClientAdmin from "./ClientAdministrator/Modal/DeleteClientAdmin";

const {
  searchBox,
  closeIcon,
  clientBorder,
  addPlus,
  filterBtn,
  addTxt,
  addBtn,
  clientTab,
  NofilterWrapper,
  filterWrapper,
  roleToggle,
  thead,
  theadtxt,
  trow,
  TableBody,
  successBar,
  delSuccess,
  successTxt,
  successBarClose,
  taction,
  tbody,
  tdata,
} = styles;

export default function ClientOrganizationList({ orgId }) {
  const [toggle, setToggle] = useState("Client Admin");
  const [filter, setFilter] = useState(false);
  const [contactList, setContactList] = useState([]);
  const [clientAdminList, setClientAdminList] = useState([]);
  const [added, setAdded] = useState(false);
  const [deleted, setDeleted] = useState(false);
  const [updated, setUpdated] = useState(false);
  const [searchtxt, setSearchTxt] = useState("");
  const [org, setOrg] = useState([]);

  const findClientAdmin = (id) => {
    const item = clientAdminList.find((org) => org.id === id);
    setOrg(item);

    window.localStorage.setItem("Client-Admin", JSON.stringify(item));
  };

  const findContactPerson = (id) => {
    const item = contactList.find((org) => org.id === id);
    setOrg(item);
    window.localStorage.setItem("Contact-Person", JSON.stringify(item));
  };

  //GET Client Admin
  async function getAdmin() {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
      method: "GET",
      headers: myHeaders,
    };

    await fetch(
      `${API_PORT_HOSTED}/${ORGANIZATIONS}/administrator/?organization=${
        orgId == undefined ? ORGKEY : orgId
      }`,
      requestOptions
    )
      .then((response) => response.json())
      .then((res) => {
        if (searchtxt == "") {
          setClientAdminList(res);
        }
      });
  }

  //GET Staff Members
  function getStaff() {
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    var requestOptions = {
      method: "GET",
      headers: myHeaders,
    };

    fetch(`${API_PORT_HOSTED}/${ORGANIZATIONS}/staff-members/`, requestOptions)
      .then((response) => response.json())
      .then((result) => setContactList(result))
      .catch((error) => alert("error", error));
  }

  useEffect(() => {
    getStaff();
  }, []);

  useEffect(() => {
    if (searchtxt.length > 0) {
      let filteredAdmin = clientAdminList.filter((admin) => {
        return (
          admin.name.toLowerCase().indexOf(searchtxt.toLowerCase()) !== -1 ||
          admin.email.toLowerCase().indexOf(searchtxt.toLowerCase()) !== -1 ||
          admin.role.toLowerCase().indexOf(searchtxt.toLowerCase()) !== -1
        );
      });
      setClientAdminList(filteredAdmin);
    } else if (searchtxt == "") {
      getAdmin();
    }
  }, [searchtxt]);

  return (
    <>
      <div className="container" id="det-clorg-ls">
        <div className={clientTab} id="cl-tab">
          <span className={roleToggle} id="cl-toggle">
            <span
              id="cl-ad-menu"
              className={toggle == "Client Admin" ? clientBorder : ""}
              onClick={() => setToggle("Client Admin")}
            >
              Client Administrator
            </span>

            <span
              id="cont-pers-menu"
              className={
                toggle == "Contact Person" ? `ml-3 ${clientBorder}` : "ml-3"
              }
              onClick={() => setToggle("Contact Person")}
            >
              Contact Person{" "}
            </span>
          </span>

          <span
            id="filt-btn"
            onClick={() => {
              setFilter(true);
            }}
          >
            <img id="filbtn-img" className={filterBtn} src="/filter-btn.svg" />
          </span>

          <button
            id="add-btn-clo"
            type="button"
            className={addBtn}
            data-toggle="modal"
            data-target={
              toggle == "Client Admin"
                ? "#add-client-admin"
                : "#add-contact-person"
            }
          >
            <img id="add-clo-img" className={addPlus} src="/plus.svg" />
            <span id="add-clo-txt" className={addTxt}>
              Add
            </span>
          </button>
        </div>

        {filter ? (
          <div className={filterWrapper} id="fltr-sec">
            <form className={"form-group has-search"} id="fltr-form">
              <span id="fltr-box-inp">
                <input
                  id="fltr-clo-inp"
                  type="text"
                  className={searchBox}
                  value={searchtxt}
                  placeholder="filter by keyword"
                  onChange={(e) => setSearchTxt(e.target.value)}
                />
              </span>

              <span id="close-fltr">
                <img
                  id="dissmiss-flr-btn"
                  className={closeIcon}
                  onClick={() => {
                    setFilter(false);
                    setSearchTxt("");
                  }}
                  src="/close-status.svg"
                />
              </span>
            </form>
          </div>
        ) : (
          <div id="fil-none" className={NofilterWrapper}></div>
        )}
        <div id="clo-ls-sec">
          {deleted ? (
            <div id="del-bar-sec" className={delSuccess}>
              <span id="del-bar-txt" className={successTxt}>
                User Successfully Deleted
              </span>
              <span id="del-dismiss-btn">
                <img
                  id="del-diss-img"
                  className={successBarClose}
                  onClick={() => setDeleted(false)}
                  src="/close-status.svg"
                />
              </span>
            </div>
          ) : (
            ""
          )}
          {added ? (
            <div id="add-bar-sec" className={successBar}>
              <span id="add-bar-txt" className={successTxt}>
                User Successfully Added
              </span>
              <span id="add-dismiss-btn">
                <img
                  id="add-diss-img"
                  className={successBarClose}
                  onClick={() => setAdded(false)}
                  src="/close-status.svg"
                />
              </span>
            </div>
          ) : (
            ""
          )}
          {updated ? (
            <div id="upd-bar-sec" className={successBar}>
              <span id="upd-bar-txt" className={successTxt}>
                User Successfully Updated
              </span>
              <span id="upd-dismiss-btn">
                <img
                  id="upd-diss-img"
                  className={successBarClose}
                  id="updateBar"
                  onClick={() => setUpdated(false)}
                  src="/close-status.svg"
                />
              </span>
            </div>
          ) : (
            ""
          )}
          <div className={TableBody} id="tab-bdy-clo">
            <table
              id="tab-clo"
              className="table"
              cellSpacing="0"
              cellPadding="0"
            >
              <colgroup>
                <col className="profImg" />
                <col span="3" />
                <col />
              </colgroup>
              <thead id="tab-hd-clo">
                <tr id="tab-row-clo">
                  <th className={theadtxt} id="th-file">
                    <img id="file-img" src="/file.svg" />
                  </th>
                  <th id="th-name" className={theadtxt} scope="col">
                    Name
                  </th>
                  <th id="th-email" className={theadtxt} scope="col">
                    Email
                  </th>
                  <th id="th-role" className={theadtxt} scope="col">
                    Role
                  </th>
                  <th id="th-actions" className={theadtxt} scope="col"></th>
                </tr>
              </thead>
              {toggle == "Client Admin" && clientAdminList.length > 0
                ? clientAdminList.map((clientAdmin) => (
                    <tbody
                      id="tb-cla-ls"
                      className={tbody}
                      key={clientAdmin.id}
                    >
                      <tr id="trow-cla-ls" className={trow}>
                        <td id="td-cla-img" className={tdata}>
                          <img
                            id="cla-pro-img"
                            src={
                              clientAdmin.image
                                ? clientAdmin.image
                                : "/profile.svg"
                            }
                          />
                        </td>
                        <td
                          id="td-cla-name"
                          className={`${tdata} text-capitalize`}
                        >
                          {clientAdmin.name}
                        </td>
                        <td id="td-cla-email" className={tdata}>
                          {clientAdmin.email}
                        </td>
                        <td id="td-cla-role" className={tdata}>
                          {clientAdmin.role}
                        </td>
                        <td id="td-cla-more" className={taction}>
                          <div
                            id="dropdown-cla-tb"
                            className="dropdown"
                            onClick={() => findClientAdmin(clientAdmin.id)}
                          >
                            <a
                              id="dropDown-cla"
                              data-toggle="dropdown"
                              aria-haspopup="false"
                              aria-expanded="false"
                            >
                              <img id="more-opt-cla" src="/more-options.svg" />
                            </a>
                            <div
                              id="dropDown-popup-cla"
                              className="dropdown-menu"
                              aria-labelledby="dropdownMenuButton"
                            >
                              <a
                                id="cla-ls-vca"
                                className="dropdown-item"
                                type="button"
                                data-toggle="modal"
                                data-target="#view-client-admin"
                                href="#viewcla"
                              >
                                View
                              </a>
                              <a
                                id="cla-ls-eca"
                                className="dropdown-item"
                                type="button"
                                data-toggle="modal"
                                data-target="#edit-client-admin"
                              >
                                Edit
                              </a>
                              <a
                                id="cla-ls-dca"
                                className="dropdown-item"
                                type="button"
                                data-toggle="modal"
                                data-target="#delete-client-admin"
                              >
                                Delete
                              </a>
                            </div>
                          </div>
                          {/* </div> */}
                        </td>
                      </tr>
                    </tbody>
                  ))
                : toggle == "Contact Person" && contactList.length > 0
                ? contactList.map((contactPerson) => (
                    <tbody
                      id="tb-cp-ls"
                      className={tbody}
                      key={contactPerson.id}
                    >
                      <tr id="trow-cp-ls" className={trow}>
                        <td id="td-cp-img" className={tdata}>
                          <img
                            id="cp-pro-img"
                            src={
                              contactPerson.image
                                ? contactPerson.image
                                : "/profile.svg"
                            }
                          />
                        </td>
                        <td
                          id="td-cp-name"
                          className={`${tdata} text-capitalize`}
                        >
                          {contactPerson.firstname} {contactPerson.lastname}
                        </td>
                        <td id="td-cp-email" className={tdata}>
                          {contactPerson.email}
                        </td>
                        <td id="td-cp-role" className={tdata}>
                          {contactPerson.role}
                        </td>
                        <td id="td-cp-more" className={taction}>
                          <div
                            id="dropdown-cp-tb"
                            className="dropdown"
                            onClick={() => findContactPerson(contactPerson.id)}
                          >
                            <a
                              id="dropDown-cp"
                              data-toggle="dropdown"
                              aria-haspopup="false"
                              aria-expanded="false"
                            >
                              <img id="more-opt-cp" src="/more-options.svg" />
                            </a>
                            <div
                              id="dropDown-popup-cp"
                              className="dropdown-menu"
                              aria-labelledby="dropdownMenuButton"
                            >
                              <a
                                id="cp-ls-vca"
                                className="dropdown-item"
                                type="button"
                                data-toggle="modal"
                                data-target="#view-contact-person"
                                href="#viewcp"
                              >
                                View
                              </a>
                              <a
                                id="cp-ls-eca"
                                className="dropdown-item"
                                type="button"
                                data-toggle="modal"
                                data-target="#edit-contact-person"
                              >
                                Edit
                              </a>
                              <a
                                id="cla-ls-dcp"
                                className="dropdown-item"
                                type="button"
                                data-toggle="modal"
                                data-target="#delete-contact-person"
                              >
                                Delete
                              </a>
                            </div>
                          </div>
                        </td>
                      </tr>
                    </tbody>
                  ))
                : ""}
            </table>
          </div>
        </div>
      </div>
      <ViewClientAdminDetail clientDetail={org} />
      <ViewContactDetail contactDetail={org} />
      <AddContactPersonModal
        setAdded={setAdded}
        orgkey={ORGKEY}
        contactDetail={org}
      />
      <AddClientAdmin
        setAdded={setAdded}
        orgkey={ORGKEY}
        setClientAdminList={setClientAdminList}
        clientAdminList={clientAdminList}
      />
      <EditClientAdmin
        getAdmin={getAdmin(ORGKEY)}
        clientDetail={org}
        setUpdated={setUpdated}
        orgkey={ORGKEY}
      />
      <DeleteClientAdmin
        clientAdminList={clientAdminList}
        setDeleted={setDeleted}
        setClientAdminList={setClientAdminList}
        clientDetail={org}
      />
    </>
  );
}
