import { useState } from "react";
import { useHistory } from "react-router-dom";

const Create = () => {

    const [title, setTitle] = useState('');
    const [body, setBody] = useState('');
    const [author, setAuthor] = useState('Mario');
    const history = useHistory();

    const handleSubmit = (e) => {
        e.preventDefault()
        const blog = {
            title,
            body,
            author
        }

        fetch("http://localhost:8000/blogs/",{
            method: 'POST',
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(blog)
        }).then(() =>{
            console.log('new blog added')
            history.push('/')
        })
    }

    return ( 
        <div className="create">
            <h2>Add a New Blog</h2>
            <form>
                <label>Blog Title</label>
                <input type="text"
                    value= { title } 
                    onChange = {(e) => setTitle(e.target.value)} 
                    required 
                />
                <label>Blog Body</label>
                <textarea 
                    value={ body }
                    onChange = {(e) => setBody(e.target.value)}
                    required 
                />
                <label>Blog Author</label>
                <select value={ author } onChange={(e) => setAuthor(e.target.value)}> 
                    <option value="Mario">Mario</option>
                    <option value="Luigi">Luigi</option>
                </select>
                <button onClick={(e) => handleSubmit(e)}>Add Blog</button>
            </form>
        </div>
     );
}
export default Create;