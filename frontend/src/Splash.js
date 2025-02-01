import React from "react";
import { useNavigate } from "react-router-dom";
import gavelImage from "./images/gavel.png"; // 이미지 경로를 정확히 import

function Splash() {
  const navigate = useNavigate();

  return (
    <div style={styles.container}>
      <div style={styles.imageContainer}>
        <img src={gavelImage} alt="Judge Gavel" style={styles.image} />
      </div>
      <h1 style={styles.title}>📜 개인정보 보호법 AI 챗봇</h1>
      <p style={styles.description}>
        개인정보 보호법과 관련된 질문을 하고, 관련 판례를 확인하세요.
      </p>
      <button style={styles.startButton} onClick={() => navigate("/chat")}>
        🚀 시작하기
      </button>
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
    justifyContent: "center",
    alignItems: "center",
    textAlign: "center",
    backgroundColor: "#000",
    color: "white",
    position: "relative",
  },
  imageContainer: {
    position: "absolute",
    top: 0,
    left: 0,
    width: "100%",
    height: "100%",
    overflow: "hidden",
    zIndex: -1,
  },
  image: {
    width: "100%",
    height: "100%",
    objectFit: "cover",
    filter: "brightness(0.8)",
  },
  title: {
    fontSize: "32px",
    fontWeight: "bold",
    zIndex: 1,
  },
  description: {
    fontSize: "18px",
    marginBottom: "20px",
    zIndex: 1,
  },
  startButton: {
    padding: "12px 24px",
    fontSize: "18px",
    color: "white",
    backgroundColor: "#007bff",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer",
    transition: "0.3s",
    zIndex: 1,
  },
};

export default Splash;