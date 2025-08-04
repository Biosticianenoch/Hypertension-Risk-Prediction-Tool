# 🩺 Hypertension Risk Prediction App  
**Empowering prevention through prediction.**  

[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-blue?logo=streamlit)](https://streamlit.io)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)  
[![Made with ❤️ in Africa](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F%20in%20Africa-red)](https://github.com/enockbereka)  

---

![Banner](https://img.freepik.com/premium-vector/hypertension-banner-design-high-blood-pressure-medical-illustration_625536-94.jpg)

> 🚀 **Live App**: [Launch Here](https://your-streamlit-app-link)

---

## 💡 Overview

The **Hypertension Risk Prediction App** is a powerful machine learning-powered web app that enables users to evaluate their risk of developing high blood pressure based on clinical and lifestyle data. Built using Python and Streamlit, the tool offers a seamless, intuitive interface for both public users and health professionals.

---

## ✨ Key Features

✅ **Predict Hypertension Risk** using a trained ML model (XGBoost)  
📊 **Real-time analysis** with personalized feedback  
💡 **Intelligent Recommendations** based on predicted risk level  
📈 **Visitor analytics dashboard**  
🔐 **Privacy-focused**: No data stored or shared  
🧾 **Data citation for research use**  
📱 **Mobile-friendly and responsive design**

---

## 🧠 How It Works

1. Users input data such as age, BMI, BP, cholesterol, and lifestyle habits.
2. The model processes the data using a trained classifier.
3. Results are displayed instantly along with tailored lifestyle advice.
4. Data and usage logs (non-personal) are aggregated for analytics.

---

## 🧪 Model Info

- Algorithm: **XGBoost Classifier**
- Framework: `scikit-learn`, `numpy`, `streamlit`
- Input Features:
  - Age
  - BMI
  - Systolic & Diastolic BP
  - Cholesterol
  - Smoking Status
  - Exercise Level
  - Medication
  - Family History

> ⚠️ Note: The model was trained on anonymized clinical data and is **not a substitute for medical advice**.

---

## 🖥️ Screenshots

| 📥 Prediction Form | 📊 Output Risk & Advice | 📚 Data Citation Page |
|-------------------|------------------------|------------------------|
| ![](https://i.imgur.com/HEwzpPc.png) | ![](https://i.imgur.com/MDr06Vq.png) | ![](https://i.imgur.com/n8gZgPq.png) |

---

## 📚 Dataset & Citation

This app uses the following dataset:

**Mia D. (2023)** – *Hypertension Risk Prediction Dataset*  
🔗 [View on Kaggle](https://www.kaggle.com/datasets/miadul/hypertension-risk-prediction-dataset)

```bibtex
@dataset{mia2023hypertension,
  author = {Mia D.},
  title = {Hypertension Risk Prediction Dataset},
  year = {2023},
  url = {https://www.kaggle.com/datasets/miadul/hypertension-risk-prediction-dataset}
}
```

---

## 📦 Installation & Setup

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/hypertension-app.git
cd hypertension-app
```

2. **Install dependencies**  
```bash
pip install -r requirements.txt
```

3. **Run the application**  
```bash
streamlit run streamlit_app.py
```

> 🛠 Don’t forget to place `hypertension_xgb_model.sav` in the app root directory.

---

## 🧰 Technologies Used

| Category        | Tech Stack |
|----------------|------------|
| Frontend       | Streamlit, HTML, CSS |
| Backend        | Python, XGBoost, Scikit-learn |
| Data Handling  | NumPy, Pickle |
| Visualization  | Streamlit Components |
| Hosting        | Streamlit Cloud |

---

## 🚀 Deployment

Deploy your own version in just a few clicks using:

- 🌐 [Streamlit Cloud](https://streamlit.io/cloud)
- 🐳 Docker (optional)
- 🧑‍💻 GitHub Pages (for docs)

---

## 🤝 Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/awesome-feature`
3. Commit changes: `git commit -m 'Add some feature'`
4. Push and open a pull request

> 📩 For major contributions, contact us directly via [email](mailto:enochosenwafulah@gmail.com)

---

## 📜 License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

---

## 🙋‍♂️ Developer & Contact

**Enock Bereka** – Health Data Scientist | CEO, DataQuest Solutions  
📧 [enochosenwafulah@gmail.com](mailto:enochosenwafulah@gmail.com)  
🌐 [DataQuest Solutions](https://your-website-link)  
📱 [+254701344230](https://wa.me/254701344230)

---

## ⭐ Support

If you like this project:

- 🌟 Star the repo
- 🍴 Fork it
- 🧠 Share with fellow researchers and med-tech enthusiasts
- 🤝 Let's collaborate to advance AI in African healthcare

---

> “Prevention is better than cure — and prediction is the new prevention.” 🧬
