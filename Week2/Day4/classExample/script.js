
//Exercise 1 : Information 
  //Part I : function with no parameters
      /*
       function infoAboutMe(){
	    console.log(" My name is Avishek")}
        infoAboutMe()

   //Part II : function with three parameters

        function infoAboutPerson(personName, personAge, personFavoriteColor){
        	console.log ("You name is "+ personName+ " you are "+personAge+ " years old, your favorite color is " + personFavoriteColor)
             }
               infoAboutPerson("David", 45, "blue")
               infoAboutPerson("Josh", 12, "yellow")
        */

//Exercise 2 : Tips
 
      /*
      	
      function calculateTip(){
      	let y = prompt("Enter bill amount")
      	let x = Number(y)
      	let tip = 0
      	if (x<50){
      		tip = (0.2*x)}
      	else if( x>=50 && x<=200 ){
      		tip = (0.15*x)}
      	else
      		tip = (0.1*x)

      	console.log("The tip is $"+tip+ " and the final bill is $"+ (tip+x) )}

      	calculateTip()
      
     */

// Exercise 3 : Find The Numbers Divisible By 23
    /*
   function isDivisible(){
   	    let arr = []
        let sum = 0
   	 for ( let i =0; i <=500; i++) 
   	    if ( i%23 ===0 ){
   	  	arr.push(i)
   	  	sum = sum + i}
   	  	console.log("The numbers that are divisible are: "+ arr)
   	  	console.log("The sum is: " + sum)}

   	isDivisible()
   
    */

//Exercise 3 : with parameter
     /*  
    function isDivisible(divisor){
   	    let arr = []
        let sum = 0
   	 for ( let i =0; i <=500; i++) 
   	    if ( i% divisor ===0 ){
   	  	arr.push(i)
   	  	sum = sum + i}
   	  	console.log("The numbers that are divisible by " + divisor+" are: "+ arr)
   	  	console.log("The sum is: " + sum)}

   	isDivisible(3)
   	isDivisible(45)
        */


//Exercise 4 : Shopping List
     /*
      let stock = { 
               "banana": 6, 
               "apple": 0,
               "pear": 12,
               "orange": 32,
               "blueberry":1}  

      let prices = {    
               "banana": 4, 
               "apple": 2, 
               "pear": 1,
               "orange": 1.5,
               "blueberry":10}
     let shoppingList = ["banana", "orange","apple"]

     function myBill(){            
        let sum = 0
        
            for (let x in shoppingList)
              {
                  let t =  stock[shoppingList[x]]

                  if (t === 0){ console.log (shoppingList[x] +" is out of stock")}

                  else{

                sum = prices[shoppingList[x]] + sum

                let u = stock[shoppingList[x]] - 1
                 
                  console.log(shoppingList[x], prices[shoppingList[x]])}  

               }
                  console.log("Sum is : $" + sum)
                  
                   }                                  
                   
                       
    myBill()
       */

//Jayesh
     /*
    let Asset = Number(prompt("enter Asset value"))
    let liability = Number(prompt("enter liability"))
    let Num_share = Number(prompt("Enter number of shares"))

    let Equity = Asset - liability 
     console.log("company equity is " + Equity)

     let nav = Equity/Num_share

      console.log ("nav is " + nav)
     */

     
