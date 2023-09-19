from flask import Flask, render_template, request
from flask import redirect, url_for, jsonify
from defs import *
app = Flask(__name__)
app.secret_key = b'e8896925b5cf99fbeae289fc187d047e391b536f8224e37a8859b64e6'


@app.route('/', methods = ['GET'])
def urllogin():
    return redirect(url_for('login_in'))

@app.route('/index', methods = ['GET'])
def index():
    # 检查请求是否来自 /login_in
    referrer = request.referrer
    if referrer == request.host_url + 'login_in':
        return render_template('game.html', session=session)
    
    # 其他情况下重定向到 /login_in
    return redirect(url_for('login_in'))


@app.route('/game', methods = ['POST'])
def game():
    print('/game')
    button_index = request.form['buttonvalue']
    print(button_index)
    deal_post(int(button_index))
    print('chuli')
    response_data = {
        'nums': session['nums'],
        'selectedposition': session['selectedposition']
    }    
    return jsonify(response_data)


@app.route('/login_in', methods = ['GET', 'POST'])
def login_in():
    if request.method == 'POST':
        subject = request.form.get('subject')
        # 创建记录被试的文件夹
        create_recording(subject=subject)
        # 初始化session
        session_init(subject)
        # 重定向
        return redirect(url_for('index'))

    return render_template('login.html')




if __name__ == '__main__':
    #print(Flask.secret_key )
    app.run(host='0.0.0.0',port=5001, debug=True)