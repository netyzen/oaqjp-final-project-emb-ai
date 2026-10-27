"""Tests for the emotion_detector application."""
import json
import unittest

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check that emotion_detector returns Watson emotion predictions."""

    def test_returns_emotion_predictions(self):
        """The response contains emotion scores for the input text."""
        result = json.loads(emotion_detector('I am really mad about this'))
        self.assertIn('emotionPredictions', result)
        self.assertIn('anger', result['emotionPredictions'][0]['emotion'])


if __name__ == '__main__':
    unittest.main()
