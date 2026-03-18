import axios from "axios";

const API = axios.create({
  baseURL: "https://trade-opportunities-analyzer.onrender.com",
});

export const analyzeSector = async (sector, token) => {
  const response = await API.get(`/analyze/${sector}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    responseType: "blob",
  });

  return response.data;
};