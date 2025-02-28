import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";

const Dashboard = () => {
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("access_token");
    if (!token) {
      navigate("/login"); // ✅ Redirect to login if not authenticated
    }
  }, [navigate]);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Dashboard</h2>
      <p>Welcome to Smart CWS!</p>
    </div>
  );
};

export default Dashboard;
