import React, { useEffect, useState } from "react";
import api from "../services/api";

const Verification = () => {
  const [verifications, setVerifications] = useState([]);

  useEffect(() => {
    api.get("verification/verifications/")
      .then(response => setVerifications(response.data))
      .catch(error => console.error("Error fetching verifications:", error));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Verification Requests</h2>
      <ul>
        {verifications.map(item => (
          <li key={item.id} className="p-4 bg-gray-100 rounded shadow-md my-2">
            <h3 className="text-xl font-semibold">Space: {item.space}</h3>
            <p>Status: <span className={item.verification_status === "APPROVED" ? "text-green-500" : "text-red-500"}>{item.verification_status}</span></p>
            <p>Verified By: {item.verified_by}</p>
            <p>Comments: {item.comments}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Verification;
