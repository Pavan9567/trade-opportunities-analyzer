import { useState } from "react";
import { analyzeSector } from "../api";

export default function Analyzer() {
  const [sector, setSector] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!sector) return alert("Enter sector");

    const token = prompt("Enter your JWT token:");

    try {
      setLoading(true);

      const blob = await analyzeSector(sector, token);

      // download file
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = `${sector}_report.md`;
      a.click();

    } catch (err) {
      alert("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ textAlign: "center", marginTop: "100px" }}>
      <h1>Trade Opportunities Analyzer</h1>

      <input
        type="text"
        placeholder="Enter sector (e.g. technology)"
        value={sector}
        onChange={(e) => setSector(e.target.value)}
        style={{ padding: "10px", width: "300px" }}
      />

      <br /><br />

      <button onClick={handleAnalyze}>
        {loading ? "Analyzing..." : "Analyze & Download"}
      </button>
    </div>
  );
}