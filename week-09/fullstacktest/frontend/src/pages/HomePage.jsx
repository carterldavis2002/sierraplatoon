import {Link} from 'react-router-dom'

function HomePage({user, whoAmI, loading}) {
    const logOut = async () => {
        await axios.post('/logout')
        whoAmI()
    }

    const renderLabel = () => {
        if (!loading && user)
            return <h1>{"Logged in as " + user.email}</h1>
        
        if (!loading && !user)
            return <h1>{"Not logged in"}</h1>
    }

    return (
        <div>
            {console.log(user)}
            {renderLabel()}
            {!loading && !user && <Link to='/signup-page'><button>Sign Up</button></Link>}
            {!loading && !user && <Link to='/login-page'><button>Log In</button></Link>}
            {!loading && user && <button onClick={logOut}>Log Out</button>}
        </div>
    )
}

export default HomePage