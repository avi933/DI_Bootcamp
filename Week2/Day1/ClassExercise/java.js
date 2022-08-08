console.log("hello worold from external file")

let x =3
let y =5
let c = x+y
console.log(c)

let Avishek = "Best student"
let mika = 99 
console.log(Avishek)
console.log(mika + "marks")

//Exercise 1

let addressNumber = "Roches-Noire "
let addressStreet = "Branch Road "
let country = "Mauritius"

let globalAddress ="I live at " + addressStreet + addressNumber + country
console.log(globalAddress)

//Exercise 2

let a = 1993
let b = 2030
let e = b - a
let f = "I will be " + e

console.log(f + " in " + b )

//Arays Example

    let arrayName = ["Avi", "Mika", "Jayesh"]
    console.log(arrayName)

//position in arry
    let colors = ["blue", "yellow", "green", 54]; 
    let favorite = colors[0];
    let secondFavorite = colors[2];
    console.log(favorite)
    console.log(secondFavorite)

//changing item in an array
     let g = ["blue", "yellow", "green"]; 
     g[0] = "pink"
     console.log(g) 
//array Mehtods
    //adding an item in an arry
        colors.push("orange") 
        console.log(colors)
    //removing last item from array
        colors.pop() 
        console.log(colors)
    //taking data from array and convert to string
        let colorstring = colors.toString() 
        console.log(colorstring) 
        console.log(colors) 
//Exercise3
    
        let animal=["cat","dog","fish","rabbit","cow"]
    //showing the initial array
    console.log(animal+" :-This is the inital array")
    //displaying dog from the array
        console.log(animal[1] +" :-showing array index 1")
    //replacing rabbit to horse
         animal[3]="horse"
         console.log(animal + " :-replacing rabbit to horse in array ")
    //showing the length of the array
    console.log(" This array contains: " + animal.length + " items")

//UserInterface Functions 
     //sending a message
       alert("Hello");
    //asking user for input
       let age = prompt('How old are you?', 20);
       alert(`You are ${age} years old!`);
    //confrimation
        let isBoss = confirm("Are you the boss?");
        alert(isBoss);




