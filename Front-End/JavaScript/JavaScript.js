/**
 *
 * Tipo de datos primitivos
 * String, Number, Bool
 *
 * String = cadena de texto
 * Number = integer/float
 * Bool = true/false
 *
 * Otros tipos de datos
 * Undefined, null, NaN
 *
 * Undefined = la variable esta declarada pero no tiene valor.
 * Null = Indica que la variable esta vacia.
 * NaN = Not a Number. Es un valor que obtenemos cuando queremos realizar una operacion matematica con algo que no es un numero.
 *
 * Tipos de Variable
 * Si no definimos un tipo de variable, por defecto es una variable de scope global.
 * var => variable clasica, alcance global, posee alcance global porque se crean dentro de la instancia del objeto
 * windows. Posee function scope, va a vivir dentro de la funcion donde es definida. Si tenes una funcion dentro de una funcion, var es accesible desde el hijo
 * let => Block Scope, solo van a existir dentro de un bloque de codigo delimitado por {}
 * const => constante, no se puede cambiar el valor y se declara cuando se inicializa
 *
 * Hoisting
 * Fases de creacion y de ejecucion
 *
 * Refers to the process whereby the interpreter allocates memort for variables and function declarations prior to execution of the code
 * Declarations that are made using var are initialized with a default value of undefined. Declarations made using let and const are initialized as part of hoisting
 *
 * Conceptually hoisting is often presented as the interpreter "splitting variable declaration and initialization, and moving (just) the declarations to the top of the code"
 * This allows varaibles to appear in code before they are defined. Note however, that any variable initialization in the original code will not happen ultil the line of code is executed.
 *
 * You can use function before they are declared
 *
 * catName("tiger")
 *
 * function catName(name) {
 *  console.log("My Cat's Name is " + name);
 * }
 *
 * Javascript only hoists declarations, not initializations. If a variables is used in code and the declared and initialized, the value when it is used will be its defualt
 * initialization (undefined)
 *
 * Funcion prompt
 *
 * prompt es una funcion que sirve como el input de php o python
 *
 * let nombre = prompt('Decime tu nombre');
 *
 *
 * Array Methods
 *
 * push() => agrega un elemento al final del array
 * pop() => elimina el ultimo elemento del array
 * shift() => elimina el primer elemento del array
 * unshift() => agrega un elemento al principio del array
 * splice(index, 1) => elimina un elemento del array
 * splice(index, 0, "new element") => agrega un elemento al array
 * slice(start, end) => devuelve una copia del array desde el indice start hasta el indice end
 * indexOf(element) => devuelve el indice del elemento
 * lastIndexOf(element) => devuelve el indice del ultimo elemento
 * concat(array) => devuelve un nuevo array con los elementos del array actual y el array que se le pasa como parametro
 * join(separator) => devuelve un string con los elementos del array separados por el separador
 * reverse() => devuelve un nuevo array con los elementos del array actual en orden inverso
 * sort() => devuelve un nuevo array con los elementos del array actual ordenados
 * length => devuelve la cantidad de elementos del array
 * search(element) => devuelve el indice del elemento
 * filter(callback) => devuelve un nuevo array con los elementos del array actual que cumplan con la condicion que se le pasa como parametro
 * map(callback) => devuelve un nuevo array con los elementos del array actual modificados por la funcion que se le pasa como parametro
 * reduce(callback) => devuelve un valor con el resultado de aplicar la funcion que se le pasa como parametro a todos los elementos del array
 * reduceRight(callback) => devuelve un valor con el resultado de aplicar la funcion que se le pasa como parametro a todos los elementos del array
 * every(callback) => devuelve true si todos los elementos del array cumplen con la condicion que se le pasa como parametro
 * some(callback) => devuelve true si algun elemento del array cumplen con la condicion que se le pasa como parametro
 * forEach(callback) => ejecuta la funcion que se le pasa como parametro sobre cada elemento del array
 *
 *
 *
 * Type Methods
 * typeof variable => devuelve el tipo de dato de una variable
 *
 * Functions
 *
 * function nombreFuncion(parametros) {} Asi se declara una funcion
 *
 * nomFuncion(parametros) Y asi se llama a la funcion
 *
 * Otras maneras de declarar una funcion
 *
 * Funciones anonimas
 *
 *  let nomFuncion = function(parametros) {}
 *  let nomFuncion = (parameters) => {}
 *  nomFunction() Asi se llama a las variables guardadas en variables
 *  let nomFuncion = function(parametros) {}
 *  nomFuncion(parametros)
 *
 * Objectos
 *
 * let objeto = {
 *  propiedad: valor,    Valor puede ser cualquier tipo de dato
 * }
 *
 * Acceder a las propiedades de un objeto objeto.propiedad tambien se puede acceder con bracket notation.
 * Agregar nuevas propiedas con dot notation o bracket notation
 * Para borrar propiedades de un objeto se puede hacer con delete object.propiedad
 *
 * Check if an object has a property
 *
 * if (object.hasOwnProperty(property)) {}
 *
 * Loops
 *
 * for (let i = 0; i < array.length; i++) {}
 *
 * while (condition) {}
 * do {} while (condition)
 *
 * foreach (array as value) {}
 *
 *
 * return value || default => devuelve el valor si existe si no devuelve el otro valor
 *
 * Ternary Operator
 * condition ? statement-if-true : statement-if-false
 *
 * return num > 0 ? "positive" : num < 0 ? "negative" : "zero";
 *
 * Rest Operator
 * ...array => devuelve un array con todos los elementos del array que se le pasa como parametro
 *
 * Spread Operator
 *
 * let newArray = [...array1, ...array2, ...array3]; => devuelve un array con todos los elementos del array que se le pasa como parametro
 *
 * Destructuring
 *
 * let [a, b, c] = array; => devuelve un array con los elementos del array que se le pasa como parametro
 * let {propiedad1, propiedad2} = objeto; => devuelve un objeto con las propiedades del objeto que se le pasa como parametro
 * let {propiedad1: nombre1, propiedad2: nombre2} = objeto; => devuelve un objeto con las propiedades del objeto que se le pasa como parametro y los nombres que se le pasa como parametro
 *
 * Create Object
 *
 * const createPerson = (name, age, gender) => {
 *      return {
 *          name: name,
 *          age: age,
 *          gender: gender
 *      }
 * }
 *
 * An object can contain a function
 *
 * const bicycle = {
 *  gear: 2,
 *  seGear(newGear) {
 *      this.gear = newGear;
 *  }
 * }
 *
 * bicycle.setGear(3);
 *
 * Class syntax
 *
 * class Person {
 *  constructor(name) {
 *     this.name = name;
 *  }
 * }
 *
 * person1 = new Person("Juan");
 *
 *
 * class Person {
 *  constructor(name) {
 *     this._name = name;
 *  }
 *
 *  get name(){
 *     return this._name;
 *  }
 *
 *  set name(value){
 *   this._name = value;
 *  }
 *
 * }
 *
 * person1 = new Person("Juan");
 * person1.name = "Pedro"; Usando el setter
 * let name = person1.name; Usando el getter
 *
 * private variable inside a Class => _variable
 *
 * require() => importa un archivo
 *
 * import variable from "file" => importa una default variable de un archivo
 * import {variable} from "file"; => importa una variable de un archivo
 * import * as name from "file"; => importa todas las variables de un archivo
 * import {variable1, variable2} from "file"; => importa varias variables de un archivo
 * import {variable1 as name1, variable2 as name2} from "file"; => importa varias variables de un archivo y las renombra
 * import {variable1, variable2 as name2} from "file"; => importa una variable de un archivo y la renombra
 * import {function1, function2 as name2} from "file"; => importa una funcion de un archivo y la renombra
 *
 * export default variable => exporta una variable
 * export {variable} => exporta una variable
 * export {variable1, variable2} => exporta varias variables
 * export {variable1, variable2} from "file"; => exporta varias variables de un archivo
 * export function() {} => exporta una funcion
 * export class {} => exporta una clase
 *
 *
 * DOM
 *
 * Selectors
 *
 * document.getElementById("id"); => devuelve un elemento del DOM
 * document.getElementsByClassName("class"); => devuelve un array con todos los elementos del DOM que tengan la clase que se le pasa como parametro
 * document.getElementsByTagName("tag"); => devuelve un array con todos los elementos del DOM que tengan el tag que se le pasa como parametro
 * document.getElementsByName("name"); => devuelve un array con todos los elementos del DOM que tengan el nombre que se le pasa como parametro
 * document.getQuerySelector("selector"); => devuelve un elemento del DOM que cumpla con el selector que se le pasa como parametro
 *
 * Write to DOM
 *
 * document.getElementById("id").innerHTML = "text"; => escribe text en el elemento del DOM que tenga el id que se le pasa como parametro
 * Not use innerHTML to pass plain text
 *
 * Usar Esta funcion para pasar texto plano
 * selector.textContent = "text"; => escribe text en el elemento del DOM que tenga el selector que se le pasa como parametro
 *
 * Change Style
 *
 * selector.style.property = "value"; => cambia el valor de la propiedad property del elemento del DOM que tenga el selector que se le pasa como parametro
 *
 * Estos de abajo reemplazan todos los inline styles
 * selector.style.cssText = "property: value;"; => cambia el valor de varias propiedades del elemento del DOM que tenga el selector que se le pasa como parametro
 * selector.setAttribute("property", "value"); => cambia el valor de la propiedad property del elemento del DOM que tenga el selector que se le pasa como parametro
 *
 *
 * window => devuelve el objeto window
 * document => devuelve el objeto document
 *
 * Eventos
 *
 * onclick => cuando se hace click
 * oninput => cuando se escribe en un input
 * onmouseover => cuando se pasa el raton por encima
 * onmouseout => cuando se pasa el raton por fuera
 * onmousemove => cuando se mueve el raton
 * onkeydown => cuando se presiona una tecla
 * onkeyup => cuando se suelta una tecla
 * onkeypress => cuando se presiona una tecla
 * onchange => cuando se cambia el valor de un input
 * onsubmit => cuando se envia un formulario
 * onload => cuando se carga la pagina
 * onunload => cuando se cierra la pagina
 * onfocus => cuando se pone el foco en un input
 * onblur => cuando se quita el foco de un input
 * onscroll => cuando se hace scroll en un elemento
 * onresize => cuando se redimensiona la ventana
 * onbeforeunload => cuando se cierra la pagina
 * onerror => cuando se produce un error
 * onabort => cuando se aborta una peticion
 * onloadstart => cuando se inicia la carga de una pagina
 * onprogress => cuando se esta cargando una pagina
 * onloadend => cuando se termina la carga de una pagina
 * ontimeout => cuando se termina el tiempo de espera de una peticion
 * onloadeddata => cuando se carga la data de una pagina
 * oncanplay => cuando se puede reproducir una pagina
 * oncanplaythrough => cuando se puede reproducir una pagina hasta el final
 * ondurationchange => cuando se cambia la duracion de una pagina
 * onplay => cuando se reproduce una pagina
 * onplaying => cuando se esta reproduciendo una pagina
 * onpause => cuando se pausa una pagina
 * onwaiting => cuando se esta esperando una pagina
 * onseeking => cuando se esta buscando una pagina
 * onseeked => cuando se busca una pagina
 * onstalled => cuando se esta esperando una pagina
 * onsuspend => cuando se esta esperando una pagina
 * ontimeupdate => cuando se esta actualizando una pagina
 * onvolumechange => cuando se cambia el volumen de una pagina
 * onratechange => cuando se cambia la velocidad de una pagina
 * ondurationchange => cuando se cambia la duracion de una pagina
 * onended => cuando se termina una pagina
 *
 * Event Listeners
 * document.addEventListener("event", function); => agrega un event listener a un elemento del DOM
 * element.addEventListener("event", function); => agrega un event listener a un elemento del DOM
 * element.removeEventListener("event", function); => elimina un event listener de un elemento del DOM
 * element.dispatchEvent(event); => dispara un evento en un elemento del DOM
 * event.preventDefault(); => evita que se ejecute el evento
 *
 * Arbol DOM
 * Document -> Root Element:HTML->body->div->p->span->a
 *                              ->Head->title->meta->link->script->style->base->body->div->p->span->a
 * Crear Elementos
 *
 * var element = document.createElement("tag"); => crea un elemento del DOM
 * var node = document.createTextNode("text"); => crea un nodo de texto
 *
 * element.appendChild(node); => agrega un nodo de texto al elemento
 * element.insertBefore(node, referenceNode); => agrega un nodo de texto antes del elemento
 *
 * Replace Element
 * parent.replaceChild(newElement, oldElement); => reemplaza un elemento por otro
 *
 * Remove Element
 * parent.removeChild(element); => elimina un elemento del DOM
 *
 * setInterval(function, time); => ejecuta una funcion cada time milisegundos
 * clearInterval(interval); => detiene un intervalo
 *
 * item.animate([keyframes], options); => anima un elemento
 * keyframes => array de objetos con las propiedades a animar
 * options => objeto con las opciones de la animacion
 *
 * La funcion de aca abajo esta mas optimizada
 * requestAnimationFrame(function); => ejecuta una funcion cada vez que se actualiza la pagina
 * cancelAnimationFrame(requestID); => detiene una animacion
 *
 * Popup
 * alert("text"); => muestra una alerta con el texto que se le pasa como parametro
 * confirm("text"); => muestra una confirmacion con el texto que se le pasa como parametro
 * prompt("text", "default"); => muestra una alerta con el texto que se le pasa como parametro y con un valor por defecto
 *
 * Cookies vs Local Storage vs Session Storage
 *
 * Cookies => guardan datos en el navegador and server. Tienen menos capacidad, se pueden acceder desde cualquier windows. Son enviadas en cada request. Experies are manually set
 * Local Storage => guardan datos en el navegador. Tienen mas capacidad, se pueden acceder desde cualquier windows. Experia cuando cerras el navegador
 * Session Storage => guardan datos en el navegador. Tienen mas capacidad, se pueden acceder desde el tab donde se crearon. Experia cuando cerras la tab.
 *
 * localStorage.setItem("key", "value"); => guarda una key y un valor en el local storage
 * localStorage.getItem("key"); => obtiene el valor de una key del local storage
 * localStorage.removeItem("key"); => elimina una key del local storage
 * localStorage.clear(); => elimina todo el local storage
 *
 * sessionStorage.setItem("key", "value"); => guarda una key y un valor en el session storage
 * sessionStorage.getItem("key"); => obtiene el valor de una key del session storage
 * sessionStorage.removeItem("key"); => elimina una key del session storage
 * sessionStorage.clear(); => elimina todo el session storage
 *
 * document.cookie = "key=value"; => guarda una cookie
 * document.cookie = "key=value; expires=date"; => guarda una cookie con una fecha de expiracion
 * document.cookie = "key=value; expires=date; path=/"; => guarda una cookie con una fecha de expiracion y una ruta
 * document.cookie = "key=value; expires=date; path=/; domain=domain.com"; => guarda una cookie con una fecha de expiracion, una ruta y un dominio
 * document.cookie = "key=value; expires=date; path=/; domain=domain.com; secure"; => guarda una cookie con una fecha de expiracion, una ruta, un dominio y una seguridad
 * document.cookie = "key=value; expires=date; path=/; domain=domain.com; secure; httponly"; => guarda una cookie con una fecha de expiracion, una ruta, un dominio, una seguridad y una httponly
 *
 * No se puede obtener las cookies por separado
 * Se obtienen todas las cookies en un string, y se separan por ;. Se obtienen con document.cookie
 * document.cookie.split("; "); => obtiene todas las cookies
 *
 * History object
 * window.history.back(); => regresa a la pagina anterior
 * window.history.forward(); => avanza a la pagina siguiente
 * window.history.go(n); => avanza a la pagina n
 * window.history.length; => obtiene la cantidad de paginas visitadas
 * window.history.state; => obtiene el estado de la pagina
 * window.history.replaceState(state, title, url); => reemplaza el estado de la pagina
 * window.history.pushState(state, title, url); => guarda un estado de la pagina
 *
 * Clean Code
 *
 * Variables
 *
 * Variables has to redable, reusable and refactorable
 * Use meaningful names amd pronounceable names
 * Use camelCase
 * Use underscores for private variables
 * Use ES6 constant when variable values do not change
 * Maintain a consistent names.
 * Use searchable names
 * Use explanatory variable names
 * Short-circuiting is clenear than conditionals
 *
 * Functions
 *
 * Ideally functions should be short, concise and easy to read and have a maximum of 2 parameters.
 * Should do one thing and do it well
 * Names should say what they do
 * functions should be one level of abstraction
 * Remove duplicate code
 * Don't use flags as function parameters
 * Avoid side effects
 * Don't write to global functions
 * Favor functional programming over imperative programming
 * Encapsulate conditionals
 * Avoid negative conditionals
 * Avoid conditionals
 *
 * Objects and Data Structures
 *
 * Use getters and setters
 * Make objects have private variables
 *
 * Classes
 *
 * Method chaining, you have to return this at the end of the method.
 *
 * Class Car {
 *  constructor(make, model, year) {
 *     this.make = make;
 *     this.model = model;
 *     this.year = year;
 *  }
 *
 *  setMake(make) {
 *     this.make = make;
 *     return this;
 *  }
 *
 *  setModel(model) {
 *    this.model = model;
 *    return this;
 *  }
 * }
 *
 * const car = new Car("Ford", "Fiesta", "2015");
 * car.setMake("Chevy")
 * .setModel("Corvette")
 * .setYear("2016");
 *
 * Prefer composition over inheritance
 *
 * Composotivion with the relationship of "has a"
 * Inheritance with the relationship of "is a"
 *
 *
 * Composition
 *
 * class EmployeeTaxData {
 *  constructor(ssn, salary) {
 *   this.ssn = ssn;
 *   this.salary = salary;
 *  }
 *
 * }
 *
 *
 * class Employee {
 *  constructor(name, age, job) {
 *    this.name = name;
 *    this.age = age;
 *    this.job = job;
 *  }
 *
 *  setTaxData(ssn, salary) {
 *    this.taxData = new EmployeeTaxData(ssn, salary);
 *  }
 *
 * SOLID
 *
 * S = Single Responsibility Principle => una clase debe tener una sola responsabilidad
 * O = Open for extension/Closed for modification Principle => una clase debe ser abierta para extension y cerrada para modificacion
 * L = Liskov Substitution Principle => una clase debe ser substitutable para sus subclases
 * I = Interface Segregation Principle => No se aplica a js porque no tiene interfaces.
 * D = Dependency Inversion Principle => Higlevel modules doesn't have to depend on lowlevel modules.Both should depend on abstractions.
 *                                       Abstractions should not depend on details. Details should depend on abstractions.
 *
 *
 * Data Structures
 *
 * stacks => LIFO. Last in, first out. last element is the first to be removed.
 * Los stacks tienen estas funciones, push, pop, peek, lenght. Los array en js ya tienen esas funciones, por lo que podriamos usar un array como un stack.
 *
 * sets => no tienen orden. No tienen duplicados.
 * Los sets tienen estas funciones, add, remove, has, size, union, intersection, difference, subset. En ES6 ya existe un objeto SET, pero no tiene todas las funciones que tendria que tener.
 *
 */

function mySet() {
    var collection = [];

    this.has = function (element) {
        return collection.indexOf(element) !== -1;
    };

    this.values = function () {
        return collection;
    };

    this.add = function (element) {
        if (!this.has(element)) {
            collection.push(element);
            return true;
        }
        return false
    };

    this.remove = function (element) {
        if (this.has(element)) {
            let index = collection.indexOf(element);
            collection.splice(index, 1);
            return true;
        }
        return false;
    };

    this.size = function () {
        return collection.length;
    };

    this.union = function (otherSet) {
        var unionSet = new mySet();
        var firstSet = this.values();
        var secondSet = otherSet.values();
        firstSet.forEach(function (e) {
            unionSet.add(e);
        });
        secondSet.forEach(function (e) {
            unionSet.add(e);
        });
        return unionSet;
    };

    this.intersection = function (otherSet) {
        var intersectionSet = new mySet();
        var firstSet = this.values();
        firstSet.forEach(function (e) {
            if (otherSet.has(e)) {
                intersectionSet.add(e);
            }
        });
        return intersectionSet;
    };

    this.difference = function (otherSet) {
        var differenceSet = new mySet();
        var firstSet = this.values();
        firstSet.forEach(function (e) {
            if (!otherSet.has(e)) {
                differenceSet.add(e);
            }
        });
        return differenceSet;
    };

    this.subset = function (otherSet) {
        var firstSet = this.values();
        return firstSet.every(function (e) {
            return otherSet.has(e);
        });
    };
}

/**
 * Queues - FIFO. First in, first out. First element is the first to be removed. Similar to Stack.
 */

function myQueue() {
    let collection = [];
    this.print = function () {
        console.log(collection);
    };

    this.enqueue = function (element) {
        collection.push(element);
    };

    this.dequeue = function () {
        return collection.shift();
    };

    this.front = function () {
        return collection[0];
    };

    this.size = function () {
        return collection.length;
    };

    this.isEmpty = function () {
        return (collection.length === 0);
    };

}

/**
 * Trees - Binary Search Tree.
 * Binary Search Tree is a binary tree where each node has at most two children.
 */


/**
 * element.classList => returns a DOMTokenList object that contains the list of classes for the element.
 * element.classList.add(className) => adds a class to the element.
 * element.classList.remove(className) => removes a class from the element.
 * element.classList.toggle(className) => adds a class to the element if it is not present, or removes it if it is.
 * element.classList.contains(className) => returns true if the element has the specified class, and false otherwise.
 *
 *
 * Object.values => returns an array with the values of the object
 * Object.keys => returns an array with the keys of the object
 * Object.entries => returns an array with the keys and values of the object
 */

/**
 * Vieja manera de hacer clases en javascripts
 * function Vehicle(make, model, year) {
 *      this.make = make;
 *      this.model = model;
 *      this.year = year;
 * }
 *
 * y despues para asignarles los metodos utilizamos el prototype
 *
 * Car.prototype.setMake = function(make) { this.make = make; };
 * Car.prototype.setModel = function(model) { this.model = model; };
 * Car.prototype.setYear = function(year) { this.year = year; };
 *
 * Los metodos se asignaban fuera de la función constructora, por temas de performance, si escribiamos los metodos
 * adentro de la funcion constructora, los metodos se duplicarian cada vez que creamos una nueva instancia de ese objecto
 * ocasionando grandes perdidas de performance.
 *
 * Para heredar con las funciones prototipicas de javascript hacemos:
 *
 * function Car(make, model, year, doors) {
 *    this.super = Vehicle;
 *    this.super(make, model, year);
 *    this.doors = doors;
 * }
 *
 * Estos dos comandos de abajo los usamos para que no se creen mas instancias de las necesarias, de esa forma mejoramos la performance
 * Car.prototype = new Vehicle();
 * Car.prototype.constructor = Car;
 *
 * Para sobrescribir metodos de la clase padre
 * Car.prototype.setMake = function(make) {}
 * Para agregar metodos particulares a la clase hija
 * Car.prototype.setDoors = function(doors) {}
 *
 */

/*
* CLASES EN JAVASCRIPT
* Esta es la nueva sintaxis para escribir clases en Javascript, sigue siendo un prototype.
* Siguen siendo objetos prototipados, pero ahora con una sintaxis mas moderna.
*/

class Vehicle {
    constructor(make, model, year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    setMake(make) {
        this.make = make;
    }

    setModel(model) {
        this.model = model;
    }

    setYear(year) {
        this.year = year;
    }

    getMake() {
        return this.make;
    }

}

class Car extends Vehicle {
    constructor(make, model, year, doors) {
        super(make, model, year);
        this.doors = doors;
    }

    setDoors(doors) {
        this.doors = doors;
    }
}

let vehicle = new Vehicle('Toyota', 'Corolla', '2015');
let car = new Car('Toyota', 'Corolla', '2015', 4);


/**
 * JavaScript - ASYNC / AWAIT
 *
 *
 * JavaScript is Single Threaded Language
 *
 * Syncronous code is executed one after another.
 *
 * statement 1
 * statement 2
 * statement 3
 * statement 4
 *
 * Asyncronous - Start something now & finish it later.
 *
 * statement 1
 * statement 2 -> statement2 Asyncronous call
 * statement 3              \
 * statement 4              \
 * statement 2 <- finish call
 *
 * This makes the code non-blocking. 
 * It means that the code can continue to execute while the asyncronous call is being processed.
 * 
 *
*/

console.log(1)
console.log(2)
console.log(3)

setTimeout(() => {  // setTimeout(function, milliseconds)
    console.log('callback function fired')
}, 1000);

/**
 * This executed the code 1000ms after. This is o way to mimic the time that take to calls an api for example
 * this is a basic example of asyncronous code.
 */

console.log(4)

/**
 * HTTP Requests
 *
 * Make HTTP requests to get data from another server
 *
 * We make these requets to API endpoints
 *
 *
 * code -> http request -> some other server
 * code <- reponse(data) <- some other server
 *            json
 *
 * For practice use JSONPlaceholder API
 */


const url = 'https://jsonplaceholder.typicode.com/posts';

// BEFORE FETCH
const request = new XMLHttpRequest();

request.opren('GET', url); // open(method, url)
request.setRequestHeader('Content-Type', 'application/json'); // setRequestHeader(name, value)
request.send(); // send()

request.onreadystatechange = () => { // onreadystatechange(function)  - reqyest.addEventListener('readystatechange', function)
    if (request.readyState === 4 && request.status === 200) {
        const data2 = JSON.parse(request.responseText);
        console.log(data2);
    }
} // FOUR STATES -> 0, 1, 2, 3, 4

/**
 * 0 - UNSET
 * 1 - OPENED
 * 2 - HEADERS_RECEIVED
 * 3 - LOADING
 * 4 - DONE
 */

/** PROMISES
 *  
 * Promises are a way to handle asyncronous code in javascript. 
 * The promise can be resolve or rejected
 * Promises are usefull for handling things that take some time to resolve
 * 
 */

const getSomething = () => {
    return new Promise((resolve, reject) => { // new Promise(function(resolve, reject))
        // code here
        resolve('some data'); // resolve(data)
        reject('some error'); // reject(error)
    });
}

getSomething() // returns a promise
    .then(data4 => { 
        console.log(data4);
    })
    .catch(error => {
        console.log(error);
     });


const getTodos = (resource) => {
    return new Promise((resolve, reject) => {
        const request2 = new XMLHttpRequest();

        request2.opren('GET', url); // open(method, url)
        request2.setRequestHeader('Content-Type', 'application/json'); // setRequestHeader(name, value)
        request2.send(); // send()

        request2.onreadystatechange = () => { // onreadystatechange(function)  - reqyest.addEventListener('readystatechange', function)
            if (request2.readyState === 4 && request2.status === 200) {
                const data5 = JSON.parse(request2.responseText);
                resolve(data5);
            } else if (request2.readyState === 4 && request2.status === 404) {
                reject(request2.statusText);
            }

        }
    })
}

getTodos('todos/luigi,json')
    .then(data7 => {
        console.log('1 promise resolved', data7);
        return getTodos('todos/mario,json')
    })
    .then(data7 => {
        console.log('2 promise resolved', data7);
        return getTodos('todos/yoshi,json')
    })
    .then(data7 => {
        console.log('3 promise resolved', data7);
    })
    .catch(error => {
        console.log('promise rejected', error);
    })



// OLD WAY TU USE FETCH, USING PROMISES

/*
fetch(url, {
    method: 'GET',
    headers: {
        'Content-Type': 'application/json'
    },
})
*/

fetch(url)
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.log(error));




// With ASYNC/AWAIT

// WHEN WE CALL AN ASYNC FUNCTION, IT RETURNS A PROMISE

const getTodos2 = async () => { // This always return a promise

    try {
        const response = await fetch(url, { // await - wait for the promise to resolve
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            },
        })

        if (response.status != 400) {
            throw new Error('Not Found');
        }

        const data10 = await response.json();

        return data10
    } catch (error) {
        console.log(error);
    }
}


// THIS IS NON-BLOCKING CODE
getTodos2()
    .then(data29 => console.log(data29))
    .catch(error => console.log(error));

const data6 = await getTodos();

/**
 * EL CALLSTACK
 * 
 *  JavaScript es un lenguaje de programacion monoproceso (Single Threaded Language)
 * 
 *  -> Solamente ejecuta una sola cosa a la vez
 * 
 *  -> Pila/Stack -> LIFO
 * 
 *  -> Tiene un unico CALLSTACK [Pila de llamada]
 *      Callstack -> Lugar donde se guardan las llamadas a las funciones.
 *                -> Esto es el porque de que los scripts js se ejecuten de forma secuencial.
 *                -> El callstack nos ayuda a saber que funcion es la que se esta ejecutando, y que funciones ya sucedieron
 * 
 * -> Para poder ver el callstack podemos usar la funcion console.trace()
 * -> o user debugger; al principio de la funcion y luego buscarla en el
 * -> source del navegador
 * 
 */

/**
 * LISTAS - FIFO
 */

class NodeList{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class List{
    constructor(){
        this.head = null;
        this.last = null;
    }

    push(value){
        const node = new NodeList(value);

        if (this.head === null) this.head = node;
        else this.last.next = node;

        this.last = node;
    }

    pop(){
        if (this.head === null) return null;

        const node = this.head;
        this.head = this.head.next;

        return node.value;
    }

    print(){
        let node = this.head;

        while(node !== null){
            console.log(node.value);
            node = node.next;
        }
    }

    length(){
        let node = this.head;
        let length = 0;

        while(node !== null){
            length++;
            node = node.next;
        }

        return length;
    }

    getLast(){
        return this.last;
    }

    getElementAt(index){
        let aux = this.head;
        let actualIndex = 0;

        while(actualIndex !== index && aux !== null){
            aux = aux.next;
            actualIndex++;
        }

        return aux
    }

    delete(node){
        node.data = node.next.data
        this.next = this.next.next 
    }

}

/*
    STACK - LIFO
*/

class NodeStack {
    constructor(value){
        this.value = value;
        this.prev = null;
    }
}

class Stack{
    constructor(){
        this.top = null;
    }

    push(value){
        const node = new NodeStack(value);

        if (this.top === null) {
            this.top = node;
        } else {
            node.prev = this.top;
            this.top = node;
        }
    }

    current(){
        return this.top;
    }

    pop(){
        if (this.top === null) return null;

        const node = this.top;
        this.top = this.top.prev;

        return node.value;
    }

    hasElement(value){
        let node = this.top;

        while(node !== null){
            if (node.value === value) return true;
            node = node.prev;
        }

        return false;
    }
}

class NodeBinaryTree {
    constructor(value){
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinaryTree {
    constructor(){
        this.root = null;
    }

    insert(value){
        const node = new NodeBinaryTree(value);

        if (this.root === null) {
            this.root = node;
            return node;
        } 
        
        return this.insertNode(this.root, node);

    }

    insertNode(node, newNode){
        if (newNode.value < node.value) {
            if (node.left === null) {
                node.left = newNode;

                return newNode;
            }

            this.insertNode(node.left, newNode);
        } else {
            if (node.right === null) {
                node.right = newNode;

                return newNode;
            }

            this.insertNode(node.right, newNode);
        }
    }
}

