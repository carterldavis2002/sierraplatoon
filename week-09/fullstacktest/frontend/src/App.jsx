import { useEffect } from 'react'
import { useState } from 'react'
import './App.css'
import {HashRouter as Router, Routes, Route} from 'react-router-dom'
import HomePage from './pages/HomePage'
import SignupPage from './pages/SignupPage'
import LoginPage from './pages/LoginPage'

const getCSRFToken = ()=>{
  let csrfToken

  const cookies = document.cookie.split(';')
  for ( let cookie of cookies ) {
      const crumbs = cookie.split('=')
      if ( crumbs[0].trim() === 'csrftoken') {
          csrfToken = crumbs[1]
      }
  }
  return csrfToken
}

axios.defaults.headers.common['X-CSRFToken'] = getCSRFToken()

function App() {
  const [message, setMessage] = useState("")
  const [user, setUser] = useState(null)
  const [loading, setLoading] = useState(true)

  const logIn = async (e) => {
    e.preventDefault()

    const res = await axios.post('/login', {
      email: e.target.email.value,
      password: e.target.password.value
    })

    if (res.data.err)
      setMessage(res.data.err)
    else
      window.location.reload()
  }

  const whoAmI = async () => {
    const response = await axios.get('/whoami')
    const youAre = response.data && response.data[0] && response.data[0].fields
    
    setUser(youAre)
    setLoading(false)
  }

  useEffect(() => {
    whoAmI()
  }, [])

  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path='/' element={<HomePage user={user} whoAmI={whoAmI} loading={loading}/>}/>
          <Route path='signup-page' element={<SignupPage message={message} setMessage={setMessage} logIn={logIn} user={user}/>}/>
          <Route path='login-page' element={<LoginPage message={message} logIn={logIn} user={user}/>}/>
        </Routes>
      </Router>
    </div>
  )
}

export default App
