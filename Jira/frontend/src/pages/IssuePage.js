import React, { useEffect, useState, useRef } from 'react'
import {Link, useParams, useNavigate} from 'react-router-dom'
import Cookies from 'js-cookie'
import ListUsers from '../components/ListUsers'
import ListStatus from '../components/ListStatus'
import ListIssueType from '../components/ListIssueType'
import ListComment from '../components/ListComment'

const IssuePage = () => {
  
  let navigate = useNavigate()
  let issueId = useParams().id
  let [issue, setIssue] = useState("Default Value")
  let [email, setEmail] = useState('')
  let [issueStatus, setIssueStatus] = useState(0)
  let [users, setUsers] = useState([{'email' : ''}])
  let [comment, setComment] = useState({'post' : '', 'user' : '', 'issue_id' : ''})
  
  let setUserEmail = (userEmail) => {
    return userEmail.email
  }

  useEffect(() => {
    getIssue()
    getUsers()
  },[setIssue, setUsers, setComment])
  let getIssue = async () => {
    let response = await fetch(`/api/v1/jira/${issueId}`)
    let issue = await response.json()
    email = setEmail(()=>setUserEmail(issue.assigned_to))
    issueStatus = setIssueStatus(issue.status)
    setIssue(issue)
  }

  let getUsers = async () =>{
    let response = await fetch('/api/v1/jira/users')
    users = await response.json()
    setUsers(users)
  }
  
  let updateIssue = (e) => {
    e.preventDefault()
    issue.assigned_to = {"email" : e.target.useremail.value}
    issue.status = e.target.IssueStatus.value
    issue.issue_type = e.target.story_type.value
    fetch(`/api/v1/jira/${issueId}/update`, {
      method : "PUT",
      headers : {
        'X-CSRFTOKEN': Cookies.get('csrftoken'),
        'Content-Type' : 'application/json'
      },
      body : JSON.stringify(issue)
    }).then(async (res) =>{
      let text = await res.json()
      if (res.status === 200){
        console.log("Server output", text)
        navigate('/api/v1/')
      }
    })
  }

  let deleteIssue = ()=>{
    fetch(`/api/v1/jira/${issueId}/delete`, {
      method : 'DELETE',
      headers : {
        'X-CSRFTOKEN': Cookies.get('csrftoken'),
        'Content-Type' : 'application/json'
      }
    }).then(async (res) =>{
      let text = await res.json()
      if (res.status === 200){
        console.log(text)
        navigate("/api/v1/")
      }else{
        console.log("Something went wrong", res.status)
      }
    })
  }

  let addComments = (e) => {
    fetch('/api/v1/jira/comment/add', {
      method : "POST",
      headers : {
        'X-CSRFTOKEN': Cookies.get('csrftoken'),
        'Content-Type' : 'application/json'
      },
      body : JSON.stringify(comment)
    })
    window.location.reload();
  }

  return (
    <div>
      <form onSubmit={e=>updateIssue(e)}>
      <label>Summary:</label>
      <textarea rows={1} cols={40} type="text" className='issue-summary' onChange={(e) => setIssue({...issue, 'summary': e.target.value})} defaultValue={issue.summary}/><br/>
      <label>Description:</label>
      <textarea rows={4} cols={40} type="text" className='description'></textarea>
      
      <ListComment issue_id = {issueId}/>
      <ListUsers email={email}/> 
      <ListStatus IssueStatus={issueStatus}/>
      <ListIssueType current_story={issue.issue_type}/>
      
      <div className='issue-update'>
        <Link to={'/api/v1'}>
          <button>Back</button>
        </Link>
          <button>Update</button>
      </div>
      </form>
      <button onClick={(e)=> {deleteIssue(e)}}>Delete</button>
      <div className="comments-section">
        <label>Comments:</label>
        <textarea rows={4} cols={44} type="text" onChange={(e)=> setComment({...comment, 'post' : e.target.value, user: issue.assigned_to['email'], issue_id : issue.id})} name="comment" className="comments"></textarea>
        <button onClick={(e)=>addComments(e)}>Add Comment</button>
      </div>
    </div>
  )
}

export default IssuePage