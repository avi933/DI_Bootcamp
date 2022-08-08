/*
//Exercise 1 -- for loop 
for (let i = 0; i <15; i++){
       if(i % 2 == 0) {
          console.log("The number "+ i + " is even.");}
        else {
           console.log("The number "+ i + " is odd.");}}
*/

//Exercise 2 

let names= ["john", "sarah", 23, "Rudolf",34,"avishek","jayesh",35,67]
for (let i in names){

	let a = typeof(names[i])
    if (a != "string"){
    	break;
    	}

    	names[i] = names[i].charAt(0).toUpperCase() + names[i].slice(1);
    	console.log(names[i])
    /*
    const str = names[i]
    const arr = str.split(" ");
    for (let i = 0; i < arr.length; i++) {
      arr[i] = arr[i].charAt(0).toUpperCase() + arr[i].slice(1);}
        const str2 = arr.join();
        console.log(str2);
        */
    }

