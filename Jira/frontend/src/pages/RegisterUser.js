import React, {useState, useEffect} from 'react'
import Cookies from 'js-cookie';
import { useNavigate } from 'react-router-dom';

const RegisterUser = () => {
    let navigate = useNavigate()

    let [user, setUser] = useState({
        'username' : '', 
        'email' : '', 
        'password':'',
        'confirm_password' : ''
    })
  
  let setUserData = (e) =>{
    return {"username" : e.target.username.value, 
            "email" : e.target.email.value, 
            "password": e.target.password.value,
            "confirm_password" : e.target.confirm_password.value
        }
    }
  let createUser = (e) =>{
        e.preventDefault()
        user = setUserData(e)
        fetch('/api/v1/jira/register', {
            method : 'POST',
            headers : {
                'X-CSRFTOKEN': Cookies.get('csrftoken'),
                'Content-Type' : 'application/json'
            },
            body : JSON.stringify(user)
        }).then(async (response) => {
            let userdata = await response.json()
            if (!userdata.email){
                console.log(userdata)
            }else{
                navigate("/api/v1")
            }    
        }) 
        
    }

  return (
    <div>
        <form onSubmit={(e)=>createUser(e)}>
            <input type='text' placeholder='username' name='username'/>
            <input type='text' placeholder='email' name='email'/>
            <input type='password' placeholder='password' name='password'/>
            <input type='password' placeholder='confirm-password' name='confirm_password'/>
            <button type='submit'>Register</button>
        </form>
    </div>
  )
}

export default RegisterUser