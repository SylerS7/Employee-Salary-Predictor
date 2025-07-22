# Employee-Salary-Predictor

# 💼 Employee Salary Prediction using Machine Learning

This project aims to predict employee salaries based on various features such as age, gender, education, job title, experience, and industry using a regression-based machine learning model.

---

## 🧠 Project Summary

A synthetic dataset was generated using the `Faker` library (Indian locale) to simulate real-world employee attributes. A regression model (Random Forest) was trained to predict salaries with reasonable accuracy. The model's performance was evaluated using standard metrics and visualized with correlation heatmaps and feature importance plots.

---

## 📂 Project Structure

employee-salary-prediction/
├── app.py
├── custom_dataset.py
├── data/
│ └── generated_employee_data.csv
├── jupyter notes/
│ └── salary_prediction_model.ipynb
├── model/
│ └── model_training.py
├── preprocessor/
| └── preprocessor.py
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy
Edit

---

## ⚙️ Tech Stack & Libraries

- Python 3.10
- Pandas & NumPy
- Scikit-learn
- Seaborn & Matplotlib
- Faker (data generation)
- Jupyter Notebook

---

## 📊 Features

- Generates realistic Indian employee profiles
- Trains a regression model (Random Forest) for salary prediction
- Performs data visualization and feature analysis
- Evaluates model accuracy and performance

---

## 🔍 Results

- Model trained on 10000 records
- Achieved an R² Score of **~0.84**
- Top features: Experience, Industry, Job Title

---

## 📌 Conclusion

- Machine Learning can estimate salaries based on employee features.
- Experience and industry type strongly influence salary predictions.
- The model shows high accuracy on synthetic data.

---

## 🚀 Future Scope

- Integrate real-world datasets for better generalization
- Build a web interface using Streamlit or Flask
- Add classification (e.g., salary range categories)
- Include NLP-based job description analysis

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/SylerS7/employee-salary-prediction.git
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the notebook:

bash
Copy
Edit
jupyter notebook notebooks/salary_prediction_model.ipynb
🙏 Acknowledgments
Faker Python library for synthetic data generation

Scikit-learn for ML modeling

Matplotlib for visualizations

📬 Contact
For questions or collaborations, reach out via LinkedIn or email.

yaml
Copy
Edit

---

Let me know if you want me to:

- Generate the `requirements.txt`
- Add badges (e.g., GitHub stars, license)
- Help deploy this as a Streamlit app or website  
Just say the word, Aryan.








Ask ChatGPT
