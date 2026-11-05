
# 🌱 Crop Recommendation System

A Machine Learning-based web application that recommends suitable crops based on soil nutrients and environmental conditions.

The system uses a Random Forest Classifier trained on agricultural data to predict the most suitable crop from the given input parameters.

## 🚀 Live Demo

Coming Soon

## 📌 Project Overview

Choosing the right crop based on soil and weather conditions is important for agricultural productivity.

This project uses Machine Learning to analyze soil nutrients and environmental parameters and recommend a suitable crop.

Users can enter soil and weather information through a simple Streamlit interface and receive an instant crop prediction.

## ✨ Features

- Crop prediction using Machine Learning.
- Random Forest Classification model.
- Seven input parameters.
- Interactive Streamlit web interface.
- Model probability display.
- Input validation and error handling.
- Exploratory Data Analysis and visualizations.
- Model evaluation using accuracy, classification report and confusion matrix.

## 🧪 Input Parameters

The model uses the following seven features:

| Parameter | Description |
|---|---|
| N | Nitrogen content in soil |
| P | Phosphorus content in soil |
| K | Potassium content in soil |
| Temperature | Temperature in Celsius |
| Humidity | Relative humidity |
| pH | Soil pH value |
| Rainfall | Rainfall in mm |

## 🤖 Machine Learning Workflow

1. Dataset collection
2. Data loading and exploration
3. Exploratory Data Analysis (EDA)
4. Data preprocessing
5. Train-test split
6. Random Forest model training
7. Model evaluation
8. Feature importance analysis
9. Hyperparameter tuning
10. Model serialization using Joblib
11. Streamlit application development

## 📊 Model Evaluation

The model was evaluated using:

- Accuracy Score
- Classification Report
- Confusion Matrix
- Feature Importance

| Metric | Result |
|---|---:|
| Accuracy | 99.95% |
| Number of Classes | 22 |
| Training Samples | 1760 |
| Testing Samples | 440 |

## 🛠️ Tech Stack

**Programming Language**
- Python

**Machine Learning & Data Analysis**
- Scikit-learn
- Pandas
- NumPy

**Data Visualization**
- Matplotlib
- Seaborn

**Web Application**
- Streamlit

**Model Storage**
- Joblib

## 📂 Project Structure

```text
Crop-Recommendation-System/
│
├── dataset/
│   └── Crop_recommendation.csv
│
├── notebooks/
│   └── crop_analysis.ipynb
│
├── models/
│   └── crop_model.pkl
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/raunak-collab/Crop-Recommendation-System.git
```

### 2. Navigate to the project directory

```bash
cd Crop-Recommendation-System
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the environment

**Windows:**

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

http://localhost:8501

## 📚 Dataset

Dataset: Crop Recommendation Dataset

Source: [Kaggle - Crop Recommendation Dataset](https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset)

The dataset contains soil nutrient values and environmental conditions for different crops.

## 🔮 Future Improvements

- Add more agricultural datasets.
- Improve model generalization.
- Add regional and seasonal crop recommendations.
- Provide detailed crop information.
- Deploy the application online.
- Improve UI and user experience.

## ⚠️ Disclaimer

This application is an educational Machine Learning project. Its predictions are based on the dataset used for training and should not be treated as professional agricultural advice.

Actual crop suitability depends on local soil testing, climate, season, irrigation and agricultural expertise.

## 👨‍💻 Author

**Raunak Raza**

- GitHub: [raunak-collab](https://github.com/raunak-collab)
- LinkedIn: [Raunak Raza](https://www.linkedin.com/in/raunak-raza-7172a1315/)
- Portfolio: [Visit Portfolio](https://raunakportfoliodev.netlify.app/)

---

If you find this project useful, consider giving it a ⭐ on GitHub.
