import React, { useState } from "react";
import CareerCards from "../components/CareerCards";

const Recommendations = () => {
  const [careers, setCareers] = useState([]);

  const handleUpload = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    // Mock API call
    const response = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setCareers(data.careers); // Example: [{ name: "Software Engineer", description: "Strong in coding" }]
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Career Recommendations</h1>
      <div>
        <input
          type="file"
          onChange={(e) => handleUpload(e.target.files[0])}
          className="block mb-4"
        />
      </div>
      {careers.length > 0 ? (
        <CareerCards careers={careers} />
      ) : (
        <p>Upload your transcript to see recommendations.</p>
      )}
    </div>
  );
};

export default Recommendations;
