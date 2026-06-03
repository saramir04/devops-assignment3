from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "flask-api",
        "message": "Assignment 3 API Running"
    })

@app.route("/health")
def health():
    return jsonify({
        "service": "flask-api",
        "status": "healthy"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
