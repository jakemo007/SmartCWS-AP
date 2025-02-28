import React, { useEffect, useState } from "react";
import api from "../services/api";

const Bookings = () => {
  const [bookings, setBookings] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchBookings = async () => {
      try {
        const response = await api.get("spaces/bookings/");
        setBookings(response.data);
      } catch (err) {
        setError("Failed to fetch bookings.");
      }
    };
    fetchBookings();
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Your Bookings</h2>
      {error && <p className="text-red-500">{error}</p>}
      <ul>
        {bookings.map((booking) => (
          <li key={booking.id} className="p-4 bg-gray-100 rounded shadow-md my-2">
            <h3 className="text-xl font-semibold">{booking.space_name}</h3>
            <p>Date: {booking.date}</p>
            <p>Seats Booked: {booking.seat_count}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Bookings;
