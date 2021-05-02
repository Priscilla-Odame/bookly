function loadBorrowedBooks() {
    console.log('We need to load the books now');

    // making a GET call to fetch all books
    fetch('https://librariesapp.herokuapp.com/api/borrow/pk/')
    .then(resp => resp.json())
    .then(data => {
        console.log("Data from backend", data)
        populateBorrowedBooks(data);
    })
    .catch(err => {
        console.log("We got an error ", err);
    })

}

function getBorrowerId(){
    
}

function populateBorrowedBooks(data) {
    // table // list

    // get the html element to inject the table
    let sectionBooks = document.getElementById('bookList');

    // clear the content first
    sectionBooks.innerHTML = "";

    // create a table 
    let booksTable = document.createElement('table');
    // booksTable.setAttribute('border', "1");

    // create a table row for heading
    let headingRow = document.createElement('tr');

    headingRow.innerHTML = "<th>Title</th><th>Date borrowed</th><th>Return date</th><th><th>Action</th>";

    // now append the heading row to the table
    booksTable.appendChild(headingRow);

    // we are now going to iterate over the data that was
    // received from the backend

    for (let i=0; i < data.length; i++) {
        // get the book object
        const books = data[i];
        console.log('Book borrowed is ', books);

        // now create a row and then put the book details in the 
        // corresponding tds
        let dataRow = document.createElement('tr');
        // let imageValue = `<img src="${book.book_cover}" alt="book cover for ${book.title}"/>`
        // let thumbnail = `<a target="_top" href="${book.book_cover}">${imageValue}</a>`

        dataRow.innerHTML = `<td>${books.book}</td><td>${book.date_borrowed}</td><td>${book.return_date}</td>`;

        const btnReturn = document.createElement('button');
        btnReturn.innerHTML = "Return";
        btnBorrow.onclick = (()=> {
            console.log('Are you seriously trying to return book with title ', books.book);
            localStorage.setItem('selectedBorrwedBook', book.borrowed_by)
            window.location.href = "/dashboard"
        });

        dataRow.appendChild(btnReturn);

        // now we append it to the 
        booksTable.appendChild(dataRow);
    }

    // now inject the sectionBooks with the generated html content
    sectionBooks.appendChild(booksTable);
}

function openCity(evt, cityName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(cityName).style.display = "block";
    evt.currentTarget.className += " active";
  }
  
  // Get the element with id="defaultOpen" and click on it
 // document.getElementById("defaultOpen").click();