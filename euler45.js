function generatePents() {
  for (let i = 144; i < 200000; i++) { 
    num = i*(2*i - 1);
    if (checkPent(num)) {
      return num;
    }
}
}

function checkPent(input) {
  return ((Math.sqrt(24*input+1)+1) % 6 === 0); 
}
    
function checkTri(input) {
  return((Math.sqrt(8 * input + 1) - 1) % 2 === 0);
}

console.log(generatePents());