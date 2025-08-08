import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow_hub as hub
import numpy as np
from data import pairs

app = Flask(__name__)

# Restrict CORS to allow only requests from your static site
CORS(app, origins=["https://chatboss-js-frontend.onrender.com"])

# Load embedding model
embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")

# Prepare questions/responses
questions = [q for q, a in pairs]
responses = [a for q, a in pairs]
question_embeddings = embed(questions)

@app.route('/chat', methods=['POST'])
def get_response():
    data = request.get_json()
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"response": "Please provide a valid message."})

    input_embedding = embed([user_input])
    similarities = np.inner(input_embedding, question_embeddings)[0]
    best_match = np.argmax(similarities)
    bot_response = responses[best_match]

    return jsonify({"response": bot_response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Default to 10000 if PORT not set
    app.run(debug=True, port=port, host='0.0.0.0')  # Ensure the app listens on all network interfaces
