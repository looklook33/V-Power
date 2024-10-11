import { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import './GalleriesPage.css'

const GalleriesPage = () => {
  const navigate = useNavigate();
  const [galleries, setGalleries] = useState([]);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    fetch('/api/galleries')
      .then((res) => res.json())
      .then((data) => setGalleries(data.galleries))
      .catch((err) => console.error('Error fetching galleries:', err));
  }, []);

  const isManager = user?.roles?.some((role) => role.isManager);

  return (
    <div>
      <h1>Workout Gallery</h1>
      
      {isManager && (
        <button className='button-man' onClick={() => navigate(`/galleries/new`)}>Add a new gallery picture</button>
      )}
      <ul className="equipment-container">
        {galleries.map((gallery) => (
          <li key={gallery.id} className="equipment-card">
            <img src={gallery.url} alt={gallery.type} 
            className="equipment-image"
            />
            <p>{gallery.describe}</p>

            {isManager && (
              <>
                <button onClick={() => navigate(`/galleries/${gallery.id}/edit`, {state: { gallery } })}>Edit information</button>
              </>
            )}
          </li>
        ))}
      </ul>

    </div>
  );
};

export default GalleriesPage;
