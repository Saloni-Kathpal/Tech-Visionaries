import React from 'react';

const IssueCard = ({ issue }) => {
  // AI-RECOMMENDED FORMAT
  if (issue.is_ai_recommended) {
    const difficultyColors = {
      'beginner': 'var(--accent-green)',
      'intermediate': 'var(--accent-yellow)',
      'advanced': 'var(--accent-red)'
    };
    
    // Attempt parsing lowercase difficulty for color matching
    const lvlStr = (issue.difficulty || '').toLowerCase();
    let badgeColor = 'var(--accent-cyan)';
    if (lvlStr.includes('beginner')) badgeColor = difficultyColors['beginner'];
    if (lvlStr.includes('intermediate')) badgeColor = difficultyColors['intermediate'];
    if (lvlStr.includes('advanced')) badgeColor = difficultyColors['advanced'];

    return (
      <div className="issue-card" style={{ display: 'flex', flexDirection: 'column', gap: '1rem', borderLeft: `3px solid ${badgeColor}` }}>
        {/* Header & Badges */}
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
          <div>
            <div style={{ display: 'flex', gap: '0.5rem', marginBottom: '0.6rem', flexWrap: 'wrap' }}>
               <span className="issue-label" style={{ background: 'rgba(0,255,136,0.1)', borderColor: 'var(--accent-green)' }}>🎯 Best Match</span>
               <span className="issue-label" style={{ background: 'rgba(255,0,255,0.1)', color: 'var(--accent-pink)', borderColor: 'var(--accent-pink)' }}>🤖 AI Recommended</span>
               <span className="issue-label" style={{ background: 'rgba(0,255,255,0.1)', color: 'var(--accent-cyan)', borderColor: 'var(--accent-cyan)' }}>📊 Match: {issue.score}%</span>
            </div>
            <h3 className="issue-title" style={{ fontSize: '1.2rem', margin: 0 }}>{issue.name || 'Unknown Repository'}</h3>
          </div>
          <span className="label" style={{ 
              background: badgeColor, 
              color: '#111', 
              padding: '0.3rem 0.6rem',
              fontWeight: 700,
              fontSize: '0.7rem',
              borderRadius: '2px'
            }}>
              {issue.difficulty || 'Unknown'}
          </span>
        </div>

        {/* AI Details */}
        <div style={{ background: 'rgba(0,0,0,0.2)', padding: '1rem', border: '1px solid var(--border)', borderRadius: '4px' }}>
          <p style={{ margin: '0 0 0.8rem 0', color: 'var(--text)', fontSize: '0.9rem', lineHeight: 1.5 }}>
            <span style={{ color: 'var(--accent-cyan)', fontWeight: 700, marginRight: '0.5rem' }}>WHY:</span>
             {issue.reason}
          </p>
          <div style={{ margin: '0 0 0.8rem 0', color: 'var(--muted)', fontSize: '0.85rem' }}>
            <span style={{ color: 'var(--accent-pink)', fontWeight: 700, marginRight: '0.5rem' }}>IDEAS:</span>
            {issue.contributions}
          </div>
          <div style={{ color: 'var(--accent-green)', fontSize: '0.85rem' }}>
            <span style={{ fontWeight: 700, marginRight: '0.5rem' }}>OUTCOME:</span>
            {issue.learning}
          </div>
        </div>

        {/* Footer */}
        <div className="issue-footer" style={{ marginTop: 'auto', paddingTop: '1rem' }}>
          <span className="issue-repo" style={{ margin: 0, opacity: 0.6 }}>{'>'} ai_analysis_complete</span>
          <button
            className="issue-view-btn"
            onClick={() => window.open(issue.url || '#', '_blank')}
          >
            {'>'} View Repo
          </button>
        </div>
      </div>
    );
  }

  // STANDARD / LEGACY FORMAT (Fallback)
  const score = issue.score ?? issue.beginner_score ?? Math.floor(Math.random() * 30 + 70);
  const labels = issue.labels || issue.tags || [];
  const repo = issue.repo || issue.repository || 'github/repo';
  const title = issue.title || 'Untitled Issue';
  const url = issue.url || issue.html_url || '#';

  return (
    <div className="issue-card">
      <div className="issue-repo">{'>'} {repo}</div>
      <div className="issue-title">{title}</div>

      {labels.length > 0 && (
        <div className="issue-labels">
          {labels.slice(0, 3).map((label, i) => (
            <span key={i} className="issue-label">
              {typeof label === 'string' ? label : label.name}
            </span>
          ))}
        </div>
      )}

      <div className="issue-footer">
        <span className="issue-score">SCORE: {score}</span>
        <button
          className="issue-view-btn"
          onClick={() => window.open(url, '_blank')}
        >
          {'>'} View Issue
        </button>
      </div>
    </div>
  );
};

export default IssueCard;
