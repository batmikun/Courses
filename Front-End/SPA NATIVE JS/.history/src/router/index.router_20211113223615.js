const router = (route) => {
    switch (route) {
        case '#/':
            return 'home';
        case '#/products':
            return 'products';
    }
}
export { router };