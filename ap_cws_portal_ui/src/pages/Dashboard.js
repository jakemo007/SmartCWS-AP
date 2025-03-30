import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../services/api";

const Dashboard = () => {
  const [user, setUser] = useState(null);
  const [analytics, setAnalytics] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    const storedUser = localStorage.getItem("user");

    if (!token || !storedUser) {
      navigate("/login");
      return;
    }

    setUser(JSON.parse(storedUser));

    const fetchData = async () => {
      try {
        const response = await api.get("analytics/government-dashboard/");
        setAnalytics(response.data);
      } catch (err) {
        console.error("Error fetching analytics:", err);
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
      <div className="flex items-center justify-center min-h-screen bg-gray-50">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header Section */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-800">Dashboard Overview</h1>
          {user && (
            <p className="text-lg text-gray-600 mt-2">
              Welcome back, <span className="font-semibold text-blue-600">{user.username}!</span>
            </p>
          )}
        </div>

        {/* Stats Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
          {/* Workspace Analytics Card */}
          <div className="bg-white rounded-xl shadow-md overflow-hidden border border-gray-200">
            <div className="bg-blue-600 px-4 py-3">
              <h2 className="text-lg font-semibold text-white">Workspace Analytics</h2>
            </div>
            <div className="p-6">
              <div className="space-y-4 text-gray-700">
                <div className="flex justify-between">
                  <span>Total Spaces:</span>
                  <span className="font-medium">{analytics?.total_spaces || 0}</span>
                </div>
                <div className="flex justify-between">
                  <span>Total Seats:</span>
                  <span className="font-medium">{analytics?.total_seats || 0}</span>
                </div>
                <div className="flex justify-between">
                  <span>Occupied Seats:</span>
                  <span className="font-medium">{analytics?.occupied_seats || 0}</span>
                </div>
                <div className="flex justify-between">
                  <span>Utilization:</span>
                  <span className="font-medium">
                    {analytics?.utilization_rate ? `${analytics.utilization_rate}%` : '0%'}
                  </span>
                </div>
              </div>
            </div>
          </div>

          {/* Quick Stats Card */}
          <div className="bg-white rounded-xl shadow-md overflow-hidden border border-gray-200">
            <div className="bg-green-600 px-4 py-3">
              <h2 className="text-lg font-semibold text-white">Quick Stats</h2>
            </div>
            <div className="p-6">
              <div className="space-y-4 text-gray-700">
                <div className="flex justify-between">
                  <span>Active Users:</span>
                  <span className="font-medium">{analytics?.active_users || 'N/A'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Available Spaces:</span>
                  <span className="font-medium">{analytics?.available_spaces || 'N/A'}</span>
                </div>
                <div className="flex justify-between">
                  <span>Bookings Today:</span>
                  <span className="font-medium">{analytics?.today_bookings || 'N/A'}</span>
                </div>
              </div>
            </div>
          </div>

          {/* Utilization Card */}
          <div className="bg-white rounded-xl shadow-md overflow-hidden border border-gray-200">
            <div className="bg-purple-600 px-4 py-3">
              <h2 className="text-lg font-semibold text-white">Utilization</h2>
            </div>
            <div className="p-6">
              <div className="h-40 flex items-center justify-center">
                <div className="relative w-32 h-32">
                  <svg className="w-full h-full" viewBox="0 0 36 36">
                    <path
                      d="M18 2.0845
                        a 15.9155 15.9155 0 0 1 0 31.831
                        a 15.9155 15.9155 0 0 1 0 -31.831"
                      fill="none"
                      stroke="#e6e6e6"
                      strokeWidth="3"
                    />
                    <path
                      d="M18 2.0845
                        a 15.9155 15.9155 0 0 1 0 31.831
                        a 15.9155 15.9155 0 0 1 0 -31.831"
                      fill="none"
                      stroke="#4f46e5"
                      strokeWidth="3"
                      strokeDasharray={`${analytics?.utilization_rate || 0}, 100`}
                    />
                  </svg>
                  <div className="absolute inset-0 flex items-center justify-center">
                    <span className="text-2xl font-bold text-gray-800">
                      {analytics?.utilization_rate || 0}%
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Recent Activity Section */}
        <div className="bg-white rounded-xl shadow-md overflow-hidden border border-gray-200">
          <div className="bg-orange-600 px-4 py-3">
            <h2 className="text-lg font-semibold text-white">Recent Activity</h2>
          </div>
          <div className="p-6">
            <div className="text-center py-8 text-gray-500">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="h-12 w-12 mx-auto text-gray-400"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  strokeWidth={2}
                  d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                />
              </svg>
              <p className="mt-4">No recent activity</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;