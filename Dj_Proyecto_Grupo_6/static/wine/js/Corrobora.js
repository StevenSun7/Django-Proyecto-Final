
function validateForm() {
    var apellido = document.forms["comprobacion"]["id_apellido"].value;
    var nombre = document.forms["comprobacion"]["id_nombre"].value;
    var email = document.forms["comprobacion"]["id_email"].value;
    var telefono = document.forms["comprobacion"]["id_telefono"].value;

    if (apellido === "") {
        alert("Por favor, ingrese su apellido.");
        return false;
        }
    if (nombre === "") {
        alert("Por favor, ingrese su nombre.");
        return false;
        }
    if (email === "") {
        alert("Por favor, ingrese su correo electrónico.");
        return false;
        }
    if (telefono === "") {
        alert("Por favor, ingrese su número de teléfono.");
        return false;
        }
    }






