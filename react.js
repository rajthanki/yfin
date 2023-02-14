import React, { useEffect, useState } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      const url =
        "https://www.nseindia.com/api/option-chain-indices?symbol=RELIANCE&expiryDate=24FEB2022";
      const response = await fetch(url);
      const jsonData = await response.json();
      setData(jsonData);
    };
    fetchData();
  }, []);

  return (
    <div>
      {data ? (
        <pre>{JSON.stringify(data, null, 2)}</pre>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;
