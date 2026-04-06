import React, { useState } from 'react';
import IssueCard from '../components/IssueCard';

const Home = () => {
  const [skills, setSkills] = useState('');
  const [issues, setIssues] = useState([]);
  const [loading, setLoading] = useState(false);

  const findIssues = async () => {
    setLoading(true);
    // TODO: Connect to real backend API
    // const response = await fetch(`http://localhost:8000/issues?skills=${skills}`);
    // const data = await response.json();
    
    // Placeholder data for now
    const dummyData = [
      {
        title: `Sample Issue for ${skills || 'any skill'}`,
        repo: "example/repo",
        url: "#",
        score: 50
      },
      {
        title: "Another Beginner Friendly Issue",
        repo: "test/repo",
        url: "#",
        score: 75
      }
    ];
    
    setTimeout(() => {
      setIssues(dummyData);
      setLoading(false);
    }, 500);
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h1>FirstPR Pro</h1>
      <p>Find your first open source contribution based on your skills!</p>
      
      <div style={{ marginBottom: '20px' }}>
        <input 
          type="text" 
          value={skills} 
          onChange={(e) => setSkills(e.target.value)} 
          placeholder="Enter skills (e.g., Python, React)"
          style={{ padding: '10px', width: '70%', marginRight: '10px' }}
        />
        <button onClick={findIssues} style={{ padding: '10px 20px' }}>
          Find Issues
        </button>
      </div>

      <div id="results">
        {loading && <p>Searching...</p>}
        {issues.map((issue, index) => (
          <IssueCard key={index} issue={issue} />
        ))}
        {!loading && issues.length === 0 && <p>No issues found yet. Enter your skills and click search!</p>}
      </div>
    </div>
  );
};

export default Home;
