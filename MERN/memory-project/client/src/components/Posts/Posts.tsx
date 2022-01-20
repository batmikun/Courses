import Post from './Post/Post';
import useStyles from './styles';
import { useSelector } from 'react-redux';
import type { RootState } from '../../reducers';

const Posts = () => {
    const classes = useStyles();
    
    const posts = useSelector((state: RootState) => state.posts);

    console.log(posts);

    return(
        <>
            <Post />
            <Post />
        </>
    );
}

export default Posts;