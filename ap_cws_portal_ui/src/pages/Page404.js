import { Link } from 'react-router-dom';

export default function Page404() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-50">
      <h1 className="text-9xl font-bold text-indigo-600">404</h1>
      <p className="text-2xl text-gray-600 mb-6">Page Not Found</p>
      <Link 
        to="/home" 
        className="px-6 py-3 bg-indigo-600 text-white rounded-md hover:bg-indigo-700 transition-colors"
      >
        Go to Home
      </Link>
    </div>
  );
}