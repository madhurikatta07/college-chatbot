from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
import random
import os

app = Flask(__name__)
CORS(app)

# Load Model
model_data = None
model_path = 'model.pkl'

if os.path.exists(model_path):
    try:
        with open(model_path, 'rb') as f:
            model_data = pickle.load(f)
        classifier = model_data['pipeline']
        intents_data = model_data['intents']
        print("Model loaded successfully.")
    except Exception as e:
        print(f"Error loading model: {e}")
else:
    print(f"Warning: {model_path} not found. Run train_model.py first.")
    classifier = None
    intents_data = None

@app.route('/')
def home():
    return jsonify({"status": "ML College Chatbot API is running!", "model_loaded": classifier is not None})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if not classifier or not intents_data:
        return jsonify({
            "error": "Model not loaded. Please train the model first.",
            "status": "error"
        }), 500

    # Handle both GET parameters and POST JSON
    if request.method == 'GET':
        user_message = request.args.get('msg')
    else:
        data = request.get_json()
        user_message = data.get('msg') if data else None
        
    if not user_message:
        return jsonify({
            "error": "Missing message. Please provide 'msg' parameter.",
            "status": "error"
        }), 400

    try:
        # Predict intent
        predicted_tag = classifier.predict([user_message])[0]
        
        # Get probability/confidence
        probabilities = classifier.predict_proba([user_message])[0]
        confidence = float(max(probabilities))
        
        # Find response
        response = "I'm sorry, I don't understand."
        for intent in intents_data['intents']:
            if intent['tag'] == predicted_tag:
                response = random.choice(intent['responses'])
                break
                
        # Send JSON response
        return jsonify({
            "user_message": user_message,
            "predicted_intent": predicted_tag,
            "confidence": round(confidence, 2),
            "response": response
        })
        
    except Exception as e:
        return jsonify({
            "error": str(e),
            "status": "error"
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
