# 💻 Laptop Price Predictor
[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org/)
[![Jupyter Notebook](https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Heroku](https://img.shields.io/badge/Heroku-430098?style=flat-square&logo=heroku&logoColor=white)](https://heroku.com/)

![Status](https://img.shields.io/badge/status-Complete-brightgreen)


A web application that predicts laptop prices based on technical specifications using a trained machine learning model (`RandomForestRegressor`). This tool is designed for educational and demo purposes and includes a stylish, user-friendly UI.

🚀 **Live Demo:** [https://laptop-predictor-61b104b84b1b.herokuapp.com/](https://laptop-predictor-61b104b84b1b.herokuapp.com/)

---

## 🌟 Features

- 📊 **Machine Learning Powered** – Predicts prices using `RandomForestRegressor` trained on real-world data.

- 🌐 **Web-Based Interface** – Built with Flask and styled with responsive CSS.

- 💱 **Multi-Currency Output** – Choose between USD, EUR, LKR, or JPY.

- 📱 **Touchscreen & IPS Support** – Checkbox inputs supported.

- 🎯 **One-Hot Encoding** – Categorical features like brand, OS, and hardware specs are one-hot encoded.

- ☁️ **Deployed on Heroku** – Live and accessible for everyone.

---


## 📦 Dataset

- **Location:** `dataset/laptop_price.csv`
- **Sample Columns:**
  - `Company`, `TypeName`, `Ram`, `Weight`, `Cpu`, `Gpu`, `OpSys`, `Price_euros`
- **Example Row:**

| Company | TypeName   | Ram | Weight | Cpu           | Gpu         | OpSys | Price_euros |
|---------|------------|-----|--------|---------------|-------------|--------|--------------|
| Apple   | Ultrabook  | 8GB | 1.37kg | Intel Core i5 | Intel Iris  | macOS  | 1339.69      |

---
## 🧠 Machine Learning

- **Model:** `RandomForestRegressor` from `scikit-learn`
- **Features Used:**
  - RAM, Weight
  - Touchscreen, IPS
  - One-hot encoded: Brand, Type, CPU, GPU, OS
- **Training Script:** `website/model/model building.ipynb`
- **Output:** `predictor.pickle`


---

## 🚀 Deployment

### 🌐 Local Deployment

#### 1. Clone the Repository
```bash
git clone https://github.com/your-username/laptop-predictor.git
cd laptop-predictor/website
```

### 2. Create a Virtual Environment
```bash
Copy code
python -m venv env
source env/bin/activate  # Windows: .\env\Scripts\activate
```



### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```
Then visit: http://127.0.0.1:5000/

----
### ☁️ Heroku Deployment

#### 1. Prepare for Heroku
Ensure you have a Procfile:
```bash
web: gunicorn app:app
```

### 2. Deploy
```bash
heroku create laptop-predictor-username
git add .
git commit -m "Initial deploy"
git push heroku main
```
Heroku automatically detects Python using your requirements.txt.


-----

## 🛠️ Customization
  -   UI Customization: Edit home.html, result.html, and style.css in templates/ and static/.

  -  Model Improvements: Add more data to laptop_price.csv, then retrain using the notebook.

  -  Currency Conversion: Update conversion logic and symbols in app.py.
------------

------
## 📌 Author

- **Name**: Angeli Wickrama Arachchi  
- **LinkedIn**: [Angeli Wickrama Arachchige](https://www.linkedin.com/in/angeli-wickrama-arachchige)  
- **GitHub**: [angeli-sliit](https://github.com/angeli-sliit)

------
## 📄 License
This project is licensed under the MIT License – feel free to use and modify!











