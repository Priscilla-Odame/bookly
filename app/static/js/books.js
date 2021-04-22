function loadBooks() {
    console.log('We need to load the books now');

    // making a GET call to fetch all books
    fetch('https://librariesapp.herokuapp.com/api/books/')
    .then(resp => resp.json())
    .then(data => {
        console.log("Data from backend", data)
        populateBooks(data);
    })
    .catch(err => {
        console.log("We got an error ", err);
    })

}

function populateBooks(data) {
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

    headingRow.innerHTML = "<th>Book Cover</th><th>Title</th><th>Author</th><th>No. of Pages</th><th>No. of Copies</th><th>Action</th>";

    // now append the heading row to the table
    booksTable.appendChild(headingRow);

    // we are now going to iterate over the data that was
    // received from the backend

    for (let i=0; i < data.length; i++) {
        // get the book object
        const book = data[i];
        console.log('Book is ', book);

        // now create a row and then put the book details in the 
        // corresponding tds
        let dataRow = document.createElement('tr');
        let imageValue = `<img src="${book.book_cover}" alt="book cover for ${book.title}"/>`
        let thumbnail = `<a target="_top" href="${book.book_cover}">${imageValue}</a>`

        dataRow.innerHTML = `<td>${thumbnail}</td><td>${book.title}</td><td>${book.author}</td><td>${book.number_of_pages}</td><td>${book.number_of_books}</td>`;

        const btnBorrow = document.createElement('button');
        btnBorrow.innerHTML = "Borrow";
        btnBorrow.onclick = (()=> {
            console.log('Are you seriously trying to borrow book with title ', book.title);
            localStorage.setItem('selectedBook', book.title)
            window.location.href = "/borrow"
        });

        dataRow.appendChild(btnBorrow);

        // now we append it to the 
        booksTable.appendChild(dataRow);
    }

    // now inject the sectionBooks with the generated html content
    sectionBooks.appendChild(booksTable);
}

function searchBook() {
    // Declare variables
    var input, filter, txtValue;
    input = document.getElementById('mySearch');
    filter = input.value.toUpperCase();
    // ul = document.getElementById("myUL");
    // li = ul.getElementsByTagName('li');
  
    // Loop through all list items, and hide those who don't match the search query
    // for (i = 0; i < li.length; i++) {
    //   a = li[i].getElementsByTagName("a")[0];
    //   txtValue = a.textContent || a.innerText;
    //   if (txtValue.toUpperCase().indexOf(filter) > -1) {
    //     li[i].style.display = "";
    //   } else {
    //     li[i].style.display = "none";
    //   }
    // }
    for (let i=0; i < data.length; i++) {
        // get the book object
        const book = data[i];
        txtValue = book.textContent || book.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1){
            data[i].style.display= "";
        }else {
            data[i].style.display="none";
        }
        }
  }