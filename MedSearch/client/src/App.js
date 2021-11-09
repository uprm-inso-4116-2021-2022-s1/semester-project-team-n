import React, { useState, useEffect } from "react";
import axios from "axios";
import Toolbar from "./components/Toolbar/Toolbar";
import Auth from "./components/Auth/Auth"
import { Form, FormInput, FormGroup } from "shards-react";
import "bootstrap/dist/css/bootstrap.min.css";
import "shards-ui/dist/css/shards.min.css"
import logo from './Logo.png';


// let baseURL = "http://localhost:5000"
// let route = "" //api endpoint goes here

const initialAuthState = {Email: '', Password: '', AccountType: '',  authType: 'logIn'} //authTypes: register, logIn, loggedIn

function App() {
  const [authState, setAuthState] = useState(initialAuthState)
  const [text, setText] = useState('')


  // const [data, setData] = useState(null)

//   useEffect(() => { 
//     axios.get(`${baseURL}/${route}`).then( 
//       res => res.data
//     ).then(data => {
//       setData(data)
//       console.log(data)
//     }).catch(err => console.error(err)) 
//   }, [])

  const handleAuthStateChange = (authStateChange) => {
    setAuthState(authStateChange)
  }

  return (
    <div className="h-screen w-screen bg-fourth p-2">
      
      {authState.authType !== 'loggedIn' &&
      
      <div className="p-14 ">
        <img src={logo} className="App-logo" alt="logo"/>
        <h1> User Authentication</h1>
        <Auth authState={authState} onAuthStateChange={(e) => handleAuthStateChange(e)} />
      </div>
      }
      {authState.authType === 'loggedIn' &&
      <div>
        <Toolbar className='fixed'/>
        <h1>APP CONTENT</h1>
      </div>
      }
    </div>


    // <div className="App">
    //   <h1>Title</h1>
    //   <p>{!data ? "Loading..." : data.msg}</p>
    // </div>
  );
}

export default App;
