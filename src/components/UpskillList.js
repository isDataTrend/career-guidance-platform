const UpskillList = ({ courses }) => {
  return (
    <div>
      <h2 className="text-lg font-bold mb-4">Recommended Courses</h2>
      <ul className="space-y-4">
        {courses.map((course, index) => (
          <li
            key={index}
            className="p-4 bg-gray-100 rounded shadow flex justify-between items-center"
          >
            <div>
              <h3 className="font-bold">{course.title}</h3>
              <p>{course.platform}</p>
            </div>
            <a
              href={course.link}
              target="_blank"
              rel="noreferrer"
              className="px-4 py-2 bg-green-500 text-white rounded"
            >
              View
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UpskillList;
