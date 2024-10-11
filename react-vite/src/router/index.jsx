import { createBrowserRouter } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import HomePage from '../components/HomePage';
import GalleriesPage from '../components/GalleriesPage';
import GalleriesForm from '../components/GalleriesForm';
import GalleryDetails from '../components/GalleriesPage/GalleryDetails';
import TrainersPage from '../components/TrainerPage';
import TrainerForm from '../components/TrainerForm';
import EquipmentPage from '../components/EquipmentPage';
import EquipmentForm from '../components/EquipmentForm';
import SchedulePage from '../components/SchedulePage/SchedulePage';
import ScheduleDetails from '../components/SchedulePage/ScheduleDetails';
import ScheduleForm from '../components/ScheduleForm';
import Layout from './Layout';

export const router = createBrowserRouter([
  {
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <HomePage />,
      },      
      {
        path: "trainers",
        element: <TrainersPage />,
      },
      {
        path: "Schedule",
        element: <SchedulePage />,
      },
      {
        path: "equipment",
        element: <EquipmentPage />,
      },
      {
        path: "galleries",
        element: <GalleriesPage />,
      },
      {
        path: "login",
        element: <LoginFormPage />,
      },
      {
        path: "signup",
        element: <SignupFormPage />,
      },
      {
        path: "schedule/new", 
        element: <ScheduleForm />,
      },
      {
        path: "schedule/:id", 
        element: <ScheduleDetails />,
        loader: async ({ params }) => {
          const res = await fetch(`/api/schedules/${params.id}`);
          if (res.ok) {
            const data = await res.json();
            return data;
          } else {
            return false;
          }
        },
      },
      {
        path: "schedule/:id/edit", // Edit an existing schedule
        element: <ScheduleForm />,
        loader: async ({ params }) => {
          const res = await fetch(`/api/schedules/${params.id}`);
          return res.ok ? await res.json() : null;
        },
      },
      {
        path: "galleries/new", 
        element: <GalleriesForm />,
      },
      {
        path: "galleries/:id", 
        element: <GalleryDetails />,
        loader: async ({ params }) => {
          const res = await fetch(`/api/galleries/${params.id}`);
          if (res.ok) {
            const data = await res.json();
            return data;
          } else {
            return false;
          }
        },
      },
      {
        path: "galleries/:id/edit", // Edit an existing galleries
        element: <GalleriesForm />,
        loader: async ({ params }) => {
          const res = await fetch(`/api/galleries/${params.id}`);
          return res.ok ? await res.json() : null;
        },
      },
      {
        path: "equipment/new", 
        element: <EquipmentForm />,
      },
      {
        path: "equipment/:id/edit", // Edit an existing equipment
        element: <EquipmentForm />,
        loader: async ({ params }) => {
          const res = await fetch(`/api/equipment/${params.id}`);
          return res.ok ? await res.json() : null;
        },
      },

      {
        path: "trainers/new", 
        element: <TrainerForm />,
      },
      {
        path: "trainers/:id/edit", // Edit an existing equipment
        element: <TrainerForm />,
        // loader: async ({ params }) => {
        //   const res = await fetch(`/api/trainers/${params.id}`);
        //   return res.ok ? await res.json() : null;
        // },
      }
    ],
  },
]);