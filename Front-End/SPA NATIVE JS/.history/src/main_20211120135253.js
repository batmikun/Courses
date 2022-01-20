import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css';
import { router } from './router/index.router.js'
router(window.location.pathname);

let navBtn = document.querySelectorAll('.nav-link');

console.log(navBtn);

for (let btn of navBtn) {
    btn.addEventListener('click', (e) => {
        console.log(this.id)
    })
}