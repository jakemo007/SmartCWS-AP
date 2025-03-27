import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    const token = localStorage.getItem("access_token");

    if (!token || !storedUser) {
      navigate("/login");
      return;
    }

    setUser(JSON.parse(storedUser));

    const fetchData = async () => {
      try {
        const [analyticsRes] = await Promise.all([
          api.get("analytics/government-dashboard/")
        ]);
        setAnalytics(analyticsRes.data);
      } catch (err) {
        console.error("Error fetching data:", err);
        setError("Failed to load dashboard data");
        // If token is invalid, clear storage and redirect
        if (err.response?.status === 401) {
          localStorage.clear();
          navigate("/login");
        }
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [navigate]);

  if (loading) {
    return (
      <div className="p-6 flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Dashboard Overview</h1>
      
      {user && (
        <div className="mb-6 p-4 bg-blue-50 rounded-lg">
          <p className="text-lg">
            Welcome back, <span className="font-semibold text-blue-700">{user.username}</span>!
          </p>
        </div>
      )}

      {error ? (
        <div className="p-4 bg-red-100 text-red-700 rounded-lg">
          {error}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {/* Analytics Card */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-xl font-semibold mb-4">Workspace Analytics</h3>
            {analytics ? (
              <div className="space-y-3">
                <p><span className="font-medium">Total Spaces:</span> {analytics.total_spaces}</p>
                <p><span className="font-medium">Total Seats:</span> {analytics.total_seats}</p>
                <p><span className="font-medium">Occupied Seats:</span> {analytics.occupied_seats}</p>
                <p><span className="font-medium">Utilization:</span> {analytics.utilization_rate}%</p>
              </div>
            ) : (
              <p>No analytics data available</p>
            )}
          </div>

          {/* Quick Actions */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-xl font-semibold mb-4">Quick Actions</h3>
            <div className="space-y-3">
              <button 
                onClick={() => navigate('/spaces')}
                className="w-full text-left p-2 hover:bg-gray-100 rounded"
              >
                Manage Workspaces
              </button>
              <button 
                onClick={() => navigate('/analytics')}
                className="w-full text-left p-2 hover:bg-gray-100 rounded"
              >
                View Detailed Analytics
              </button>
              <button 
                onClick={() => navigate('/notifications')}
                className="w-full text-left p-2 hover:bg-gray-100 rounded"
              >
                Check Notifications
              </button>
            </div>
          </div>

          {/* Recent Activity */}
          <div className="bg-white p-6 rounded-lg shadow">
            <h3 className="text-xl font-semibold mb-4">Recent Activity</h3>
            <p className="text-gray-500">No recent activity</p>
          </div>
        </div>
      )}
    </div>
  );
};

export default Dashboard;