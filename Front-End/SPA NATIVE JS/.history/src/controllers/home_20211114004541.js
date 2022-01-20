import view from '../views/home.html'

export default () => {
    const views = `

    `;

    const divElement = document.createElement('div')
    divElement.innerHTML = views;

    return divElement;
}