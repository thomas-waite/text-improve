import React, { useState } from 'react';
import TextBox from './TextBox';
import Button from '@material-ui/core/Button';

import './App.css';

function App() {
  const [inputText, setInputText] = useState('Type here...');
  const [outputText, setOutputText] = useState('');

  return (
    <div className="App">
      <TextBox
        text={inputText}
        onChange={setInputText}
        title="Content from which to generate"
      />
      <Button variant="contained" style={{ padding: '5px' }}>
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
