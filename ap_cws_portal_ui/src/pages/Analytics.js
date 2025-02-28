import React, { useEffect, useState } from "react";
import api from "../services/api";

const Analytics = () => {
  const [analytics, setAnalytics] = useState({ total_spaces: 0, total_seats: 0, occupied_seats: 0 });
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchAnalytics = async () => {
      try {
        const response = await api.get("analytics/government-dashboard/");
        setAnalytics(response.data);
      } catch (err) {
        setError("Failed to fetch analytics data.");
      }
    };
    fetchAnalytics();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Analytics Dashboard</h2>
      {error && <p className="text-red-500">{error}</p>}
      <div className="bg-gray-100 p-4 rounded shadow-md">
        <p><strong>Total Spaces:</strong> {analytics.total_spaces}</p>
        <p><strong>Total Seats:</strong> {analytics.total_seats}</p>
        <p><strong>Occupied Seats:</strong> {analytics.occupied_seats}</p>
      </div>
    </div>
  );
};

export default Analytics;
