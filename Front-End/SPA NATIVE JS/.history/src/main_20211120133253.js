import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css';
import { router } from './router/index.router.js'

router(window.location.hash)

window.addEventListener('hashchange', () => {
    console.log(window);
    router(window.location.hash)
});