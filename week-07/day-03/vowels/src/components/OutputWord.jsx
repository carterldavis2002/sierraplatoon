function OutputWord (props) {

    const displayCharacters = () => {
        let arr = []
        for (let i = 0; i < props.word.length; i++) {
            if (props.word[i] == 'a' || props.word[i] == 'i' || props.word[i] == 'e' || props.word[i] == 'o' || props.word[i] == 'u')
            {
                arr.push(<span className="vowel">{props.word[i]}</span>)
            }
            else
                arr.push(<span>{props.word[i]}</span>)
        }

        return arr
    }

    return (
        <div>
            <div className="OutputWord">
                {displayCharacters()}
            </div>
            <p>Vowel Count: {props.vowels}</p>
        </div>
    )
}

export default OutputWord;