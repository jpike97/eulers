function generatePents() {
  for (let i = 143; i < 1000000 i++;)
    num = i*(2*i - 1);
    if checkPent(num) && checkTri(num) {
      return num;
    }
}


function checkPent(input) {
  return ((Math.sqrt(24*input+1)+1) % 6 === 0); 
}
    
function checkTri(input) {
  return(Math.sqrt((sqrt(8n+1) - 1) % 2 === 0));
}

console.log(generatePents(10000));