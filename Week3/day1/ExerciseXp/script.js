//Exercise 1 : Users
   /*
    function display1 (){
      let y = document.getElementById("container").textContent
      console.log (y)}

       display1()
    */
   
//Change the name “Pete” to “Richard”.

     /*
   let x  = document.querySelectorAll("ul")[0].children[1]
       x.innerHTML = "Richard"
    */

//Change each first name of the two <ul>'s to your name.
     /*
     let q = document.querySelectorAll("ul")[0].children[0]
       q.innerHTML = "Avishek"

    document.querySelectorAll("ul")[1].children[0].innerHTML="Avishek"
       */

//Delete the <li> that contains the text node “Sarah”.
     /*
  document.querySelectorAll("ul")[1].children[1].remove()
     */

//Exercise 2 : Users And Style
     /*
      //Add a “light blue” background color and some padding to the <div>
            let w = document.getElementById("container")
                w.style.backgroundColor = "blue"
                w.style.paddingTop = 20 
     //Do not display the <li> that contains the text node “John”
            let e = document.getElementsByTagName("ul")[0].children[0]
                e.style.display = "none"
     //Add a border to the <li> that contains the text node “Pete”
            let r = document.getElementsByTagName("ul")[0].children[1]
            r.style.border = " thin solid black"
     //Change the font size of the whole body.
             document.body.style.fontSize = "large"
      */

//Exercise 3 : Change The Navbar
     
    //In the <div>, change the value of the id attribute from navBar 
    //to socialNetworkNavigation, using the setAttribute method
       /*
    document.getElementById("navBar").setAttribute("id", "socialNetworkNavigation")
      

    //Create a new text node with “Logout”
         
      const list = document.createElement("li")
          list.innerText = "Logout"
          document.body.children[0].children[0].appendChild(list)
          
    //Use the firstElementChild and the lastElementChild properties 

    document.body.firstElementChild.firstElementChild.firstElementChild.innerHTML       
    document.body.firstElementChild.firstElementChild.lastChild.innerHTML
             */

//Exercise 4 : My Book List
  
   let allBooks = [
   {
    title : "A Line to Kill",
    author : "Anthony Horowitz",
    alreadyRead : "true"},

  {
    title : "You Better Be Lightning",
    author : "Andrea Gibson",
    alreadyRead :"false"
  }]

  function generateTableHead(table, data) {
  let thead = table.createTHead();
  let row = thead.insertRow();
  for (let key of data) {
    let th = document.createElement("th");
    let text = document.createTextNode(key);
    th.appendChild(text);
    row.appendChild(th);
  }
}

function generateTable(table, data) {
  for (let element of data) {
    let row = table.insertRow();
    for (key in element) {
      let cell = row.insertCell();
      let text = document.createTextNode(element[key]);
      cell.appendChild(text);
    }
  }
}

let table = document.querySelector("table");
let data = Object.keys(allBooks[0]);
generateTableHead(table, data);
generateTable(table, allBooks);