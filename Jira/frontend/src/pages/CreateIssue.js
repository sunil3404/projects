import React, {useEffect, useState} from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import Cookies from 'js-cookie';

const CreateIssue = () => {
  
  let navigate = useNavigate()
  let [data, setData] = useState("")
  let [users, setUsers] = useState([{'email': ''}])
  let [stories, setStories] = useState([{'story': ''}])
  let [status, setStatus] = useState([{'status': ''}])

  useEffect(() =>{
    getUsers()
    getStories()
    getStatus()
  }, [])

  let getStories = async () => {
      let response = await fetch('/api/v1/jira/story')
      stories = await response.json()
      setStories(stories)
  }

  let getStatus = async() => {
    let response = await fetch('/api/v1/jira/status')
    status = await response.json()
    setStatus(status)
}

  let getUsers = async () => {
      let response = await fetch('/api/v1/jira/users')
      users = await response.json()
      setUsers(users)
  }
  let handleCreateIssue = async (e) => {
    
    e.preventDefault()
    data = {
      summary : e.target.summary.value,
      assigned_to : e.target.assigned_to.value,
      issue_type : e.target.issue_type.value,
      status : e.target.status.value
  }
    fetch("jira/create", {
        method:"POST",
        headers : {
            'X-CSRFTOKEN': Cookies.get('csrftoken'),
            'Content-Type' : "application/json"
        },
        body : JSON.stringify(data)
    }).then(async (res) =>{
      let text = await res.json()
      console.log(text)
    })
    navigate('/api/v1')
  }
  return (
    <div>
        <form onSubmit={(e) => handleCreateIssue(e)}>
            <input placeholder='summary' name='summary'/>
            <select name='assigned_to' defaultValue="AssignUser" onChange={(e) => e.target.value}>
                <option value="assigned_to">Assign To</option>
                {users.map((user, index)=> <option key={index} value={user.email}>{user.email}</option>)}
            </select>
            <select name='issue_type' defaultValue="bug">
                <option value="bug">---Issue Type---</option>
                {stories.map((issuetype, index)=> <option key={index} value={issuetype.story}>{issuetype.story}</option>)}
            </select>
            <select name='status' defaultValue="new">
                <option value="new">---set status---</option>
                {status.map((stat, index)=> <option key={index} value={stat.status}>{stat.status}</option>)}
            </select>
            <button>Submit</button>
        </form>
    </div>
  )
}

export default CreateIssue