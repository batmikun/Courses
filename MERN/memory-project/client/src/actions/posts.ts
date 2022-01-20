import * as api from '../api';
import { createPosts } from '../api/index';

export const getPosts = () => async (dispatch: any) => {
    try {
        const { data } = await api.fetchPosts();

        dispatch({ type: 'FETCH_ALL', payload: data });
    } catch (error) {
        console.log(error);
    }
}

export const createPost = (post:Record<string,unknown>) => async (dispatch: any) => {
    try{
        const { data } = await createPosts(post);

        dispatch({ type: 'CREATE', payload: data });
    } catch (error) {
        console.log(error);
    }
}