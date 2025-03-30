import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./pages/Login";
import Home from "./pages/Home";
import Spaces from "./pages/Spaces";
import Analytics from "./pages/Analytics";
import Notifications from "./pages/Notifications";
import Navbar from "./components/Navbar";

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(
    !!localStorage.getItem("access_token")
  );

  useEffect(() => {
    const handleStorageChange = () => {
      setIsAuthenticated(!!localStorage.getItem("access_token"));
    };

    window.addEventListener('storage', handleStorageChange);
    return () => window.removeEventListener('storage', handleStorageChange);
  }, []);

  return (
    <Router>
      {isAuthenticated && <Navbar />}
      <div className={isAuthenticated ? "mt-16" : ""}> {/* Offset for fixed navbar */}
        <Routes>
          <Route path="/" element={
            isAuthenticated ? <Navigate to="/home" /> : <Navigate to="/login" />
          } />
          <Route path="/login" element={
            isAuthenticated ? <Navigate to="/home" /> : <Login />
          } />
          <Route path="/home" element={
            isAuthenticated ? <Home /> : <Navigate to="/login" />
          } />
          <Route path="/spaces" element={
            isAuthenticated ? <Spaces /> : <Navigate to="/login" />
          } />
          <Route path="/analytics" element={
            isAuthenticated ? <Analytics /> : <Navigate to="/login" />
          } />
          <Route path="/notifications" element={
            isAuthenticated ? <Notifications /> : <Navigate to="/login" />
          } />
          <Route path="*" element={<h1 className="text-center mt-10">404 Not Found</h1>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;