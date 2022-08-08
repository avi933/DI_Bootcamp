//Using a DOM property, retrieve the h1 and console.log it

     let x = document.getElementsByTagName("h1")[0].innerHTML
       console.log(x)

//Using DOM methods, remove the last paragraph in the <article> tag

    document.body.children[0].lastElementChild.remove()

//Add a event listener which will change the background color of 
//the h2 to red, when it’s clicked on.

    let y = document.getElementById("back")
        y.addEventListener("click", Respond);
     function Respond(e){
        	if (e.type == "click"){
        		e.target.style.backgroundColor = "red"}}


//Add an event listener which will hide the h3 when it’s clicked on 
     let r = document.getElementById("hide")
         r.addEventListener("click", Respond);
       function Respond(e){
        	if (e.type == "click"){
        		e.target.style.display = "none"}}
//Add a <button> to make the text of all the paragraphs, bold

       let u = document.getElementById("b")
       let p = document.getElementsByTagName("P")
           u.addEventListener("click",Respond)
        function Respond(e){
    	    if (e.type == "click"){
    	    	for ( let i = 0;  i <= p.length; i++){ p[i].style.fontWeight = "bolder"}}}
/*
//hover on the h1, set the font size to a random pixel size
  
   let z = document.getElementsByTagName("h1")[0]

   z.addEventListener("mouseover",Respond)
       function Respond(e){

       if (e.type == "mouseover"){
       	z.style.fontSize = Math.floor(Math.random() * 100)
       }}
   
   */

