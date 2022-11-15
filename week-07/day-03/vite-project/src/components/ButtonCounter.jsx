// ButtonCounter.jsx

// react
import { useState } from "react"

// components
import MyButton from "./MyButton.jsx"
import MyOutputLabel from "./MyOutputLabel.jsx"

function ButtonCounter() {
  // states
  const [counter, setCounter] = useState(0)

  // event handlers
  const incrementCounter = () => {
    setCounter(prevCounter => prevCounter + 1)
  }

  // render
  return (
    <div>
      <MyButton handleClick={incrementCounter} /> {/* new component, taking in a prop value of handleClick */}
      <MyOutputLabel counter={counter} /> {/* new component, taking in a prop value of myValue */}
    </div>
  )
}

export default ButtonCounter;