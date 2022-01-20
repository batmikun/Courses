import type { RequestHandler } from '@sveltejs/kit';
import { api } from "./_api";

export const del: RequestHandler = (request) => {
    return api(request)
} 

export const patch: RequestHandler<unknown, FormData> = (request) => {
    return api(request, {
        text: request.body.get("text") ? request.body.get("text") : undefined,
        done: request.body.get("done") ? !!request.body.get("done") : undefined
    })
}