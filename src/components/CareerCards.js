const CareerCards = ({ careers }) => {
  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
      {careers.map((career, index) => (
        <div
          key={index}
          className="p-4 bg-white shadow rounded hover:bg-blue-100 transition"
        >
          <h3 className="text-lg font-bold">{career.name}</h3>
          <p>{career.description}</p>
          <button className="mt-2 px-4 py-2 bg-blue-600 text-white rounded">
            Explore Career
          </button>
        </div>
      ))}
    </div>
  );
};

export default CareerCards;
