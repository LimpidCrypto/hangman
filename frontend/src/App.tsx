import React from 'react';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import './App.css';
import HomePage from './pages/home';
import { GamePage } from './pages/game';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/">
          <Route index element={<HomePage />} />
        </Route>
        <Route path="/game/:id">
          <Route index element={<GamePage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
