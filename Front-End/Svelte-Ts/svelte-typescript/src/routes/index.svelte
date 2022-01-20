<style>
    .todos{
        width: 100%;
        max-width: 42rem;
        margin: 4rem auto 0 auto;
    }

    .new {
        margin: 0 0 0.5 0;
    }

    .new input {
        width: 100%;
        font-size: 2rem;
        padding: 0.5em 1em 0.5em 1em;
        border-radius: 8px;
        text-align: center;
    }

    /* if we want to affect the component childres */
    .todos :global(input) {
        border:1px solid transparent;
        background: none;
    }

    .todos :global(input:focus-visible) {
        box-shadow: inset 1px 6px rgba(0, 0, 0, 0, 1);
        outline: none;
    }
</style>

<svelte:head>
    <title>{title}</title>
</svelte:head>

<script context="module" lang="ts">
    import type { Load } from "@sveltejs/kit";
    import { enhance } from "$lib/actions/form";

    export const load: Load = async ({ fetch }) => {
        const res = await fetch("/api/todos.json")

        if (res.ok) {
            const todos = await res.json();
            return {
                props: {
                    todos
                }
            }
        }

        const message = await res.json();

        return{
            error: new Error(message)
        }
    }
</script>

<script lang="ts">
    import TodoItem from "$lib/todo-item.svelte";
    import type { Todo } from "src/global";

    const title = "Todo List";

    export let todos: Todo[];
</script>

<div class="todos">
    <h1>{title}</h1>
        <form action="/api/todos.json" method="post" class="new" use:enhance> 
            <input type="text" name="text" aria-label="Add a todo" placeholder="+ type to add a todo" />
        </form>
        
        {#each todos as todo}
            <TodoItem {todo} />
        {/each}   
</div>




