"""Unit tests for the emotion_detector function."""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases verifying dominant emotion detection for each emotion."""

    def test_joy(self):
        """Test that joyful text returns joy as dominant emotion."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Test that angry text returns anger as dominant emotion."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_sadness(self):
        """Test that sad text returns sadness as dominant emotion."""
        result = emotion_detector("I am sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Test that fearful text returns fear as dominant emotion."""
        result = emotion_detector("I am afraid of this")
        self.assertEqual(result["dominant_emotion"], "fear")

    def test_disgust(self):
        """Test that disgusting text returns disgust as dominant emotion."""
        result = emotion_detector("I am disgusted by this")
        self.assertEqual(result["dominant_emotion"], "disgust")


if __name__ == "__main__":
    unittest.main()
