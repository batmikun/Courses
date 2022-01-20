const router = (route) => {
    switch (route) {
        case '#/':
            return console.log('Home');
        case '#/products':
            return console.log('Products');
    }
}
export { router };