import 'bootstrap/dist/css/bootstrap.min.css';
import './main.css';

window.addEventListener('hashchange', () => {
    console.log(window.location.hash);
});