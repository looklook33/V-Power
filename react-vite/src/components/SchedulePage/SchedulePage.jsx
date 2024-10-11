import { useSelector } from 'react-redux';
import { NavLink, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import './SchedulePage.css';

export default function SchedulePage() {
  const sessionUser = useSelector((state) => state.session.user);
  const [scheduleList, setScheduleList] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchSchedules = async () => {
      const response = await fetch('/api/schedules');
      const data = await response.json();
      const sortedSchedules = data.schedules.sort((a, b) => new Date(a.date) - new Date(b.date));
      setScheduleList(sortedSchedules);
    };
    fetchSchedules();
  }, []);

  const hasSchedulePassed = (schedule) => {
    const now = new Date();
    const scheduleEndDate = new Date(`${schedule.date}T${schedule.endTime}`);
    return now > scheduleEndDate;
  };


  const isScheduleWithinNext24Hours = (schedule) => {
    const now = new Date();
    const scheduleStartDate = new Date(`${schedule.date}T${schedule.startTime}`);
    const hoursDifference = (scheduleStartDate - now) / (1000 * 60 * 60);
    return hoursDifference > 0 && hoursDifference <= 24;
  };

  const cannotEditOrCancel = (schedule) => {
    return hasSchedulePassed(schedule) || isScheduleWithinNext24Hours(schedule);
  };

  if (!sessionUser) {
    return (
      <div>
        <button onClick={() => navigate('/signup')}>Please Sign up for a Free Class</button>
      </div>
    );
  }

  return (
    <div className="schedule-container">
      <h1>Your Class Schedule</h1>
      <ul className="schedule-list">
        {scheduleList.map((schedule) => (
          <li key={schedule.id}>
            <NavLink to={`/schedule/${schedule.id}`}>
              {schedule.describe} - {schedule.date} from {schedule.startTime} to {schedule.endTime}
            </NavLink>
            {hasSchedulePassed(schedule) ? (
              <span className="good-workout-sign">GOOD WorkOut!</span>
            ) : cannotEditOrCancel(schedule) ? (
              <span className="no-edit-cancel">No Cancel or Edit within 24 hours.</span>
            ) : (
              <div>
              </div>
            )}
          </li>
        ))}
      </ul>

      <NavLink to="/schedule/new">
        <button>Create a New Schedule</button>
      </NavLink>
    </div>
  );
}
