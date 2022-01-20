6import { v4 as uuid } from 'uuid';

import type { RequestHandler } from "@sveltejs/kit"
import type { Request } from "@sveltejs/kit"
import  { api } from "./_api";


export const get: RequestHandler = (request: Request) => {
    return api(request);
}

export const post: RequestHandler<never, FormData> = (request) => {
    return api(request, {
        uid: uuid(),
        created_at: new Date(),
        text: request.body.get("text"),
        done: false
    })
}