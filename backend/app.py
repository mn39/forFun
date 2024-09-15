from flask import Flask, send_from_directory
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_cors import CORS
from bson import json_util
import json 
load_dotenv()


app = Flask(__name__, static_folder='../frontend/build', static_url_path='')

CORS(app)

def parse_json(data):
    return json.loads(json_util.dumps(data))

# MongoDB 연결
client = MongoClient(os.environ.get('MONGODB_URI'))
db = client['MN']
collection = db['MN']


@app.route('/api/data')
def get_data():
    data = collection.find_one()
    return parse_json(data)

# 프론트엔드 정적 파일 서빙
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)