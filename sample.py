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

# f文字列(f"...")を使うと変数を{}の中に埋め込める
print(f"名前: {name}, 年齢: {age}, スコア: {score}, 会員: {is_member}")
# 出力 → 名前: Alice, 年齢: 20, スコア: 85.5, 会員: True


# --- if 文 ---
# 条件によって処理を分岐させる。
# if → elif → else の順に評価され、最初に True になったブロックだけ実行される。
# score = 85.5 なので「score >= 70」が True → "評価: A" が出力される。

print("\n--- if 文 ---")
if score >= 90:
    print("評価: S")       # score が 90以上なら実行(今回はスキップ)
elif score >= 70:
    print("評価: A")       # ← score=85.5 はここに該当 → 出力される
elif score >= 50:
    print("評価: B")       # 上の elif が True なのでスキップ
else:
    print("評価: C")       # すべて False のときだけ実行
# 出力 → 評価: A


# --- for 文 ---
# リスト(配列)などの要素を1つずつ取り出して繰り返し処理する。
# fruit に "りんご"→"バナナ"→"みかん" の順に入り、3回ループする。

print("\n--- for 文 ---")
fruits = ["りんご", "バナナ", "みかん"]

for fruit in fruits:
    print(f"フルーツ: {fruit}")
# 出力 →
#   フルーツ: りんご
#   フルーツ: バナナ
#   フルーツ: みかん


# --- range() と for 文 ---
# range(5) は 0,1,2,3,4 の5つの数値を順番に生成する(5は含まれない)。
# i に 0→1→2→3→4 が順番に入り、5回ループする。

print("\n--- range() と for 文 ---")
for i in range(5):
    print(f"  {i} 番目のループ")
# 出力 →
#   0 番目のループ
#   1 番目のループ
#   2 番目のループ
#   3 番目のループ
#   4 番目のループ


# --- 組み合わせ例: 合格者リストを作る ---
# 変数・if文・for文をすべて組み合わせた実用的な例。
# 辞書のリストを for でループしながら、if でスコアを判定する。

print("\n--- 組み合わせ例 ---")
students = [
    {"name": "Alice", "score": 92},   # 92 >= 60 → 合格
    {"name": "Bob",   "score": 58},   # 58 <  60 → 不合格
    {"name": "Carol", "score": 75},   # 75 >= 60 → 合格
    {"name": "Dave",  "score": 43},   # 43 <  60 → 不合格
]

passing_score = 60  # 合格ライン

for student in students:
    # student には毎ループ1人分の辞書が入る
    # 例: {"name": "Alice", "score": 92}
    if student["score"] >= passing_score:
        result = "合格"
    else:
        result = "不合格"
    print(f"{student['name']}: {student['score']}点 → {result}")
# 出力 →
#   Alice: 92点 → 合格
#   Bob: 58点 → 不合格
#   Carol: 75点 → 合格
#   Dave: 43点 → 不合格
