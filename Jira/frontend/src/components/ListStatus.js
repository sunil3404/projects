import React, { useEffect, useState } from "react"

const ListStatus = ({IssueStatus}) => {

    let [isStatus, setIsStatus] = useState([{'id' : '', 'status': ''}])
    let [jiraStat, setJiraStat] = useState()
  
    useEffect(()=>{
      getStatus()
      setJiraStat(IssueStatus)
    },[IssueStatus])
  
    let getStatus = async () =>{
      let response = await fetch('/api/v1/jira/status')
      isStatus = await response.json()
      setIsStatus(isStatus)
    }
    return (
        <div>
          <select name="IssueStatus" value={jiraStat} onChange={(e)=>setJiraStat(e.target.value)} >
              {isStatus.map((stat, index)=>
                  <option key={index} value={stat.id}>{stat.status}</option>
                  )}
          </select>
      </div>
    )
  }

export default ListStatus