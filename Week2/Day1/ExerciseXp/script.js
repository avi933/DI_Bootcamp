 //Exercise 1
    let favMeal = ["lunch","breakfast","dinner","souper"]
    let food = ["fried rice","plain rice","briyani","boiled noddles","fried noddles"]
    console.log("I eat " + food[3] +" at every " + favMeal[0])

//Exercise 2
     let myWatchedSeries = ["black mirror", "money heist", "the big bang theory"]
     let  myWatchedSeriesLength= myWatchedSeries.length
//displaying the lenght of the array
     console.log(myWatchedSeriesLength)
//displaying as a sentence
     let myWatchedSeriesSentence = myWatchedSeries.toString() 
     console.log(myWatchedSeriesSentence)
//adding both sentence above
     console.log("I watched " + myWatchedSeriesLength + " series : " + myWatchedSeriesSentence)

//changing "the bigban theory " to friends
      myWatchedSeries[2]="Friends"
      console.log(myWatchedSeries)
//add a serie name at the end of the array
      myWatchedSeries.push ("Tulsi")
      console.log(myWatchedSeries)
//replacing 1st item in the begining 
     myWatchedSeries[0]="Anupama"
     console.log(myWatchedSeries)


//Exercise 3: Temperature convertor

     let Temcl = prompt('Enter temperature in celsius', 20);
         let a = Temcl
         let b = (((a/5)*9) +32)
       alert(`The temperature in celsius is : ${Temcl} and in fahrenheit is : ${b.toFixed(0)} `);

//Exercise 4:

let c;
    let t = 34;
    let y = 21;

    console.log(t+y) //first expression
    // Prediction: 55
    // Actual: 55

    t = 2;

    console.log(t+y) //second expression
    // Prediction:23 
    // Actual: 23
    console.log(3+4+'5')
    //prediction:12
    //actual : 75

  typeof(15)
// Prediction: number
// Actual: number

typeof(5.5)
// Prediction: Number
// Actual:Number

typeof(NaN)
// Prediction: Number
// Actual:Number

typeof("hello")
// Prediction: string
// Actual: string

typeof(true)
// Prediction: boolean
// Actual: boolean

typeof(1 != 2)
// Prediction: true
// Actual: true

"hamburger" + "s"
// Prediction:hamburgers
// Actual: hambburgers

"hamburgers" - "s"
// Prediction:hamburger
// Actual:hamburger

"1" + "3"
// Prediction:4
// Actual:4

"1" - "3"
// Prediction: -2
// Actual: -2 

"johnny" + 5
// Prediction:johnny5
// Actual: johnny5

"johnny" - 5
// Prediction:NaN
// Actual:NaN

99 * "hello"
// Prediction: NaN
// Actual:Nan

1 != 1
// Prediction: false
// Actual:false

1 == "1"
// Prediction: true
// Actual:true

1 === "1"
// Prediction: false
// Actual: false


//Exercise 6:


5 + "34"
// Prediction: 39
// Actual: 39

5 - "4"
// Prediction:1
// Actual:1

10 % 5
// Prediction:0
// Actual:

5 % 10
// Prediction:5
// Actual:5

"Java" + "Script"
// Prediction: JavaScript
// Actual: JavaScript

" " + " "
// Prediction: blank
// Actual:blank

" " + 0
// Prediction:0
// Actual:0

true + true
// Prediction: true
// Actual:2

true + false
// Prediction: false
// Actual:1

false + true
// Prediction:false
// Actual: 1

false - true
// Prediction:-1
// Actual:-1

!true
// Prediction:false
// Actual: false

3 - 4
// Prediction: -1
// Actual: -1

"Bob" - "bill"
// Prediction: NaN
// Actual:NaN









