import React, {useState, useEffect} from 'react';
import ListIssue from '../components/ListIssue'
import { Link } from 'react-router-dom';

const IssueListPage = () => {
  let [issues, setIssue] = useState([])

  useEffect(() => {
    getIssues()
  }, [])

const getIssues = async () => {
    let response = await fetch('/api/v1/')
    let data = await response.json()
    setIssue(data)
}
  return (
    <div>
        <div className='issues-list'>
            {issues.map((issue, index) => (
                <ListIssue key={index} issue={issue}/>
            ))}
        </div>
        <Link to='/api/v1/create'>
        <button className='create-issue'>Create</button>
        </Link>
            
    </div>
  )
}

export default IssueListPage