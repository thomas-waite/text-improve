import React, { useState } from 'react';
import TextBox from './TextBox';
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
import Typography from '@material-ui/core/Typography';
import red from '@material-ui/core/colors/red';

import './App.css';

function App() {
  const [endpoint, setEndPoint] = useState('http://localhost/predict');
  const [inputText, setInputText] = useState('Chocolate is');
  const [outputText, setOutputText] = useState('');
  const [loading, setLoading] = useState(false);

  const sendText = async (text: string) => {
    setLoading(true);
    const response = await fetch(endpoint, {
      method: 'POST',
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });
    const jsonData = await response.json();
    const generatedText = JSON.parse(jsonData.body)[0].generated_text;
    setLoading(false);
    setOutputText(generatedText);
  };

  return (
    <div className="App">
      <Typography
        component="h1"
        variant="h3"
        align="center"
        style={{ padding: '10px', color: red[500] }}
      >
        TextGen
      </Typography>{' '}
      {/* <>
        <h3>API endpoint</h3>
        <div>
          <input
            onChange={(event) => setEndPoint(event.target.value)}
            value={endpoint}
          />
        </div>
      </> */}
      <TextBox text={inputText} onChange={setInputText} title="Input text" />
      <Button
        variant="contained"
        color="secondary"
        onClick={() => sendText(inputText)}
        style={{ padding: '10px' }}
      >
        Generate
        {loading && <CircularProgress />}
      </Button>
      <TextBox
        text={outputText}
        onChange={setOutputText}
        title="Generated paragraph"
      />
    </div>
  );
}

export default App;
