function solve() {
let numProd = 1;
let denProd = 1;
    for (let i = 11; i < 100; i ++) {
       for (let j = i + 1; j  < 100; j++) {
         if (split(i, j) && i % 10 != 0) {
           numProd = numProd * i
           denProd = denProd * j
         }
       } 
      
    }
return findDenom(numProd, denProd);   
}
function split(num, den) {
    var decimal = den / num;
    var numArr = num.toString().split('').map(Number);
    var denArr = den.toString().split('').map(Number);
    for (let i = 0; i < numArr.length; i++) {
      for (let j = 0; j < denArr.length; j++) {
          if (numArr[i] === denArr[j]) {
             numArr.splice(i, 1);
             denArr.splice(j, 1)
             if (denArr[0] / numArr[0] === decimal) {
               return true;
             }
          }
      }
    }
  return false;
}
function findDenom(num1, num2) {
if (num2 % num1 === 0) {
  return num2 / num1;
}
else {
  //do other stuff
}
}

console.log(solve())