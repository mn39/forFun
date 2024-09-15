from flask import Flask, send_from_directory
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# 나머지 코드는 이전과 동일import os

app = Flask(__name__, static_folder='frontend/build')

# MongoDB 연결
client = MongoClient(os.environ.get('MONGODB_URI'))
db = client['your_database']

@app.route('/api/data')
def get_data():
    data = db.collection.find_one()
    return str(data)

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