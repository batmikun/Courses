import Home from '../views/home'

const content = document.getElementById('root');

const router = (route) => {
    switch (route) {
        case '#/':
            return content.appendChild(Home());
        case '#/products':
            return console.log('Products');
        default:
            return console.log('404');
    }
}
export { router };