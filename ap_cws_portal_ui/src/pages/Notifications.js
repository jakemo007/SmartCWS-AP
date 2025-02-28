import React, { useEffect, useState } from "react";
import api from "../services/api";

const Notifications = () => {
  const [notifications, setNotifications] = useState([]);

  useEffect(() => {
    api.get("notifications/")
      .then(response => setNotifications(response.data))
      .catch(error => console.error("Error fetching notifications:", error));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Your Notifications</h2>
      <ul>
        {notifications.map(notification => (
          <li key={notification.id} className="p-4 bg-gray-100 rounded shadow-md my-2">
            <p>{notification.message}</p>
            <p className="text-sm text-gray-500">Received at: {new Date(notification.created_at).toLocaleString()}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Notifications;
