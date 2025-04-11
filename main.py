from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Webhook de Google Apps Script
WEBHOOK_URL = "https://script.google.com/macros/s/AKfycbzg44oxDb0whJcBlO08n5rV8ZJsvkR8BB5EswGQLWdJ6EQNVnHVHv-pyucubDG8HSr1/exec"  # Reemplazá con el tuyo

@app.route('/')
def home():
    return "✅ API puente activa y funcionando"

@app.route('/enviar', methods=['POST'])
def enviar():
    return enviar_datos()

@app.route('/actualizar_tareas', methods=['POST'])
def actualizar_tareas():
    return enviar_datos()

def enviar_datos():
    data = request.get_json()

    if not data:
        return jsonify({"status": "error", "message": "No se recibió JSON válido"}), 400

    try:
        response = requests.post(WEBHOOK_URL, json=data)
        return jsonify({"status": "ok", "message": "Enviado a Apps Script", "response": response.text})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
