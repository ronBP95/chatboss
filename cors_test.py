from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    return jsonify({"response": f"You said: {data.get('message', '')}"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
