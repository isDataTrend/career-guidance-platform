const JobCards = ({ jobs }) => {
  return (
    <div>
      <h2 className="text-lg font-bold mb-4">Job Opportunities</h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
        {jobs.map((job, index) => (
          <div
            key={index}
            className="p-4 bg-white shadow rounded hover:bg-gray-100"
          >
            <h3 className="font-bold">{job.title}</h3>
            <p>{job.company}</p>
            <button className="mt-2 px-4 py-2 bg-blue-600 text-white rounded">
              Apply
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default JobCards;
