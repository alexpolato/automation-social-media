from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN", "meutokenseguro")
APP_SECRET = os.environ.get("APP_SECRET", "sua_app_secret_aqui")


@app.route("/")
def home():
    return "<p>Servidor Flask está rodando!</p>", 200


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


if __name__ == "__main__":
    app.run(port=5000)
