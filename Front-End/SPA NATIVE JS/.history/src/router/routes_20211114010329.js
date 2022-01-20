import Home from '../controllers/home';
import Products from '../controllers/products';
import notFound from '../controllers/404';


const routes = {
    home: Home,
    products: Products,
    notFound: notFound
};

export { routes };
