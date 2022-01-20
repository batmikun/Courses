import Home from '../viws/home'

const router = (route) => {
    switch (route) {
        case '#/':
            return;
        case '#/products':
            return console.log('Products');
        default:
            return console.log('404');
    }
}
export { router };