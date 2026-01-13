# 开源项目推荐 

说明：本目录新增了一个简单的 Flask 封装（`app.py`）和一个有炫酷特效的前端页面（`前端设计.html`），用于调用工作区中 `smartreporecommend` 中的 `SmartRepoRecommender`，运行需求参考`requirements.txt`,top_300项目数据网盘链接：通过网盘分享的文件：top300_20_23log.7z
链接: https://pan.baidu.com/s/1cmgWPun7EoOJtJ6uB6EP7w?pwd=k5ri 提取码: k5ri。

运行步骤：

1. 建议创建并激活 Python 虚拟环境：

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. 启动服务：

```powershell
python app.py
```

1. 打开浏览器访问：http://127.0.0.1:5000/ ，在界面输入 GitHub Token（可选）和用户名，点击“开始推荐”。

注意：
- `smartreporecommmond.py` 必须位于同一目录或可被 Python 导入的位置（当前项目根目录下已存在）。
- 如果 `smartreporecommend.generate_recommendation` 在执行时有外部网络请求或依赖本地数据文件，第一次请求可能较慢。
