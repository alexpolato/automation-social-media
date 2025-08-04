from flask import Flask, request, jsonify
import json
import os
from ai_function.gemini_text import generate_text
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/api/python")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/privacy-policy")
def privacy_policy():
    return jsonify({"privacy_policy": "https://www.seusite.com/privacy-policy"}), 200


@app.route("/webhook", methods=["GET", "POST"])
def webhooks():
    if request.method == "GET":
        # Verificação do token de webhook
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if challenge:
            return challenge
        else:
            return "<p>This is GET Request, Hello Webhook</p>"

    elif request.method == "POST":

        try:
            print(json.dumps(request.json, indent=4))
        except:
            pass
        return "<p>This is POST Request</p>"


@app.route("/agent-ia", methods=["POST"])
def agent_ia(prompt=str):

    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "Invalid request"}), 400

    # response = generate_text(prompt=data["prompt"])
    print("prompt:", data["prompt"])
    # print("response:", response)
    return prompt
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(port=5328)
