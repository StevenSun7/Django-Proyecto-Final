// Esta función valida todos los campos del form.
// Si alguno no cumple con los requisitos, se aborta
// con return. Caso contrario, al final se realiza
// efectivamente el envio de los datos
function checkEnviar() {
    //valido el nombre
    if (document.comprobacion.apellido.value.length  == 0) {
        alert("Ingresar Apellido por favor")
        document.comprobacion.apellido.focus()
        return 0
    }
    if (document.comprobacion.nombre.value.length  == 0) {
        alert("Ingres Nombre por favor.")
        document.comprobacion.nombre.focus()
        return 0
    }
    if (document.comprobacion.email.value.length  == 0) {
        alert("Ingrese Mail por favor.")
        document.comprobacion.email.focus()
        return 0
    }
    tel = document.comprobacion.telefono.value
    tel = validarTel(tel)
    document.comprobacion.telefono.value = tel
    if (tel == "") {
        document.comprobacion.telefono.focus()
        return 0
    }
    if (document.comprobacion.consulta.selectedIndex == 0) {
        alert("Seleccione una de las opciones consulta.")
        document.comprobacion.consulta.focus()
        return 0
    }
    alert("Muchas gracias. El formulario fue enviado con exito.")
    document.comprobacion.submit()
}

function validarTel(valor) {
    valor = parseInt(valor)
    //Compruebo si es un valor numérico
    if (isNaN(valor)) {
        alert("El campo de teléfono debe contener solo números sin espacios")
            document.comprobacion.telefono.focus()
        return ""
    } else {
        return valor
    }
}



// function validateForm() {
//     var apellido = document.forms["comprobacion"]["id_apellido"].value;
//     var nombre = document.forms["comprobacion"]["id_nombre"].value;
//     var email = document.forms["comprobacion"]["id_email"].value;
//     var telefono = document.forms["comprobacion"]["id_telefono"].value;

//     if (apellido === "") {
//         alert("Por favor, ingrese su apellido.");
//         return false;
//         }
//     if (nombre === "") {
//         alert("Por favor, ingrese su nombre.");
//         return false;
//         }
//     if (email === "") {
//         alert("Por favor, ingrese su correo electrónico.");
//         return false;
//         }
//     if (telefono === "") {
//         alert("Por favor, ingrese su número de teléfono.");
//         return false;
//         }
//     }






