import React, { useEffect, useState } from "react";
import api from "../services/api";

const Spaces = () => {
  const [spaces, setSpaces] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchSpaces = async () => {
      try {
        const response = await api.get("spaces/space-providers/");
        setSpaces(response.data);
      } catch (err) {
        setError("Failed to fetch spaces. Please login again.");
      }
    };
    fetchSpaces();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Available Co-Working Spaces</h2>
      {error && <p className="text-red-500">{error}</p>}
      <ul>
        {spaces.map((space) => (
          <li key={space.id} className="p-4 bg-gray-100 rounded shadow-md my-2">
            <h3 className="text-xl font-semibold">{space.company_name}</h3>
            <p>{space.address}</p>
            <p><strong>Seats Available:</strong> {space.available_seats}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Spaces;
