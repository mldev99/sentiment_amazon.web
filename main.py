import streamlit as st
import pandas as pd
import requests
from io import BytesIO

# If the Flask API is unreachable (e.g. when deployed separately),
# import the local prediction function as a fallback so Streamlit can
# run predictions without a network call.
try:
    from api import predict_sentiment
except Exception:
    predict_sentiment = None

# flask --app api.py run --port=5000
prediction_endpoint = "http://127.0.0.1:5000/predict"

st.title("Text Sentiment Predictor")

uploaded_file = st.file_uploader(
    "Choose a CSV file for bulk prediction - Upload the file and click on Predict",
    type="csv",
)

# Text input for sentiment prediction
user_input = st.text_input("Enter text and click on Predict", "")

# Prediction on single sentence
if st.button("Predict"):
    if uploaded_file is not None:
        # Try API first, then fallback to local prediction if it fails
        try:
            file = {"file": uploaded_file}
            response = requests.post(prediction_endpoint, files=file, timeout=5)
            response.raise_for_status()
            response_bytes = BytesIO(response.content)
            response_df = pd.read_csv(response_bytes)

            st.download_button(
                label="Download Predictions",
                data=response_bytes,
                file_name="Predictions.csv",
                key="result_download_button",
            )
        except requests.exceptions.RequestException:
            st.warning("Prediction API unreachable — running predictions locally.")
            try:
                df = pd.read_csv(uploaded_file)
                if predict_sentiment is None:
                    st.error("Local prediction function not available. Make sure API or local models exist.")
                else:
                    df["Predicted"] = df["Sentence"].apply(lambda x: predict_sentiment(x))
                    buf = BytesIO()
                    df.to_csv(buf, index=False)
                    buf.seek(0)
                    st.download_button(
                        label="Download Predictions (local)",
                        data=buf,
                        file_name="Predictions_local.csv",
                        key="local_result_download_button",
                    )
            except Exception as e:
                st.error(f"Local prediction failed: {e}")

    else:
        # Single-text prediction: prefer JSON to match the Flask API
        try:
            response = requests.post(prediction_endpoint, json={"text": user_input}, timeout=5)
            response.raise_for_status()
            response_json = response.json()
            # API returns {'result': ...}
            st.write(f"Predicted sentiment: {response_json.get('result')}")
        except requests.exceptions.RequestException:
            st.warning("Prediction API unreachable — running prediction locally.")
            if predict_sentiment is None:
                st.error("Local prediction function not available. Make sure API or local models exist.")
            else:
                try:
                    st.write(f"Predicted sentiment: {predict_sentiment(user_input)}")
                except Exception as e:
                    st.error(f"Local prediction failed: {e}")
