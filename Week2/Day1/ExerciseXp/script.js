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
