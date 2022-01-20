import view from '../views/home.html'

export default () => {
    const divElement = document.createElement('div')
    divElement.innerHTML = view;

    const button = document.getElementsById('btnClick')
    button.addEventListener('click', () => {
        alert('Click');
    })

    return divElement;
}