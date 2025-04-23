import React, {useState, useEffect} from 'react'

const ListIssueType = ({current_story}) => {
    let [storyTypes, setStoryTypes] = useState([{'id' : '', 'story': ''}])
    let [story, setStory] = useState()

    useEffect(()=>{
    getStory()
    setStory(current_story)
    },[current_story])

    let getStory = async () =>{
    let response = await fetch('/api/v1/jira/story')
    storyTypes = await response.json()
    setStoryTypes(storyTypes)
    }
    return (
        <div>
        <select name="story_type" value={story?story:'TASK'} onChange={(e)=>setStory(e.target.value)} >
            {storyTypes.map((st, index)=>
                <option key={index} value={st.id}>{st.story}</option>
                )}
        </select>
    </div>
    )
}

export default ListIssueType