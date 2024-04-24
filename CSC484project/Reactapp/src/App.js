import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'; // Import Routes instead of Switch
import Navbar from './Navbar';
import HelloWorld from './HelloWorld';
import Home from './Home';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <div className="container">
          <Routes> {/* Use Routes instead of Switch */}
            <Route path="/" element={<Home /> } />
            <Route path="/hello" element={<HelloWorld />} />
            {/* Add routes for other pages here */}
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;
