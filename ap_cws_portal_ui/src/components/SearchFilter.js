export default function SearchFilters({ onFilter }) {
    const [filters, setFilters] = useState({
      district: '',
      capacity: ''
    });
  
    const handleChange = (e) => {
      const { name, value } = e.target;
      setFilters(prev => ({ ...prev, [name]: value }));
    };
  
    const handleSubmit = (e) => {
      e.preventDefault();
      onFilter(filters);
    };
  
    return (
      <form onSubmit={handleSubmit} className="flex space-x-2">
        <select
          name="district"
          value={filters.district}
          onChange={handleChange}
          className="border rounded-md px-3 py-1 text-sm"
        >
          <option value="">All Districts</option>
          <option value="Visakhapatnam">Visakhapatnam</option>
          <option value="Vijayawada">Vijayawada</option>
        </select>
        
        <select
          name="capacity"
          value={filters.capacity}
          onChange={handleChange}
          className="border rounded-md px-3 py-1 text-sm"
        >
          <option value="">Any Capacity</option>
          <option value="10">10+ Seats</option>
          <option value="20">20+ Seats</option>
        </select>
        
        <button 
          type="submit"
          className="bg-indigo-600 text-white px-3 py-1 rounded-md text-sm"
        >
          Filter
        </button>
      </form>
    );
  }