# 🌟 Amazon product Review Sentiment Analyzer (Streamlit App)

A machine-learning powered **Sentiment Analysis Web App** built using **Streamlit**.  
This app predicts whether an Amazon Alexa product review is **Positive** or **Negative** using trained ML models.

---

## 📁 Project Structure

```
.
├── Data/
│   ├── Predictions.csv
│   ├── SentimentBulk.csv
│   ├── amazon_alexa.tsv
│   └── Models/
│       ├── countVectorizer.pkl
│       ├── model_dt.pkl
│       ├── model_rf.pkl
│       ├── model_xgb.pkl
│       └── scaler.pkl
│
├── templates/
│   ├── index.html
│   └── landing.html
│
├── Data Exploration & Modelling.ipynb
├── main.py
├── api.py
├── requirements.txt
└── README.md
```

---

## 🧩 Introduction

This project performs **sentiment classification** on Amazon Alexa customer reviews.  
A trained ML model (Random Forest, Decision Tree, XGBoost) predicts the sentiment using:

- Count Vectorizer  
- Text preprocessing (cleaning, tokenization)  
- Scaler for normalization  

A **Streamlit interface** allows users to enter text and receive instant predictions.

---

## ✨ Features

✔ Real-time sentiment prediction  
✔ Bulk CSV prediction support  
✔ Multiple trained ML models  
✔ Clean UI built with Streamlit  
✔ Pre-loaded vectorizer & scaler for accuracy  
✔ Jupyter Notebook for EDA & training  

---

## 🛠 Tech Stack

- **Python 3.x**
- **Streamlit**
- **Scikit-learn**
- **XGBoost**
- **Pandas / NumPy**
- **Pickle for loading models**

---

## ⚙ Installation

Clone the project:

```bash
git clone https://github.com/yourusername/alexa-sentiment-streamlit.git
cd alexa-sentiment-streamlit
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Streamlit App

```bash
streamlit run main.py
```

This opens the app in browser:

```
h
```

---

## 🖥 How the App Works

1. User enters a review in the text box  
2. Text is cleaned and transformed using `countVectorizer.pkl`  
3. The model (`model_rf.pkl`, `model_dt.pkl`, or `model_xgb.pkl`) makes prediction  
4. The Streamlit UI displays:

- **Positive 😄**
- **Negative 😞**

5. Optional: Upload CSV for bulk predictions

---

## 📊 File Descriptions

| File | Description |
|------|-------------|
| `main.py` | Streamlit app for UI & prediction |
| `api.py` | Optional Flask API for external POST requests |
| `countVectorizer.pkl` | Pretrained vectorizer |
| `model_rf.pkl`, `model_dt.pkl`, `model_xgb.pkl` | Trained ML models |
| `Predictions.csv` | Output sample |
| `amazon_alexa.tsv` | Raw dataset |
| `Data Exploration & Modelling.ipynb` | Notebook for training/EDA |

---


### **Render / HuggingFace Spaces**  
Streamlit is supported out-of-the-box.

---

## 🧪 Future Enhancements

- Add BERT / DistilBERT for advanced NLP  
- Add dark mode UI  
- Multi-class sentiment (Very Positive → Very Negative)  
- Dashboard for analytics  

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 🤝 Contributing

Contributions, issues and suggestions are welcome!


