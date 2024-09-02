Data Description
Given a data set, the first step is to understand what it contains. Information about a data set can be gained simply by looking at its metadata. Metadata, in simple terms, is the data that describes each variable in detail. Information such as the size of the data set, how and when the data set was created, what the rows and variables represent, etc. are captured in the metadata.  


Let us learn more about data description in the following video.

In this lecture, you learnt about metadata description.

 

Types of Variables

 

You learnt the difference between ordered and unordered categorical variables -

Ordered ones have some kind of ordering. Some examples are
Salary = High-Medium-low
Month = Jan-Feb-Mar etc.
Unordered ones do not have the notion of high-low, more-less etc. Example:
Type of loan taken by a person = home, personal, auto etc.
Organisation of a person = Sales, marketing, HR etc.
Apart from the two types of categorical variables, the other most common type is quantitative variables. These are simply numeric variables which can be added up, multiplied, divided etc. For example, salary, number of bank accounts, runs scored by a batsman, the mileage of a car etc.

 

So far, we have discussed the following types of variables:

Categorical variables
Unordered 
Ordered
Quantitative / numeric variables

After getting a basic feel for the variables in the dataset, the next step is to gain insights from the data. In the next few lectures, you will learn to do univariate analysis on the following types of variables:

Categorical Variables
Unordered categorical
Ordered categorical
Quantitative variables


## Ordered and Unordered Categorical Variables
Categorical variables can be of two types - ordered categorical and unordered categorical. In unordered, it is not possible to say that a certain category is 'more or less' or 'higher or lower' than others. For example, color is such a variable (red is not greater or more than green etc.)

On the other hand, ordered categories have a notion of 'higher-lower', 'before-after', 'more-less' etc. For e.g. the age-group variable having three values - child, adult and old is ordered categorical because an old person is 'more aged' than an adult etc. In general, it is possible to define some kind of ordering.

Which of the following variables are ordered categorical?



Unordered Categorical Variables - Univariate Analysis
Let’s now move to the most interesting part of EDA — getting useful insights from the data. So far, you have seen two types of variables - categorical (ordered / unordered) and quantitative (or numeric). In this segment, you will learn how to conduct univariate analysis on unordered categorical variables. 

 

But before studying that, think a bit about how you would conduct analysis on such a variable.


Unordered Categorical Variables - Univariate Analysis
You have worked with some unordered categorical variables in the past, for example:

The Product_Category in the retail sales dataset
The Customer_Segment in the retail sales dataset
The name of a batsman in any of the cricket datasets
Now imagine someone (say a client) gives you only an unordered categorical variable (and nothing else!), such as a column of size 4000 named 'country_of_person' with 130 unique countries and asks you 'can you extract anything useful from just this one variable?'. 

Write down how you would analyse just that variable to get some meaning out of it. Note that you have only one column to analyse.

Suggested Answer
The only thing you can do with an unordered categorical variable is to count the frequency of each category in the column. For example, you could observe that the product category 'furniture' appears 1000 times, 'technology' appears 810 times and so on. 

 

Turns out that, in some datasets, this simple analysis can also reveal interesting insights.



## Ordered Categorical Variables - Univariate Analysis
In the previous lecture, you saw how to conduct univariate analysis on unordered categorical variables. Let's now see how to do the same on ordered categorical variables.

 

Before that, think about the type of analysis you would do on ordered categorical variables.

Ordered Categorical Variables
You have already worked with ordered categorical variables before - there is a certain order or notion of 'high-low', 'before-after' etc. among the categories. For e.g. days of the week (Monday comes before Tuesday), grades of students (A is better than B), number of overs bowled by a bowler (3, 4, 9) etc.

Which of the following are other examples of ordered categorical variables? Choose all the correct options.



## Quantitative Variables - Univariate Analysis
You have seen how to conduct univariate analysis on categorical variables. Now, let's look at quantitative or numeric variables.

 

Prerequisites

In this segment, Anand will take you through various summary metrics. In case you are not familiar with the basics of descriptive statistics such as mean, median, mode, and standard deviation, you are recommended to go through the study material provided on the resources page. Knowledge of these concepts is essential for this topic and the forthcoming topics in other modules, so make sure you make yourself familiar before moving on. 


Let’s now learn how to analyse quantitative variables.


Mean and median are single values that broadly give a representation of the entire data. As Anand stated very clearly, it is very important to understand when to use these metrics to avoid doing inaccurate analysis.


While mean gives an average of all the values, median gives a typical value that could be used to represent the entire group. As a simple rule of thumb, always question someone if someone uses the mean, since median is almost always a better measure of ‘representativeness’.

 

Let’s now look at some other summary descriptive statistics such as mode, interquartile distance, standard deviation, etc.

Standard deviation and interquartile difference are both used to represent the spread of the data.

 

Interquartile difference is a much better metric than standard deviation if there are outliers in the data. This is because the standard deviation will be influenced by outliers while the interquartile difference will simply ignore them.

 

You also saw how box plots are used to understand the spread of data.


## Quantitative Variables - Summary Metrics

Let's take some time to understand why summary metrics such as mean and standard deviation are not representative of the data in some cases. 

News Popularity Data Set - Reading Box Plots 

 

You saw that quartiles are a better measure of the spread than the standard deviation. A good way to visualise quartiles is to use a box plot. The 25th percentile is represented by the bottom horizontal line of the box, the 75th is the top line of the box, and the median is the line between them.   

 https://archive.ics.uci.edu/dataset/332/online+news+popularity

In the following questions, let us use the news popularity data set to understand the measures of the deviation of the number of shares of a news article across the days of the week, weekends, and types of articles. 

 

You can access the data dictionary of the news popularity data set (to understand the variables in detail) here.

 

You can download the data set below:

The box plots given below show the variation of the number of shares of a news article (on the y-axis) against three variables — weekend (1 implies weekend), weekday (0 implies weekday), and the channel type. Read the charts carefully and answer the questions that follow. 

 

1. Shares vs Weekend  
