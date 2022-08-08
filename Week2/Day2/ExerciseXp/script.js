//Exercise 1
/*
let x = 5;
let y = 2;
if (x > y){
	console.log("x is the biggest number")}
else { 
    console.log("y is the biggest number")}

//Exercise 2:Chihuahua

    let newDog = "Chihuahua"
    console.log("The length of Chihuahua is: "+ newDog.length)
    console.log(newDog.toUpperCase())
    console.log(newDog.toLowerCase())

    if (newDog == "Chihuahua"){
    	console.log ("I love Chihuahuas, it’s my favorite dog breed")}
    else{
    	console.log("I dont care, I prefer cats")}


//Exercise 3: Even Or Odd
    let num1 = prompt("Please enter a number");
       num2 = Number(num1)
       if(num2 % 2 == 0) {
          console.log("The number "+ num1 + " is even.");}
        else {
           console.log("The number "+ num1 + " is odd.");} */

//Exercise 4: Group Chat

let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"];
    let n = users.length
       switch(n){
    	 case 0:
    	 if (n == 0) 
    	 console.log('no one is online');
        break;
         case 1:
        if (n == 1 ) console.log(users[0] + " is online");
        break;
         case 2:
        if (n == 2 ) console.log(users[0] + " and " + users[1]+ " are online");
        break;
         default: 
        	if (n ==n) 
        		console.log(users[0] + " , " + users[1]+ " and "+(n-2) + " more are online");
        break;
    }