import React, {useState, useEffect} from 'react'

const ListUsers = ({email}) => {

  let [users, setUsers] = useState(() =>[{'email': ''}])
  let [userEmail, setUserEmail] = useState("")
  
  useEffect(()=>{
    getUsers()
    setUserEmail(email)
  },[email])

  let getUsers = async () =>{
    let response = await fetch('/api/v1/jira/users')
    users = await response.json()
    setUsers(users)
    setUserEmail(email)
  }
  
  return (
      <div>
        <select cols={40} name="useremail" value={userEmail?userEmail:'NEW'} onChange={(e)=>setUserEmail(e.target.value)} >
            {users.map((user, index)=>
                <option key={index} value={user.email}>{user.email}</option>
                )}
        </select>
    </div>
  )
}

export default ListUsers