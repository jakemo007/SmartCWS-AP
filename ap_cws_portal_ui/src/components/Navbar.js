import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-primary p-3">
      <div className="container">
        <Link className="navbar-brand" to="/">Co-Working Space Portal</Link>
        <div className="navbar-nav">
          <Link className="nav-link" to="/">Home</Link>
          <Link className="nav-link" to="/spaces">Spaces</Link>
          <Link className="nav-link" to="/bookings">Bookings</Link>
          <Link className="nav-link" to="/analytics">Analytics</Link>
          <Link className="nav-link" to="/notifications">Notifications</Link>
          <Link className="nav-link" to="/verification">Verification</Link>
          <Link className="nav-link" to="/login">Login</Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
