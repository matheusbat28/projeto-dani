let numero = document.getElementById('numero');

let numeroInt = parseInt(numero.value)

function menos() {
    event.preventDefault();
    if (numero.value >= 1){
        numero.value -= 1
    }
}
function mais() {
    event.preventDefault();
    numeroInt += 1
    numero.value = numeroInt
}