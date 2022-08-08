
// Exercise 1: Timer
     /*
    //Part I : using setTimeout,alert “Hello World” after 2 sec
         function hello() {
            alert( "Hello World" );}
         setTimeout(hello, 2000);
    //Part II : call a function after 2 seconds,add a new paragraph <p>Hello World</p> to div

      function para() {
      	let x = document.getElementById('container')
            let p =  document.createElement("p")
            p.innerHTML = "Hello World"
            x.appendChild(p)
            }
            para()
         */
    //Part III : using setInterval, call a function will add a new paragraph every 2 sec
            
            
             function para() {
      	       let x = document.getElementById('container')
               let p =  document.createElement("p")
               p.innerHTML = "Hello World"
               x.appendChild(p)}


               let i = 0
          let timer =  setInterval(function() {
                 
                 para()
                     i = i+1 

                     if ( i >=5 )
              clearInterval(timer)}, 2000);


          

           


             
         