import React, { useEffect, useState } from "react";
import api from "../services/api";

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchNotifications = async () => {
      try {
        const response = await api.get("notifications/");
        setNotifications(response.data);
      } catch (err) {
        setError("Failed to fetch notifications.");
      }
    };
    fetchNotifications();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Your Notifications</h2>
      {error && <p className="text-red-500">{error}</p>}
      <ul>
        {notifications.map((notification) => (
          <li key={notification.id} className="p-4 bg-gray-100 rounded shadow-md my-2">
            <p>{notification.message}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
