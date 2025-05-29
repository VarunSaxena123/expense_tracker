import React from 'react';
import UserForm from './components/user';
import ExpenseList from './components/userexpenses';
import ExpenseForm from './components/allexpenses';

function App() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Expense Tracker</h1>
      <h2>Create User</h2>
      <UserForm />
      <h2>Create Expense</h2>
      <ExpenseForm />
      <h2>Expenses</h2>
      <ExpenseList />
    </div>
  );
}

export default App;
