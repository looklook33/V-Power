import { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate, useParams ,useLocation} from 'react-router-dom';
import './GalleriesForm.css';

export default function GalleriesForm() {
  const location = useLocation()
  const gallery = location.state?.gallery || null;

  const [type, setType] = useState(gallery?.type ||'');
  const [url, setUrl] = useState(gallery?.url || '');
  const [description, setDescription] = useState(gallery?.describe || '');
  const [errors, setErrors] = useState({});
  const { id } = useParams();
  const user = useSelector((state) => state.session.user);
  const navigate = useNavigate();

  useEffect(() => {
    if (id) {
      fetch(`/api/galleries/${id}`)
        .then((res) => res.json())
        .then((data) => {
          setType(data.gallery.type);
          setUrl(data.gallery.url);
          setDescription(data.gallery.describe);
        })
        .catch((error) => console.error('Error fetching gallery:', error));
    }
  }, [id]);


  const validateForm = () => {
    const newErrors = {};
    if (!type.trim()) newErrors.type = 'Gallery type is required.';
    if (!url.trim()) newErrors.url = 'Gallery URL is required.';
    if (!description.trim()) newErrors.description = 'Description is required.';
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!validateForm()) return;

    const galleryData = {
      type,
      url,
      describe: description,
      userId: user.id,
    };

    const method = id ? 'PUT' : 'POST';
    const endpoint = id ? `/api/galleries/${id}` : '/api/galleries';

    const res = await fetch(endpoint, {
      method,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(galleryData),
    });

    if (res.ok) {
      await res.json();
      navigate('/galleries');
    }
  };

  const handleDelete = async () => {
    if (id) {
      const confirmed = window.confirm('Are you sure you want to delete this gallery?');
      if (confirmed) {
        const res = await fetch(`/api/galleries/${id}`, { method: 'DELETE' });
        if (res.ok) {
          navigate('/galleries');
        }
      }
    }
  };

  return (
    <div>
      <h1>{id ? 'Edit Gallery' : 'Create Gallery'}</h1>
      <form onSubmit={handleSubmit} className="gallery-form">
        <label>
          Type:
          <input
            type="text"
            name="type"
            value={type}
            onChange={(e) => setType(e.target.value)}
            placeholder="Gallery Type"
            className="gallery-input"
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
            placeholder="Gallery URL"
            className="gallery-input"
          />
          {errors.url && <p className="error">{errors.url}</p>}
        </label>

        <label>
          Description:
          <textarea
            name="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Gallery Description"
            className="gallery-input"
          />
          {errors.description && <p className="error">{errors.description}</p>}
        </label>

        <button type="submit" className="gallery-submit-btn">
          {id ? 'Update' : 'Create'} Gallery
        </button>

        {id && (
          <button
            type="button"
            onClick={handleDelete}
            className="gallery-delete-btn"
          >
            Delete Gallery
          </button>
        )}
      </form>
    </div>
  );
}
