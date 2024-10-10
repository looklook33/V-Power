import { useState, useEffect } from 'react';
// import { useSelector } from 'react-redux';
import { useNavigate, useParams, useLocation } from 'react-router-dom';
import './TrainerForm.css';

export default function TrainerForm() {
  const location = useLocation();
  const trainer = location.state?.trainer || null;
  
  const [email, setEmail] = useState(trainer?.email || '');
  const [username, setUsername] = useState(trainer?.username || '');
  const [description, setDescription] = useState(trainer?.roles[0]?.describe || '');
  const [url, setUrl] = useState(trainer?.roles[0]?.url || '');
  const [errors, setErrors] = useState({});
  const { id } = useParams();
  // const user = useSelector((state) => state.session.user);
  const navigate = useNavigate();

  useEffect(() => {
    if (id) {
      fetch(`/api/trainers/${id}`)
        .then((res) => res.json())
        .then((data) => {
          setUsername(data.trainer.username);
          setDescription(data.trainer.roles[0].describe);
          setEmail(data.trainer.email)
          setUrl(data.trainer.roles[0].url);
        })
        .catch((error) => console.error('Error fetching trainer:', error));
    }
  }, [id]);

  const validateForm = () => {
    const newErrors = {};
    if (!username.trim()) newErrors.username = 'Username is required.';
    if (!description.trim()) newErrors.description = 'Description is required.';
    if (!email.trim()) newErrors.email = 'Email is required.';
    if (!url.trim()) newErrors.url = 'Trainer URL is required.';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    const trainerData = {
      username,
      email,
      password:'password', 
      description,
      url, 
    };


    const method = id ? 'PUT' : 'POST';
    const endpoint = id ? `/api/trainers/${id}` : '/api/trainers';

    const res = await fetch(endpoint, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(trainerData),
    });

    if (res.ok) {
      await res.json();
      navigate('/trainers');
    } else {
      const errorData = await res.json();
      setErrors({ form: errorData.message });
    }
  };

  const handleDelete = async () => {
    if (id) {
      const confirmed = window.confirm('Are you sure you want to delete this trainer?');
      if (confirmed) {
        const res = await fetch(`/api/trainers/${id}`, { method: 'DELETE' });
        if (res.ok) {
          navigate('/trainers');
        }
      }
    }
  };

  return (
    <div>
      <h1>{id ? 'Edit Trainer' : 'Create Trainer'}</h1>
      {errors.form && <p className="error">{errors.form}</p>}
      <form onSubmit={handleSubmit} className="trainer-form">
        <label>
          Username:
          <input
            type="text"
            name="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Trainer Username"
            className="trainer-input"
          />
          {errors.username && <p className="error">{errors.username}</p>}
        </label>

        <label>
          Description:
          <textarea
            name="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Trainer Description"
            className="trainer-input"
          />
          {errors.description && <p className="error">{errors.description}</p>}
        </label>

        <label>
          Email:
          <input
            type="text"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Trainer Email"
            className="trainer-input"
          />
          {errors.email && <p className="error">{errors.email}</p>}
        </label>

        <label>
          URL:
          <input
            type="text"
            name="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Trainer Image URL"
            className="trainer-input"
          />
          {errors.url && <p className="error">{errors.url}</p>}
        </label>

        <button type="submit" className="trainer-submit-btn">
          {id ? 'Update' : 'Create'} Trainer
        </button>

        {id && (
          <button
            type="button"
            onClick={handleDelete}
            className="trainer-delete-btn"
          >
            Delete Trainer
          </button>
        )}
      </form>
    </div>
  );
}
