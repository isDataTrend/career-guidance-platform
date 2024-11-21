import React, { useState } from "react";
import { useDropzone } from "react-dropzone";

const UploadTranscript = () => {
  const [skills, setSkills] = useState([]);
  const { getRootProps, getInputProps } = useDropzone({
    onDrop: async (files) => {
      const formData = new FormData();
      formData.append("file", files[0]);
      const response = await fetch("http://localhost:5000/analyze", {
        // Mock API
        method: "POST",
        body: formData,
      });
      const data = await response.json();
      setSkills(data.skills);
    },
  });

  return (
    <div className="p-6 bg-gray-100 rounded shadow">
      <h2 className="text-lg font-bold mb-4">Upload Your Transcript</h2>
      <div
        {...getRootProps()}
        className="border-dashed border-2 p-6 rounded bg-white text-center cursor-pointer"
      >
        <input {...getInputProps()} />
        <p>Drag & drop your file here, or click to upload</p>
      </div>
      {skills.length > 0 && (
        <div className="mt-4">
          <h3 className="font-bold">Identified Skills:</h3>
          <ul>
            {skills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

export default UploadTranscript;
