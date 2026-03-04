# OIBSIP_DATASCIENCE_TASK5
Sales prediction using Python and Machine Learning

Overview :
This project focuses on predicting product sales based on advertising expenditure using machine learning techniques in Python. The objective is to understand how different advertising platforms influence sales and to build a model capable of predicting future sales values.

Objective :
The main goal of this task is to develop a regression model that predicts sales using advertising budgets spent on TV, Radio, and Newspaper promotions.

Dataset Description :
The dataset contains advertising data with the following features:
1. TV : Advertising budget spent on TV
2. Radio : Advertising budget spent on radio
3. Newspaper : Advertising budget spent on newspapers
4. Sales : Total sales generated (target variable)

An unnecessary index column was removed during preprocessing to ensure accurate model training.

Tools and Technologies Used :
1. Python
2. Pandas (data handling and preprocessing)
3. Scikit-learn (machine learning model)
4. Linear Regression algorithm

Methodology :
The dataset was first loaded and cleaned using pandas. After removing irrelevant columns, the data was divided into input features and the target variable. The dataset was then split into training and testing sets to evaluate the model’s performance. A Linear Regression model was trained on the training data and used to predict sales values. Model performance was evaluated using Mean Absolute Error.

Results :
The trained model was able to successfully learn the relationship between advertising spending and product sales. The prediction results showed a low error value, indicating that the model performs well in estimating sales outcomes.

Conclusion :
This project demonstrates how machine learning can be applied to real-world business problems such as sales forecasting. By analyzing advertising investments, the model can help estimate expected sales and support better marketing decisions.
