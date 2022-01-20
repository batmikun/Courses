import { useState } from "react";
import axios from 'axios';
import { useCookies } from 'react-cookie';

const Auth = () => {
    const [cookie, setCookie, removeCookie] = useCookies(['user']);
    const [isLogin, setIsLogin] = useState(true);
    const [username, setUsername] = useState(null);
    const [password, setPassword] = useState(null);
    const [confirmPassword, setConfirmPassword] = useState(null);
    const [error, setError] = useState(null);

    const handleSubmit = async () => {
        
        if (password !== confirmPassword) {
            setError(true);
            return;
        }

        const response = await axios.post('http://localhost:8000/singup', {
            username,
            password
        })

        console.log(response);

        setCookie('Username', response.data.username)
        setCookie('HashedPassword', response.data.hashedPassword)
        setCookie('UserId', response.data.userId)
        setCookie('AuthToken', response.data.token)

        window.location.reload();
    }   

    return ( 
        <div className="auth__container">
            <div className="auth__container__box">
                <div className="auth__container__form">
                    <input 
                        type="text"
                        id="username"
                        name="username"
                        placeholder="Username"
                        onChange = {(e) => setUsername(e.target.value)}
                    />
                    <input 
                        type="text"
                        id="password"
                        name="password"
                        placeholder="password"
                        onChange = {(e) => setPassword(e.target.value)}
                    />
                    {!isLogin && <input 
                        type="text"
                        id="password-check"
                        name="password-check"
                        placeholder="password-check"
                        onChange = {(e) => setConfirmPassword(e.target.value)}
                    />}
                    <button onClick={handleSubmit}>GO!</button>
                </div>
                {error && <p>Passwords do not match</p>}
            </div>
            <div className="auth__container__options">
                <button onClick={() => setIsLogin(false)} name="singUp" id="singUp">Sing Up</button>
                <button onClick={() => setIsLogin(true)} name="login" id="login">Login !!</button>
            </div>
        </div>    
     );
}
 
export default Auth;
