from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import traceback
import os

# 直接导入用户提供的推荐器模块
try:
    from smartreporecommend import SmartRepoRecommender
except Exception:
    SmartRepoRecommender = None

app = Flask(__name__, static_folder='.')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', '前端设计.html')


@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json or {}
    token = data.get('token')
    opendigger = data.get('opendigger')
    username = data.get('username')
    top_n = int(data.get('top_n') or 8)

    if SmartRepoRecommender is None:
        return jsonify({'ok': False, 'error': '无法导入 advanced_backup.SmartRepoRecommender，请检查文件是否存在且可导入。'}), 500

    if not username:
        return jsonify({'ok': False, 'error': '缺少 username 参数'}), 400

    try:
        recommender = SmartRepoRecommender(github_token=token, opendigger_api_key=opendigger)
        results = recommender.generate_recommendation(username, top_n=top_n)
        return jsonify({'ok': True, 'results': results})
    except Exception as e:
        return jsonify({'ok': False, 'error': str(e), 'trace': traceback.format_exc()}), 500


@app.route('/mock_recommend', methods=['GET'])
def mock_recommend():
    # 返回示例数据，便于前端调试特效与链接
    sample = [
        {
            'full_name': 'python/cpython',
            'name': 'cpython',
            'repo_url': 'https://github.com/python/cpython',
            'total_score': 92.5,
            'language': 'Python',
            'domain': '工具',
            'tags': ['语言', '解释器']
        },
        {
            'full_name': 'facebook/react',
            'name': 'react',
            'repo_url': 'https://github.com/facebook/react',
            'total_score': 88.2,
            'language': 'JavaScript',
            'domain': '前端',
            'tags': ['界面开发', '组件']
        }
    ]
    return jsonify({'ok': True, 'results': sample})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting frontend+wrapper on http://127.0.0.1:{port}/")
    app.run(host='127.0.0.1', port=port, debug=True)
