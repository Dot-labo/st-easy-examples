import streamlit as st

# セッションの初期化
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0  # 現在の問題番号
if 'score' not in st.session_state:
    st.session_state.score = 0  # 正解数

# クイズのデータ
questions = [
    {"No": 1, "question": "地球は何番目の惑星？", "options": ["1", "3", "5"], "answer": "3"},
    {"No": 2, "question": "りんごは何色？", "options": ["赤", "青", "黄色"], "answer": "赤"}
]

st.title("クイズゲーム 🎮")

# 現在の問題を取得
if st.session_state.current_question < len(questions):
    question = questions[st.session_state.current_question]

    # 問題を表示
    st.write(f"問題 {question['No']} : {question['question']}")
    answer = st.radio("答えを選んでね", question["options"], key=f"q_{question['No']}")

    # 答え合わせボタン
    if st.button("答え合わせ"):
        if answer == question["answer"]:
            st.success("正解！✨")
            st.balloons()
            st.session_state.score += 1  # スコアを加算
        else:
            st.error("不正解！💦")
        
        # 次の問題へ進む
        st.session_state.current_question += 1
        st.rerun()
else:
    # 全ての問題が終わった場合
    st.write(f"クイズ終了！あなたのスコアは {st.session_state.score}/{len(questions)} 点です 🎉")
    if st.button("もう一度遊ぶ"):
        # セッションをリセット
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.rerun()
