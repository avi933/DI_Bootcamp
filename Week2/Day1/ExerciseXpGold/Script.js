//Exercise 1

    let sentence = ["my","favorite","color","is","blue"];
    console.log(sentence.toString())

//Exercise 2: joinig two word

     let str1 = "mix";
     let str2 = "pod";
     let a = str1.substring(0,2)
     let b = str2.substring(0,2)
     let c = a.concat(" ",b)
     console.log(c)


//Exercise 3 : Calculator
    
        const num1 = parseInt(prompt('Enter the first number '));
        const num2 = parseInt(prompt('Enter the second number '));
        const num3 = parseInt(prompt('operation to be carried '));
       
//add two numbers
     const sum = num1 + num2;
     

// display the sum
     console.log(`The sum of ${num1} and ${num2} is ${sum}`);
     alert(`The sum of ${num1} and ${num2} is ${sum}`);
     
