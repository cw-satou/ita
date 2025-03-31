from flask import render_template, request, session
from rockpaperscissor import app
import random  # 乱数を生成するためのモジュールをインポート

# じゃんけんゲームの開始処理
# '/start' にアクセスしたときの処理（GETメソッドのみ許可）
@app.route('/start', methods=['GET'])
def start():
    # セッション情報を削除（前回のゲーム結果をリセット）
    session.pop("wins", None)
    session.pop("losses", None)
    session.pop("draws", None)

    # 勝敗カウントを初期化
    session['wins'] = 0
    session['losses'] = 0
    session['draws'] = 0

    # じゃんけんゲームの初期画面表示
    return render_template('game.html')

# じゃんけんのプレイ処理
# '/play' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/play', methods=['POST'])
def play():
    # フォームから送信されたプレイヤーの手（グー:0、チョキ:1、パー:2）を取得
    playerHand = request.form['playerHand']

    # 勝敗判定関数を呼び出して、結果を取得
    onceResult = onceGame(playerHand)

    # セッション内の勝敗カウントを更新
    result = ""
    if onceResult == 0:  # プレイヤーの勝ち
        session['wins'] = session.get("wins") + 1
        result = "あなたの勝ちです！"
    elif onceResult == 1:  # プレイヤーの負け
        session['losses'] = session.get("losses") + 1
        result = "あなたの負けです。"
    else:  # 引き分け
        session['draws'] = session.get("draws") + 1
        result = "引き分けです。"

    # 勝敗結果を渡して表示
    return render_template('game.html', onceResult=result)

# ゲーム終了処理
# '/finish' にアクセスしたときの処理（POSTメソッドのみ許可）
@app.route('/finish', methods=['POST'])
def finish():
    # セッションから最終的な勝敗カウントを取得
    wins = session.get("wins")
    losses = session.get("losses")
    draws = session.get("draws")

    # セッション情報を削除（新しいゲームを始められるようにする）
    session.pop("wins", None)
    session.pop("losses", None)
    session.pop("draws", None)

    # ゲーム結果（勝敗回数）を表示
    return render_template('result.html', wins=wins, losses=losses, draws=draws)

# じゃんけんの勝敗を判定する関数
def onceGame(playerHand):
    # プレイヤーの手を整数に変換（HTMLフォームでは文字列として送信されるため）
    playerHand = int(playerHand)

    # コンピュータの手をランダムに決定（0: グー、1: チョキ、2: パー）
    computerHand = random.randint(0, 2)

    # 勝敗結果を格納する変数（2: 引き分け、0: プレイヤー勝利、1: プレイヤー敗北）
    onceResult = 2

    # じゃんけんの勝敗ルールに基づいて判定
    if playerHand == computerHand:
        onceResult = 2  # 引き分け
    elif ((playerHand == 0 and computerHand == 1) or
          (playerHand == 1 and computerHand == 2) or
          (playerHand == 2 and computerHand == 0)):
        onceResult = 0  # プレイヤーの勝ち
    else:
        onceResult = 1  # プレイヤーの負け

    return onceResult
