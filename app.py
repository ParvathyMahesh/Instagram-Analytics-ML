import streamlit as st
import joblib
import numpy as np
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="📊 Instagram Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

add_bg_from_local("Instagram.png")

scaler = joblib.load("scalar.pkl")  
model = joblib.load("RandomForestRegressor_Model.pkl")

if "reset_id" not in st.session_state:
    st.session_state.reset_id = 0


st.markdown("<h1 style='text-align:center; color:Purple;'>📊 Instagram Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")
st.sidebar.markdown("### 📌 About This Dashboard")
st.sidebar.info("""This Instagram Analytics Dashboard predicts the engagement rate of your posts using a trained RandomForest ML model.

**How It Works:**  
- Enter post metrics such as likes, comments, shares, saves, reach, impressions, hashtags used, and followers gained.  
- Click **Predict** to estimate the engagement rate of your post.  

**Tips for Better Engagement:**  
- Post at times when your audience is most active  
- Use relevant and trending hashtags  
- Engage with your followers in comments  
- Share content consistently and creatively  

**Disclaimer:**  
Predictions are based on historical data and a machine learning model. They are **estimates only** and may not always reflect actual engagement.
""")

st.subheader("📥 Enter Post Analytics")
st.caption("Fill in the post metrics and click Predict to estimate engagement rate.")



with st.form(f"engagement_form_{st.session_state.reset_id}"):
    col1, col2 = st.columns(2)
    with col1:
        likes = st.number_input("👍 ****Likes****", min_value = 0)
        comments = st.number_input("💬 ****Comments****", min_value = 0)
        shares = st.number_input("🔁 ****Shares****", min_value = 0)
        saves = st.number_input("💾 ****Saves****", min_value = 0)
    with col2:    
        reach = st.number_input("👀 ****Reach (Unique Accounts)****", min_value = 0)
        impressions = st.number_input("👁 ****Impressions (Total Views)****", min_value = 1)
        hashtag_count = st.number_input("🏷 ****Hashtag Count****", min_value = 0)
        followers_gained = st.number_input("➕ ****Followers Gained****", min_value = 0)
    predict = st.form_submit_button("🚀 Predict")


    if predict:
        if all([likes==0, comments==0, shares==0, saves==0, reach==0, impressions==1, hashtag_count==0, followers_gained==0]):
            st.warning("⚠️ Please enter some metrics before predicting.")
        else:
            features = np.array([[likes,comments,shares,saves,reach,impressions,hashtag_count,followers_gained]])
            features_scaled = scaler.transform(features)
            prediction = model.predict(features_scaled)
            engagement = prediction[0]
            if engagement <= 10:
                st.warning(f"🔴 Low Engagement Rate: **{engagement:.4f}**")
                st.caption("This post may need better content, timing, or hashtags.")
            elif engagement <= 25:
                st.info(f"🟡 Average Engagement Rate: **{engagement:.4f}**")
                st.caption("Good performance, but there’s room to optimize.")
            else:
                st.success(f"🟢 High Engagement Rate: **{engagement:.4f}**")
                st.caption("Great job! This post is performing very well.")



if st.button("🔄 Reset Form",use_container_width=True):
    st.session_state.reset_id += 1
    st.rerun()



