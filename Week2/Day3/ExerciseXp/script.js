/* //Exercise 1: List of People

    let people = ["Greg", "Mary", "Devon", "James","Jayesh","Nayar"];
      const firstitem = people.shift(); //removing "Greg from the array"
      console.log(people);

      people[2]= "Jason" //renaming James to Jason
      console.log(people)

      people.push("Avishek") //Adding my name at the end of the array 
      console.log(people)
      
      let index = people.indexOf("Mary"); //finding the index of "Mary" in the array
      console.log("The index of Marry is : " + index )

      let newlist = people.slice(1,-1)//displaying new list excluding first and last item in the array 
      console.log("New list of people is: " + newlist)

      let int = people.indexOf("foo"); //finding the index of an item not in the array
      console.log("Index of foo is: "+ int) // display -1 because item not in array 

      let last = people[people.length - 1]; //Geting to the last item to the array
      console.log("The last item in the array is: "+last)

      let last1 = people.slice(-1); //fetching last item using slice function
      console.log( "The last item in the array is: " + last1)

      //"index of" is the position of the item in the array  
      //"length of" is how many item in the array 

//Part II - Loops
      
      for (i in people) //using loop to display all item in array people 
      	console.log(people[i])

      console.log("") //Breaking the display when jason is encountered

      for (i in people){ 
      	if (people[i] == "Jason")
      		break
      	console.log(people[i])}

      	console.log("")

//Exercise 2 : Your Favorite Colors
   let colors = ["Red","Blue","Green","Orange","Black"];
   let sup = ["st","nd","rd","th","th"];
     for (let i =0 ; i < colors.length ; i++){
	  console.log("My " + (i+1)+ sup[i] +" color is: " +colors[i])}

//Exercise 3 : Repeat The Question
    let b = 0;
     while (b<10){
     let a = prompt("Please enter a Number:")
         b = Number(a);
    console.log("entered number is less than 10")} */

//Exercise 4 : Building Management
/*
       let building = {
    numberOfFloors : 4,
    numberOfAptByFloor : {
        firstFloor : 3,
        secondFloor : 4,
        thirdFloor : 9,
        fourthFloor : 2,
                },
    nameOfTenants : ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:{
        sarah: [3, 990],
        dan :  [4, 1000],
        david : [1, 500],
                          },
                          }
      console.log("There are " + building.numberOfFloors +" floors")
      console.log("There are " + building.numberOfAptByFloor.firstFloor + " Apt on the first floor")
      console.log("There are " + building.numberOfAptByFloor.thirdFloor + " Apt on the third floor")
      console.log(building.nameOfTenants[1])
      console.log("The second tenant is " + building.nameOfTenants[1]  + " and has " + building.numberOfRoomsAndRent.dan[0] +" in his appartment")

        //console.log(building.numberOfRoomsAndRent.sarah[1])
        //console.log(building.numberOfRoomsAndRent.david[1])
        //console.log(building.numberOfRoomsAndRent.dan[1])

        let a = building.numberOfRoomsAndRent.sarah[1]
        let b = building.numberOfRoomsAndRent.david[1]
        let c = a + b
        let d = building.numberOfRoomsAndRent.dan[1]

       // console.log(a)  checking if variable has been properly assing 
        //console.log(b)
       // console.log(d)
          console.log("The sum of Sara and David is: " + c)

             if (c< d){
        	  d= d+200 ;}
        console.log("The new rent for dan is: " + d)
        building.numberOfRoomsAndRent.dan[1] = d 
        console.log("details of dan: "+ building.numberOfRoomsAndRent.dan ) 
        */
/*
//Exercise 5 : Family

        let family = {
        	Surname:"Ramjeeawon",
        	FirstName: "Avishek",
        	Address: "Brach Road",
        	Village: "Roches-Noires"};
        for (let x in family){
        	console.log(x)}

        for (let r in family){
            console.log(family[r])} 

*/

//Exercise 6
/*

    let details = {
      my: 'name',
      is: 'Rudolf',
      the: 'raindeer'
                    }
    let str = " "
     for ( t in details){

      str = str + t+ " " + details[t]+ " " 

        }
        console.log(str) */

 /*
//calculate year 
   const currentYear = new Date().getFullYear();
   console.log("this is the current year " + currentYear);

     let u = 1998   //older date of birth
     let o = 2015   //younger date of birth
     let p = currentYear - u //older current age
     let v = currentYear - o //younger current age
     let n = o - u //the age difference between both
     let r = "1" 
     let i = n
     console.log("the age of elder " +p)
     console.log("the age of younger " +v)
     console.log("the age difference is " +n)

    do {
        let y = r/i
        r++
        i++
        if (y == 0.5){
          let newyear= o + r
          console.log("the year the younger will be half the age of the older is: "+newyear )

                      }}
	while (  i < 50 )


*/
//Exercise 7 : Secret Group
  let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle","Avishek"];     
	let firstletter = []
    for (name of names){
        firstletter.push(name.charAt(0))
    }
       firstletter=firstletter.sort()

       firstletter = firstletter.join("")
       console.log(firstletter)







