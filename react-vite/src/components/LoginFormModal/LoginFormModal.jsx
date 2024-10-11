import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";
import { useNavigate } from "react-router-dom";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  const loginMember = async () => {
    await dispatch(
      thunkLogin({
        email: 'demo@aa.io',
        password: 'password'
      })
    );

    closeModal();
    navigate('/')
  }

  const loginDemo = async () => {
    await dispatch(
      thunkLogin({
        email: 'min@aa.io',
        password: 'password'
      })
    );

    closeModal();
    navigate('/')
  }

  return (
    <>
    <div className="modal-container"> 
    <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Email
          <input
            type="text"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        {errors.email && <p>{errors.email}</p>}
        <label>
          Password
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        {errors.password && <p>{errors.password}</p>}
        <button type="submit">Log In</button>
        <a className='login-demo center' onClick={loginMember}>Log In as Demo Member User</a>
        <a className='login-demo center' onClick={loginDemo}>Log In as Demo Manager User</a>
      </form>
    </div>
      
    </>
  );
}

export default LoginFormModal;
