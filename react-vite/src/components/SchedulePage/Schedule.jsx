import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';
import { useEffect, useState } from 'react';
import ScheduleForm from '../ScheduleForm';

export default function SchedulePage() {
  const sessionUser = useSelector(state => state.session.user);
  const [scheduleList, setScheduleList] = useState([]);
  const [editingSchedule, setEditingSchedule] = useState(null);
  
  useEffect(() => {
    // Fetch schedule list when component loads
    async function fetchSchedules() {
      const response = await fetch('/api/schedules/my');
      const data = await response.json();
      setScheduleList(data.schedules);
    }
    fetchSchedules();
  }, []);

  const handleEdit = (schedule) => {
    setEditingSchedule(schedule);
  };

  const handleDelete = async (scheduleId) => {
    const response = await fetch(`/api/schedules/${scheduleId}`, {
      method: 'DELETE',
    });

    if (response.ok) {
      setScheduleList(scheduleList.filter(schedule => schedule.id !== scheduleId));
    } else {
      console.error('Failed to delete schedule.');
    }
  };

  const handleSuccess = (newSchedule) => {
    setEditingSchedule(null);
    setScheduleList((prev) =>
      prev.map((schedule) => (schedule.id === newSchedule.id ? newSchedule : schedule))
    );
  };

  if (!sessionUser) {
    // Guest View
    return (
      <div>
        <h1>Schedule a Free Class</h1>
        <button>One Day Free Pass</button>
        <p>
          <NavLink to="/signup">Sign up</NavLink> to view the full schedule and book your class!
        </p>
      </div>
    );
  }

  return (
    <div>
      <h1>Your Class Schedule</h1>
      <ul>
        {scheduleList.map((schedule) => (
          <li key={schedule.id}>
            {schedule.describe} - {schedule.date} {schedule.startTime} to {schedule.endTime}
            {new Date(`${schedule.date}T${schedule.startTime}:00`) > new Date(Date.now() + 24 * 60 * 60 * 1000) && (
              <>
                <button onClick={() => handleEdit(schedule)}>Edit</button>
                <button onClick={() => handleDelete(schedule.id)}>Cancel</button>
              </>
            )}
          </li>
        ))}
      </ul>
      <ScheduleForm scheduleToEdit={editingSchedule} onSuccess={handleSuccess} />
    </div>
  );
}
