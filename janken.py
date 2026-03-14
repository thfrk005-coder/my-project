# =============================================
# じゃんけんゲーム
# 使用するPython機能: import / 変数 / リスト /
#                     関数 / if文 / for文 / input()
# =============================================

import random  # ランダムな値を生成するための標準ライブラリ


# --- 定数定義 ---
# じゃんけんの手をリストで管理する。
# インデックス: 0=グー, 1=チョキ, 2=パー

HANDS = ["グー", "チョキ", "パー"]
# ゲームを何回行うか
ROUNDS = 3


# --- 関数: 勝敗判定 ---
# 関数とは「処理をひとまとめにして名前をつけたもの」。
# def 関数名(引数1, 引数2): で定義し、return で値を返す。

def judge(player, cpu):
    """プレイヤーとCPUの手を受け取り、勝敗を返す関数。"""
    if player == cpu:
        return "引き分け"                    # 同じ手なら引き分け
    elif (player == "グー"   and cpu == "チョキ") or \
         (player == "チョキ" and cpu == "パー")  or \
         (player == "パー"   and cpu == "グー"):
        return "あなたの勝ち"               # プレイヤーが勝つパターン
    else:
        return "CPUの勝ち"                  # それ以外はCPUの勝ち


# --- メインループ ---
# for文で ROUNDS 回(3回)繰り返す。
# range(1, ROUNDS + 1) → 1, 2, 3 の連番を生成。

print("=============================")
print("    じゃんけんゲーム スタート！")
print(f"    全{ROUNDS}回戦")
print("=============================\n")

# スコアを記録する変数（ループ前に 0 で初期化）
player_score = 0
cpu_score    = 0
draw_count   = 0

for round_num in range(1, ROUNDS + 1):   # 1, 2, 3 の順でループ
    print(f"--- 第{round_num}回戦 ---")

    # プレイヤーに手を選ばせる
    # input() はキーボード入力を受け取り、文字列として返す
    print("手を入力してください: グー / チョキ / パー")
    player_hand = input("> ").strip()     # strip() で前後の空白を除去

    # 入力値のバリデーション(正しい手かチェック)
    if player_hand not in HANDS:
        print(f"「{player_hand}」は無効な入力です。グーを選んだことにします。\n")
        player_hand = "グー"              # 無効入力時はグーに固定

    # CPUの手をランダムに選ぶ
    # random.choice(リスト) → リストからランダムに1つ取り出す
    cpu_hand = random.choice(HANDS)

    print(f"あなた: {player_hand}  vs  CPU: {cpu_hand}")

    # 勝敗判定(関数を呼び出す)
    result = judge(player_hand, cpu_hand)
    print(f"結果: {result}\n")

    # スコアを更新
    if result == "あなたの勝ち":
        player_score += 1                 # += 1 は player_score = player_score + 1 と同じ
    elif result == "CPUの勝ち":
        cpu_score += 1
    else:
        draw_count += 1


# --- 最終結果表示 ---
# ループが終わったら合計スコアを表示する。

print("=============================")
print("         最終結果")
print("=============================")
print(f"あなた: {player_score}勝  CPU: {cpu_score}勝  引き分け: {draw_count}回")

# 総合勝敗の判定
if player_score > cpu_score:
    print("★ 総合: あなたの勝ちです！おめでとう！")
elif player_score < cpu_score:
    print("★ 総合: CPUの勝ちです。またチャレンジ！")
else:
    print("★ 総合: 引き分けです！")
