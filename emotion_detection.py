import requests

def emotion_detector(text_to_analyse):
    url = "https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/YOUR_ID/v1/analyze?version=2021-08-01"
    
    headers = {"Content-Type": "application/json"}
    
    json_data = {
        "text": text_to_analyse,
        "features": {"emotion": {}}
    }

    response = requests.post(url, json=json_data, headers=headers)

    if response.status_code == 400:
        return None

    data = response.json()
    emotions = data['emotion']['document']['emotion']

    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }
