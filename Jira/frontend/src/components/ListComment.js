import React, {useState, useEffect} from 'react'

const ListComment = ({issue_id}) => {
  let [comments, setComments] = useState([])
  let [id, setId] = useState(issue_id)
  
  useEffect(()=>{
    getComments()
  }, [setComments])

  let getComments = async () => {
    let response = await fetch(`/api/v1/jira/comments/${issue_id}`)
    comments = await response.json()
    setComments(comments)
  }
  return (
    <div>
        {comments.map((comment, index)=>
                <p key={index} value={comment.id}>{comment.post}</p>
        )}
    </div>
  )
}

export default ListComment