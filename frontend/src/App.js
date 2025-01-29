import React, { useState } from "react";
import { searchCase } from "./api"; // API 요청 함수 가져오기

function App() {
  const [query, setQuery] = useState("");   // 검색어 상태
  const [result, setResult] = useState(""); // 검색 결과 상태
  const [loading, setLoading] = useState(false); // 로딩 상태
  const [error, setError] = useState(null); // 오류 상태

  // 검색 버튼 클릭 시 실행되는 함수
  const handleSearch = async () => {
    if (!query.trim()) {
      alert("검색어를 입력하세요!");
      return;
    }

    setLoading(true);
    setError(null);
    try {
      const response = await searchCase(query); // FastAPI로 요청 보내기
      setResult(response.message); // 결과 저장
    } catch (err) {
      setError("검색 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>🔍 판례 검색</h2>
      
      <input 
        type="text" 
        value={query} 
        onChange={(e) => setQuery(e.target.value)} 
        placeholder="검색어를 입력하세요"
        style={{
          padding: "8px",
          width: "250px",
          marginRight: "10px"
        }}
      />
      <button 
        onClick={handleSearch}
        style={{
          padding: "8px 15px",
          cursor: "pointer"
        }}
      >
        검색
      </button>

      {loading && <p>⏳ 검색 중...</p>}

      {error && <p style={{ color: "red" }}>{error}</p>}

      {result && (
        <div style={{ marginTop: "20px", border: "1px solid #ddd", padding: "10px", width: "300px", margin: "auto" }}>
          <h3>📌 검색 결과:</h3>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default App;