import React from 'react';
import {Link} from 'react-router-dom';

const ListIssue = ({issue}) => {
  return (
    <div>
        <Link to={`/api/v1/jira/${issue.id}`}>
            <div className='issue-summary'>{issue.summary}</div>
        </Link>
    </div>
  )
}
export default ListIssue