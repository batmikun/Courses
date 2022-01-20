import Home from '../views/home'

let content = document.getElementById('root');
content.innerHtml = '';

let router = (route) => {
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