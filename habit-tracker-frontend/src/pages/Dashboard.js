import { useEffect, useState } from "react";
import API from "../services/api";

function Dashboard() {
  const [habits, setHabits] = useState([]);

  useEffect(() => {
    API.get("/habits/").then(res => setHabits(res.data));
  }, []);

  const completeHabit = (id) => {
    API.post(`/habits/${id}/log/`).then(() => alert("Completed"));
  };

  return (
    <div>
      <h2>Dashboard</h2>
      {habits.map(h => (
        <div key={h.id}>
          <b>{h.name}</b>
          <button onClick={() => completeHabit(h.id)}>Complete</button>
        </div>
      ))}
    </div>
  );
}

export default Dashboard;
