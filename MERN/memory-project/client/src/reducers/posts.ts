export const reducer = (posts:Array<Record<string,unknown>> = [], action: Record<string, unknown>) => {
    switch (action.type) {
        case 'FETCH_ALL':
            return action.payload;
        case 'CREATE':
            return [...posts, action.payload];	
        default:
            return posts;
    }
}

export default reducer;