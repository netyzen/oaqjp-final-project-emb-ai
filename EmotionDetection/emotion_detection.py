"""Emotion detection using the Watson NLP EmotionPredict service."""
import requests

URL = ('https://sn-watson-emotion.labs.skills.network/v1/'
       'watson.runtime.nlp.v1/NlpService/EmotionPredict')
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
EMOTIONS = ('anger', 'disgust', 'fear', 'joy', 'sadness')
BAD_REQUEST = 400


def emotion_detector(text_to_analyze):
    """Return the emotion scores and the dominant emotion for the given text.

    For blank input Watson answers with status 400, and every value is None.
    """
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(URL, json=payload, headers=HEADERS, timeout=10)
    if response.status_code == BAD_REQUEST:
        return {key: None for key in (*EMOTIONS, 'dominant_emotion')}
    scores = response.json()['emotionPredictions'][0]['emotion']
    result = {emotion: scores[emotion] for emotion in EMOTIONS}
    return {**result, 'dominant_emotion': max(result, key=result.get)}
