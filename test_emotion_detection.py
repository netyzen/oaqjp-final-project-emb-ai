"""Tests for the emotion_detector application."""
import unittest

from emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Check that emotion_detector returns the formatted emotion scores."""

    def test_returns_formatted_output(self):
        """The result has all five emotion scores and the dominant emotion."""
        result = emotion_detector('I am really mad about this')
        for key in ('anger', 'disgust', 'fear', 'joy', 'sadness'):
            self.assertIn(key, result)
        self.assertEqual(result['dominant_emotion'], 'anger')


if __name__ == '__main__':
    unittest.main()
