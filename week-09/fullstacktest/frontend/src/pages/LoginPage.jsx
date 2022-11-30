import {Navigate} from 'react-router-dom'

function LoginPage({message, logIn, user}) {
    return (
        <div>
            {user && <Navigate to='/'/>}
            <h1>{message}</h1>
                <form onSubmit={logIn} method='POST'>
                <h2>Log In</h2>
                <input type='text' placeholder='email' name='email'></input>
                <input type='password' placeholder='password' name='password'></input><br></br>
                <input type='submit' id='login' name='submit' value='Log In'></input>
            </form>
        </div>
    )
}

export default LoginPage