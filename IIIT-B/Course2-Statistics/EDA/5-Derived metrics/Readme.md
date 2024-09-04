## What Are Derived Metrics?
Sometimes, you would not get the most valuable insights by analysing the data available to you. You often need to create new variables using the existing ones to get meaningful insights.


New variables could be created based on your business understanding or they can be suggested by your clients. Let’s understand how business understanding plays an important role in deriving new variables.

To summarise, you saw two examples of different problems — analysing restaurant sales and understanding the marks distribution of class XII students.

 

In the first example, the ‘day of the week’ was a derived variable which was not provided in the original data set (only the date was provided). Using this new variable (day of the week), you can ‘drill down’ to compare the total sales on each day of the week and present the results on the calendar, as shown in figure 1 below.

In the second example, by plotting the marks against the ‘month of birth’ (derived variable), it was observed that the children who were born after June would have missed the cutoff by a few days and gotten admission at the age of 5. The ones born after June (e.g. July, August, etc) were intellectually and emotionally more mature than their peers because of their higher age, resulting in better performance.

This is a classic example of how derived metrics can help you discover unexpected insights.

 

So far, we have discussed only how to derive a new variable from the date variable. Are there other types of derived metrics as well? And is there a process of deriving new metrics?


In the next lecture, you will learn some new types of derived metrics.

ypes of Derived Metrics: Type Driven Metrics
In the last lecture, you saw some examples of derived metrics. Now, let’s understand the various types of derived metrics. Watch the following lecture to get an idea of the different types of derived metrics.

Broadly, there are three different types of derived metrics:

1.    Type-driven metrics

2.    Business-driven metrics

3.    Data-driven metrics

 

Type-Driven Metrics

 

These metrics can be derived by understanding the variable’s typology. You have already learnt one simple way of classifying variables/attributes — categorical (ordered, unordered) and quantitative or numeric. Similarly, there are various other ways of classification, one of which is Steven's typology.

 

Steven’s typology classifies variables into four types — nominal, ordinal, interval and ratio:

Nominal variables: Categorical variables, where the categories differ only by their names; there is no order among categories, e.g. colour (red, blue, green), gender (male, female), department (HR, analytics, sales)

These are the most basic form of categorical variables

Ordinal variables: Categories follow a certain order, but the mathematical difference between categories is not meaningful, e.g. education level (primary school, high school, college), height (high, medium, low), performance (bad, good, excellent), etc.

Ordinal variables are nominal as well

Interval variables: Categories follow a certain order, and the mathematical difference between categories is meaningful but division or multiplication is not, e.g. temperature in degrees celsius ( the difference between 40 and 30 degrees C is meaningful, but 30 degrees x 40 degrees is not), dates (the difference between two dates is the number of days between them, but 25th May / 5th June is meaningless), etc.

Interval variables are both nominal and ordinal

Ratio variables: Apart from the mathematical difference, the ratio (division/multiplication) is possible, e.g. sales in dollars ($100 is twice $50), marks of students (50 is half of 100), etc.

Ratio variables are nominal, ordinal and interval type


https://www.graphpad.com/support/faqid/1089/


## Types of Derived Metrics: Business Driven Metrics
So far, you've learned how to extract meaningful information from existing variables, e.g. extracting a "month" variable from the date variable. But what if you want to extract information that requires business expertise? For example, if you wish to know which students passed based on a list of scores in an exam, you need to know the criteria for passing the exam.

 

Let’s see how Anand approaches business-driven metrics. 

To summarise, there are three types of derived metrics:

Type-driven
Business-driven
Data-driven
 

Deriving metrics from the business perspective is not an easy task. It requires decent domain experience. Without understanding the domain correctly, deriving insights becomes difficult and prone to errors. 

 

Let's try out an exercise. You have been using the National Achievement Survey data set starting since EDA. In case you don't have the data set yet, you can download the National Achievement Survey from the link below to answer the question that follows.


Choose the correct option/s.


Business-driven metrics can be created from the ‘Runs’ column
A business-driven metrics could be creating a new column which gives information on whether a player scored a century or not.



Type-driven metrics can be created from the ‘Match Date’ column
A type-driven metric could be extracting years from the date column.


To summarise, data-driven metrics can be created based on the variables present in the existing data set. For example, if you have two variables in your data set such as "weight" and "height" which shows a high correlation. So, instead of analysing "weight" and "height" variables separately, you can think of deriving a new metric "Body Mass Index (BMI)". Once you get the BMI, you can easily categorise people based on their fitness, e.g. a BMI below 18.5 should be considered as an underweight category, while BMI above 30.0 is considered as obese, by standard norms. This is how data-driven metrics can help you discover hidden patterns out of the data.



Module Summary
Exploratory data analysis helps you, as a data analyst, to look beyond the data. It is a never ending process — the more you explore the data, the more insights you get. Almost 80% of the time, you would spend your time as a data analyst understanding the data and solving various business problems through EDA. If you understand EDA properly, then half the battle is won.

 

So far in this module, you have learnt the five most crucial topics for any kind of analysis. They are as follows:

Understanding domain

Understanding data and preparing it for analysis

Univariate analysis and segmented univariate analysis

Bivariate analysis

Deriving new metrics from the existing data

Let’s see how Anand looks at EDA.


