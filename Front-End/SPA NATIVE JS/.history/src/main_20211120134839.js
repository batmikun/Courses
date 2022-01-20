import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css';
import { router } from './router/index.router.js'
router(window.location.pathname);

let navBtn = document.querySelectorAll('.nav-link');

console.log(navBtn);

navBtn.foreach((element) => {
    element.addEventListener('click', (e) => {
        console.log('click');
    })
})