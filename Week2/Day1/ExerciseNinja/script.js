     5 >= 1
//expexted :true
//result: true
    0 === 1
//expexted : false
//result:false
    4 <= 1
//expexted :false
//result:false
    1 != 1
//expexted :false
//result:false
    "A" > "B"
//expexted :true
//result:true
    "B" < "C"
//expexted :true
//result:true
    "a" > "A"
//expexted :false
//result:false
    "b" < "A"
//expexted :false
//result:false
    true === false
//expexted :false
//result:false
    true != true
//expexted :false
//result:false


//Exercise 2: Ask for number then add up
    let Num = prompt("Please enter the numbers to be added seperated by a , ")
    let Num1 = Num.replace(/,/g, "+")
    let result = eval(Num1)
    console.log(result)

//Exercise 3:
 
 let p = prompt( "please enter your text with nemo");
 if (p.search("nemo") != -1) {
    console.log("I fount nemo at " + p.indexOf("nemo") )
} else {
    console.log("I cannot find nemo")
}
