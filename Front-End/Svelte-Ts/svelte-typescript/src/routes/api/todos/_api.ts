import type { Request } from '@sveltejs/kit';
import type { Todo } from 'src/global';

let todos: Todo[] = [];

export const api  = (request: Request, data?: Record<string,unknown>) : Record<string, unknown> => {

    let body = {};
    let status = 500;

    switch (request.method.toUpperCase()) {
        case 'GET':
            body = todos;
            status = 200;
            break;
        case 'POST':
            status = 303;
            todos.push(data as Todo);
            body = data;
            break;
        case 'DELETE':
            todos = todos.filter(todo => todo.uid !== request.params.uid );
            status = 200;
            break;
        case 'PATCH':
            todos = todos.map(todo => {
                if (todo.uid === request.params.uid) {
                    return {
                        ...todo, ...data
                    }
                }
                
                return todo;
            })
            status = 200;
            break;    
        default:
            return {
                status: 404,
                body: 'Not found'
            };
    }
    
    if (request.method.toUpperCase() !== 'GET') {
        return {
            status: 303,
            headers: {
                location: '/'
            }
        }
    }

    return {
        status, 
        body
    }
};