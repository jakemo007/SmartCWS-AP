// src/Routes.js
import React, { Suspense, lazy } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider } from './contexts/AuthContext';
import { LoadingSpinner } from './components/LoadingSpinner';

// Lazy-loaded components
const Login = lazy(() => import('./pages/Login'));
const Register = lazy(() => import('./pages/Register'));
const DashboardLayout = lazy(() => import('./layouts/DashboardLayout'));
const Home = lazy(() => import('./pages/Home'));
const Spaces = lazy(() => import('./pages/Spaces'));
const Analytics = lazy(() => import('./pages/Analytics'));
const Notifications = lazy(() => import('./pages/Notifications'));
const Bookings = lazy(() => import('./pages/Bookings'));
const Verification = lazy(() => import('./pages/Verification'));
const Page404 = lazy(() => import('./pages/Page404'));

const AppRoutes = () => {
  return (
    <Router>
      <AuthProvider>
        <Suspense fallback={<LoadingSpinner fullScreen />}>
          <Routes>
            {/* Public Routes */}
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />

            {/* Protected Routes */}
            <Route element={<PrivateRouteWrapper />}>
              <Route element={<DashboardLayout />}>
                <Route index element={<Navigate to="/home" replace />} />
                <Route path="/home" element={<Home />} />
                <Route path="/spaces" element={<Spaces />} />
                <Route path="/bookings" element={<Bookings />} />
                <Route path="/analytics" element={<Analytics />} />
                <Route path="/notifications" element={<Notifications />} />
                <Route path="/verification" element={<Verification />} />
              </Route>
            </Route>

            {/* Error Routes */}
            <Route path="/404" element={<Page404 />} />
            <Route path="*" element={<Navigate to="/404" replace />} />
          </Routes>
        </Suspense>
      </AuthProvider>
    </Router>
  );
};

// Private Route Wrapper Component
const PrivateRouteWrapper = () => {
  const { isAuthenticated } = useAuth(); // Your authentication context hook

  return isAuthenticated ? (
    <Outlet />
  ) : (
    <Navigate to="/login" replace state={{ from: location.pathname }} />
  );
};

export default AppRoutes;