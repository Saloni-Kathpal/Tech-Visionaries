import React, { useState } from 'react';
import { useAuth } from '../AuthContext';

const GithubLoginModal = ({ onClose }) => {
  const { loginWithGithub, loading, loginError } = useAuth() || {};
  const [input, setInput] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const success = await loginWithGithub(input);
    if (success) onClose();
  };

  return (
    <div style={{
      position: 'fixed', inset: 0, zIndex: 9999,
      background: 'rgba(0,0,0,0.8)', backdropFilter: 'blur(4px)',
      display: 'flex', alignItems: 'center', justifyContent: 'center'
    }}>
      <div className="terminal c-cut" style={{ width: '100%', maxWidth: '460px', margin: '1rem' }}>
        <div className="terminal-bar">
          <span className="t-dot red" />
          <span className="t-dot yellow" />
          <span className="t-dot green" />
          <span className="t-title">github_auth.sh</span>
          <button
            onClick={onClose}
            style={{ marginLeft: '1rem', background: 'none', border: 'none', color: 'var(--muted)', cursor: 'pointer', fontSize: '1rem' }}
          >✕</button>
        </div>
        <div className="terminal-body" style={{ padding: '2rem' }}>
          <p style={{ color: 'var(--accent-cyan)', marginBottom: '0.5rem', fontSize: '0.85rem' }}>
            {'>'} Authenticate with GitHub
          </p>
          <p style={{ color: 'var(--muted)', fontSize: '0.8rem', marginBottom: '1.5rem' }}>
            Paste your GitHub profile URL — we'll fetch your username via the public API. No token required.
          </p>

          <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            <input
              type="text"
              className="cyber-input"
              style={{ background: 'rgba(0,0,0,0.4)', border: '1px solid var(--border)', padding: '0.75rem 1rem', borderRadius: '2px' }}
              placeholder="https://github.com/your-username"
              value={input}
              onChange={e => setInput(e.target.value)}
              autoFocus
              required
            />

            {loginError && (
              <p style={{ color: '#ff5f56', fontSize: '0.8rem', margin: 0 }}>
                {'>'} {loginError}
              </p>
            )}

            <button type="submit" className="cyber-submit" disabled={loading || !input.trim()} style={{ alignSelf: 'flex-start' }}>
              {loading ? 'Verifying...' : '> Connect GitHub'}
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default GithubLoginModal;
