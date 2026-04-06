import React from 'react';

const IssueCard = ({ issue }) => {
  return (
    <div style={{ border: '1px solid #ccc', padding: '15px', margin: '10px 0', borderRadius: '8px' }}>
      <h3>{issue.title}</h3>
      <p><strong>Repo:</strong> {issue.repo}</p>
      <p><strong>Score:</strong> {issue.score}</p>
      <a href={issue.url} target="_blank" rel="noopener noreferrer">View on GitHub</a>
    </div>
  );
};

export default IssueCard;
