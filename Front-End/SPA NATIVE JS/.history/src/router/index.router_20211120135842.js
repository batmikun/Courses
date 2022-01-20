import { routes } from './routes'

let content = document.getElementById('root');
let router = async (route) => {
    content.innerHTML = ' ';

    window.history.pushState({}, route, window.location.origin + route)

    switch (route) {
        case '/home':
            return content.appendChild(routes.home());
        case '/products':
            return content.appendChild(await routes.products());
        default:
            return content.appendChild(routes.notFound());
    }
}
export { router };