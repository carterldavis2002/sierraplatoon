// components/MyButton.jsx

function MyButton(props) { // notice that we take in a parameter for our functional component, which is an object that captures ALL props that are passed down
    // render
    return (
      <div>
        <button id="my-button" onClick={props.handleClick}>Click Me!</button> {/* access items from props */}
      </div>
    )
  }
  
  export default MyButton;