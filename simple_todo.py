import streamlit as st
import os

# ファイル名
TODO_FILE = "todo_list.txt"

# ファイルからTODOリストを読み込み, リストにして返す
def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return f.read().splitlines()
    else:
        return []

# TODOリストをファイルに保存
def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        f.write("\n".join(todos))

# 初期化
st.title("かんたんTODOリスト ✅")
todo_list = load_todos()

# TODOの追加
new_todo = st.text_input("新しいTODOを入力してください")
if st.button("追加"):
    if new_todo:
        todo_list.append(new_todo)
        save_todos(todo_list)
        st.success(f"'{new_todo}' を追加しました！")
        st.rerun()

# TODOリストの表示と削除
if todo_list:
    st.write("### 現在のTODOリスト")
    for i, todo in enumerate(todo_list): #enumerateを使うと、リストの要素とインデックスを同時に取得できる
        st.write(f"- {todo}")
        if st.button("チェック ✅", key=f"check-{i}"):
            todo_list.pop(i)
            save_todos(todo_list)
            st.success(f"'{todo}' を削除しました！")
            st.rerun()
        st.write("---")
else:
    st.write("TODOリストが空です！何かやることを追加してみましょう！ ✍️")
