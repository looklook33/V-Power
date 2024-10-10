import { useParams, useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';

export default function GalleryDetails() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [gallery, setGallery] = useState(null);

  useEffect(() => {
    // Fetch gallery details by ID
    async function fetchGalleryDetails() {
      const response = await fetch(`/api/galleries/${id}`);
      const data = await response.json();
      setGallery(data.gallery);  
    }
    fetchGalleryDetails();
  }, [id]);


  if (!gallery) return <div>Loading...</div>;

  return (
    <div>
      <h1>Gallery Details</h1>
      <p><strong>Type:</strong> {gallery.type}</p>
      <p><strong>Description:</strong> {gallery.describe}</p>
      <img src={gallery.url} alt={gallery.type} />

      <button onClick={() => navigate(`/galleries/${id}/edit`, {state: { gallery } })}>
        Edit Gallery
      </button>
    </div>
  );
}
