import './App.css'
import on from './assets/icons/on.svg'
import off from './assets/icons/off.svg'

function App() {

  const toggle = (e) => {
    if (e.target.dataset.src == on) {
      e.target.dataset.src = off
      e.target.src = off
      return
    }

    e.target.dataset.src = on
    e.target.src = on
  }

  return (
    <div>
      <img data-src={on} src={on} onClick={toggle}></img>
    </div>
  )
}

export default App