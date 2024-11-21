import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-blue-600 p-4 text-white">
      <div className="container mx-auto flex justify-between items-center">
        <h1 className="text-xl font-bold">Career Guidance</h1>
        <div className="flex space-x-4">
          <Link to="/" className="hover:text-gray-200">
            Home
          </Link>
          <Link to="/recommendations" className="hover:text-gray-200">
            Recommendations
          </Link>
          <Link to="/upskilling" className="hover:text-gray-200">
            Upskilling
          </Link>
          <Link to="/jobs" className="hover:text-gray-200">
            Jobs
          </Link>
          <Link to="/admin" className="hover:text-gray-200">
            Admin
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
