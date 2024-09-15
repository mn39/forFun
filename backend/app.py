from flask import Flask, send_from_directory
from pymongo import MongoClient
from dotenv import load_dotenv
import os
from flask_cors import CORS

from flask import jsonify
load_dotenv()


app = Flask(__name__, static_folder='../frontend/build', static_url_path='')

CORS(app)


# MongoDB 연결
client = MongoClient(os.environ.get('MONGODB_URI'))
db = client['MN']
collection = db['MN']


@app.route('/api/data')
def get_data():
    data = collection.find_one()
    data['_id'] = str(data['_id'])
    return jsonify(data)

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