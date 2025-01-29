import axios from "axios";

const API_URL = "http://127.0.0.1:8000";  // FastAPI 서버 주소

export const searchCase = async (query) => {
  try {
    const response = await axios.post(`${API_URL}/search/`, { query }, {
      headers: {
        "Content-Type": "application/json",
      },
    });
    return response.data;
  } catch (error) {
    console.error("Error fetching search results:", error);
    return { message: "오류 발생" };
  }
};