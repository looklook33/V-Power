import { useSelector } from 'react-redux';
import { NavLink,useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import './SchedulePage.css'

export default function SchedulePage() {
  const sessionUser = useSelector((state) => state.session.user);
  const [scheduleList, setScheduleList] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    async function fetchSchedules() {
      const response = await fetch('/api/schedules');
      const data = await response.json();
      setScheduleList(data.schedules);
    }
    fetchSchedules();
  }, []);

  // Check if the schedule has passed
  const hasSchedulePassed = (schedule) => {
    const now = new Date();
    const scheduleEndDate = new Date(`${schedule.date}T${schedule.endTime}`);
    return now > scheduleEndDate;
  };

  // Check if the schedule is within the next 24 hours
  const isScheduleWithinNext24Hours = (schedule) => {
    const now = new Date();
    const scheduleStartDate = new Date(`${schedule.date}T${schedule.startTime}`);
    const timeDifference = scheduleStartDate - now; // Difference in milliseconds
    const hoursDifference = timeDifference / (1000 * 60 * 60); // Convert to hours
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
            {hasSchedulePassed(schedule) && (
              <span className="good-workout-sign">GOOD WorkOut!</span>
            )}
            {cannotEditOrCancel(schedule) ? (
              <span className="no-edit-cancel">No Cancel (within 24 hours or passed.)</span>
            ) : (
              <div>
                <button onClick={() => handleCancel(schedule.id)}>Cancel</button>
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

function handleCancel(scheduleId) {
  const confirmation = window.confirm('Are you sure you want to cancel this schedule?');
  if (confirmation) {
    fetch(`/api/schedules/${scheduleId}`, {
      method: 'DELETE',
    })
    .then(response => {
      if (response.ok) {
        alert('Schedule canceled successfully.');
        window.location.reload(); // Reload page after canceling
      } else {
        alert('Failed to cancel schedule.');
      }
    });
  }
}
