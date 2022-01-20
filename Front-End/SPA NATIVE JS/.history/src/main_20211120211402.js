import { Library } from '@fortawesome/fontawesome-svg-core';
import { fas } from '@fortawesome/free-solid-svg-icons';
import { far } from '@fortawesome/free-regular-svg-icons';
import './main.css';
import { router } from './router/index.router.js'
router(window.location.pathname);

const menuBtn = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('is-active');
    menuLinks.classList.toggle('active');
})

let navBtn = document.querySelectorAll('.nav__link');

for (let btn of navBtn) {
    btn.addEventListener('click', (e) => {
        const route = btn.id
        route.toLowerCase()
        router(`/${route}`)
    })
}