from flask import Flask, make_response, jsonify
from flask_cors import CORS
import datetime

x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)
CORS(app)


# Route for root api page
@app.route("/")
def home():
    return make_response(jsonify({"success": True}), 200)


# Route for seeing a data
@app.route("/data")
def get_time():
    # Returning an api for showing in  reactjs
    return {"name": "geek", "age": "22", "date": x, "programming": "python"}


# Running app
if __name__ == "__main__":
    app.run(debug=True, port=5000)
