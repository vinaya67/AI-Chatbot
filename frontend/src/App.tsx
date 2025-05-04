import React, { useState } from 'react';
import { analyzeLog } from './api';

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async () => {
    const res = await analyzeLog(file, text);
    setResult(res.result + (res.ticket_url ? `\nTicket: ${res.ticket_url}` : ''));
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Jenkins Log Analyzer</h1>

      <input type="file" accept=".log,.txt" onChange={e => setFile(e.target.files?.[0] || null)} />
      <p>OR paste log below:</p>
      <textarea rows={10} cols={80} value={text} onChange={e => setText(e.target.value)} />

      <br /><br />
      <button onClick={handleSubmit}>Analyze</button>

      <h3>Result:</h3>
      <pre>{result}</pre>
    </div>
  );
}

export default App;
