from flask import Flask, request, jsonify
import os

app = Flask(__name__)

DATASET = "dataset-ai.txt"

def load_data():
    if os.path.exists(DATASET):
        with open(DATASET, "r", encoding="utf-8") as f:
            return f.read()
    return ""

DATA = load_data()

@app.route("/chat", methods=["POST"])
def chat():
    q = request.json.get("question", "").lower()
    if q in DATA.lower():
        return jsonify({"answer": "Jawaban ditemukan di basis data Anda."})
    return jsonify({"answer": "Belum ada di data. Tambahkan artikel baru."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
