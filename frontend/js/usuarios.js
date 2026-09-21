// URL base del servicio de usuarios en el backend
const API_URL = "http://127.0.0.1:5000/api/usuarios";

// Referencias a los elementos del DOM
const vistaLista = document.getElementById("vista-lista");
const vistaForm = document.getElementById("vista-form");
const btnVerLista = document.getElementById("btn-ver-lista");
const btnVerForm = document.getElementById("btn-ver-form");
const tbody = document.querySelector("#tabla-usuarios tbody");
const formUsuario = document.getElementById("form-usuario");
const divMensaje = document.getElementById("mensaje");

// Control de navegación entre vistas (listado y formulario)
btnVerLista.addEventListener("click", () => {
    vistaLista.classList.remove("oculto");
    vistaForm.classList.add("oculto");
    btnVerLista.classList.add("activo");
    btnVerForm.classList.remove("activo");
    divMensaje.style.display = "none";
    cargarUsuarios();
});

btnVerForm.addEventListener("click", () => {
    vistaForm.classList.remove("oculto");
    vistaLista.classList.add("oculto");
    btnVerForm.classList.add("activo");
    btnVerLista.classList.remove("activo");
    divMensaje.style.display = "none";
});

// Despliegue de notificaciones de estado (éxito o error)
function mostrarMensaje(texto, tipo) {
    divMensaje.textContent = texto;
    divMensaje.className = tipo;
    
    // Ocultar la notificación tras 4 segundos
    setTimeout(() => { 
        divMensaje.style.display = "none"; 
        divMensaje.className = ""; 
    }, 4000);
}

// Consulta y renderizado del listado de usuarios
async function cargarUsuarios() {
    try {
        const respuesta = await fetch(API_URL);
        if (!respuesta.ok) throw new Error("Error en la respuesta del servidor");
        
        const usuarios = await respuesta.json();
        
        // Limpieza de datos previos en la tabla
        tbody.innerHTML = "";
        
        usuarios.forEach(u => {
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${u.id}</td>
                <td>${u.identificacion}</td>
                <td>${u.nombre}</td>
                <td>${u.apellido}</td>
                <td>${u.correo}</td>
                <td>${u.telefono}</td>
                <td><strong>${u.rol.toUpperCase()}</strong></td>
            `;
            tbody.appendChild(fila);
        });
    } catch (error) {
        // Notificación en caso de fallo de conexión con el backend
        mostrarMensaje("Error: No fue posible conectarse con el servidor.", "error");
    }
}

// Manejo del formulario para el registro de un nuevo usuario
formUsuario.addEventListener("submit", async (e) => {
    e.preventDefault();

    // Mapeo de los campos del formulario a un objeto plano
    const datosFormulario = Object.fromEntries(new FormData(e.target));

    try {
        const respuesta = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(datosFormulario)
        });

        const resultado = await respuesta.json();

        if (respuesta.ok) {
            mostrarMensaje(resultado.message, "ok");
            formUsuario.reset();
            // Retorno automático a la vista de listado tras registro exitoso
            setTimeout(() => btnVerLista.click(), 1500); 
        } else {
            // Manejo de respuestas de validación o conflicto del servidor
            mostrarMensaje(resultado.message, "error");
        }
    } catch (error) {
        mostrarMensaje("Error: No fue posible conectarse con el servidor.", "error");
    }
});

// Carga inicial de usuarios al iniciar la vista
cargarUsuarios();