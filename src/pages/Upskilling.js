import React, { useEffect, useState } from "react";
import UpskillList from "../components/UpskillList";
import { fetchCourseraCourses } from "../services/courseraService";

const Upskilling = () => {
  const [courses, setCourses] = useState([]);

  useEffect(() => {
    const fetchCourses = async () => {
      const courseraCourses = await fetchCourseraCourses();
      setCourses(courseraCourses);
    };

    fetchCourses();
  }, []);

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Upskilling Opportunities</h1>
      {courses.length > 0 ? (
        <UpskillList courses={courses} />
      ) : (
        <p>Loading courses...</p>
      )}
    </div>
  );
};

export default Upskilling;
