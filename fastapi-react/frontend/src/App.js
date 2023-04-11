import './App.css';
import { useState } from 'react';
import { useEffect } from 'react';

function App() {
  const [text, setText] = useState('')
  const fetchData = async () => {
    //const response = await fetch("http://localhost:8000/mastodon")
    const response = await fetch("http://172.26.132.211/:8000/mastodon");
    const data = await response.json()
    setText(data)
    console.log(data)
  }
  useEffect(() => {
    fetchData()
    const timer = setInterval(() => fetchData(), 1000); // Fetch data every 1 seconds
    return () => clearInterval(timer); // Clean up the interval on component unmount
  }, [])

  return (
    <div className="App">
      <h1>The text retrived from Mastodon through fastAPI</h1>
      <h3>{text.username}</h3>
      <div dangerouslySetInnerHTML={{ __html: text.content }} />
      <a href ={text.url}>{text.url}</a>
    </div>
  );
}

export default App;
