function handleBorrow() {
    // console.log("We are about to submit the form");
    // let dateBorrowedVal = document.getElementById('dateborrowed').value;
    // let dateReturnedVal = document.getElementById('datereturned').value;
    let bookBorrowedVal = document.getElementById('book').value

    // let data = {date_borrowed: dateBorrowedVal, return_date: dateReturnedVal, book : bookBorrowedVal };
    let data = {book : bookBorrowedVal };

    console.log('We are submitting this data to the backend in the right one', data);


    fetch('https://librariesapp.herokuapp.com/api/borrow/', {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
          'Content-Type': 'application/json'
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
      })
      .then(response => response.json())
      .then(data => {
        console.log('Success:', data);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
        //   response => {
        //   if (response.status != 201) {
        //       console.log('You have a problem');
        //       return;
    //       } else {
    //           let goodData = response.json();
    //           goodData.then(() => {
    //               console.log('Success:', data);
    //               window.location.href = '/books.html';
    //           })
    //       }
    //   })
    //   .catch((error) => {
    //     console.error('Error:', error);
    //   });
}