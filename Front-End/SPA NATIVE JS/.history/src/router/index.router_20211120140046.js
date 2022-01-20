import { routes } from './routes'

let content = document.getElementById('root');
let router = async (route) => {
    content.innerHTML = ' ';

    window.history.pushState({}, route, window.location.origin + route)

    switch (route) {
        case '/':
            return content.appendChild(routes.home());
        case '/Products':
            return content.appendChild(await routes.products());
        default:
            return content.appendChild(routes.notFound());
    }
}
export { router };