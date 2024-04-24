// myfrontend/src/Home.js
import React, { useState, useEffect } from 'react';

function Home() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    fetch('/api/home/')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => console.error(err));
  }, []);

  return (
    <div>
      <h1>Welcome to the Homepage</h1>
      <p>{message}</p>
    </div>
  );
}

export default Home;
