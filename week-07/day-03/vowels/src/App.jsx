import { useState } from 'react'

import './App.css'
import InputWord from './components/InputWord.jsx'
import OutputWord from './components/OutputWord.jsx'

function App() {
  const [word, setWord] = useState("")
  const [vowels, setVowels] = useState(0)

  return (
    <div className="App">
      <InputWord handleSubmit={setWord} vowelSet={setVowels} />
      <OutputWord word={word} vowels={vowels} />
    </div>
  )
}

export default App
