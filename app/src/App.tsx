import React, { useState } from 'react';
import TextBox from './TextBox';
import Button from '@material-ui/core/Button';

import './App.css';

function App() {
  const [endpoint, setEndPoint] = useState('http://localhost:5000');
  const [inputText, setInputText] = useState('Type here...');
  const [outputText, setOutputText] = useState('');

  console.log(endpoint);

  const sendText = async (text: string) => {
    const result = await fetch(endpoint);
    console.log('result: ', result);
  };

  return (
    <div className="App">
      <>
        <h3>API endpoint</h3>
        <div>
          <input
            onChange={(event) => setEndPoint(event.target.value)}
            value={endpoint}
          />
        </div>
      </>
      <TextBox
        text={inputText}
        onChange={setInputText}
        title="Content from which to generate"
      />
      <Button
        variant="contained"
        onClick={() => sendText(inputText)}
        style={{ padding: '5px' }}
      >
        Generate
      </Button>
      <TextBox
        text={outputText}
        onChange={setOutputText}
        title="Generated content"
      />
    </div>
  );
}

export default App;
