import React, { useEffect, useState } from "react";
import api from "../services/api";

const Spaces = () => {
  const [spaces, setSpaces] = useState([]);

  useEffect(() => {
    api.get("spaces/")
      .then(response => setSpaces(response.data))
      .catch(error => console.error("Error fetching spaces:", error));
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Available Co-Working Spaces</h2>
      <ul>
        {spaces.map(space => (
          <li key={space.id} className="p-4 bg-gray-100 rounded shadow-md my-2">
            <h3 className="text-xl font-semibold">{space.name}</h3>
            <p>{space.address}</p>
            <p><strong>Seats Available:</strong> {space.available_seats}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Spaces;
