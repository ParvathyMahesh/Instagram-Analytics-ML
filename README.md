# 📊 Instagram Analytics – Engagement Rate Prediction

This project is a **Machine Learning–based Instagram Analytics system** that predicts the **Engagement Rate** of Instagram posts using post-level metrics.  
The model is deployed as an **interactive Streamlit dashboard** for real-time predictions.

---

## 🚀 Project Highlights
- Predicts Instagram post engagement rate
- Built using **Random Forest Regressor**
- Interactive **Streamlit dashboard**
- Realistic dataset with **30,000 Instagram posts**
- Supports multiple content types: Reels, Photos, Videos, Carousels

---

## 🧠 Machine Learning Model
- **Algorithm:** Random Forest Regressor
- **Why Random Forest?**
  - Handles large datasets efficiently
  - Captures non-linear relationships
  - Robust to noisy social media data
  - Faster and more stable than KNN and SVR for large datasets

---

## 📂 Dataset Overview
- 30,000 simulated Instagram posts
- Features include:
  - Likes
  - Comments
  - Shares
  - Saves
  - Reach
  - Impressions
  - Hashtag Count
  - Followers Gained
- **Target Variable:** Engagement Rate

---

## 📈 Model Evaluation
Multiple regression models were trained and evaluated using:
- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Cross-Validation Score

### 🏆 Best Model
- **Random Forest Regressor**
- Highest R² score
- Lowest prediction error
- Strong generalization without overfitting

---

## 🖥 Streamlit Dashboard
Users can input post metrics such as:
- Likes
- Comments
- Shares
- Saves
- Reach
- Impressions
- Hashtag Count
- Followers Gained

### Output:
- 🔴 Low Engagement
- 🟡 Average Engagement
- 🟢 High Engagement

---

## ▶️ Run the Application Locally

```bash
pip install -r requirements.txt
streamlit run app.py
