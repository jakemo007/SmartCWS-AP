import React from "react";
import { NavLink, useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.clear();
    window.dispatchEvent(new Event('storage'));
    navigate("/login");
  };

  return (
    <nav className="fixed top-0 w-full bg-gradient-to-r from-blue-600 to-blue-800 shadow-lg z-10">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <h1 className="text-white font-bold text-xl">Smart CWS</h1>
            </div>
            <div className="hidden md:block ml-10">
              <div className="flex space-x-4">
                <NavLink
                  to="/home"
                  className={({ isActive }) => 
                    `px-3 py-2 rounded-md text-sm font-medium ${
                      isActive ? 'bg-blue-900 text-white' : 'text-blue-200 hover:bg-blue-700 hover:text-white'
                    }`
                  }
                >
                  Home
                </NavLink>
                <NavLink
                  to="/spaces"
                  className={({ isActive }) => 
                    `px-3 py-2 rounded-md text-sm font-medium ${
                      isActive ? 'bg-blue-900 text-white' : 'text-blue-200 hover:bg-blue-700 hover:text-white'
                    }`
                  }
                >
                  Workspaces
                </NavLink>
                <NavLink
                  to="/analytics"
                  className={({ isActive }) => 
                    `px-3 py-2 rounded-md text-sm font-medium ${
                      isActive ? 'bg-blue-900 text-white' : 'text-blue-200 hover:bg-blue-700 hover:text-white'
                    }`
                  }
                >
                  Analytics
                </NavLink>
                <NavLink
                  to="/notifications"
                  className={({ isActive }) => 
                    `px-3 py-2 rounded-md text-sm font-medium ${
                      isActive ? 'bg-blue-900 text-white' : 'text-blue-200 hover:bg-blue-700 hover:text-white'
                    }`
                  }
                >
                  Notifications
                </NavLink>
              </div>
            </div>
          </div>
          <button
            onClick={handleLogout}
            className="bg-red-500 hover:bg-red-600 px-4 py-2 rounded-md text-sm font-medium text-white"
          >
            Logout
          </button>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;