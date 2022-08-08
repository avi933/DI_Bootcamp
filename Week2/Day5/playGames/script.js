function  playTheGame() {

	let text;
      if (confirm("Press a button!") !== true)
      	{text = "No Problem, Goodbye";
         alert(text)}
      
      else 
      	{text = "You pressed OK!";

         alert(text)
         let num = Number(prompt("Please enter a number between 0 to 10"))
         console.log(num)

         if (typeof(num) != "number"){alert ("Sorry not a number,Goodbye")}

         else if (num <0 || num > 10){ ("Sorry it is not a good number, Goodbye")}

         else {let computerNumber = Math.floor(Math.random() * 10)
         	console.log ("Random number is " + computerNumber)}

  } 
      
}

playTheGame()