/**
 * STRUCTURAL PATTERNS:
 *          - Module
 *          - Mixin
 *          - Facade
 *          - Flyweight
 *          - Decorator
 * 
 * Organization of your code
 * 
 * CREATIONAL PATTERNS:
 *          - Class
 *          - Constructor
 *          - Singleton
 *          - Factory
 *          - Abstract Factory
 *          - Builder
 *          - Prototype
 *         
 * Control the creation of an object
 * 
 * BEHAVIORAL PATTERNS:
 *          - Strategy
 *          - Iterator
 *          - Mediator
 *          - Observer
 *          - State
 *  
 * Use for behaviors in code
 * 
 * Design Pattern:
 *          A general, reusable solution to a commonly occurring problem within a given context
 *          in software design 
 * 
 *          Is a way to resolve common problems in code        
 * 
 * FUNCTIONS AS FIRST-CLASS CITIZENS
 * 
 * They can be passed as arguments to other functions, assigned to variables, and returned from functions
 * 
 * CALLBACK
 * 
 * A callback is a function that we pass as argument to another function
 * and we expect that function to execute in some point of the future
 */

console.log('Hola');

/**
 * CREATIONAL PATTERNS
 */

/**
 * Prototype Class Pattern
 * 
 * A prototype is a class that is used as a blueprint for creating objects
 * 
 * 
 */

class Car { // Blueprint for new objects that we are going to create
    constructor(doors, engine, color) {
        this.doors = doors;
        this.engine = engine;
        this.color = color;
    }
}

const civic = new Car(4, 'V6', 'grey');

/**
 * Constructor Pattern
 * 
 * We use it to extend classes
 */

class SUV extends Car {
    constructor(doors, engine, color, brand) {
        super(doors, engine, color);
        this.brand = brand;
    }
}

const cx5 = new SUV(4, 'V6', 'grey', 'BMW');

/**
 * Singleton Pattern
 * 
 * This pattern make that an object is only create once
 */

let instance = null

class Singleton {
    constructor(props) {
        if (!instance) {
            this.props = props;
            instance = this;
        }
        return instance;
    }
}

const singleton = new Singleton();
const singleton2 = new Singleton();

console.log(singleton === singleton2);

/**
 * Factory Pattern
 * 
 * This pattern is used to create objects without having to specify the exact class of the object that will be created
 */

class Store {
    constructor(name, adress, type) {
        this.name = name;
        this.adress = adress;
        this.type = type;
    }
}

class Factory {
    createStore(type) {
        switch (type) {
            case 'farmacia':
                return new Store('Farmacia', 'Calle 1', 'farmacia');
            case 'tienda':
                return new Store('Tienda', 'Calle 2', 'tienda');
            case 'supermercado':
                return new Store('Supermercado', 'Calle 3', 'supermercado');
        }
    }
}

const factory = new Factory();
const farmacia = factory.createStore('farmacia');
const tienda = factory.createStore('tienda');

console.log(store1 === store2);

class Database {
    constructor(host, user, password) {
        this.host = host;
        this.user = user;
        this.password = password;
    }
}

class FactoryDatabase {
    createDatabase(type) {
        switch (type) {
            case 'mysql':
                return new Database('localhost', 'sql', 'password');
            case 'mongodb':
                return new Database('localhost', 'mongo', 'password');
            case 'postgres':
                return new Database('localhost', 'postgres', 'password');
        }
    }
}

const factoryDatabase = new FactoryDatabase();
const mysql = factoryDatabase.createDatabase('mysql');
const mongodb = factoryDatabase.createDatabase('mongodb');

/**
 * Abstract Factory Pattern
 * 
 * This pattern is used to create families of related or dependent objects without specifying their concrete classes
 */

    class CarFactory {
        createCar(type) {
            switch (type) {
                case 'civic':
                    return new Car(4, 'V6', 'grey');
                case 'cx5':
                    return new SUV(4, 'V6', 'grey', 'BMW');
            }
        }
    }

    class SUVFactory {
        createCar(type) {
            switch (type) {
                case 'cx5':
                    return new SUV(4, 'V6', 'grey', 'BMW');
                case 'cx7':
                    return new SUV(4, 'V6', 'red', 'BMW');
            }
        }
    }

    const autoManuFacturer = (type, model) => {
        switch (type) {
            case 'car':
                return new CarFactory().createCar(model);
            case 'suv':
                return new SUVFactory().createCar(model);
        }
    }

    const car = autoManuFacturer('car', 'civic');
    const suv = autoManuFacturer('suv', 'cx5');

/**
 * Builder Pattern
 * 
 * This pattern is used to create complex objects without having to specify the exact class of the object that will be created
 */

class House {
    constructor(street, number, zipCode, state) {
        this.street = street;
        this.number = number;
        this.zipCode = zipCode;
        this.state = state;
    }
}

class HouseBuilder {
    constructor() {
        this.house = new House();
    }

    setStreet(street) {
        this.house.street = street;
        return this;
    }

    setNumber(number) {
        this.house.number = number;
        return this;
    }

    setZipCode(zipCode) {
        this.house.zipCode = zipCode;
        return this;
    }

    setState(state) {
        this.house.state = state;
        return this;
    }

    getHouse() {
        return this.house;
    }
}

const houseBuilder = new HouseBuilder();
const house = houseBuilder
    .setStreet('Avenida Siempreviva')
    .setNumber('123')
    .setZipCode('12345')
    .setState('SP')
    .getHouse();


/**
 * STRUCTURAL PATTERNS
*/

/**
 * Module Pattern -> IIFE -> Immediately Invoked Function Expression
 *                -> Modules are usually pure functions that we use 
 *                -> to organize our code. We can decompose our larger code
 *                -> into smaller pieces that we can reuse. This smaller pieces
 *                -> are called modules. We usually use modules through imports                     
 */

    const module = (function () {
        let counter = 0;

        return {
            increment() {
                return counter++;
            },
            decrement() {
                return counter--;
            }
        }
    })

    const counter = module();

    console.log(counter.increment());

/**
 * Mixin Pattern -> Mixins are a way to add functionality to existing classes
 */

    const carMixin = {
        drive() {
            return 'Vroom!';
        }
    }

    Object.assign(Car.prototype, carMixin); // We can use Object.assign to add methods to an object
    // All the car objects created after this line will have the drive method

    const carWithNewProperties = autoManuFacturer('car', 'cx5');

    console.log(carWithNewProperties.drive());

    // Mixin Pattern

    const mixin = (BaseClass, ...mixins) => {
        class MixedClass extends BaseClass {
            constructor(...args) {
                super(...args);
                mixins.forEach(mixin => {
                    copyProperties(this, new mixin());
                });
            }
        }

        for (let mix of mixins) {
            copyProperties(MixedClass, mix);
        }

        return MixedClass;
    }

    const copyProperties = (target, source) => {
        for (let key of Reflect.ownKeys(source)) {
            if (key !== 'constructor' && key !== 'prototype' && key !== 'name') {
                Object.defineProperty(target, key, Object.getOwnPropertyDescriptor(source, key));
            }
        }
    }

    class MyClass {
        constructor() {
            this.name = 'MyClass';
        }

        myMethod() {
            return 'MyMethod';
        }
    }

    class MyMixin {
        myMethod() {
            return 'MyMixin';
        }
    }

    const MyClass = mixin(MyClass, MyMixin);

/**
 * Facade Pattern -> Facade is a way to provide a simplified interface to a library or tool
 *                 -> is about to hide the complexity of a library or tool
 */

    const facade = (function () {
        const api = {};

        api.get = function (url) {
            return fetch(url);
        }

        return api;
    })();

    facade.get('https://google.com').then(response => {
        console.log(response);
    });

/**
 * Flyweight Pattern -> Flyweight is a way to reduce the memory footprint of a large object by sharing parts of it
 *                     -> that are the same
 */

    const FlyweightFactory = (function () {
        const flyweights = {};

        return {
            get: function (key) {
                if (!flyweights[key]) {
                    flyweights[key] = new ConcreteFlyweight(key);
                }

                return flyweights[key];
            }
        }
    })();

    const Flyweight = {
        getKey: function () {
            return this.key;
        }
    }

    const ConcreteFlyweight = function (key) {
        this.key = key;
    }

    ConcreteFlyweight.prototype = Flyweight;

/**
 * Decorator Pattern -> Decorators are a way to modify the behavior of an object at runtime
 */

    class Bike {
        constructor(model, price) {
            this.model = model;
            this.price = price;
        }
    }

    class BikeDecorator {
        constructor(bike) {
            this.bike = bike;
        }

        getPrice() {
            return this.bike.getPrice() + 2000;
        }

        getDescription() {
            return this.bike.getDescription() + ', Custom Paint';
        }
    }

    const bike = new BikeDecorator(new Bike('Trek', 1000));

    console.log(bike.getPrice());
    console.log(bike.getDescription());

/**
 * Proxy Pattern -> Proxy is a way to control access to certain objects
 *                 -> by intercepting the calls to the object and/or by
 *                 -> modifying the behavior of the object
 */

    const user = {
        firstName: 'John',
        lastName: 'Doe',
        getFullName: function () {
            return `${this.firstName} ${this.lastName}`;
        }
    };

    const handler = {
        get: function (target, name) {
            if (name in target) {
                return target[name];
            } else {
                throw new Error(`Property ${name} does not exist`);
            }
        }
    };

    const proxiedUser = new Proxy(user, handler);

    proxiedUser.getFullName();


/**
 * MVP Pattern -> This pattern is used to create a model-view-presenter (MVP)
 * 
 * Model = Data
 * 
 * View = Visuals (HTML)
 * 
 * Presenter = Logic
 * 
 * The difference between MVP and MVC the view doesn't have to access the model directly.
 * Instead, the view can access the model through the presenter. And the presenter pulls from the model
 * 
 * This is popular in Android Development
 * 
*/

/**
 * MVC Pattern -> This pattern is used to create a model-view-controller (MVC)
 * 
 * Model = Data
 * 
 * View = Visuals (HTML)
 * 
 * Controller = Logic
 */

/**
 * MVVM Pattern -> This pattern is used to create a model-view-viewmodel (MVVM)
 * 
 * Model = Data
 * 
 * View = Visuals (HTML)
 * 
 * ViewModel/ViewController = Logic
 * 
 * In react we can see it, this way
 * 
 * Model = Data
 * 
 * View = Stateless Visuals Components
 * 
 * View Model = Stateful Components
 * 
 */

/**
 * BEHAVIORAL PATTERNS
 * 
 * Focused on the communications between objects
 * 
 * Similar to implementing better communications in between us
 * 
 * 
 * 1. Command Pattern -> This pattern is used to encapsulate a request as an object,
 *                    -> thereby letting you parameterize other objects with different requests,
 *                    -> queue or log requests, and support undoable operations.
 * 
 * 2. Observer Pattern -> This pattern is used to allow an object to notify other objects when its state changes.
 *                     -> We mantain a list of objects based on events, and is tipically used to update the data
 *                     -> through Events.
 * 
 */

/**
 * COMMAND PATTERN
 * 
*/

    const command = (function () {
        const commands = {};

        return {
            add: function (command) {
                commands[command.name] = command;
            },
            execute: function (name) {
                commands[name].execute();
            }
        }
    })()

    const command1 = {
        name: 'command1',
        execute: function () {
            console.log('command1');
        }
    }

    const command2 = {
        name: 'command2',
        execute: function () {
            console.log('command2');
        }
    }

    command.add(command1);
    command.add(command2);

    command.execute('command1');
    command.execute('command2');

/**
 * Observer Pattern
*/

    const observer = (function () {
        const subscribers = [];

        return {
            subscribe: function (subscriber) {
                subscribers.push(subscriber);
            },
            unsubscribe: function (subscriber) {
                subscribers.splice(subscribers.indexOf(subscriber), 1);
            },
            publish: function (data) {
                subscribers.forEach(subscriber => subscriber.update(data));
            }
        }
    })()

    const subscriber1 = {
        update: function (data) {
            console.log('subscriber1', data);
        }
    }

    const subscriber2 = {
        update: function (data) {
            console.log('subscriber2', data);
        }
    }

    observer.subscribe(subscriber1);
    observer.subscribe(subscriber2);

    observer.publish('Hello World');

/**
 * State Pattern -> This pattern is used to encapsulate the state of an object and the transitions between states.
 *               -> It become popular with React, Angular, Vue, etc.
 *               -> When we change the state it update the rendering of the application
 */

    const state = (function () {
        const states = {};

        return {
            add: function (state) {
                states[state.name] = state;
            },
            get: function (name) {
                return states[name];
            }
        }
    })()

    const state1 = {
        name: 'state1',
        render: function () {
            console.log('state1');
        }
    }

    const state2 = {
        name: 'state2',
        render: function () {
            console.log('state2');
        }
    }

    state.add(state1);
    state.add(state2);

    const stateMachine = (function () {
        let currentState = state.get('state1');

        return {
            changeState: function (newState) {
                currentState = state.get(newState);
            },
            getState: function () {
                return currentState;
            }
        }
    })()

    stateMachine.changeState('state2');
    stateMachine.getState().render();

/**
 * Chain of Responsibility Pattern -> This pattern is used to process a request in a chain of handlers.
 *                                  -> Each handler decides if it can handle the request or not.
 *                                  -> If not, the next handler in the chain is called.
 * 
 * Help solve common practical problem issues of having a request from a client
 * and need ing this request to pass through multiple functions or logic to get the result
 * 
 * For example
 * 
 * We have a button buy that launchs a series of event
 * 
 * Button Buy:
 *          1 - Loggend In?
 *          2 - Address?
 *          3 - Calculate Taxes?
 *          4 - Shipping?
 *          5 - Process Payment?
 *          6 - ETC
 * 
 * We can implement Chaing of Responsabilit
 *
 * Abstract Handler: -> We create a chain that garanted us that the actions will be call in a linear way
 *                   -> The abstract handler handles the error from the handlers
 *         1 - Login Handler
 *         2 - Check Address Handler
 *         3 - Tax Handler
 *         4 - Shipping Handler
 *         5 - Payment processing Handler
 */

    const abstractHandler = (function () {
        const handlers = [];

        return {
            add: function (handler) {
                handlers.push(handler);
            },
            get: function (index) {
                return handlers[index];
            },
            setSuccessor: function (successor) {
                handlers.forEach(handler => handler.setSuccessor(successor));
            }
        }
    })()

    const loginHandler = (function () {
        let successor;

        return {
            setSuccessor: function (handler) {
                successor = handler;
            },
            handleRequest: function (request) {
                if (request === 'login') {
                    console.log('loginHandler');
                } else {
                    successor.handleRequest(request);
                }
            }
        }
    })()

    const checkAddressHandler = (function () {
        let successor;

        return {
            setSuccessor: function (handler) {
                successor = handler;
            },
            handleRequest: function (request) {
                if (request === 'checkAddress') {
                    console.log('checkAddressHandler');
                } else {
                    successor.handleRequest(request);
                }
            }
        }
    })()

    const taxHandler = (function () {
        let successor;

        return {
            setSuccessor: function (handler) {
                successor = handler;
            },
            handleRequest: function (request) {
                if (request === 'tax') {
                    console.log('taxHandler');
                } else {
                    successor.handleRequest(request);
                }
            }
        }
    })()

    const shippingHandler = (function () {
        let successor;

        return {
            setSuccessor: function (handler) {
                successor = handler;
            },
            handleRequest: function (request) {
                if (request === 'shipping') {
                    console.log('shippingHandler');
                } else {
                    successor.handleRequest(request);
                }
            }
        }
    })()

    const paymentHandler = (function () {
        let successor;

        return {
            setSuccessor: function (handler) {
                successor = handler;
            },
            handleRequest: function (request) {
                if (request === 'payment') {
                    console.log('paymentHandler');
                } else {
                    successor.handleRequest(request);
                }
            }
        }
    })()

    abstractHandler.add(loginHandler);
    abstractHandler.add(checkAddressHandler);
    abstractHandler.add(taxHandler);
    abstractHandler.add(shippingHandler);
    abstractHandler.add(paymentHandler);
    
    abstractHandler.setSuccessor(checkAddressHandler);
    abstractHandler.setSuccessor(taxHandler);
    abstractHandler.setSuccessor(shippingHandler);
    abstractHandler.setSuccessor(paymentHandler);

    abstractHandler.handleRequest('login');
    abstractHandler.handleRequest('checkAddress');
    abstractHandler.handleRequest('tax');
    abstractHandler.handleRequest('shipping');
    abstractHandler.handleRequest('payment');


/**
 * Iterator Pattern -> This pattern is used to iterate over a collection of items.
 *                  -> Is perfect when you want to iterate over array of objects
 * 
 * 
 */

    const collection = (function () {
        const items = [];

        return {
            add: function (item) {
                items.push(item);
            },
            get: function (index) {
                return items[index];
            },
            getLength: function () {
                return items.length;
            },
            createIterator: function () {
                return new iterator(this);
            }
        }
    })()

    const iterator = (function () {
        let collection;
        let index = 0;

        return {
            init: function (collection) {
                this.collection = collection;
            },
            hasNext: function () {
                return index < collection.getLength();
            },
            next: function () {
                return collection.get(index++);
            }
        }
    })()

    const item1 = {
        name: 'item1'
    }

    const item2 = {
        name: 'item2'
    }

    const item3 = {
        name: 'item3'
    }

    collection.add(item1);
    collection.add(item2);
    collection.add(item3);

    const iterator1 = collection.createIterator();

    while (iterator1.hasNext()) {
        console.log(iterator1.next().name);
    }

/**
 * Strategy Pattern -> This pattern is used to encapsulate an algorithm inside a class.
 * 
 * A way to encapsulate different algorithms or functions and then at runtime practically use the same code
 * to run different escenarios
 */

    const strategy = (function () {
        const strategies = {};

        return {
            add: function (name, strategy) {
                strategies[name] = strategy;
            },
            get: function (name) {
                return strategies[name];
            }
        }
    })()

    const strategy1 = (function () {
        return {
            execute: function () {
                console.log('Strategy 1');
            }
        }
    })()

    const strategy2 = (function () {
        return {
            execute: function () {
                console.log('Strategy 2');
            }
        }
    })()

    strategy.add('strategy1', strategy1);
    strategy.add('strategy2', strategy2);

    const strategy3 = strategy.get('strategy1');
    strategy3.execute();

    const strategy4 = strategy.get('strategy2');
    strategy4.execute();

/**
 * Memento Pattern -> This pattern is used to save and restore the state of an object.
 * 
 */

    const memento = (function () {
        let state;

        return {
            getState: function () {
                return state;
            },
            setState: function (state) {
                this.state = state;
            }
        }
    })()

    const careTaker = (function () {
        const mementos = [];

        return {
            add: function (memento) {
                mementos.push(memento);
            },
            get: function (index) {
                return mementos[index];
            }
        }
    })()

    const originator = (function () {
        let state;

        return {
            setState: function (state) {
                this.state = state;
            },
            getState: function () {
                return state;
            },
            saveStateToMemento: function () {
                return memento.setState(this.getState());
            },
            restoreStateFromMemento: function (memento) {
                this.setState(memento.getState());
            }
        }
    })()

    const memento1 = originator.saveStateToMemento();
    originator.setState('state1');

    const memento2 = originator.saveStateToMemento();
    originator.setState('state2');

    careTaker.add(memento1);
    careTaker.add(memento2);

    originator.restoreStateFromMemento(careTaker.get(0));
    console.log(originator.getState());

    originator.restoreStateFromMemento(careTaker.get(1));
    console.log(originator.getState());

/**
 * Mediator Pattern -> This pattern is used to communicate between objects.
 */

class TrafficTower {
    constructor() {
        this.airplanes = [];
    }

    requestPosition() {
        return this.airplanes.map(airplane => airplane.position);
    }
}

class Airplane {
    constructor(position, trafficTower) {
        this.position = position;
        this.trafficTower = trafficTower;
        this.trafficTower.airplanes.push(this);
    }

    requestPosition() {
        return this.trafficTower.requestPosition();
    }
}