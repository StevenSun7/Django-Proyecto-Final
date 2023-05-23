
        // Esta función valida todos los campos del form.
        // Si alguno no cumple con los requisitos, se aborta
        // con return. Caso contrario, al final se realiza
        // efectivamente el envio de los datos.

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
            tel = document.comprobacion.tel.value
            tel = validarTel(tel)
            document.comprobacion.tel.value = tel
            if (tel == "") {
                document.comprobacion.tel.focus()
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
                alert("Ingresar el numero telefonico sin espacios")
                    document.comprobacion.tel.focus()
                return ""
            } else {
                return valor
            }
        }
