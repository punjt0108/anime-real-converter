import streamlit as st

st.set_page_config(page_title="二次元真人化提示詞工具", page_icon="✨")

st.title("二次元真人化提示詞工具")
st.caption("免費版：產生提示詞後，回到 ChatGPT 上傳圖片使用。")

uploaded_file = st.file_uploader(
    "上傳參考圖片，這裡只做預覽，不會送出扣費",
    type=["png", "jpg", "jpeg", "webp"]
)

if uploaded_file:
    st.image(uploaded_file, caption="參考圖片預覽", use_container_width=True)

st.subheader("角色基本設定")

age = st.selectbox("年齡設定", ["20歲", "22歲", "24歲", "26歲", "30歲", "35歲"])
style = st.selectbox("真人風格", ["台灣女性", "亞洲女性", "日系寫實", "韓系寫實"])
hair_color = st.selectbox("髮色", ["保留原髮色", "淺棕色", "深棕色", "黑色", "亞麻棕"])
hair_style = st.selectbox("髮型", ["保留原髮型", "高馬尾", "長直髮", "微捲長髮", "短髮", "公主頭"])
expression = st.selectbox("神情", ["保留原神情", "甜美可愛", "氣質溫柔", "俏皮淘氣", "成熟嫵媚", "曖昧迷人"])
photo_style = st.selectbox("攝影風格", ["自然寫實攝影", "高級人像攝影", "電影感光影", "日系清新寫真", "韓系雜誌風"])

st.subheader("常用角色模式")

mode = st.radio(
    "套用模式",
    ["一般模式", "Vivi模式", "Joan模式"]
)

extra = st.text_area(
    "其他補充要求",
    placeholder="例如：背景改成台北街景、服裝保留原設計、眼神更溫柔、不要歐美臉",
    height=100
)

base_prompt = f"""
請將我上傳的二次元圖片轉換為真人圖像風格。

角色設定：
- 年齡：{age}
- 風格：{style}
- 髮色：{hair_color}
- 髮型：{hair_style}
- 神情：{expression}
- 攝影風格：{photo_style}

請保留原角色的核心辨識特徵，包括臉型輪廓、髮型結構、表情氣質、服裝元素與整體氛圍。
請轉換為真實自然的人像攝影效果，膚質自然、五官真實、光線柔和。
避免動漫線條、塑膠感、過度修圖、歐美臉或臉部失真。
"""

if mode == "Vivi模式":
    base_prompt += """
角色偏向 Vivi 風格：甜美、俏皮、青春活潑、鄰家女孩氣質，神情帶有可愛淘氣感。
"""

elif mode == "Joan模式":
    base_prompt += """
角色偏向 Joan 風格：氣質清新、知性自然、成熟溫柔，整體呈現都會女性的人像質感。
"""

if extra.strip():
    base_prompt += f"""

額外要求：
{extra}
"""

st.subheader("產生提示詞")

if st.button("產生提示詞"):
    st.text_area(
        "複製下面這段，回到 ChatGPT 上傳圖片後貼上",
        value=base_prompt.strip(),
        height=360
    )

    st.success("提示詞已產生。複製後回到 ChatGPT 使用即可。")
