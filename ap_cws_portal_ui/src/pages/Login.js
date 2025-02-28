import React, { useState } from "react";
import api from "../services/api";

const Login = () => {
  const [credentials, setCredentials] = useState({ username: "", password: "" });
  const [error, setError] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await api.post("accounts/token/", credentials);
      localStorage.setItem("access_token", response.data.access);
      localStorage.setItem("refresh_token", response.data.refresh);
      console.log(response.data);
      alert("Login successful!");
    } catch (err) {
      setError("Login failed! Check username and password.");
    }
  };

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold">Login</h2>
      {error && <p className="text-red-500">{error}</p>}
      <form onSubmit={handleLogin}>
        <input
          type="text"
          placeholder="Username"
          className="border p-2 m-2"
          onChange={(e) => setCredentials({ ...credentials, username: e.target.value })}
        />
        <input
          type="password"
          placeholder="Password"
          className="border p-2 m-2"
          onChange={(e) => setCredentials({ ...credentials, password: e.target.value })}
        />
        <button type="submit" className="bg-blue-600 text-white p-2">Login</button>
      </form>
    </div>
  );
};

export default Login;
