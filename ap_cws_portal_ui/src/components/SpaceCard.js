export default function SpaceCard({ space }) {
    return (
      <div className="bg-white rounded-lg shadow-md overflow-hidden border border-gray-200 hover:shadow-lg transition-shadow">
        <div className="h-48 bg-gray-200 flex items-center justify-center">
          {space.image ? (
            <img src={space.image} alt={space.name} className="h-full w-full object-cover" />
          ) : (
            <span className="text-gray-500">No Image</span>
          )}
        </div>
        <div className="p-4">
          <h3 className="font-bold text-lg mb-1">{space.name}</h3>
          <p className="text-gray-600 text-sm mb-2">{space.address}</p>
          <div className="flex justify-between text-sm">
            <span>Seats: {space.available_seats}</span>
            <span className="font-medium">₹{space.price}/seat</span>
          </div>
          <button className="mt-3 w-full bg-indigo-600 text-white py-2 rounded-md hover:bg-indigo-700 transition-colors">
            View Details
          </button>
        </div>
      </div>
    );
  }