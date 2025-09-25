from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import requests

app = Flask(__name__)
CORS(app)

genai.configure(api_key="AIzaSyCTc3LOyVq0rz-pwtBysKQp5Pau85pNnno")
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').strip()
    lat = data.get('lat', 28.6139)  # Fallback: New Delhi
    lng = data.get('lng', 77.2090)
    if not message:
        return jsonify({'response': 'Please ask something about EV charging!'})

    try:
        # Check if query is about charging stations or locations
        is_location_query = any(keyword in message.lower() for keyword in ['nearest', 'charger', 'charging', 'station', 'location', 'where'])
        context = ""
        if is_location_query:
            stations_url = f"https://api.openchargemap.io/v3/poi/?output=json&maxresults=5&key=632427e5-a4de-492e-963a-02ef45862f37&latitude={lat}&longitude={lng}&distance=50&distanceunit=KM"
            stations_res = requests.get(stations_url)
            stations = stations_res.json() if stations_res.ok else []
            context = f"User location: ({lat}, {lng}). Nearby stations: {stations[:2]}"

        prompt = f"You are an EV charging assistant. User asked: '{message}'. {'Use this context: ' + context if context else 'Answer concisely without location details unless requested.'}"
        response = model.generate_content(prompt)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'response': f'Sorry, error occurred: {str(e)}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)