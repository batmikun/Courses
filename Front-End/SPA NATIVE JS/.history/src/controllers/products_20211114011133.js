import view from '../views/products.html'

const getPosts = async () => {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts')
    return await response.json();
}

export default () => {
    const divElement = document.createElement('div')
    divElement.innerHTML = view

    return divElement
}