import streamlit as st
from datetime import datetime

st.title("秘密の日記 📖")
SECRET_PASSWORD = "sakunyan" #これが秘密の合言葉

# 合言葉入力
password = st.text_input("合言葉を入力してください", type="password") #type="password"で、隠された入力になる

# 日記の入力と保存
if password == SECRET_PASSWORD:
    st.success("合言葉が正解！日記を開くことができます!")

    try:
        with open("diary.txt", "r") as f:
            st.text(f.read())
    except:
        st.warning("まだ日記がありません！")

    diary_entry = st.text_area("今日の日記を書く:")
    if st.button("保存する"):
        with open("diary.txt", "a") as f:
            #datetime.now()は現在時刻を取得する関数。
            save_string = str(datetime.now()) + ": " + diary_entry + "\n" #日付と内容を文字列に追記
            f.write(save_string) #ファイルに書き込む
            st.success("日記が保存されました！")
        st.rerun() #ページを再実行
else:
    st.info("正しい合言葉を入力すると日記が見れます！")
