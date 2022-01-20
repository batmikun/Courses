import { routes } from './routes'

let content = document.getElementById('root');
let router = async (route) => {
    content.innerHTML = ' ';
    switch (route) {
        case '/':
            window.history.pushState({}, route, window.location.origin + route)
            return content.appendChild(routes.home());
        case '/products':
            window.history.pushState({}, route, window.location.origin + route)
            return content.appendChild(await routes.products());
        default:
            window.history.pushState({}, route, window.location.origin + route)
            return content.appendChild(routes.notFound());
    }
}
export { router };