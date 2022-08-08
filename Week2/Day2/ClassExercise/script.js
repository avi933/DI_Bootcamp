//Exercise 1 
/*
   let age = prompt('How old are you?', 20);
       age = Number(age)

        if (age === 18){
        alert("Congratulations on your first year of driving. Enjoy the ride!") 
    }   else if (age < 18) {
        alert("Sorry, you are too young to drive this car. Powering off")
    }   else {
        alert("Powering On. Enjoy the ride!")
    } 
    */

//Exercise 2 
/*
     let a = 2 + 2;

         switch (a) {
         case 3:
              alert( 'Too small' );
         break;
         case 4:
              alert( 'Exactly!' );
         break;
         case 5:
              alert( 'Too large' );
         break;
         default:
              alert( "I don't know such values" );}
//Expected to display "Exctly!" because value of a will be 4

*/

//Exercise 3 
 /*
    let a = 2 + 2;

    switch (a) {
       case 4:
            alert('Right!');
       break;

       case 3:
       case 5:
            alert('Wrong!');
            alert("Why don't you take a math class?");
       break;

       default:
            alert('The result is strange. Really.');}
            */

// Ojects

//Exercise 1

        let signin ={
              username:"Avi",
              password: "vatel", };

       let database =[signin]

       let newsfeed = [ 
       {
       username = signin.username,
       timeline : 1,
       }

       {
       username = signin.username
       timeline: 2,}

       {
       username = signin.username
       timeline = 3,} 
       ]
       console.log(newsfeed)

