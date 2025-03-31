from flask import render_template
from bootstrapsamples import app

# "/" にアクセスしたときの処理
@app.route('/')
def index():
    return render_template('index.html')

# "/sample01" にアクセスしたときの処理
@app.route('/sample01')
def sample01():
    return render_template('sample01.html')

# "/sample02" にアクセスしたときの処理
@app.route('/sample02')
def sample02():
    return render_template('sample02.html')

# "/sample03" にアクセスしたときの処理
@app.route('/sample03')
def sample03():
    return render_template('sample03.html')

# "/sample04" にアクセスしたときの処理
@app.route('/sample04')
def sample04():
    return render_template('sample04.html')

# "/c_navbar" にアクセスしたときの処理
@app.route('/c_navbar')
def c_navbar():
    return render_template('c_navbar.html')

# "/c_buttons" にアクセスしたときの処理
@app.route('/c_buttons')
def c_buttons():
    return render_template('c_buttons.html')

# "/c_forms" にアクセスしたときの処理
@app.route('/c_forms')
def c_forms():
    return render_template('c_forms.html')

# "/c_tables" にアクセスしたときの処理
@app.route('/c_tables')
def c_tables():
    return render_template('c_tables.html')
