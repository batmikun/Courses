import Home from '../controllers/home'

let content = document.getElementById('root');
let router = (route) => {
    content.innerHTML = ' ';
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