from myproject import app

# "/" にアクセスしたときの処理
@app.route('/')
def index():
    # 画面に "Hello, world!" を表示
    return "Hello, world!"
