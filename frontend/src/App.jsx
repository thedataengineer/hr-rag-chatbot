import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await axios.post('http://localhost:8000/chat', { query });
    setResponse(result.data.response);
  };

  return (
    <div className="App">
      <h1>HR RAG Chatbot</h1>
      <form onSubmit={handleSubmit}>
        <input 
          type="text" 
          value={query} 
          onChange={(e) => setQuery(e.target.value)} 
          placeholder="Ask an HR question"
        />
        <button type="submit">Send</button>
      </form>
      {response && <p>Response: {response}</p>}
    </div>
  );
}

export default App;
