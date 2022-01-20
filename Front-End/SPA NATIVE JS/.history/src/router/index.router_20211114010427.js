import { routes } from './routes'

let content = document.getElementById('root');
let router = (route) => {
    content.innerHTML = ' ';
    switch (route) {
        case '#/':
            return content.appendChild(routes.home());
        case '#/products':
            return console.log('Products');
        default:
            return console.log('404');
    }
}
export { router };