import { useState, useEffect } from 'react';
import api from '../services/api';
import  SpaceCard from '../components/SpaceCard';
import SearchFilters from '../components/SearchFilter';

export default function Spaces() {
  const [spaces, setSpaces] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filters, setFilters] = useState({
    district: '',
    capacity: ''
  });

  useEffect(() => {
    const fetchSpaces = async () => {
      try {
        const params = new URLSearchParams();
        if (filters.district) params.append('district', filters.district);
        if (filters.capacity) params.append('capacity', filters.capacity);
        
        const response = await api.get(`spaces/?${params.toString()}`);
        setSpaces(response.data);
      } catch (err) {
        console.error("Error fetching spaces:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchSpaces();
  }, [filters]);

  return (
    <div className="p-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Available Spaces</h1>
        <SearchFilters onFilter={setFilters} />
      </div>

      {loading ? (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {[...Array(3)].map((_, i) => (
            <div key={i} className="bg-gray-100 rounded-lg h-48 animate-pulse"></div>
          ))}
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
          {spaces.map(space => (
            <SpaceCard key={space.id} space={space} />
          ))}
        </div>
      )}
    </div>
  );
}