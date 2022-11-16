function Dropdown(props) {

    return (
      <div>
        <h1>Choose a State</h1>
        <select onChange={(e) => props.setState(e.target.value)}>
            {
              props.states.map((s, i) => {
                return (
                  <option key={i} value={s['alpha-2']}>
                    {s.name}
                  </option>
                )
              })
            }
        </select>
      </div>
    )
  
  }
  
export default Dropdown