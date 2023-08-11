from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/get_translation')
def get_translation():
    response = requests.get('https://fourtonfish.com/hellosalut/?lang=fr')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

