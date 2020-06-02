var totalDigits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"];
sum = 0;
function solve () { 
for (let i = 1234; i < 9876 ; i++)  {
   var digits = (""+i).split("");
   var setDigits = new Set(digits);
   //cant be added if duplicates or has 0
   if (!hasDuplicates(digits) && !setDigits.has("0")) {
      var a = totalDigits;
      //finding leftover digits
      var difference = [...new Set([...a].filter(x => !setDigits.has(x)))];
      if (checkPan(i, difference)) {
        sum+=i
        console.log(i)
      }
   }    
}
  
return "sum is " + sum;
}

function hasDuplicates(array) {
    return (new Set(array)).size !== array.length;
}


function checkPan(num, remainDig) {
    //find all factors of i
     var factArr = getFactors(num);
    //sort factor array
     factArr = factArr.sort((a, b) => a - b);
    //sort leftover digits being passed in
     var sortedDig = remainDig.sort();
    //check if digits of factors match with leftover digits array
     for (let m = 0; m < factArr.length; m++) {
     var firstNum = factArr[m].toString().split("")
     var secondNum = factArr[factArr.length - m - 1].toString().split("");
     var factArr2 = firstNum.concat(secondNum).sort();
     if (arraysEqual(factArr2, sortedDig)) {
       return true;
     }
     }
   return false;
}
function getFactors(num) {
  const isEven = num % 2 === 0;
  let inc = isEven ? 1 : 2;
  let factors = [1, num];
  for (let curFactor = isEven ? 2 : 3; Math.pow(curFactor, 2) <= num; curFactor += inc) {
    if (num % curFactor !== 0) continue;
    factors.push(curFactor);
    let compliment = num / curFactor;
    if (compliment !== curFactor) factors.push(compliment);
  }
  return factors;
}

function arraysEqual(a1,a2) {
   return JSON.stringify(a1)==JSON.stringify(a2);
}

console.log(solve())