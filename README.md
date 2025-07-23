# 💼 AI-Based Employee Salary Prediction

This project uses **Machine Learning** and **Artificial Intelligence** to predict employee salaries based on various features such as education, job title, industry, experience, and performance. It uses a synthetic dataset generated with realistic distributions to simulate real-world scenarios.

---

## 📁 Table of Contents

- [Project Overview](#-project-overview)
- [System Requirements](#-system-requirements)
- [Libraries Used](#-libraries-used)
- [Dataset Description](#-dataset-description)
- [Data Generation](#-data-generation)
- [Data Preprocessing](#-data-preprocessing)
- [Model Building](#-model-building)
- [Evaluation](#-evaluation)
- [Results](#-results)
- [How to Run](#-how-to-run)
- [Conclusion](#-conclusion)
- [Future Scope](#-future-scope)

---

## 🧠 Project Overview

This project aims to predict the salary of an employee using machine learning models based on factors like:

- Name, Age, Gender
- Education Level
- Job Title, Industry
- Experience (Years)
- Performance Score

The system can help HR departments estimate fair salary ranges, identify underpaid employees, and make informed hiring decisions.

---

## 💻 System Requirements

- Python 3.8+
- pip (Python package manager)
- Jupyter Notebook or any Python IDE

---

## 📚 Libraries Used

- `pandas` — Data manipulation  
- `numpy` — Numerical operations  
- `matplotlib`, `seaborn` — Visualization  
- `sklearn` — Machine learning models and metrics  
- `faker` — Synthetic data generation  
- `random` — Control distributions  
- `joblib` — Model saving/loading

Install all with:
```bash
pip install pandas numpy matplotlib streamlit scikit-learn faker joblib
```
## 📂 Dataset Description

The dataset is generated using Faker and includes over 10,000 samples. Each record has:

Feature	Description
Name	Random full name
Age	Integer (20–60)
Gender	Male or Female
Education	High School, Bachelor's, Master's, PhD
Job Title	Role (e.g., Data Scientist, Manager)
Industry	Sector (e.g., IT, Healthcare)
Experience	Work experience in years
Performance	Rating from 1 to 5
Salary	Computed target (based on logic + noise)

## 🧾 Data Generation

Used faker (Indian locale) for realistic names

Custom logic added to:

Adjust base salary per job title

Increase salary based on experience and performance

Model gender wage gap (~5% lower for females)

Output saved as realistic_employee_dataset.csv

## 🧹 Data Preprocessing

Label encoding for categorical features (Education, Gender, Job Title, Industry)

Normalization and scaling (if needed)

Correlation analysis and EDA (heatmaps, histograms, boxplots)

## 🧪 Model Building

Several regression models were evaluated:

Model	Description
Linear Regression	Baseline model
Random Forest Regressor	High performance and handles non-linearity
Gradient Boosting	Boosted trees for better accuracy

Best model: Random Forest (based on R² and RMSE)

## 📈 Evaluation

Used the following metrics:

R² Score

Mean Absolute Error (MAE)

Root Mean Squared Error (RMSE)

```bash
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
```

## 🧪 Results

R² Score: ~0.87

MAE: ₹6,500

RMSE: ₹9,800

Visualizations include:

Actual vs Predicted Salary plots

Feature Importance chart (for Random Forest)

## ▶️ How to Run
Clone the repo or download the files

```bash
git clone https://github.com/SylerS7/Employee-Salary-Predictor.git
cd Employee-Salary-Predictor
```
Install the required libraries

```bash
pip install -r requirements.txt
```
(Optional) Generate your own dataset
Run the script to create a custom dataset:

```bash
python custom_dataset.py
```
Train and evaluate the model
Open the Jupyter Notebook to train the model:

```bash
jupyter notebook model_training.ipynb
```
Launch the web app (optional)
Run the Streamlit app for an interactive interface:

```bash
streamlit run app.py
```
## 📝 Or Simply:

Use the pre-generated dataset and pretrained model provided in this repo and directly launch the app:

```bash
streamlit run app.py
```

## ✅ Conclusion
The model can predict employee salaries with good accuracy

Custom salary logic makes the data generation realistic

Useful for HR and hiring teams to make salary decisions

The system is modular and can be extended further

🔮 Future Scope
🔁 Integrate with real-time job market APIs

🧠 Use deep learning models for even better predictions

🌐 Build a cloud-deployed web app or mobile app

📈 Include features like promotions, certifications, and market demand

🏢 Extend to predict bonuses and career growth paths

## 📩 Contact
Developed by K Aryan.
For suggestions or collaboration, feel free to reach out!
