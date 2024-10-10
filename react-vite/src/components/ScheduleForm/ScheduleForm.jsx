import { useState, useEffect } from "react";
import { useSelector } from "react-redux";
import { useNavigate, useLocation } from "react-router-dom";
import './ScheduleForm.css'

export default function ScheduleForm() {
  const navigate = useNavigate();
  const location = useLocation();
  const schedule = location.state?.schedule || null;

  const [trainers, setTrainers] = useState([]);
  const [members, setMembers] = useState([]);
  const [selectedTrainer, setSelectedTrainer] = useState(schedule?.users.find(user => user.roles.some(role => role.isTrainer))?.id || "");
  const [selectedMember, setSelectedMember] = useState(schedule?.users.find(user => user.roles.some(role => role.isMember && !role.isTrainer))?.id || "");
  const [date, setDate] = useState(schedule?.date || "");
  const [description, setDescription] = useState(schedule?.describe || "");
  const [startTime, setStartTime] = useState(schedule?.startTime || "");
  const [endTime, setEndTime] = useState(schedule?.endTime || "");
  const [errors, setErrors] = useState({});
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    // Fetch trainers and members from the backend
    fetch("/api/trainers")
      .then((res) => res.json())
      .then((data) => setTrainers(data.trainers || []));

    fetch("/api/members")
      .then((res) => res.json())
      .then((data) => setMembers(data.members || []));
  }, []);

  const validateForm = () => {
    const newErrors = {};

    if (user.roles.some((role) => role.isMember) && !selectedTrainer) {
      newErrors.trainer = "Please select a trainer.";
    }
    if (user.roles.some((role) => role.isTrainer) && !selectedMember) {
      newErrors.member = "Please select a member.";
    }
    if (!description.trim()) {
      newErrors.description = "Please provide a description.";
    }
    if (!date) {
      newErrors.date = "Date is required.";
    }
    if (!startTime) {
      newErrors.startTime = "Start time is required.";
    }
    if (!endTime) {
      newErrors.endTime = "End time is required.";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    const scheduleData = {
      describe: description,
      date,
      startTime,
      endTime,
      member_id: selectedMember || user.id,
      trainer_id: selectedTrainer || user.id,
    };

    const method = schedule ? 'PUT' : 'POST';
    const endpoint = schedule ? `/api/schedules/${schedule.id}` : '/api/schedules';

    const response = await fetch(endpoint, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(scheduleData),
    });

    if (response.ok) {
      navigate('/schedule');
    } else {
      alert('Failed to submit schedule');
    }
  };

  return (
    <div className="schedule-form-container">
      <h1 className="schedule-form-title">{schedule ? "Edit Schedule" : "Create Schedule"}</h1>
      <form onSubmit={handleSubmit} className="schedule-form">
        {user.roles.some((role) => role.isMember || role.isManager) && (
          <>
            <label htmlFor="trainer">Select Trainer:</label>
            <select
              id="trainer"
              value={selectedTrainer}
              onChange={(e) => setSelectedTrainer(e.target.value)}
              className="schedule-form-select"
            >
              <option value="">-- Select a Trainer --</option>
              {trainers.map((trainer) => (
                <option key={trainer.id} value={trainer.id}>
                  {trainer.username}
                </option>
              ))}
            </select>
            {errors.trainer && <p className="error">{errors.trainer}</p>}
          </>
        )}

        {user.roles.some((role) => role.isTrainer || role.isManager) && (
          <>
            <label htmlFor="member">Select Member:</label>
            <select
              id="member"
              value={selectedMember}
              onChange={(e) => setSelectedMember(e.target.value)}
              className="schedule-form-select"
            >
              <option value="">-- Select a Member --</option>
              {members.map((member) => (
                <option key={member.id} value={member.id}>
                  {member.username}
                </option>
              ))}
            </select>
            {errors.member && <p className="error">{errors.member}</p>}
          </>
        )}

        <label htmlFor="description">Description:</label>
        <input
          id="description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="schedule-form-input"
        />
        {errors.description && <p className="error">{errors.description}</p>}

        <label htmlFor="date">Date:</label>
        <input
          id="date"
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
          className="schedule-form-input"
        />
        {errors.date && <p className="error">{errors.date}</p>}

        <label htmlFor="startTime">Start Time:</label>
        <input
          id="startTime"
          type="time"
          value={startTime}
          onChange={(e) => setStartTime(e.target.value)}
          className="schedule-form-input"
        />
        {errors.startTime && <p className="error">{errors.startTime}</p>}

        <label htmlFor="endTime">End Time:</label>
        <input
          id="endTime"
          type="time"
          value={endTime}
          onChange={(e) => setEndTime(e.target.value)}
          className="schedule-form-input"
        />
        {errors.endTime && <p className="error">{errors.endTime}</p>}

        <button type="submit" className="schedule-form-submit-button">
          {schedule ? "Update Schedule" : "Create Schedule"}
        </button>
      </form>
    </div>
  );
}
