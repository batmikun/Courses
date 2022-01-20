import './main.css';
import { router } from './router/index.router.js'
router(window.location.pathname);

const hamburguer = document.querySelector('.hamburguer');

hamburguer.addEventListener('click', function () {
    this.classList.toggle('is-active');
});


let navBtn = document.querySelectorAll('.nav__link');

console.log(navBtn);

for (let btn of navBtn) {
    btn.addEventListener('click', (e) => {
        const route = btn.id
        route.toLowerCase()
        router(`/${route}`)
    })
}