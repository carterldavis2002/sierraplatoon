function InputWord (props) {

    const updateWord = () => {
        const text = document.querySelector('input').value
        props.handleSubmit([text, ...props.word])

        let vowels = 0
        for (let i = 0; i < text.length; i++) {
            if (text[i] == 'a' || text[i] == 'i' || text[i] == 'e' || text[i] == 'o' || text[i] == 'u')
                vowels++
        }
        props.vowelSet([vowels, ...props.vowels])
    }

    return (
        <div className="InputWord">
            <h1>Type Thy Word</h1>
            <input type="text" placeholder="Type here..." /><br />
            <button onClick={updateWord}>Submit</button>
        </div>
    )
}

export default InputWord;