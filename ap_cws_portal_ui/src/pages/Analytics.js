import { useState, useEffect } from 'react';
import api from '../services/api';
import { BarChart, PieChart } from '../components/Charts';

export default function Analytics() {
  const [data, setData] = useState(null);
  const [timeRange, setTimeRange] = useState('week');

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get(`analytics/?range=${timeRange}`);
        setData(response.data);
      } catch (err) {
        console.error("Error fetching analytics:", err);
      }
    };
    fetchData();
  }, [timeRange]);

  return (
    <div className="p-6 space-y-6">
      <div className="flex justify-between items-center">
        <h1 className="text-2xl font-bold">Analytics Dashboard</h1>
        <select 
          value={timeRange}
          onChange={(e) => setTimeRange(e.target.value)}
          className="border rounded-md px-3 py-1 text-sm"
        >
          <option value="week">Last Week</option>
          <option value="month">Last Month</option>
          <option value="quarter">Last Quarter</option>
        </select>
      </div>

      {data ? (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div className="bg-white p-4 rounded-lg shadow">
            <h2 className="font-semibold mb-3">Space Utilization</h2>
            <BarChart data={data.occupancy} />
          </div>
          <div className="bg-white p-4 rounded-lg shadow">
            <h2 className="font-semibold mb-3">District Distribution</h2>
            <PieChart data={data.districts} />
          </div>
        </div>
      ) : (
        <div className="flex justify-center items-center h-64">
          <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-indigo-500"></div>
        </div>
      )}
    </div>
  );
}