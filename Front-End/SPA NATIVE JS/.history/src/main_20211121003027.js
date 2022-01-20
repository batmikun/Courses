import './main.css';
import { router } from './router/index.router.js'

window.addEventListener('load', () => {
    console.log('Hola');
});
router(window.location.pathname);

const menuBtn = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
})

let navBtn = document.querySelectorAll('.navbar__link');

for (let btn of navBtn) {
    btn.addEventListener('click', (e) => {
        const route = btn.id
        route.toLowerCase()
        router(`/${route}`)
    })
}