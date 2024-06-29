import streamlit as st
import numpy as np

st.title("英単語クイズ")

biginner_word_pairs = {
    "Apple": "りんご",
    "Dog": "犬",
    "Cat": "猫",
    "Book": "本",
    "School": "学校",
    "Car": "車",
    "Ball": "ボール",
    "Sun": "太陽",
    "Tree": "木",
    "Fish": "魚"
}

intermediate_words_pairs = {
    "Science": "科学",
    "History": "歴史",
    "Mathematics": "数学",
    "Geography": "地理",
    "Literature": "文学",
    "Biology": "生物学",
    "Physics": "物理学",
    "Chemistry": "化学",
    "Economics": "経済学",
    "Philosophy": "哲学"
}

advanced_words_pairs = {
    "Ephemeral": "儚い",
    "Ubiquitous": "遍在する",
    "Ostentatious": "派手な",
    "Equanimity": "平静",
    "Magnanimous": "寛大な",
    "Sagacious": "賢明な",
    "Perspicacious": "洞察力のある",
    "Tenacious": "粘り強い",
    "Assiduous": "勤勉な",
    "Perfunctory": "形式的な"
}


quiz_data_set = {
  "初級": biginner_word_pairs,
  "中級": intermediate_words_pairs,
  "上級": advanced_words_pairs
}

level = st.sidebar.radio("レベルを選択", ["初級","中級","上級"])
word_pairs = quiz_data_set[level]

if st.button("出題"):
  index = np.random.randint(0,9)
  english_word = list(word_pairs.keys())[index]
  st.markdown(f"## {english_word}")

  with st.expander("解答を見る"):
    japanese_word = word_pairs[english_word]
    st.write(f"## {japanese_word}")

if st.button("次の問題へ"):
  placeholder = st.empty()
  placeholder.empty()