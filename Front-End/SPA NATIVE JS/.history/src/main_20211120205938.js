import './main.css';
import { router } from './router/index.router.js'
router(window.location.pathname);

const menuBtn = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('#mobile-menu-links');

let navBtn = document.querySelectorAll('.nav__link');

for (let btn of navBtn) {
    btn.addEventListener('click', (e) => {
        const route = btn.id
        route.toLowerCase()
        router(`/${route}`)
    })
}