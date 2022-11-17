import './App.css'
import {useRef} from 'react'
import { useState } from 'react'

function App() {

  const inputRef = useRef(null)
  const [message, setMessage] = useState("")
  const checkPalindrome = () => {
    let text = inputRef.current.value
    let palindrome = text.toString().toLowerCase().replace(/\W|_|\s/g, "") ===
                     text.toString().toLowerCase().replace(/\W|_|\s/g, "").split("").reverse().join("")

    if (text.trim() == "") {
      setMessage("")
      return
    }

    setMessage(`${text} ${palindrome ? 'is' : 'is not' } a palindrome`)
  }

  return (
    <div className="App">
      <h1>Palindrome Checker</h1>
      <input ref={inputRef} type="text" onChange={checkPalindrome}></input>
      <p>{message}</p>
    </div>
  )
}

export default App
