import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css';
import { router } from './router/index.router.js'

window.addEventListener('hashchange', () => {
    router(window.location.hash)
});