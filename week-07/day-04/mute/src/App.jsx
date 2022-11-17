import './App.css'
import on from './assets/icons/on.svg'
import off from './assets/icons/off.svg'
import {useState} from 'react'

function App() {

  const [link, setLink] = useState(on)
  const toggle = () => setLink(link == on ? off : on)

  return (
    <div>
      <img src={link} onClick={toggle}></img>
    </div>
  )
}

export default App