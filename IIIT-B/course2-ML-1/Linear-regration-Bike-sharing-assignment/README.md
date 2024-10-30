# Linear Regression: Bike Sharing Demand Prediction

> A case study and assignment on building a multiple linear regression model to predict bike-sharing demand, submitted as a Jupyter Notebook.

---

## Table of Contents
- [Overview](#overview)
- [Business Goal](#business-goal)
- [Data Preparation](#data-preparation)
- [Model Building](#model-building)
- [Model Evaluation](#model-evaluation)
- [Dataset Details](#dataset-details)
- [Assignment Steps](#assignment-steps)
- [Conclusions](#conclusions)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contributors](#contributors)
- [Contact](#contact)

---

## Overview

**Problem Statement**  
BoomBikes, a US-based bike-sharing service, is striving to sustain post-COVID. To prepare for future demand, they aim to understand factors influencing bike rental rates. This analysis helps identify key predictors of demand, allowing the company to create a tailored business strategy for revenue optimization.

## Business Goal
Create a predictive model for bike-sharing demand using historical data. Management can leverage the model to align business strategies with demand trends, helping them meet customer expectations and optimize profits.

## Data Preparation
- Convert numeric labels for categorical variables (e.g., season, weather) into strings as per the data dictionary.
- Retain the `yr` variable, which captures annual demand trends.
- Conduct EDA and clean data, including dummy variable creation for categorical features and data scaling.

## Model Building
The target variable for the linear regression model is **`cnt`** (total daily rentals), which includes both casual and registered user counts.

## Model Evaluation
Use the **R-squared** score on the test set to evaluate model accuracy:
```python
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)

Where y_test is the actual target values, and y_pred contains predicted values. High R-squared on test data indicates good model performance.

Dataset Details
File: day.csv
Features:
instant: Record index
dteday: Date
season: Season (1: Spring, 2: Summer, 3: Fall, 4: Winter)
yr: Year (0: 2018, 1: 2019)
holiday, weekday, workingday: Day indicators
weathersit: Weather situation (1–4, indicating clarity to severity)
temp, atemp: Temperature indicators
hum, windspeed: Humidity and wind speed
casual, registered, cnt: User counts (target variable)
Assignment Steps
Data Preparation

Clean data, drop unnecessary columns, and create dummy variables.
Split data into training and testing sets, scale features, and separate target and predictors.
Data Visualization

Conduct EDA to understand variable relationships and check correlations.
Modeling and Evaluation

Build and refine the model using linear regression, performing residual analysis and model validation on test data.
Conclusions
R-squared values indicate strong predictive power (82.2% on training and 81.1% on testing).
The model achieves near-zero mean squared error, effectively explaining variance with selected features.
Techniques like EDA, VIF, RFE, and residual analysis were instrumental.
Technologies Used
Python - 3.12.4
Pandas - 1.5.3
Numpy - 1.24.3
Matplotlib - 3.7.1
Seaborn - 0.12.2
Statsmodels - 0.14.1
Scikit-learn - 1.4.2
License
Data used in this project must cite: Fanaee-T, Hadi, and Gama, Joao, Event labeling combining ensemble detectors and background knowledge, Progress in Artificial Intelligence (2013).

Acknowledgements
Special thanks to the Upgrad team and instructors for guidance.

Contributors
Prathamesh Kulkarni
Contact
Created by @pratham98k - feel free to reach out!

Developed as part of the Linear Regression Module for the Post Graduate Diploma in Machine Learning and AI - IIIT, Bangalore (Upgrad).