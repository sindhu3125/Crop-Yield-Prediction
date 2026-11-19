# 🌾 Crop Yield Prediction Using Machine Learning

## 📌 Project Overview

Crop yield depends on several factors, including rainfall, temperature, soil conditions, crop type, and agricultural practices. Predicting crop yield can help understand the relationship between agricultural factors and crop productivity.

This project develops a **Crop Yield Prediction System** using Machine Learning regression algorithms to estimate crop yield based on agricultural features.

The project involves data preprocessing, exploratory data analysis, feature selection, model training, hyperparameter tuning, and evaluation to identify a model that performs effectively in predicting crop yield. An interactive Streamlit application is developed to make predictions through a user-friendly interface.

## 🎯 Objectives

- Analyze agricultural data to identify factors influencing crop yield.
- Perform data cleaning and exploratory data analysis (EDA).
- Prepare features for machine learning model training.
- Apply feature selection using Mutual Information.
- Train and compare regression models.
- Optimize model performance using GridSearchCV.
- Evaluate models using regression metrics.
- Develop an interactive crop yield prediction application using Streamlit.

## 📊 Dataset

**Dataset:** Crop Yield Dataset

**Data Type:** Agricultural and crop-related structured data

**Prediction Target:** Crop Yield

The dataset contains agricultural features used to analyze crop productivity and develop a regression model.

### Important Features

| Feature | Description |
|---|---|
| Crop | Type of crop cultivated |
| Agricultural Features | Relevant crop-related input variables |
| Environmental Features | Environmental conditions influencing crop yield |
| Numerical Features | Quantitative variables used for model training |
| Target | Crop yield to be predicted |

*Note: Refer to the dataset used in the project notebook for the exact feature names and descriptions.*

## ⚙️ Technologies Used

- **Programming Language:** Python
- **Data Analysis:** Pandas, NumPy
- **Data Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn
- **Feature Selection:** Mutual Information
- **Model Optimization:** GridSearchCV
- **Web Application:** Streamlit
- **Development Environment:** Jupyter Notebook, VS Code

## 🧠 Machine Learning Approach

The project follows a regression-based machine learning workflow to predict crop yield.

### Feature Selection

- Applied Mutual Information to evaluate the relationship between input features and the target variable.
- Selected relevant features to improve model learning and reduce unnecessary inputs.

### Model Development

- Trained regression models using Scikit-learn.
- Evaluated model performance and compared prediction results.
- Applied hyperparameter tuning using GridSearchCV to identify suitable model parameters.

### Model Evaluation

The model was evaluated using regression metrics to measure prediction accuracy and error.

## 🔬 Methodology

1. **Data Collection:** Load the agricultural dataset into Python.
2. **Data Preprocessing:** Clean the data and prepare features for analysis.
3. **Exploratory Data Analysis:** Analyze feature distributions and relationships with crop yield.
4. **Feature Selection:** Apply Mutual Information to identify informative features.
5. **Data Splitting:** Divide the dataset into training and testing sets.
6. **Model Training:** Train regression algorithms using the selected features.
7. **Hyperparameter Tuning:** Use GridSearchCV to optimize model parameters.
8. **Model Evaluation:** Evaluate the final model using MAE, MSE, RMSE, and R².
9. **Model Persistence:** Save the trained model for future predictions.
10. **Application Development:** Integrate the model into Streamlit for interactive predictions.

## 📈 Model Performance

| Metric | Score |
|---|---:|
| R² Score | 92.33% |
| MSE | 61,462.68 |

The model achieved an R² score of 92.33% on the evaluated dataset, indicating that it explains a substantial portion of the variation in crop yield. The MSE measures the squared prediction error.

## 📏 Evaluation Metrics

Model performance is evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

## 🌐 Streamlit Application

The project includes an interactive Streamlit application that allows users to:

- Enter relevant agricultural feature values.
- Submit inputs to the trained machine learning model.
- Obtain a predicted crop yield.
- Interact with the prediction system through a simple interface.

## 🚀 Project Structure

```text
Crop-Yield-Prediction/
│
├── dataset/
│   └── crop_yield.csv
│
├── notebooks/
│   └── Crop_Yield_Prediction.ipynb
│
├── models/
│   └── crop_yield_model.pkl
│
├── app.py
├── requirements.txt
└── README.md
```

*Note: Folder structure and filenames are illustrative and can be adjusted to match your repository.*

## 💻 Installation and Usage

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd Crop-Yield-Prediction
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Jupyter Notebook

```bash
jupyter notebook
```

Open the crop yield prediction notebook and run the cells sequentially to reproduce the analysis and model training.

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will provide an interface to enter agricultural data and obtain crop yield predictions.

## 🌟 Expected Outcome

The project provides a machine learning-based approach for crop yield prediction using agricultural data. It demonstrates a complete workflow from data analysis and feature selection to model tuning and interactive deployment.

The application allows users to obtain yield estimates based on input features, while the analysis helps identify the usefulness of agricultural variables in predicting crop productivity.

## 🔮 Future Enhancements

- Explore additional regression algorithms and ensemble methods.
- Incorporate more environmental and soil-related features.
- Improve model performance through advanced tuning techniques.
- Add interactive data visualization and feature importance analysis.
- Deploy the application to a cloud platform.

## 👩‍💻 Author

**Sindhu Reddyvari**

- GitHub: https://github.com/sindhu3125
