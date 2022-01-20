import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css';
import { router } from './router/index.router.js'
router(window.location.pathname);

let navBtn = document.querySelectorAll('.nav-link');

navBtn.foreach((element) => {
    element.addEventListener('click', (e) => {
        e.preventDefault();
        router(element.getAttribute('href'));
    })
})
navBtn.addEventListener('click', () => {
    console.log('click');
});