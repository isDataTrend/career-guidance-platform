import axios from "axios";

export const fetchCourseraCourses = async () => {
  try {
    const response = await axios.get(
      "https://api.coursera.org/api/courses.v1", // Example Coursera API endpoint
      {
        headers: {
          Authorization: `Bearer qoEKz6H7rVLekYM9A6OdQo914bvYJXZE5FUX6sn047ssYjCs`,
        },
        params: {
          fields: "id,name,description,photoUrl", // Add fields based on what you need
        },
      }
    );

    return response.data.elements.map((course) => ({
      id: course.id,
      name: course.name,
      description: course.description,
      photoUrl: course.photoUrl,
    }));
  } catch (error) {
    console.error("Error fetching Coursera courses:", error);
    return [];
  }
};
