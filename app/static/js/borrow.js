function handleFill() {
  let bookTitle = localStorage.getItem('selectedBook')
  document.getElementById('book').value = bookTitle
}


function handleBorrow() {
    // console.log("We are about to submit the form");
    // let dateBorrowedVal = document.getElementById('dateborrowed').value;
    // let dateReturnedVal = document.getElementById('datereturned').value;
    let bookBorrowedVal = document.getElementById('book').value 
    let durationVal = document.getElementById('duration').value

    // let data = {date_borrowed: dateBorrowedVal, return_date: dateReturnedVal, book : bookBorrowedVal };
    let data = {book : bookBorrowedVal , duration : durationVal};

    console.log('We are submitting this data to the backend in the right one', data);


    fetch('https://librariesapp.herokuapp.com/api/borrow/', {
        method: 'POST', // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
          'Content-Type': 'application/json',
          'Authorization':'Bearer access_token',
          // 'Content-Type': 'application/x-www-form-urlencoded',
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
      })
      .then(response =>{
        if (response.status == 401) {
              console.log('You have a problem');
              window.location.href = '/login';
              return;
          }else if (response.status != 201){
            console.log('You have a problem');

          }
           else {
              let goodData = response.json();
      goodData.then(data => {
        console.log('Success:', data);
        window.location.href = '/books';
      })}})
      .catch((error) => {
        console.error('Error:', error);
      });
      // .then(response => response.json())
      // .then(data => {
      //   console.log('Success:', data);
      // })
      // .catch((error) => {
      //   console.error('Error:', error);
      // });
}

