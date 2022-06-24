import React from 'react'
import styles from "../../../../styles/dashboard/AdminPanel/clientorganizationlist.module.css"

const Pagination = ({ organizationsPerPage, totalOrganizations, pageCounter, paginate}) => {

    //Define styles

    const {paginationContainer, tableItemsCounter, navPagination, pageItem, prevItems, pageLink, nextItems} = styles

    const pageNumbers = [];

    for(let i=1; i<=Math.ceil(totalOrganizations / organizationsPerPage); i++){
        pageNumbers.push(i);
    }
    return (
        <div>

           

            <div className={paginationContainer}>

                <div className={tableItemsCounter}>
                    <div id="table-item-counter">
                        {Math.ceil(organizationsPerPage)} out of {Math.ceil(totalOrganizations)}
                    </div>
                </div>

                <div className={navPagination}>
                    
                    <ul id="table-paginator">
                        
                        <button className={prevItems}>Previous</button>
                        
                        {pageNumbers.map(number => (
                            <li key={number} className={pageItem} id="page-item">
                                <a onClick={()=>paginate(number)} href="#" className={pageLink} id="table-number-link">
                                    {number}
                                </a>
                            </li>
                        ))}

                        <button className={nextItems}>Next</button>
  
                    </ul>

                </div>
            </div>
            
        </div>
    )
}

export default Pagination;