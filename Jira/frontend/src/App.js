import './App.css';
import Header from './components/Header';
import IssueListPage from './pages/IssueListPage'
import IssuePage from './pages/IssuePage'
import CreateIssue from './pages/CreateIssue';
import RegisterUser from './pages/RegisterUser';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom'

function App() {
  return (
    <Router>
      <div className="App">
        <Header/>
        <Routes>
          <Route path='/api/v1' exact Component={IssueListPage}></Route>
          <Route path='/api/v1/jira/:id' exact Component={IssuePage}></Route>
          <Route path='/api/v1/create' exact Component={CreateIssue}></Route>
          <Route path='/api/v1/jira/Register' exact Component={RegisterUser}></Route>

        </Routes>
      </div>
    </Router>
  );
}

export default App;
