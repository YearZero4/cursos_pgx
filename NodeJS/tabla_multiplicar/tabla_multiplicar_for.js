const prompt = require('prompt-sync')();

const numero = parseInt(prompt("Ver la tabla del numero = "))

let n;
let n2 = 10;

for(n=1; n<=n2 ; n++){
 console.log(`${numero} X ${n} = ${numero*n}`);
}
