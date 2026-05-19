import base64
from io import BytesIO
from PIL import Image
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="二次元真人化工具")
st.title("二次元真人化工具")

uploaded_file = st.file_uploader("上傳二次元圖片", type=["png", "jpg", "jpeg", "webp"])

prompt = st.text_area(
    "想轉換成什麼樣子？",
    value="請將上傳圖片轉換為亞洲真人寫實風格，保留原角色的核心辨識特徵、髮型輪廓、表情氣質與服裝元素。自然膚質、真實五官、柔和光線，不要保留動漫線條。"
)

def to_png_file(image_bytes, name="image.png"):
    img = Image.open(BytesIO(image_bytes)).convert("RGB")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    buffer.name = name
    return buffer

def edit_image(image_bytes, prompt_text):
    img_file = to_png_file(image_bytes)

    result = client.images.edit(
        model="gpt-image-1",
        image=img_file,
        prompt=prompt_text,
        size="auto"
    )

    return base64.b64decode(result.data[0].b64_json)

if uploaded_file:
    original_bytes = uploaded_file.getvalue()
    st.image(original_bytes, caption="原始圖片")

    if st.button("開始轉換"):
        with st.spinner("真人化轉換中..."):
            st.session_state["result_image"] = edit_image(original_bytes, prompt)
        st.rerun()

if "result_image" in st.session_state:
    st.subheader("轉換結果")
    st.image(st.session_state["result_image"])

    edit_prompt = st.text_area(
        "後續修改文字",
        placeholder="例如：改成淺棕色長髮、高馬尾、眼神更溫柔"
    )

    if st.button("再次修改"):
        with st.spinner("依照文字修改中..."):
            st.session_state["result_image"] = edit_image(
                st.session_state["result_image"],
                edit_prompt
            )
        st.rerun()

    st.download_button(
        "下載圖片",
        data=st.session_state["result_image"],
        file_name="realistic_result.png",
        mime="image/png"
    )
