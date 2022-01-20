import view from '../views/products.html'

const getPosts = async () => {
    const response = await fetch('https://jsonplaceholder.typicode.com/posts')
    return await response.json();
}

export default async () => {
    const divElement = document.createElement('div')
    divElement.innerHTML = view

    const postElement = divElement.querySelector('#posts')

    const posts = await getPosts()

    posts.forEach(post => {
    })

    return divElement
}