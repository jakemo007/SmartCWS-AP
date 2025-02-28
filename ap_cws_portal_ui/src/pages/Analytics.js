import React, { useEffect, useState } from "react";
import api from "../services/api";

const Analytics = () => {
  const [analytics, setAnalytics] = useState([]);

  useEffect(() => {
    api.get("analytics/reports/")
      .then(response => setAnalytics(response.data))
      .catch(error => console.error("Error fetching analytics:", error));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Analytics Dashboard</h2>
      <ul>
        {analytics.map(report => (
          <li key={report.id} className="p-4 bg-gray-100 rounded shadow-md my-2">
            <h3 className="text-xl font-semibold">{report.report_name}</h3>
            <p>Total Bookings: {report.total_bookings}</p>
            <p>Available Spaces: {report.available_spaces}</p>
            <p>Occupied Seats: {report.occupied_seats}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Analytics;
