function abrirMenu() {
    const cbx = document.getElementById('cbx')
    const menu = document.getElementById("menu")

    if (!cbx.checked) {
        menu.style.display = 'flex';
    } else {
        menu.style.display = 'none';
    }
}


function entrarLogin() {
    window.location = '../login/index.html'
}