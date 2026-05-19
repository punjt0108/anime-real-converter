import streamlit as st

st.set_page_config(page_title="二次元真人化工具")

st.title("二次元真人化工具")

uploaded_file = st.file_uploader(
    "上傳二次元圖片",
    type=["png","jpg","jpeg","webp"]
)

if uploaded_file:
    st.image(
        uploaded_file,
        caption="你上傳的圖片"
    )

style = st.text_area(
    "想轉換成什麼樣子？",
    value="請轉換成亞洲真人風格，保留原本角色特徵"
)

if st.button("開始轉換"):
    st.success("未來真人化會從這裡開始執行")

edit = st.text_area(
    "後續修改文字",
    placeholder="例如：淺棕色長髮、高馬尾、眼神溫柔"
)

if st.button("再次修改"):
    st.success("未來會根據文字修改圖片")
