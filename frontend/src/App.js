import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch('/api/data')
      // fetch('http://127.0.0.1:5000/api/data')
      .then((response) => {
        console.log('response:', response);
        if (!response.ok) {
          throw new Error('API 요청 실패');
        }
        return response.text();
      })
      .then((data) => {
        console.log(data);
        setData(data);
      })
      .catch((error) => {
        console.error('에러 발생:', error);
      });
  }, []);

  return (
    <div className='App'>
      <header className='App-header'>
        {data ? <p>{data}</p> : <p>'데이터를 불러오는 중입니다...'</p>}
      </header>
    </div>
  );
}

export default App;
