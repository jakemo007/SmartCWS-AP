import React, { useEffect, useState } from "react";
import api from "../services/api";

const Verification = () => {
  const [verifications, setVerifications] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchVerifications = async () => {
      try {
        const response = await api.get("verification/verifications/");
        setVerifications(response.data);
      } catch (err) {
        setError("Failed to fetch verification data. Please login again.");
      }
    };
    fetchVerifications();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Verification Requests</h2>
      {error && <p className="text-red-500">{error}</p>}
      <ul>
        {verifications.map((item) => (
          <li key={item.id} className="p-4 bg-gray-100 rounded shadow-md my-2">
            <h3 className="text-xl font-semibold">Space: {item.space}</h3>
            <p>Status: {item.verification_status}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Verification;
