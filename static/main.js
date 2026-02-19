document.addEventListener("DOMContentLoaded", () => {
  const button = document.getElementById("analyze-button");
  const resultDiv = document.getElementById("result");

  button.addEventListener("click", async () => {
    const youtubeUrl = document.getElementById("youtube-url").value;

    if (!youtubeUrl) {
      resultDiv.innerHTML = "❗ Please enter a YouTube URL.";
      return;
    }

    resultDiv.innerHTML = "⏳ Analyzing video...";

    try {
      const response = await fetch("/analyze", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ youtube_url: youtubeUrl }),
      });

      const data = await response.json();

      if (data.error) {
        resultDiv.innerHTML = "❌ Error: " + data.error;
        return;
      }

      let html = "<h3>✅ Features Extracted:</h3><ul>";
      for (const [key, value] of Object.entries(data)) {
        html += `<li><strong>${key}</strong>: ${value}</li>`;
      }
      html += "</ul>";

      resultDiv.innerHTML = html;
    } catch (error) {
      resultDiv.innerHTML = "❌ Failed to analyze. Check console for details.";
      console.error(error);
    }
  });
});
