function Dropdown(props) {
    return (
      <div>
        <h1>Choose a State</h1>
        <select id="dropdown" onChange={(e) => props.setState(e.target.value)} value={props.states[0]['alpha-2']}>
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