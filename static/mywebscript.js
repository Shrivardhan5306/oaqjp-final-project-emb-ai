let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value.trim();
    let responseDiv = document.getElementById("system_response");

    if (!textToAnalyze) {
        responseDiv.innerHTML =
            '<div class="error-box">Please enter some text before analyzing.</div>';
        return;
    }

    responseDiv.innerHTML = '<p class="loading">Analyzing emotions…</p>';

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState !== 4) return;

        let data;
        try { data = JSON.parse(this.responseText); } catch (e) { data = {}; }

        if (this.status === 200 && data.emotions) {
            let e = data.emotions;
            let capitalize = s => s.charAt(0).toUpperCase() + s.slice(1);

            let chips = ["anger", "disgust", "fear", "joy", "sadness"]
                .map(em => `
                    <div class="emotion-chip">
                        <div class="label">${capitalize(em)}</div>
                        <div class="value">${parseFloat(e[em]).toFixed(4)}</div>
                    </div>`).join("");

            responseDiv.innerHTML = `
                <div class="result-box">
                    <h2>Emotion Analysis Results</h2>
                    <div class="emotion-grid">${chips}</div>
                    <div class="dominant-banner">
                        Dominant Emotion: <strong>${capitalize(e.dominant_emotion)}</strong>
                    </div>
                </div>`;
        } else {
            let msg = (data && data.error) ? data.error : "Analysis failed. Please try again.";
            responseDiv.innerHTML = `<div class="error-box">${msg}</div>`;
        }
    };

    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
