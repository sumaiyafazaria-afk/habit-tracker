import { useState } from "react";
import API from "../services/api";

function AddHabit() {
  const [name, setName] = useState("");
  const [frequency, setFrequency] = useState("DAILY");

  const addHabit = async () => {
    await API.post("/habits/", { name, frequency });
    alert("Habit added");
  };

  return (
    <div>
      <h2>Add Habit</h2>
      <input placeholder="Habit name" onChange={e => setName(e.target.value)} />
      <select onChange={e => setFrequency(e.target.value)}>
        <option>DAILY</option>
        <option>WEEKLY</option>
        <option>MONTHLY</option>
      </select>
      <button onClick={addHabit}>Add</button>
    </div>
  );
}

export default AddHabit;
