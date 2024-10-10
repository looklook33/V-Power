import { useState, useEffect } from 'react';
// import { useSelector } from 'react-redux';
import { useNavigate, useParams, useLocation } from 'react-router-dom';
import './EquipmentForm.css';

export default function EquipmentForm() {
  const location = useLocation();
  const equipment = location.state?.item || null;
  // console.log('eeeeeeeeeeeee',equipment)

  const [type, setType] = useState(equipment?.type || '');
  const [url, setUrl] = useState(equipment?.url || '');
  const [description, setDescription] = useState(equipment?.describe || '');
  const [errors, setErrors] = useState({});
  const { id } = useParams();
  // const user = useSelector((state) => state.session.user);
  const navigate = useNavigate();

  useEffect(() => {
    if (id) {
      fetch(`/api/equipment/${id}`)
        .then((res) => res.json())
        .then((data) => {
          setType(data.equipment.type);
          setUrl(data.equipment.url);
          setDescription(data.equipment.describe);
        })
        .catch((error) => console.error('Error fetching equipment:', error));
    }
  }, [id]);

  const validateForm = () => {
    const newErrors = {};
    if (!type.trim()) newErrors.type = 'Equipment type is required.';
    if (!url.trim()) newErrors.url = 'Equipment URL is required.';
    if (!description.trim()) newErrors.description = 'Description is required.';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    const equipmentData = {
      type,
      url,
      describe: description,
      // userId: user.id,
    };

    const method = id ? 'PUT' : 'POST';
    const endpoint = id ? `/api/equipment/${id}` : '/api/equipment';

    const res = await fetch(endpoint, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(equipmentData),
    });

    if (res.ok) {
      await res.json();
      navigate('/equipment');
    }
  };

  const handleDelete = async () => {
    if (id) {
      const confirmed = window.confirm('Are you sure you want to delete this equipment?');
      if (confirmed) {
        const res = await fetch(`/api/equipment/${id}`, { method: 'DELETE' });
        if (res.ok) {
          navigate('/equipment');
        }
      }
    }
  };

  return (
    <div>
      <h1>{id ? 'Edit Equipment' : 'Add New Equipment'}</h1>
      <form onSubmit={handleSubmit} className="equipment-form">
        <label>
          Type:
          <input
            type="text"
            name="type"
            value={type}
            onChange={(e) => setType(e.target.value)}
            placeholder="Equipment Type"
            className="equipment-input"
          />
          {errors.type && <p className="error">{errors.type}</p>}
        </label>

        <label>
          URL:
          <input
            type="text"
            name="url"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Equipment Image URL"
            className="equipment-input"
          />
          {errors.url && <p className="error">{errors.url}</p>}
        </label>

        <label>
          Description:
          <textarea
            name="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Equipment Description"
            className="equipment-input"
          />
          {errors.description && <p className="error">{errors.description}</p>}
        </label>

        <button type="submit" className="equipment-submit-btn">
          {id ? 'Update Equipment' : 'Add Equipment'}
        </button>

        {id && (
          <button
            type="button"
            onClick={handleDelete}
            className="equipment-delete-btn"
          >
            Delete Equipment
          </button>
        )}
      </form>
    </div>
  );
}
