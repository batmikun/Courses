import BlogList from './BlogList';
import useFetch from './useFetch';

const Home = () => {

    const {data: blogs, error} = useFetch("http://localhost:8000/blogs");
    
    return (  
        <div className="Home">
            { blogs ? <BlogList blogs={ blogs } title="All Blogs!" /> : <div>Loading...</div> }
            { error ? <div>{ error }</div> : null }
        </div> 
    );
}
 
export default Home;