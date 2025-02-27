from flask import Flask, jsonify
import os

app = Flask(__name__)
APP_NAME = os.environ.get('APP_NAME', 'simple-flask')
APP_VERSION = os.environ.get('APP_VERSION', '1.0.0')

@app.route('/')
def home():
    print(f"{APP_NAME} v{APP_VERSION} - Home route accessed")
    return f"<h1>{APP_NAME} v{APP_VERSION}</h1><p>Welcome! Check <a href='/health'>health</a>.</p>"

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'app': APP_NAME, 'version': APP_VERSION})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting {APP_NAME} v{APP_VERSION} on port {port}")
    app.run(host='0.0.0.0', port=port)