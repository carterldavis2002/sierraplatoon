import './App.css'
import RuleMessage from './components/RuleMessage'

function App() {

  const buildMessages = () => {
    let arr = []
    for (let i = 0; i < 100; i++) {
      arr.push(<RuleMessage key={`${i}`} />)
    }
    return arr
  }

  return (
    <div>
      {buildMessages()}
    </div>
  )
}

export default App
