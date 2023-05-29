import { ChangeEvent, FormEvent, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [question, setQuestion] = useState('');
  const [answer, setAnswer] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e: ChangeEvent<HTMLTextAreaElement>) => {
    setQuestion(e.target.value);
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await axios.post('http://127.0.0.1:5000/ask', { question });
      setAnswer(response.data.answer);
    } catch (error) {
      console.error(error);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Chat with GPT</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Question:
          <textarea value={question} onChange={handleChange} rows={4} cols={50} />
        </label>
        <button type="submit">Ask</button>
      </form>
      {loading && <div>Loading...</div>}
      {answer && <div className="answer">Answer: {answer}</div>}
    </div>
  );
}

export default App;
