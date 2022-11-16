function OutputWord (props) {

    let key = 0;
    const displayCharacters = () => {
        let arr = []

        for (let i = 0; i < props.word.length; i++) {
            arr.push(<div key={`${key}`}>{getSpans(props.word[i])}</div>)
            key++;
            arr.push(<p key={`${key}`}>Vowel Count: {props.vowels[i]}</p>)
            key++;
        }

        return arr
    }

    const getSpans = (w) => {
        let arr = []

        for (let i = 0; i < w.length; i++) {
            key++;
            if (w[i] == 'a' || w[i] == 'i' || w[i] == 'e' || w[i] == 'o' || w[i] == 'u')
            {
                arr.push(<span key={`${key}`} className="vowel">{w[i]}</span>)
            }
            else
                arr.push(<span key={`${key}`}>{w[i]}</span>)
        }

        return arr
    }

    return (
        <div>
            {displayCharacters()}
        </div>
    )
}

export default OutputWord;