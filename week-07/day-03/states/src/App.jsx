import './App.css'
import {useState} from 'react'
import Dropdown from './components/Dropdown'
import Output from './components/Output'
import states from './statedata/index'

function App() {

  const [state, setState] = useState(states[0]['alpha-2'])

  return (
    <div>
      <Dropdown states={states} setState={setState} />
      <Output state={state} />
    </div>
  )

}

export default App
