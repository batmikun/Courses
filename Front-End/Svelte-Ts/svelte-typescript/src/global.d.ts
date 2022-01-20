import uuid from 'uuid/v4';
/// <reference types="@sveltejs/kit" />

type Todo = {
    uid: uuid;
    created_at: Date;
    text: string;
    done: boolean;
}