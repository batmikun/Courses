import view from '../views/404.html'

const getPosts = async () => {
    await fetch('https://jsonplaceholder.typicode.com/posts')
}

export default () => {
    const divElement = document.createElement('div')
    divElement.innerHTML = view

    return divElement
}