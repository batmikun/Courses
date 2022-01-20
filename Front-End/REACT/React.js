// REACT

/**
 * JavaScript Library used to created websites or applications
 * 
 * It is mostly use to create interactive web pages or single page applications
 * 
 */

/**
 * node_modules - Inside of node_modules lives all the depencies of the project
 * 
 * public - All the public files to the browser lives in here
 * 
 * src - source code of the project
 */

/**
 * In the boiler plate, we hace the index.html inside public
 * 
 * and we have the script that renders the react component call index.js
 * 
 * For testing we can use the react-testing-library, jest, cipress
 * 
 */

/**
 * REACT STRIC TYPE
 * 
 * Does a little more checking when we compile to production
 * 
 */

/**
 * To preview the project and use the live reloading
 * 
 * we hace to run in the console npm start
 * 
 */

/**
 * Components are the building blocks of React applications.
 * 
 * Components are the smallest possible building blocks of a React application.
 * 
 * Components are reusable pieces of code that encapsulate some part of the user interface.
 * 
 * A navbar can be a component, a link can be a component, any html element can be a component.
 */

/**
 * React use jsx to write html
 * 
 * is not html
 * 
 * jsx is a syntax extension to javascript
 * 
 * is very similar to html
 * 
 * the differences instead of class we huse className
 * 
 * we can not use class because it is a reserved word in javascript. And basically we are coding in javascript
 */

/**
 * Before the version 16.8.0 we hace to import the react library
 * import react from 'react'
 * 
 * After the 17 version we don't have to import it
 * 
 */

/**
 * When we create a component we have to export it
 * 
 * export default function Navbar() {}
 * 
 * we can import it as a function or a class
 * 
 * we can use name exports or default exports
 * 
 */

/**
 * To use javascript inside JSX
 * 
 * we have to use the { } and inside write the javascript
 * 
 * we can write javascript inside of jsx, and outside of jsx
 * 
 * to write outside of jsx we write it outside of the return of the component
 * 
 * TO THE VIEW
 * 
 * We can pass string, number, arrays and jsx convert it to string
 * 
 * we can not pass boolean, objects
 * 
 * we can pass dinamic values to the jsx elements
 * 
 * for example in a href={props.link}
 * 
 * ALL THE THINGS THAT WE PUT INSIDE {} ARE CONVERTED TO STRING
 * 
 */

/**
 * The app component is the root component, is what it renders the index.js
 */

/**
 *                App.js -> Root Component
 *       Nabar.js     BlogDetails.js          Sidebar.js
 *                                    Categories.js  Component,js 
 * 
 */

/**
 * If we import a css file in a component, that css file affects all the components
 */

/**
 * Inline Styles
 * 
 * inside the element style={{}} -> The outer curly braces are to indicate that is a dynmaic value, and the inner curly braces are for a javascript object
 * 
 * style = {{
 *  backgroundColor: 'red',
 *  color: 'white',
 *  borderRadius: '5px',
 * }}
 * 
 * In this case we can define the elements outside of the element and then import the object inside the dynamic value
 * 
 */

/**
 * To invoque a function inside a element
 * 
 * onCick={handleClick} we don't need to add () because that is gonna call it
 * 
 * To pass an argument we hace to wrap the function inside an anonymus function
 * 
 * <button onClick={() => handleClick(name)}>Click Me</button>
 * 
 * const handleClick = (name) => {
 *  console.log('Clicked', name)
 * }
 * 
 * We only need the {} if we put it in another line
 * if we put it in the same line we don't need the {}
 * 
 *
 * onClick((event) => handleClick(name, event))
 * 
 * 
 * 
 * 
 */

/**
 * To update things like a value or a state
 * 
 * we have to make the value reactive
 * 
 * This makes that when the variable change, the component automatically update
 */

/**
 * All hooks starts with use
 */


/**
 * To make a variable reactive
 * 
 * we have to use the hook useState
 * 
 * const [variable, setVariable] = useState(inicialValue)) 
 * 
 * The variable can be of any data type
 * 
 * And we can have as many useState as we want
 *
 */

/**
 * There is an extension that allow us to debug better our react code
 * 
 * React Developer Tools - Browser Extension
 * 
 */

/**
 * We can pass a function as a prop, so we can use it inside of a parent copmonent to interact with the data but lunck it from the child.
 */

/**
 * Use the useEffect hook to run a function after the component is rendered
 * 
 * useEffect(() => {
 *  console.log('Component rendered')
 * }, [])
 * 
 * UseEffect runs innp every render
 * 
 * Also we can access the state inside useEffect
 * 
 * It can use to fetching data
 * 
 * We can select when we want to run the useEffect using a dependency array
 * we pass it as second parameter.
 * 
 * If we leave it empty, it will run only one time
 * 
 * If we want to run useEffect every time a state change, we pass the state as a array
 * 
 * const [name, setName] = useState('React')
 * 
 * useEffect(() => {
 *  console.log('Name changed', name)
 * }, [name])
 * 
 * 
 * WE CAN NOT USE ASYNC AWAIT INSIDE useEFFECT
 * 
 */

/**
 * 
 * CONDITIONAL RENDERING
 * 
 * { blogs && <BlogList blogs={ blogs } title="All Blogs!" /> }
 * 
 * If blogs evaluates to false, javascript doesn't bother to read the right part
 * Ig blogs evaluates to true, Js evealuates the right part, and when evaluates to true it ouputs to the screen
 * 
 * 
 * Also we can use the ternary operator
 * { blogs ? <BlogList blogs={ blogs } title="All Blogs!" /> : <h1>Loading...</h1> }
 * 
 * 
 */

/**
 * CUSTOM HOOKS
 * 
 * JavaScript Code that we have in a seperate file, that manage one task
 * and we can useIt in all the component
 * 
 * Custom hook Example
 * 
 * import { useState ,useEffect } from "react";

    const useFetch = () => {

        const [data, setData] = useState([]);
        const [error, setError] = useState(null);

        useEffect(() => {
            fetch("http://localhost:8000/blogs", {method: "GET"})
                .then(response => {
                    if(!response.ok) {
                        throw new Error(response.statusText);
                    }
                    return response.json()
                })
                .then(data => {
                    setData(data)
                })
                .catch(error => setError(error.message))
        }, []);

        return {
            
        }
    }

    export default useFetch;

    the custom hook name has to start with USE and we have to have return values
    like useEffect returns data and setData
 * 
 */

/**
 * To have different pages we have to use the Route component
 * 
 * npm install react-router
 * 
 * import { BrowserRouter, Route, Switch } from 'react-router-dom';
 * 
 * The first step is wrap the root component with the <BrowserRouter> component
 * 
 * The Second step is to decide where we want to swtich the content of the different pages
 * And in that place add the <Switch> component
 * 
 * The third step is to add the <Route> component inside the switch
 *
 * 
        <Router>
        <div className="App">
            <Navbar />
            <div className="content">
                <Switch>
                    <Route exact path="/">
                        <Home />
                    </Route>
                    <Route exact path="/create" component={Create} />
        </Router>

        if we have a route that takes parameters we can pass ir
        like this :

        <Route exact path="/:id" component={BlogDetails} />

        To catch the id inside of the component we use a hook from react-router-dom

        import { useParams } from 'react-router-dom';

        const { id } = useParams();




 * 

    Instead of use anchor tags for the links, we have to use the <Link> component of react-router-dom


    <div className="links">
        <Link to="/"> Home </Link>
        <Link to="/create"> New Post </Link>
    </div>

    If we have something that update the state, we have to look up for errors
    it can happen that if you do a quick switch between routes it can trow an error
    because it wants to update a state in a unmont component
    
    In case of a fecth, we can use the AbortController

import { useState ,useEffect } from "react";

const useFetch = (url) => {

    const [data, setData] = useState([]);
    const [error, setError] = useState(null);

    useEffect(() => {
        const abortController = new AbortController();


        fetch(url, {signal: abortController.signal, method: "GET"})
            .then(response => {
                if(!response.ok) {
                    throw new Error(response.statusText);
                }
                return response.json()
            })
            .then(data => {
                setData(data)
            })
            .catch(error => {
                if(error.name === "AbortError") {
                    console.log("Request aborted");
                } else {
                    setError(error.message)
                }
            })

        return () => { abortController.abort() }   
    }, [url]);

    return { data, error }
}

export default useFetch;

 */

/**
 * Controlled Inputs - we can track the state of the input
 * 
 * const [name, setName] = useState('')
 * 
 * <input 
 *  type="text"
 *  value={ name }
 *  onChange={ e => setName(e.target.value) }
 * />
 * 
 * HOOK USEREF - with this we avoid infinite loops - it similar to querySelector in JS, it returns the element node
 * 
 * another use it to store the previus state of the component
 * 
 * import React, { useRef } from 'react';
 * 
 * preserves values between renders
 * does not trigger re-render
 * target DOM nodes/elements
 * 
 * const UseRefBasics = () => {
 * 
 *      const inputRef = useRef(value) -> this return an object with { current: value }
 * 
        const handleSubmit = (e) => {
            e.preventDefault();

            console.log(inputRef.current.value)
        }
 * 
 *      retyrb 
 *      <>
 *          <form className="form" onSubmit={handleSubnit}>
 *              <div>
 *                  <input type="text" ref={ inputRef } />
 *                  <button type="submit">Submit</button>
 *             </div>
 *         </form>
 *      </>
 * }
 * 
 */

/**
 * Fore redirects we use another hook
 * call useHistory from reac-router-dom
 * 
 * const history = useHistory()
 * 
 * history.push('/')
 * history.go(+1) goes one page after in history
 * history.go(-1) goes one page before in history
 */

/**
 * 404 page
 * 
 * where we got all the routes
 * 
 * we add a new route
 * 
 * <Route path="*">
 *      <Component404 />
 * </Route
 */

/**
 * useReducer hook is an alternative to useState
 * 
 * import { useReducer } from "react";
 * 
 * const reducer = (state, action) => {
 *      switch(action.type) {
 *        case 'INCREMENT':
 *             return { count: state.count + 1 } 
 *      }
 * }
 * 
 * useReducer => [state, dispatch] => [{ count: 0 }, { type: 'INCREMENT' }]
 * 
 * An alternative to useState. 
 * Accepts a reducer of type (state, action) => newState, 
 * and returns the current state paired with a dispatch method. 
 * (If you’re familiar with Redux, you already know how this works.)
   useReducer is usually preferable to useState when you have complex state logic that involves multiple sub-values 
   or when the next state depends on the previous one. 
   useReducer also lets you optimize performance for components that trigger deep updates because you can pass dispatch 
   down instead of callbacks.
 * 

const initialState = {count: 0};

function reducer(state, action) {
  switch (action.type) {
    case 'increment':
      return {count: state.count + 1};
    case 'decrement':
      return {count: state.count - 1};
    default:
      throw new Error();
  }
}

function Counter() {
  const [state, dispatch] = useReducer(reducer, initialState);
  return (
    <>
      Count: {state.count}
      <button onClick={() => dispatch({type: 'decrement'})}>-</button>
      <button onClick={() => dispatch({type: 'increment'})}>+</button>
    </>
  );
}

reducer is just a function 

state is the state just before the update
action is the action that triggered the update

reducer will happen when we dispatch an action

we will have a defaultState

const reducer = (state, action) => {

}

const defaultState = {
    people: [],
    isModalOpen: false,
    modalContent: 'I'm a modal';
};

const [state, dispatch] = useReducer(reducer, defaultState);


state will have the properties that we pass in defaultState

state.people
state.isModalOpen
state.modalContent

when we call dispatch always we have
to pass an object with the property type

dispatch({type: 'increment'});

when we launch an action with dispatch it go to the reducer function
in reducer you will always wanna return a new state

we can use if(action.type) or switch(action.type)

const reducer = (state, action) => {
    switch (action.type) {
        case 'increment':
            return {
                ...state, 
                people:data,
                isModalOpen: true,
                modalContent: 'I am a new modal'
            }
    }
}

we can add more properties to the object that we pass in dispatch
generally to this other property we call it payload
this payload will be inside the action object


CONTEXT API

Context is designed to share data that 
can be considered “global” for a tree of React 
components, such as the current authenticated user,
theme, or preferred language

Example without context

class App extends React.Component {
  render() {
    return <Toolbar theme="dark" />;
  }
}

function Toolbar(props) {
  // The Toolbar component must take an extra "theme" prop
  // and pass it to the ThemedButton. This can become painful
  // if every single button in the app needs to know the theme
  // because it would have to be passed through all components.
  return (
    <div>
      <ThemedButton theme={props.theme} />
    </div>
  );
}

class ThemedButton extends React.Component {
  render() {
    return <Button theme={this.props.theme} />;
  }
}

The same but with context

// Context lets us pass a value deep into the component tree
// without explicitly threading it through every component.
// Create a context for the current theme (with "light" as the default).

export const ThemeContext = React.createContext('light');

export const app = () => {
    return (
        <ThemeContext.Provider value="dark">
            <Toolbar />    
        </ThemeContext.Provider>
    }
}

To use the context in the functions component we use useContext

import React, { useContext } from 'react';
import { ThemeContext } from './ThemeContext';

const Toolbar = () => {
    const darkTheme = usecontect(ThemeContext);
    return (
        <div>
            -----
        </div>    
    )
}


In the class component

class App extends React.Component {
    render() {
        rerturn (
            <ThemeContext.Consumer>
                {theme => (
                    return jsx     
                }
            </ThemeContext.Consumer>
        )
    }
}

PERFORMING OPTIMIZATIONS

MEMOIZATION -> CACHING RESULTS

BASICALLY THIS OPTIMIZATION CENTERS AROUND NOT RE-RENDER COMPONENTS THAT DOENS'T HAVE
MOTIVES TO CHANGE

MEMO FUNCTION

WE CAN USE REACT.MEMO() to wrap a component and only re-render it if the props change

const BigList = React.memo((props) => {
    return 
    <div>
        <List />
    </div>
})

USEMEMO HOOK -> only returns the value of the functions

DIFFERENT FROM USECALLBACK, USEMEMO IS SPECIFICALLY FOR A VALUE

const calculate = (data) => {
    return data.reduce((total, current) =>  total = current.price >= total ? current.price : total, 0);
}

We use it when we have a slow function that we want to memoize, we wrap the function into a useMemo

const mostExpensive = useMemo(() => calculate(data), [data]);

and we use the function mostExpensive instead of the calculate function

array.reduce(callback, initialValue)

useMemo(callback, deps)

Returns a memoized value.

We can use it also with variables to avoid comprasion between reference and variable

const themStyles = useMemo(() => {
    return {
        backgroundColor: 'red',
        color: 'white'
    }
}

This will avoid that react create a new object every time we reload the component for other reason

USECALLBACK -> You use it when you have to worry about referencial equality

Similar to UseMemo, the difference is that re runs the function when a especfic property changes.

const getItem = useCallback((incrementer) => {
    return [number, number+incrementer, number+incrementer];
}, [number]) 

getItem(1)

Also the difference is that useCallback return the function and not the result of the function
we can pass parameter to the function 

REFERENCIAL EQUALITY -> We represent it with === in JS

PROP DRILLING - PASS PROPS FROM GRAMPA TO CHILD

 */