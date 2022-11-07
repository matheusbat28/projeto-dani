let numero = document.getElementById('numero');


function menos() {
    event.preventDefault();
    numero.value = numero.value-1
}
function mais() {
    event.preventDefault();
    numero.value = numero.value+1
}