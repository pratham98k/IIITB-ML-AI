# Segmented Univariate Analysis

In this session
We will extend univariate analysis and learn to conduct univariate analysis across ‘segments’. The broad agenda for this session is as follows:

Basis of segmentation

Comparison of averages

Comparison of other metrics

Introduction to Segmented Univariate Analysis
In segmented univariate analysis, we segment the categorical variables and then conduct univariate analysis across its categories. Let’s see how this simple technique can help you unveil powerful insights.

You have already done some segmented univariate analysis in the previous lectures, such as in the news popularity example, where you wanted to test the following three hypotheses:

On average, a higher number of articles are shared on weekdays than weekends

Among the weekdays, articles published on Wednesdays get shared more than on any other weekday

Articles of the type (or channel) 'lifestyle' and 'social media' are shared more than the other types on average

In this case, the categorical variables used for grouping were ‘channel type’, ‘day of week’, etc.  Across these categories or groups, you had then conducted segmented univariate analysis to compare the average number of shares across days, channel types etc.

 

In the next few lectures, we will take multiple examples and conduct segmented univariate analysis in detail.


## Basis of Segmentation
In the last lecture, you have seen some glimpses of segmented univariate analysis. Now, let’s go deeper into the segmentation process. The entire segmentation process can be divided into four parts:

Take raw data

Group by dimensions

Summarise using a relevant metric such as mean, median, etc.

Compare the aggregated metric across groups/categories
Let's see how Anand explains the process of segmentation.

To summarise, the standard process of segmented univariate analysis is as follows:

Take raw data

Group by dimensions

Summarise using a relevant metric like mean, median, etc.

Compare the aggregated metric across groups/categories

So with this, you have now performed segmented univariate analysis on a few variables, but what if you have a large number of variables in your data set? How would you go about analysing and explaining the results of hundreds of categorical variables to your client? Let’s see what such a table would look like in the next lecture.

 

Comprehension: National Achievement Survey

 

In the examples you just saw, the variables used for grouping were gender, the number of siblings, handicap status, etc. The metric for comparison was the average marks in mathematics. Using this process, you can ask interesting questions by choosing various grouping variables and summary metrics, some of which you will see in the following questions.

 

Note: This data set is subsetted only for the state of Maharashtra. You can download the data from the link below:

Quick Way of Segmentation
In the last lecture, you learnt the process of segmentation. But what if you have a large number of variables in your dataset. It looks very repetitive task to perform the same analysis on the large bunch of variables. One way of solving this problem is to make a table with the categorical variables on one axis and the numeric variables (or measures/facts) on the other. Let’s see what such a table would look like.

Note: At 3:02 Anand mentions 'Never watching Television to watching Television everyday'. However, it should be 'Never playing games to playing games everyday'.

 

Comprehension: National achievement Survey Analysis

You saw how various factors have an impact on a student’s performance and marks. Let’s analyse how segmented univariate analysis can help you understand the factors affecting class VIII marks in the different states. You are required to go to the below website app, play around with the filters (gender, poverty, state, siblings, etc.) and answer the following questions.

 

You can find the dataset here.

 

Note that the data used for developing this exercise is different from the dataset provided to you in the previous lectures.

https://gramener.com/nas/


## Bivariate Analysis on Continuous Variables


In the last session, you learnt how to perform segmented univariate analysis e.g. how gender or father’s education impacts student’s percentage in science, maths and reading. But what if you want to analyse pairs of continuous variables at a time? For example, how the sales figure depends on the marketing spends, or, for that matter, how two continuous variables depend on each other. Is there any way or concept to identify the relationship between two variables?

 

Let’s start with the bivariate analysis on pairs of continuous variable to answer these questions.

To summarise, correlation is a number between -1 and 1 which quantifies the extent to which two variables ‘correlate’ with each other.

If one increases as the other increases, the correlation is positive

If one decreases as the other increases, the correlation is negative

If one stays constant as the other varies, the correlation is zero

 

In general, a positive correlation means that two variables will increase together and decrease together, e.g. an increase in rain is accompanied by an increase in humidity. A negative correlation means that if one variable increases the other decreases, e.g. in some cases, as the price of a commodity decreases its demand increases.

 

A perfect positive correlation means that the correlation coefficient is exactly 1. This implies that as one variable moves, either up or down, the other one moves in the same direction. A perfect negative correlation means that two variables move in opposite directions, while a zero correlation implies no relationship at all. 

 

Comprehension: Correlation

 

Note: The following questions will require you to manipulate dates and time in Python. In case you want to learn how to do that, you can access some quick tutorials here and you may read in detail about date and time here. 

 

Let us take an example of gold and silver prices in Indian currency per troy ounce ( = 31.8 grams). Do you expect gold and silver price to be correlated? Let’s find out. Download the file and import it in Python for analysis. The dataset provided below contains the gold and silver prices across various years and months.

https://docs.python.org/3/library/datetime.html


https://machinelearningmastery.com/how-to-use-correlation-to-understand-the-relationship-between-variables/

https://www.youtube.com/watch?v=jf-SIOFUuEo



## Business Problems Involving Correlation
In the last lecture, you learnt the concept of correlation and its interpretation. But it is also important to understand how correlation is used in the industry. Let’s see how correlation is used through a real example of stock market analysis.


There are two things which you would have noticed from the lecture:

The correlation matrix of stock prices of different countries gives a real sense of the relationship between many variables.

The correlated variables are grouped by similarities, and correlation can also be calculated for ‘groups of variables’. This is called ‘clustering’ which you will study in detail later in the machine learning course, but the idea is to form a hierarchy of similar groups of variables.

 

You can also see how you can interpret the extent of correlation among the variables from their scatter plot at this link. 

​​

Let’s take one more example to understand how clustering helps in understanding customer behaviour of ordering food at restaurants.


https://imf.org/external/np/fin/data/param_rms_mth.aspx


## Bivariate Analysis on Categorical Variables

So far, you have learnt how to analyse the relationship between two continuous variables. You will now learn how to quantify and understand the relationship between pairs of categorical and continuous variables.

 

Continuous vs. Categorical Bivariate Analysis: A Comparative Overview
Bivariate analysis is a statistical method used to examine the relationship between two variables. It can be categorized into two primary types: continuous and categorical.

Continuous Bivariate Analysis
Focus: The relationship between two continuous variables (e.g., height and weight, income and education).
Common Methods:
Correlation: Measures the strength and direction of the linear relationship between two variables.
Regression: Predicts the value of one variable based on the value of another.
Scatter Plots: Visualize the relationship between two variables.
Example: Analyzing the relationship between a person's age and their blood pressure.
Categorical Bivariate Analysis
Focus: The relationship between two categorical variables (e.g., gender and eye color, product type and customer satisfaction).
Common Methods:
Cross-Tabulation (Contingency Tables): Create a table to show the frequency of occurrence of different combinations of categories.
Chi-Square Test: Tests the independence of two categorical variables.
Odds Ratios: Measure the odds of an event occurring in one group compared to another.
Example: Examining the relationship between a person's favorite color and their preferred pet.
Similarities and Differences
Feature	Continuous Bivariate Analysis	Categorical Bivariate Analysis
Variables	Both continuous and categorical	Both categorical
Relationship	Linear or nonlinear	Association or independence
Visualization	Scatter plots	Bar charts, pie charts, contingency tables
Statistical Tests	Correlation, regression	Chi-square test, odds ratios

Export to Sheets
In essence, the key difference lies in the nature of the variables being analyzed. Continuous variables can be measured on a numerical scale, while categorical variables are divided into distinct groups or categories. The choice of method depends on the specific research question and the types of variables involved.

https://g.co/gemini/share/9772d9724f42

Similarities and Differences Between Derived Metrics
Derived metrics are created by combining or manipulating existing metrics to gain deeper insights into data. They can provide more nuanced and actionable information than raw metrics alone.

Let's explore three common methods used to derive metrics:

1. Aggregations:
Similarities: Like EDA, aggregations involve summarizing data.
Differences: Derived metrics focus on creating new, meaningful metrics, while EDA often involves exploring existing metrics.
2. Ratios and Proportions:
Similarities: Both methods involve comparing values.
Differences: Ratios and proportions are more specific, often used to assess relationships between different metrics.
3. Time-Series Analysis:
Similarities: Both methods can involve time-based data.
Differences: Time-series analysis focuses on identifying patterns, trends, and anomalies over time, while derived metrics can be used for various purposes.
To summarize: While EDA and derived metrics share the goal of understanding data, derived metrics go a step further by creating new, customized metrics that provide more specific insights.
