//Exercise 1 : The World Translator (Using if..else)
/*
   let ask = prompt("Which language do you speak?")
   let lower = ask.toLowerCase()
   console.log(lower)

   if (lower =="english" )
   	console.log("Hello")
   else if (lower=="french")
   	console.log("Bonjour")
   else if (lower=="hebrew")
   	console.log("Shalom")
   else
   	console.log("01110011 01101111 01110010 01110010 01111001")
*/

/*
//Exercise 1 ->Using switch case
  let ask = prompt("Which language do you speak?")
   let lower = ask.toLowerCase()
   console.log(lower)

  switch(lower){
  	case "english": 
  	console.log("Hello")
  	break;
  	case "french": 
    console.log("Bonjour")
    break;
    case "hebrew":
    console.log("Shalom")
    break;
    default :
    console.log("01110011 01101111 01110010 01110010 01111001")}
    */

/*
 //Exercise 2 : The Grade Assigner
 let grade = prompt("Enter mark to calculate the Grade")
   let grade1=Number(grade)
   if (grade1>90)
   	console.log("A")
   else if (grade1 <= 90 && grade1 >80)
   	console.log("B")
   else if (grade1 <=80 && grade1> 70)
   	console.log("C")
   else
   	console.log("D")
   */

  

//Exercise 3 : Verbing
   let verb = prompt("Please enter verb")
   let verb1 = verb.toLowerCase()
   let n =verb1.length
   let str = verb1;
   let part = /ing$/i;
   let result = str.match(part);

      console.log(result)
           if (n <3){
      console.log(verb1)} 

           else if (n >3 &&  result != null )
      console.log(verb1+"ly")

           else 
      console.log(verb1 + "ing")



