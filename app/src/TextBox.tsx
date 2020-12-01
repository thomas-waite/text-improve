import React from 'react';

interface TextBoxProps {
  text: string;
  title: string;
  onChange: (value: string) => void;
}

export default function TextBox({ text, title, onChange }: TextBoxProps) {
  return (
    <>
      <h2>{title}</h2>
      <div>
        <textarea
          onChange={(event) => onChange(event.target.value)}
          value={text}
          style={{ width: '500px', height: '150px' }}
        />
      </div>
    </>
  );
}
