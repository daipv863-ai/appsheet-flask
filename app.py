from flask import Flask, request, jsonify

app = Flask(__name__)

# Route test
@app.route("/")
def home():
    return "Flask is running OK"

# Route cho AppSheet
@app.route("/appsheet", methods=["POST"])
def appsheet():
    data = request.json
    return jsonify({
        "status": "ok",
        "data": data
    })

if __name__ == "__main__":
    app.run()
