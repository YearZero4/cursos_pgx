const axios = require('axios');

console.log("[+] Realizando peticion a Google\nComenzaremos en 2 segundos")

setTimeout(() => {
 axios.get("https://www.google.com")
 .then(response => {
  console.log(response.data);
 })
 .catch(error => {
  console.log("error al realizar solicitud");
 })
 
}, 2000)

