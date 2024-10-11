import { useState, useEffect } from 'react';
import { useSelector } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import './EquipmentPage.css'

const EquipmentPage = () => {
  const navigate = useNavigate();
  const [equipment, setEquipment] = useState([]);
  const user = useSelector((state) => state.session.user);

  useEffect(() => {
    fetch('/api/equipment')
      .then((res) => res.json())
      .then((data) => setEquipment(data.equipment))
      .catch((err) => console.error('Error fetching equipment:', err));
  }, []);

  const isManager = user?.roles?.some((role) => role.isManager);

  return (
    <div>
      <h1>Gym Equipment</h1>
      {isManager && (
        <button className='button-man' onClick={() => navigate(`/equipment/new`)}>Add new equipment</button>
      )}
      <ul className="equipment-container">
        {equipment.map((item) => (
          <li key={item.id} className="equipment-card">
            <img src={item.url} alt={item.type} 
            className="equipment-image"
            />
            <p>{item.describe}</p>

            {isManager && (
              <>
                <button onClick={() => navigate(`/equipment/${item.id}/edit`, { state: { item } })}>Edit information</button>
              </>
            )}
          </li>
        ))}
      </ul>


    </div>
  );
};

export default EquipmentPage;
