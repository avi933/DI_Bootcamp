//write a JavaScript function to add rows to a table

   function insertRow(){
   	let count = 2
	    let table = document.getElementById("sampleTable")
	    let newrow = document.createElement("tr")
	    newrow.innerHTML=  "<td> Row" + count + "cell1 </td>"
	                       "<td> Row" + count +  "cell2</td>"

        //let row = table.insertRow(0)
        //let c1 = row.insertCell(0)
        //let c2 = row.insertCell(1)
        //c1.innerHTML = "just added"
        //c2.innerHTML = "just added"
    }



 /*
//Add a few event listener to the button
      let x = document.getElementById("jsstyle")
        x.addEventListener("mouseover", Respond);
        x.addEventListener("click", Respond);
        x.addEventListener("mouseout", Respond);

        function Respond(e){
        	if (e.type == "mouseover"){
        		e.target.style.fontSize = 50
        		e.target.style.color = "red"
        		e.target.style.backgroundColor = "skyblue"}
        	else if(e.type == "click"){
        		e.target.style.fontSize = "x-small"
        		e.target.style.color = "purple"
        		e.target.style.backgroundColor = "green"}
        	else if (e.type == "mouseout") { 
        		e.target.style.fontSize = "medium"
        		e.target.style.color = "black"
        		e.target.style.backgroundColor = "white"}
        	}
        */
