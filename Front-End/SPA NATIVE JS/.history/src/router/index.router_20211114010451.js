import { routes } from './routes'

let content = document.getElementById('root');
let router = (route) => {
    content.innerHTML = ' ';
    switch (route) {
        case '#/':
            return content.appendChild(routes.home());
        case '#/products':
            return content.appendChild(routes.products());
        default:
            return content.appendChild(routes.notFound());
    }
}
export { router };