// src/components/Topbar/Topbar.js
import { useAuth } from "../contexts/AuthContext";

const Topbar = () => {
  const { user, logout } = useAuth();

  return (
    <header className="bg-white shadow-sm">
      <div className="flex justify-between items-center p-4">
        <h2 className="text-lg font-semibold">Dashboard</h2>
        <div className="flex items-center space-x-4">
          <span className="text-sm">{user?.username}</span>
          <button
            onClick={logout}
            className="px-3 py-1 bg-red-50 text-red-600 rounded-md text-sm hover:bg-red-100"
          >
            Logout
          </button>
        </div>
      </div>
    </header>
  );
};

export default Topbar;