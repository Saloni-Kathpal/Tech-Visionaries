import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

// Extract GitHub username from a URL or raw username input
const extractGithubUsername = (input) => {
  const trimmed = input.trim();
  // Handles: https://github.com/username, github.com/username, or plain "username"
  const match = trimmed.match(/(?:https?:\/\/)?(?:www\.)?github\.com\/([a-zA-Z0-9_-]+)/i);
  return match ? match[1] : trimmed;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(() => localStorage.getItem('mock_user') || '');
  const [avatar, setAvatar] = useState(() => localStorage.getItem('mock_avatar') || '');
  const [loading, setLoading] = useState(false);
  const [loginError, setLoginError] = useState('');

  useEffect(() => {
    if (user) {
      localStorage.setItem('mock_user', user);
      localStorage.setItem('mock_avatar', avatar);
    } else {
      localStorage.removeItem('mock_user');
      localStorage.removeItem('mock_avatar');
    }
  }, [user, avatar]);

  // Login by fetching GitHub public profile
  const loginWithGithub = async (input) => {
    if (!input || !input.trim()) return;
    setLoading(true);
    setLoginError('');

    const username = extractGithubUsername(input);

    try {
      const res = await fetch(`https://api.github.com/users/${username}`);
      if (!res.ok) {
        setLoginError(`GitHub user "${username}" not found. Check the URL and try again.`);
        setLoading(false);
        return false;
      }
      const data = await res.json();
      setUser(data.login);           // Use the exact GitHub login (lowercase)
      setAvatar(data.avatar_url);
      setLoading(false);
      return true;
    } catch (err) {
      setLoginError('Could not reach GitHub API. Check your connection.');
      setLoading(false);
      return false;
    }
  };

  const logout = () => {
    setUser('');
    setAvatar('');
    setLoginError('');
  };

  // Legacy plain login kept for compatibility
  const login = (username) => {
    if (username && username.trim()) setUser(username.trim());
  };

  return (
    <AuthContext.Provider value={{ user, avatar, loading, loginError, loginWithGithub, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
