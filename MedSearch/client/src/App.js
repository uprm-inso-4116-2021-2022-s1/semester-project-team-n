import React, { useState, useEffect } from "react";
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'
import axios from "axios";
import Toolbar from "./components/Toolbar/Toolbar";
import Auth from "./components/Auth/Auth"
import logo from './Logo.png';
import Appointments from "./pages/Appointments/Appointments";
import Offices from "./pages/Offices/Offices";
import Home from "./pages/Home/Home";


// let baseURL = "http://localhost:5000"
// let route = "" //api endpoint goes here

const initialAuthState = {Email: '', Password: '', AccountType: '',  authType: 'logIn'} //authTypes: register, logIn, loggedIn

function App() {
  const [authState, setAuthState] = useState(initialAuthState)

  // const [data, setData] = useState(null)

//  EXAMPLE OF AXIOS GET FUNCTION
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
    <Router>
      <div className=" h-screen bg-fifth overflow-auto">
        
        {authState.authType !== 'loggedIn' &&
        <div className="p-14 flex flex-col justify-center items-center">
          <img src={logo}  alt="logo"/>
          <Auth authState={authState} onAuthStateChange={(e) => handleAuthStateChange(e)} />
        </div>
        }

        {authState.authType === 'loggedIn' &&
        <div>
          <Toolbar/>
          <div className=" pt-20">
            <Routes>
              {/* HERE GOES THE HOME PAGE which shows DOCTORS/OFFICES OR WHTVR */}
              {/* en el caso de DOCTOR it would show their patients */}
              <Route exact path="/" element={<Home/>} />
              <Route path="appointments" element={<Appointments />} />
              <Route path="offices" element={<Offices />} />
            </Routes>
          </div>
        </div>
        }
      </div>
    </Router>
  );
}

export default App;
