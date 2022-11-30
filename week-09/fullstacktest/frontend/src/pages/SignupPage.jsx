import {Navigate} from 'react-router-dom'

function SignupPage({message, setMessage, logIn, user}) {

    const signUp = async (e) => {
        e.preventDefault()
    
        const res = await axios.post('/signup', {
          email: e.target.email.value,
          password: e.target.password.value
        })
    
        if (res.data.err)
          setMessage(res.data.err)
        else
          logIn(e)
      }

    return (
        <div>
            {user && <Navigate to='/'/>}
            <form onSubmit={signUp} method='POST'>
                <h1>{message}</h1>
                <h2>Sign Up</h2>
                <input type='text' placeholder='email' name='email'></input>
                <input type='password' placeholder='password' name='password'></input><br></br>
                <input type='submit' id='signup' value='Sign Up'></input>
            </form>
        </div>
    )
}

export default SignupPage