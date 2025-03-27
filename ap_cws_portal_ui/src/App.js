import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Spaces from "./pages/Spaces";
import Analytics from "./pages/Analytics";
import Notifications from "./pages/Notifications";
import Navbar from "./components/Navbar";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(
    !!localStorage.getItem("access_token")
  );

  // Check auth status on initial load and storage changes
  useEffect(() => {
    const checkAuth = () => {
      setIsAuthenticated(!!localStorage.getItem("access_token"));
    };

    checkAuth();
    window.addEventListener('storage', checkAuth);
    return () => window.removeEventListener('storage', checkAuth);
  }, []);

  return (
    <Router>
      {isAuthenticated && <Navbar />}
      <Routes>
        <Route path="/" element={
          <Navigate replace to={isAuthenticated ? "/dashboard" : "/login"} />
        } />
        <Route path="/login" element={
          isAuthenticated ? <Navigate replace to="/dashboard" /> : <Login />
        } />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={
          isAuthenticated ? <Dashboard /> : <Navigate replace to="/login" />
        } />
        <Route path="/spaces" element={
          isAuthenticated ? <Spaces /> : <Navigate replace to="/login" />
        } />
        <Route path="/analytics" element={
          isAuthenticated ? <Analytics /> : <Navigate replace to="/login" />
        } />
        <Route path="/notifications" element={
          isAuthenticated ? <Notifications /> : <Navigate replace to="/login" />
        } />
        <Route path="*" element={<h2 className="text-center text-red-500">404 Page Not Found</h2>} />
      </Routes>
    </Router>
  );
}

export default App;