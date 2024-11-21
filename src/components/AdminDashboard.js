import { Bar } from "react-chartjs-2";

const AdminDashboard = ({ data }) => {
  const chartData = {
    labels: data.labels,
    datasets: [
      {
        label: "Student Activity",
        data: data.values,
        backgroundColor: "rgba(75, 192, 192, 0.6)",
      },
    ],
  };

  return (
    <div className="p-6 bg-gray-100 rounded shadow">
      <h2 className="text-lg font-bold">University Dashboard</h2>
      <Bar data={chartData} />
    </div>
  );
};

export default AdminDashboard;
