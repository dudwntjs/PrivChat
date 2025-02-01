import React, { useState, useEffect, useRef } from "react";
import { searchCase } from "./api"; // API 요청 함수 가져오기

function App() {
  const [query, setQuery] = useState("");   // 사용자 입력 상태
  const [messages, setMessages] = useState([]); // 대화 목록
  const [relatedCases, setRelatedCases] = useState([]); // 관련 판례 목록
  const [loading, setLoading] = useState(false); // 로딩 상태
  const [error, setError] = useState(null); // 오류 상태
  const chatContainerRef = useRef(null); // 채팅창 스크롤 관리

  // 검색 버튼 클릭 시 실행되는 함수
  const handleSearch = async () => {
    if (!query.trim()) {
      alert("메시지를 입력하세요!");
      return;
    }

    setLoading(true);
    setError(null);
    
    // 사용자 메시지 추가
    const newMessages = [...messages, { role: "user", text: query }];
    setMessages(newMessages);
    setQuery(""); // 입력창 초기화

    try {
      const response = await searchCase(query);
      console.log("✅ 검색 결과:", response);  // 🔥 응답 데이터 콘솔 출력

      // AI 응답
      const aiMessage = response && response.response 
        ? response.response.split("\n").map((line, index) => <p key={index}>{line}</p>) 
        : "검색 결과 없음";

      // 관련 판례 데이터 저장
      setRelatedCases(response.related_cases || []);

      // 메시지 업데이트
      setMessages([...newMessages, { role: "assistant", text: aiMessage }]);
    } catch (err) {
      console.error("❌ 오류:", err);
      setError("검색 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  // 채팅창이 업데이트될 때 자동 스크롤
  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop = chatContainerRef.current.scrollHeight;
    }
  }, [messages]);

  return (
    <div style={styles.container}>
      <h2 style={styles.title}>💬 PrivChat</h2>

      {/* 채팅 & 관련 판례를 가로로 배치 */}
      <div style={styles.contentContainer}>
        
        {/* 채팅 창 */}
        <div ref={chatContainerRef} style={styles.chatContainer}>
          {messages.map((msg, index) => (
            <div key={index} style={msg.role === "user" ? styles.userMessage : styles.aiMessage}>
              {msg.text}
            </div>
          ))}
          {loading && <div style={styles.loading}>⏳ AI가 생각 중...</div>}
          {error && <div style={styles.error}>{error}</div>}
        </div>

        {/* 관련 판례 패널 */}
        {relatedCases.length > 0 && (
          <div style={styles.caseContainer}>
            <h3 style={styles.caseTitle}>📜 관련 판례</h3>
            <ul style={styles.caseList}>
              {relatedCases.map((caseText, index) => (
                <li key={index} style={styles.caseItem}>{caseText}</li>
              ))}
            </ul>
          </div>
        )}
      </div>

      {/* 입력창 */}
      <div style={styles.inputContainer}>
        <input 
          type="text" 
          value={query} 
          onChange={(e) => setQuery(e.target.value)} 
          placeholder="메시지를 입력하세요..."
          style={styles.input}
        />
        <button onClick={handleSearch} style={styles.sendButton}>📩</button>
      </div>
    </div>
  );
}

// 스타일 정의
const styles = {
  container: {
    width: "100vw",
    height: "100vh",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    fontFamily: "Arial, sans-serif",
    backgroundColor: "#1a1a1a",
    color: "white",
    padding: "20px",
  },
  title: {
    marginBottom: "10px",
  },
  contentContainer: {
    display: "flex",
    width: "100%",
    maxWidth: "900px",
    height: "500px",
    borderRadius: "10px",
    overflow: "hidden",
  },
  chatContainer: {
    flex: 2,
    border: "1px solid #444",
    borderRadius: "10px",
    padding: "10px",
    overflowY: "auto",
    display: "flex",
    flexDirection: "column",
    backgroundColor: "#2a2a2a",
  },
  userMessage: {
    alignSelf: "flex-end",
    backgroundColor: "#007bff",
    color: "white",
    padding: "10px",
    borderRadius: "10px",
    marginBottom: "5px",
    maxWidth: "70%",
  },
  aiMessage: {
    alignSelf: "flex-start",
    backgroundColor: "#444",
    color: "white",
    padding: "10px",
    borderRadius: "10px",
    marginBottom: "5px",
    maxWidth: "70%",
  },
  loading: {
    alignSelf: "center",
    color: "#888",
    fontSize: "14px",
    marginTop: "5px",
  },
  error: {
    alignSelf: "center",
    color: "red",
    fontSize: "14px",
    marginTop: "5px",
  },
  inputContainer: {
    display: "flex",
    width: "100%",
    maxWidth: "900px",
    marginTop: "10px",
  },
  input: {
    flex: 1,
    padding: "10px",
    borderRadius: "5px",
    border: "1px solid #ddd",
    outline: "none",
  },
  sendButton: {
    padding: "10px",
    borderRadius: "5px",
    border: "none",
    backgroundColor: "#007bff",
    color: "white",
    marginLeft: "5px",
    cursor: "pointer",
  },
  caseContainer: {
    flex: 1,
    backgroundColor: "#222", 
    padding: "10px",
    borderLeft: "1px solid #444",
    overflowY: "auto",
  },
  caseTitle: {
    fontSize: "16px",
    fontWeight: "bold",
    marginBottom: "10px",
  },
  caseList: {
    listStyle: "none",
    padding: 0,
  },
  caseItem: {
    fontSize: "14px",
    lineHeight: "1.5",
    marginBottom: "10px",
    backgroundColor: "#333",
    padding: "8px",
    borderRadius: "5px",
  },
};

export default App;