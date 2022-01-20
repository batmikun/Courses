import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css';
import { router } from './router/index.router.js'
console.log(window.location.pathname);
router(window.location.pathname);

window.addEventListener('hashchange', () => {
    router(window.location.hash)
});