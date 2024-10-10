import { NavLink } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  return (
    <ul className="navigation_container">
      <li>
        <NavLink to="/">Home</NavLink>
        <NavLink to='/trainers'>Trainers</NavLink>
        <NavLink to="/equipment">Equipment</NavLink>
        <NavLink to="/galleries">Workout Gallery</NavLink>
        <NavLink to="/schedule">Schedule</NavLink>
        <NavLink to="/signup">Contact Us</NavLink>
      </li>

      <li>
        <ProfileButton />
      </li>
    </ul>
  );
}

export default Navigation;
