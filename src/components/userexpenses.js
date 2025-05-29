// ExpenseList.js
import React, { useState, useEffect, useCallback} from 'react';
import api from '../api';

export default function ExpenseList() {
  const [expenses, setExpenses] = useState([]);
  const [userId, setUserId] = useState('');

  const fetchExpenses = useCallback(async () => {
  try {
    const endpoint = userId ? `/expenses/user/${userId}` : '/expenses/';
    const res = await api.get(endpoint);
    setExpenses(res.data);
  } catch (error) {
    console.error('Error fetching expenses:', error);
  }
}, [userId]);

useEffect(() => {
  fetchExpenses();
}, [fetchExpenses]);

  return (
    <div>
      <h2>Expenses</h2>
      <input
        value={userId}
        onChange={e => setUserId(e.target.value)}
        placeholder="Filter by User ID"
      />
      <button onClick={fetchExpenses}>Fetch Expenses</button>
      <ul>
        {expenses.map(exp => (
          <li key={exp.id}>
            {exp.title} - ${exp.amount} on {exp.date} ({exp.category}) [User: {exp.user_id}]
          </li>
        ))}
      </ul>
    </div>
  );
}
