import Home from '../viws/home'

const router = (route) => {
    switch (route) {
        case '#/':
            const root = document.getElementById('root');
            return document.get;
        case '#/products':
            return console.log('Products');
        default:
            return console.log('404');
    }
}
export { router };