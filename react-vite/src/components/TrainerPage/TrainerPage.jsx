import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import './TrainerPage.css'; 

function TrainerPage() {

  const navigate = useNavigate();
  const [trainers, setTrainers] = useState([]);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    fetch('/api/trainers')
      .then((res) => res.json())
      .then((data) => setTrainers(data.trainers))
      .catch((err) => console.error('Error fetching trainers:', err));
  }, []);

  const isManager = user?.roles?.some((role) => role.isManager);

  return (
    <div>
      <h1>Our Trainers</h1>
      {isManager && (
        <button onClick={() => navigate('/trainers/new')}>Add a new trainer</button>
      )}
      <div className="trainer-container">
        {trainers.length > 0 ? (
          trainers.map((trainer) => (
            <div key={trainer.id} className="trainer-card">

              <h2>{trainer.username}</h2>
              <p>{trainer.roles[0].describe}</p>
              {trainer.roles[0].url ? (
                <img 
                  src={trainer.roles[0].url} 
                  alt={`${trainer.username}'s profile`} 
                  className="trainer-image"
                />) : (
                <p>No picture available</p> 
              )}

              {isManager && (
              <>
                <button onClick={() => navigate(`/trainers/${trainer.id}/edit`, { state: { trainer } })}>
                  Edit information
                </button>
              </>
               )}
            </div>
          ))
        ) : (
          <p>Loading trainers...</p>
        )}
      </div>


    </div>
  );
}

export default TrainerPage
