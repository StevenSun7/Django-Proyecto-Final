// Selecciones para Barra de navegación hamburguesa

const burger = document.querySelector("#menu-hamburguesa");
const ul = document.querySelector(".div-ul");
const nav = document.querySelector("nav");

burger.addEventListener("click", () => {
    ul.classList.toggle("show");
    });