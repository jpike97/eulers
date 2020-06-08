const sieve2 = max => {
    
    const sieve = new Array(max).fill(true)
  
    
    for (let i = 2; i < Math.sqrt(max); i++) {
     
      if (sieve[i]) {
        for (let j = Math.pow(i, 2); j < max; j += i) {
          sieve[j] = false
        }
      }
    }

    for (let k = 3; k < sieve.length; k+=2) {
        if (!sieve[k]) {
          //check to see if conditions are satisfied
            if (!checkNum(k, sieve)) {
                return k;
            }
        }
    }
    
  }

function checkNum(currIndex, mySieve) {
  let myNum = 3;
    while (myNum < currIndex) {
        if (mySieve[myNum]) {
        for (let m = 1; m < Math.sqrt(currIndex) + 2 ; m++) {
            if (currIndex === myNum + 2*(m*m)) {
                return true;
            }
        }

        myNum = myNum + 2;
    }
    else { 
    
    myNum = myNum + 2;
    }
} 
}
console.log(sieve2(6000));