import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../AuthContext';
import GithubLoginModal from './GithubLoginModal';

const Navbar = ({ onLaunch, isDashboard }) => {
  const [scrolled, setScrolled] = useState(false);
  const [showModal, setShowModal] = useState(false);
  const { user, avatar, logout } = useAuth() || {};

  useEffect(() => {
    const onScroll = () => setScrolled(window.scrollY > 30);
    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  return (
    <>
      {showModal && <GithubLoginModal onClose={() => setShowModal(false)} />}

      <nav className="navbar" style={{ boxShadow: scrolled ? '0 2px 40px rgba(0,255,136,0.06)' : 'none' }}>
        <div className="container">
          <div className="navbar-inner">
            <Link to="/" className="nav-logo">
              <span className="nav-logo-bracket">[</span>
              FirstPR Pro
              <span className="nav-logo-bracket">]</span>
            </Link>

            <ul className="nav-links">
              {!isDashboard ? (
                <>
                  <li><a href="#features">Features</a></li>
                  <li><a href="#how-it-works">How It Works</a></li>
                  <li><a href="#demo">Demo</a></li>
                  <li>
                    <button
                      className="nav-cta"
                      onClick={(e) => { e.preventDefault(); onLaunch && onLaunch(); }}
                      style={{ background: 'none', border: 'none', font: 'inherit', cursor: 'pointer' }}
                    >
                      Launch App
                    </button>
                  </li>
                </>
              ) : (
                <>
                  <li><Link to="/dashboard" style={{ textDecoration: 'none', color: 'var(--text)' }}>Scanner</Link></li>
                  <li><Link to="/marketplace" style={{ textDecoration: 'none', color: 'var(--text)' }}>Marketplace</Link></li>
                  <li><Link to="/leaderboard" style={{ textDecoration: 'none', color: 'var(--text)' }}>Leaderboard</Link></li>

                  {user ? (
                    <li style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
                      {avatar && (
                        <img
                          src={avatar}
                          alt={user}
                          style={{ width: '26px', height: '26px', borderRadius: '50%', border: '1px solid var(--accent-green)' }}
                        />
                      )}
                      <span style={{ color: 'var(--accent-green)', fontFamily: 'var(--font-mono)', fontSize: '0.85rem' }}>
                        {user}
                      </span>
                      <button
                        onClick={logout}
                        style={{ background: 'none', border: '1px solid var(--muted)', color: 'var(--muted)', cursor: 'pointer', padding: '0.15rem 0.5rem', borderRadius: '4px', fontSize: '0.75rem' }}
                      >
                        Exit
                      </button>
                    </li>
                  ) : (
                    <li>
                      <button
                        onClick={() => setShowModal(true)}
                        className="nav-cta"
                        style={{ background: 'none', border: '1px solid var(--accent-cyan)', color: 'var(--accent-cyan)', font: 'inherit', cursor: 'pointer', padding: '4px 12px' }}
                      >
                        GitHub Login
                      </button>
                    </li>
                  )}

                  <li style={{ marginLeft: '0.5rem' }}>
                    <Link to="/" className="nav-cta" style={{ textDecoration: 'none' }}>
                      &lt; Home
                    </Link>
                  </li>
                </>
              )}
            </ul>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
