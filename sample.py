# =============================================
# Pythonサンプル: 変数・if文・for文
# =============================================

# --- 変数 ---
# 変数とは、データを入れておく「箱」のようなもの。
# Python では型宣言不要で、代入するだけで使える。

name = "Alice"          # 文字列 (str)
age = 20                # 整数 (int)
score = 85.5            # 小数 (float)
is_member = True        # 真偽値 (bool)

print(f"名前: {name}, 年齢: {age}, スコア: {score}, 会員: {is_member}")


# --- if 文 ---
# 条件によって処理を分岐させる。
# if → elif → else の順に評価され、最初に True になったブロックだけ実行される。

print("\n--- if 文 ---")
if score >= 90:
    print("評価: S")
elif score >= 70:
    print("評価: A")
elif score >= 50:
    print("評価: B")
else:
    print("評価: C")


# --- for 文 ---
# リスト(配列)などの要素を1つずつ取り出して繰り返し処理する。

print("\n--- for 文 ---")
fruits = ["りんご", "バナナ", "みかん"]

for fruit in fruits:
    print(f"フルーツ: {fruit}")


# --- range() と for 文 ---
# range(n) で 0〜n-1 の連番を生成できる。

print("\n--- range() と for 文 ---")
for i in range(5):
    print(f"  {i} 番目のループ")


# --- 組み合わせ例: 合格者リストを作る ---
# 変数・if文・for文をすべて組み合わせた実用的な例。

print("\n--- 組み合わせ例 ---")
students = [
    {"name": "Alice", "score": 92},
    {"name": "Bob",   "score": 58},
    {"name": "Carol", "score": 75},
    {"name": "Dave",  "score": 43},
]

passing_score = 60  # 合格ライン

for student in students:
    if student["score"] >= passing_score:
        result = "合格"
    else:
        result = "不合格"
    print(f"{student['name']}: {student['score']}点 → {result}")
