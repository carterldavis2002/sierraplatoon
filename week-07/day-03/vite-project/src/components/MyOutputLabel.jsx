// components/MyOutputLabel.jsx

function MyOutputLabel(props) { // accept "props" object as the first parameter
    // render
    const renderOutput = () => {
      console.log(">> internal counter value: ", props.counter)
  
      if (props.counter == 0) {
        return "You haven't clicked the button yet!"
      }
      
      const maxCount = 10
      if (props.counter > maxCount) {
        return `You've clicked the counter more than ${maxCount} times. I'm not counting anymore.`
      }
  
      return `You've clicked the button ${props.counter} times.`
    }
    
    return (
      <div>
        <p id="my-output">{ renderOutput() }</p> {/* calling a function here */}
      </div>
    )
  }
  
  export default MyOutputLabel;