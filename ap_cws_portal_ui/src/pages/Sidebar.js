import { NavLink } from 'react-router-dom';
import { FiHome, FiMap, FiUsers, FiSettings, FiBell } from 'react-icons/fi';

const navItems = [
  { path: '/home', icon: <FiHome />, label: 'Home' },
  { path: '/spaces', icon: <FiMap />, label: 'Spaces' },
  { path: '/analytics', icon: <FiUsers />, label: 'Analytics' },
  { path: '/notifications', icon: <FiBell />, label: 'Notifications' }
];

export default function Sidebar() {
  return (
    <div className="w-64 bg-white shadow-md">
      <div className="p-4 border-b">
        <h1 className="text-xl font-bold text-indigo-600">Smart CWS</h1>
      </div>
      <nav className="mt-4">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) => 
              `flex items-center p-3 mx-2 rounded-lg transition-colors ${
                isActive ? 'bg-indigo-50 text-indigo-600' : 'hover:bg-gray-100'
              }`
            }
          >
            <span className="mr-3">{item.icon}</span>
            {item.label}
          </NavLink>
        ))}
      </nav>
    </div>
  );
}