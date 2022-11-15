import './App.css';

// components
import ButtonCounter from "./components/ButtonCounter.jsx"

function App() {
  // render
  return (
    <div className="App">
      <h2 id="my-header">My Button Click Counter App</h2>
      <ButtonCounter />
      <ButtonCounter />
      <ButtonCounter />
    </div>
  )
}

export default App;