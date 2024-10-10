import { useParams, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';
import './ScheduleDetails.css'

export default function ScheduleDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [schedule, setSchedule] = useState(null);

  useEffect(() => {
    // Fetch schedule details by ID
    async function fetchScheduleDetails() {
      const response = await fetch(`/api/schedules/${id}`);
      const data = await response.json();
      setSchedule(data.schedule);  
    }
    fetchScheduleDetails();
  }, [id]);

  const handleCancelSchedule = async () => {
    const confirmation = window.confirm("Are you sure you want to cancel this schedule? This action cannot be undone.");
    if (confirmation) {
      const response = await fetch(`/api/schedules/${id}`, {
        method: 'DELETE',
      });
      if (response.ok) {
        alert('Schedule canceled successfully.');
        navigate('/schedule');
      } else {
        alert('Failed to cancel schedule.');
      }
    }
  };

  if (!schedule) return <div>Loading...</div>;

  const trainer = schedule.users.find(user => user.roles.some(role => role.isTrainer));
  const member = schedule.users.find(user => user.roles.some(role => role.isMember && !role.isTrainer));

  return (
    <div className='schedule-details-container'>
      <h1>Schedule Details</h1>
      <p><strong>Date:</strong> {schedule.date}</p>
      <p><strong>Time:</strong> {schedule.startTime} - {schedule.endTime}</p>
      <p><strong>Description:</strong> {schedule.describe}</p>

      {trainer && (
        <div className='trainer-info'>
          <p><strong>Trainer:</strong> {trainer.username}</p>
        </div>
      )}

      {member && (
        <div className='member-info'>
          <p><strong>Member:</strong> {member.username}</p>
          {/* <p>{member.email}</p> */}
        </div>
      )}

      <button onClick={() => navigate(`/schedule/${id}/edit`, { state: { schedule } })}>
        Edit
      </button>
      <button onClick={handleCancelSchedule}>Cancel Schedule</button>
    </div>
  );
}
