import React, {useState, useEffect} from "react";
import axios from "axios";
import { Form, FormInput, FormGroup, Card, CardBody, CardTitle, Button, ButtonGroup, FormSelect} from "shards-react";

import "bootstrap/dist/css/bootstrap.min.css";
import "shards-ui/dist/css/shards.min.css"


export default function Auth(props) {

    // structure
    // authState = {
    //     Email: //email//,
    //     Password: //Password//,
    //     AccountType: //'med' or 'patient'//,
    //     authType: //'loggedIn' or 'logIn' or 'register'// 
    // }

    const handleChange = (e) => {
      props.onAuthStateChange({...props.authState, [e.target.name]: e.target.value})
    }

    const submit = (e) => {
      if (e.target.name === 'register')
        axios.post('/user', {Email: props.authState.Email, Password: props.authState.Password, AccountType: props.authState.AccountType})
          .then((res) => {
            props.onAuthStateChange({...props.authState, authType: 'logIn'})
            console.log(res)
          })
          .catch(error => {
            console.log(error)
          })
      else if (props.authState.authType === 'logIn') {
        console.log("log in!")
      }
    }


    return (
        <Card >
          <CardBody>
            {props.authState.authType === 'register' && 
              <CardTitle>Register an Account</CardTitle>
            }
            {props.authState.authType === 'logIn' && 
              <CardTitle>Sign in</CardTitle>
            }
            <Form>
              <FormGroup>
                <FormInput name="Email" onChange={(e) => handleChange(e)} placeholder="Email"/>
              </FormGroup>
              <FormGroup>
                <FormInput name="Password" onChange={(e) => handleChange(e)} type="Password" placeholder="Pasword"/>
              </FormGroup>
              {props.authState.authType === 'register' && 
                <FormGroup>
                  <FormSelect name="AccountType" onChange={(e) => handleChange(e)}>
                      <option value="" disabled> Select an Account Type... </option>
                      <option value="med">Med Consultant</option>
                      <option value="patient">Patient</option>
                  </FormSelect>
                </FormGroup>
              }
            </Form>
            {props.authState.authType === 'register' &&
            <ButtonGroup>
              <Button name='register' onClick={(e) => submit(e)}>Register</Button>
              <Button theme="secondary" name='authType' value='logIn' onClick={(e) => handleChange(e)} >Log In Intead</Button>
            </ButtonGroup>
            }
            {props.authState.authType === 'logIn' &&
            <ButtonGroup>
                          {/* change this to actually verify user authentication !!  */}
              <Button name='authType' value='loggedIn' onClick={(e) => handleChange(e)}>Log In</Button>
              <Button theme="secondary" name="authType" value='register' onClick={(e) => handleChange(e)} >Register an account</Button>
            </ButtonGroup>
            }  
          </CardBody>
        </Card>
    );
}