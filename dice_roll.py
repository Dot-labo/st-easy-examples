import random
import streamlit as st

st.title("ダイスを振ろう! 🎲")

dice_num = st.slider(label="ダイスはいくつ？", min_value=1, max_value=10)
dice_side = st.number_input(label="何面ダイス？", min_value=6, max_value=100)

if st.button("ダイスをロールする！"):
    dice_sum = 0
    for i in range(dice_num):
        result = random.randint(1, dice_side)
        dice_sum += result
        st.write(result)
    st.write(f"合計 {dice_sum}")