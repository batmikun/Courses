<style>
.todo{
    display:grid;
    grid-template-columns: 2rem 1fr 2rem;
    grid-column: 0.5rem;
    align-items: center;
    margin: 0 0 0.5rem 0;
    padding: 0.5rem;
    background-color: white;
    border-radius: 8px;
    filter: drop-shadow(2px 4px 6px rgba(0, 0, 0, 0.1));
    transform: translate(-1px, -1px);
    transition: filter 0.2s, transform 0.2s;
}

.todo button {
    width: 2rem;
    height: 2rem;
    border: none;
    background-color: transparent;
    background-position: 50% 50%;
    background-repeat: no-repeat;
}

.todo input {
    flex: 1;
    padding: 0.5em 2em 0.5em 0.8em;
    border-radius: 3px;
}

button.toggle{
    border: 1px solid rgba(0,0,0,0.2);
    border-radius: 50%;
    box-sizing: border-box;
    background-size: 1em auto;
}

.text {
    position: relative;
    display:flex;
    align-items: center;
    flex: 1;
}


.save{
    position: absolute;
    right: 0;
    opacity: 0;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath d='M17 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14c1.1 0 2-.9 2-2V7l-4-4zm-5 16c-1.66 0-3-1.34-3-3s1.34-3 3-3 3 1.34 3 3-1.34 3-3 3zm3-10H5V5h10v4z'/%3E%3C/svg%3E");
}

.todo input:focus + .save, 
.save:focus{
    transition: opacity 0.2s;
    opacity: 1;
}

.delete {
    opacity: 0.2;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3Cpath d='M6 19c0 1.1.9 2 2 2h8c1.1 0 2-.9 2-2V7H6v12zM19 4h-3.5l-1-1h-5l-1 1H5v2h14V4z'/%3E%3C/svg%3E");
    transition: opacity 0.5s;
}

.delete:hover{
    opacity: 1;
}

.delete:focus {
    opacity: 1;
}

.done {
    transform: none;
    opacity: 0.4;
    filter: drop-shadow(0px 0px 0px rgba(0, 0, 0, 0.1));
}

.done .toggle {
    background-image: url("https://img.icons8.com/material-outlined/24/000000/checked--v1.png");
}

</style>

<script lang="ts">
    import type { Todo } from "src/global";


    export let todo: Todo

</script>

<div class="todo {todo.done ? 'done' : '' }">
    <form action="/api/todos/{todo.uid}.json?_method=patch" method="post">
        <input type="hidden" name="done" value="{todo.done ? '' : 'true'}" />
        <button class="toggle" aria-label="Mark todos as {todo.done ? 'Not Done' : 'Done'}"></button>
    </form>

    <form class="text" action="/api/todos/{todo.uid}.json?_method=patch" method="post">
        <input type="text" name="text" value="{ todo.text }" >
        <button aria-label="Save todo" class="save"></button>
    </form>

    <form action="/api/todos/{todo.uid}.json?_method=delete" method="post">
        <button aria-label="Delete todo" class="delete"></button>
    </form>
</div>