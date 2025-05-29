// ExpenseForm.js
import React, { useState } from 'react';
import api from '../api';

export default function ExpenseForm() {
  const [title, setTitle] = useState('');
  const [amount, setAmount] = useState('');
  const [date, setDate] = useState('');
  const [category, setCategory] = useState('');
  const [userId, setUserId] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/expenses/', {
        title,
        amount: parseFloat(amount),
        date,
        category,
        user_id: parseInt(userId),
      });

      // Clear form
      setTitle('');
      setAmount('');
      setDate('');
      setCategory('');
      setUserId('');
    } catch (error) {
      console.error('Error creating expense:', error);
    }
  };

  return (
    <div>
      <h2>Add Expense</h2>
      <form onSubmit={handleSubmit}>
        <input
          value={title}
          onChange={e => setTitle(e.target.value)}
          placeholder="Title"
          required
        />
        <input
          value={amount}
          onChange={e => setAmount(e.target.value)}
          placeholder="Amount"
          type="number"
          required
        />
        <input
          value={date}
          onChange={e => setDate(e.target.value)}
          type="date"
          required
        />
        <input
          value={category}
          onChange={e => setCategory(e.target.value)}
          placeholder="Category"
          required
        />
        <input
          value={userId}
          onChange={e => setUserId(e.target.value)}
          placeholder="User ID"
          required
        />
        <button type="submit">Add Expense</button>
      </form>
    </div>
  );
}
