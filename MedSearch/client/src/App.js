import React, { useState, useEffect } from "react";
import axios from "axios";

let baseURL = "http://localhost:5000"
let route = "" //api endpoint goes here
function App() {

  const [data, setData] = useState(null)

  useEffect(() => { 
    axios.get(`${baseURL}/${route}`).then( 
      res => res.data
    ).then(data => {
      setData(data)
      console.log(data)
    }).catch(err => console.error(err)) 
  }, [])

  return (
      <div className="App">
        <h1>Title</h1>
        <p>{!data ? "Loading..." : data.msg}</p>
      </div>
  );
}

export default App;
