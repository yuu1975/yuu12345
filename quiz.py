import streamlit as st
import random
from PIL import Image

# 漢字と花の名前の辞書
KANJI_YOMI = {
    "紫陽花": "アジサイ",
    '向日葵': 'ヒマワリ',
    '蒲公英': 'タンポポ',
    '竜胆': 'リンドウ',
    '仏桑花':'ハイビスカス',
    '花車':'ガーベラ',
    '石楠花':'シャクナゲ',
    '風信子':'ヒヤシンス',
    '木春菊':'マーガレット',
    '孔雀草':'マリーゴールド'
}

def get_random_kanji():
    return random.choice(list(KANJI_YOMI.keys()))

def change_session():
  st.session_state["input"]=""
  st.session_state.status=0

st.title("漢字クイズ 花の名前わかるかな？")

if 'status' not in st.session_state: 
	st.session_state.status = 0 

if st.session_state.status == 0: 
    current_kanji = get_random_kanji()
    st.session_state.corrent_kanji = current_kanji
else:
    current_kanji = st.session_state.corrent_kanji 

st.write(f"## {current_kanji}")
st.session_state.user_input = st.text_input("花の名前をカタカナで入力してEnterを押してね",key= "input")

if st.session_state.status == 0: 
    st.session_state.status = 1

if st.button("答え"):
    correct_yomi = KANJI_YOMI[st.session_state.corrent_kanji]
    if st.session_state.user_input == correct_yomi:
        st.success("正解！")
        img = Image.open(correct_yomi+'.jpg')
        st.image(img)
        st.session_state.status=2
    else:
        st.error("残念！！")
        st.write(f"正解は {correct_yomi}だよ。")
        st.session_state.status=2

if st.session_state.status == 2 :
    st.button("次の問題へ",on_click=change_session)

