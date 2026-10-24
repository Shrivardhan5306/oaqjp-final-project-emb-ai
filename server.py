"""Flask server for the Emotion Detector web application."""

from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render the main Emotion Detector page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Accept a GET request with textToAnalyze and return emotion scores.

    Returns HTTP 400 with an error message if the text is blank or if
    the emotion API returns no dominant emotion (e.g. blank input).
    Returns HTTP 500 if the API is unreachable.
    """
    text_to_analyze = request.args.get("textToAnalyze", "").strip()

    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!"}), 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return (
            jsonify({"error": "Invalid text! Please try again!"}),
            400,
        )

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"response": response_text, "emotions": result})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
