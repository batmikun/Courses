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
        postElement.innerHTML += `
            <li class="list-group">
                <h4>${post.title}</h4>
                <p>${post.body}</p>
            </li>
        `
    })

    return divElement
}