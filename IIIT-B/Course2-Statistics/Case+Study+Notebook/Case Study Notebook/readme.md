

Case Study: Mind Map segment]

The dataset contains a total of 10,841 apps and 13 features or columns. The df.info() function showed us that some of the columns (like Rating) have missing values and some have incorrect data types associated with them. Let’s discuss both of them briefly here:

Missing values: You would almost always encounter data which have rows where no observation is recorded for a certain variable. These can affect the analysis process and the generated insights significantly. Some common techniques to treat this issue are
Imputation, where you replace the missing value with another estimated value
Dropping the rows containing the missing values altogether
or depending on the case, you can also go ahead and keep the missing values as long as they don’t affect the analysis.
 

Incorrect data types: This discrepancy mostly occurs due to some incorrect entry in the column which is stored in a format other than the desired one due to which the entire column gets misclassified. Or in some other cases, the format of the entire column is different from what we need for our analysis purposes. You either have to fix certain values or clean the entire column only to bring it to the correct format.
 

Missing values will affect our statistics drastically, for starters our inbuild functions of mean, sum, var etc will give incorrect results which clearly is quite dangerous. Also, you need the values to be in the numeric format of int or float to perform these operations, you cannot find the mean or median of a collection of strings, can we? Now, before you proceed to the data analysis and visualisation part, it is essential for you to remove the above discrepancies.


As explained by Rahim, you can easily use the isnull() and isnull().sum() functions to determine the missing values in a dataset. This will give you the number of missing values corresponding to each column.

 

 Now, there are a number of ways in which you can handle missing values. In some cases, you delete the records containing the null values. For example, the Rating column is our target variable, which would influence our analysis greatly as we keep progressing. Therefore, imputing values may skew our results significantly and hence we should drop them. 

 

Now let’s go ahead and check the other columns and see what actions are required for them.


Note - For the in-video question, the first option should be '4.1 and up' and not '4.1 and above'. Similarly the corresponding answer would be len(inp1[inp1['Android Ver']=="4.1 and up"])

 

In the case of the Android Ver column, you imputed, or you replaced the missing value with the mode for that column. Computing the mode can be done either using the value_counts() function or using the mode function directly.

 

Imputations are generally done when keeping the missing values disbars you from doing further analysis and eliminating the rows containing those values leads to some bias. The estimation is based on the mean, mode, median, etc. of the data.

 

In cases where there are numerical columns involved, both mean and median offer up as a good imputed value. In the case of the categorical column, mode turns out to be a decent enough imputation to carry out.



As you just learned, one way to impute missing values for the categorical variable is to use mode. Can you find which value occurs the maximum number of times?

 

You will find the inbuilt mode functionality useful for this question. You may also use the value_counts() functionality of pandas Series.

inp1["Android Ver"].value_counts()


In the previous segment, you were briefly introduced to the dataset and also performed some basic data-cleaning tasks by handling the null values. The next step would be to handle the data types of the columns. It is essential that your columns are also in the correct format or else it may hamper any further analysis. To understand the motivation for doing this, try answering the following question:


If you recall the earlier modules where you learnt about data types available in python, you know that aggregations like average, sum or mean cannot be performed on character variables or strings. Only numeric datatypes like float or int would allow you to calculate those values. Therefore, it is crucial that you convert all the columns having the incorrect data types to the correct ones.

 

The info() function is pretty handy here to start inspecting the datatypes of the various columns, and we can use it as a stepping stone to performing the data conversion tasks. Let's hear Rahim talk about converting the data types of columns. 


As you saw in the video, the Price column had an additional ‘$’ sign for every paid app that was visible clearly once we used the value_counts() function. This resulted in the column being treated as an object instead of a float-type value. So, your first task was to clean those columns.

 

Now, let’s go ahead and inspect the Reviews column and perform the necessary changes to it.


In the previous segment, you had fixed the row 'Life Made Wi-Fi' where all the values had shifted to the right. There you had a value of 3.0M under the 'Reviews' column due to which the entire column got treated like an object. Since that row got removed, you no longer had any issues with the 'Reviews' column and all you had to do was convert it into an int type.

 

Then, you saw the issue with the Installs column and observed the problem with it - the values contain both the ‘,’ and ‘+’ symbols, which led to this misrepresentation as an object type. Try solving it on your own and answer the question given below:


In the next segment, let's make sure that the data follows common sense. 

Additional Notes:
You can observe that the value_counts() function is quite versatile in its utility. As a matter of fact, it is one of the most commonly used functions throughout the pandas library, along with the describe() function, to perform a quick analysis of the data and obtain summary statistics like sum, median, average, frequency, etc. 



Sanity Checks
“I became insane, with long intervals of horrible sanity.” - EA Poe

 

Once you’ve completed the basic data cleaning and data handling tasks, the next step is to ensure that the data that is available with us ‘makes sense’. What it means is that the data needs to be factually correct apart from being of the correct data type.

 

For example, on a test where you can score between 0 and 100, it is not possible for a student to score 110 marks. Therefore, if such discrepancies occur in a data set, then you need to take care of them accordingly. So, in order to quickly check whether the data in the columns is rational and makes sense, you need to perform the so-called sanity checks.


As you saw in the video, three essential sanity checks were performed on the data:

Rating is between 1 and 5 for all the apps.
Number of Reviews is less than or equal to the number of Installs.
Free Apps shouldn’t have a price greater than 0.
The first and third conditions were satisfied, whereas the second condition was not satisfied with some records. When you inspected those records, you realised that those apps were likely junk apps and therefore you should ideally remove those records. As mentioned, you are free to apply sanity checks to the dataset on your own as long as they’re logically sound. 





Histograms vs Bar Plots
You have already studied bar plots in the previous module. Now it is a common misconception to confuse them with histograms. To understand the difference try analysing the following two situations and then choose the correct option:

 

Situation A - You want to visualise the total number of runs scored by MS Dhoni in a single year against all the teams he has played against.

Situation B - You want to visualise the spread of the runs scored by MS Dhoni in a single year.

Situation A requires a bar plot whereas Situation B requires a histogram.

✓ Correct
Feedback:
A Histogram plots the frequency of a numeric variable, whereas the Bar plot shows the aggregation of a certain numerical entity for some categorical variable. In Situation A, you are analysing the total sum of runs, which is a numeric variable for all the teams, which is a categorical variable. Hence it will need a bar plot. For Situation B, you're understanding the spread of a numeric variable by checking the frequency. Hence a histogram will be used here.


==========================================================================================================================================================================================================

### SeaBorn

Distribution Plots
In the previous session, you learnt about the basic data-handling and data-cleaning tasks that were essential to be performed. In this session, you will begin the journey with Seaborn library and start extracting insights. Recall that the target variable for this case study is the Rating column. The main task is to analyse this column and compare it with other variables to observe how the ratings change through different categories.


NOTE: The distplot function is deprecated, but you can still use it. It will stop working in Seaborn 0.14.

It has been replaced by two different functions: 


sns.histplot():
It creates a histogram for a single continuous variable.

sns.histplot(data=None, *, x=None, y=None, hue=None)

sns.displot():
This function is more flexible than sns.distplot().
It creates a complete grid of distribution plots in one go. You can use it for creating histograms, KDE plots, or other distribution visualizations.

Try this code:

#Create a distribution plot for rating
sns.displot(inp1.Rating, kde=True)
plt.show()
 

 

So, you have plotted a distribution plot to check the distribution of ratings using both the Matplotlib function and the Seaborn functions. In the latter case, you must have noticed that instead of the hist command, you are now using a distplot or a distribution plot.The corresponding Seaborn command is sns.distplot(inp1.Rating). 


You can go through distplot’s documentation here to learn more about the various parameters that can be used. Notice that this view is quite different from the histogram plot that we had obtained earlier in Matplotlib.

The difference arises due to the fact that instead of calculating the ‘frequency’, the distplot in Seaborn directly computes the probability density for that rating bucket. And the curve (or the KDE as noted in the documentation for Seaborn) that gets drawn over the distribution is the approximate probability density curve.*


Coming back to the visualisation, the bars that get plotted in both the cases are proportional. For example, the maximum frequency occurs around the 4-4.5 bucket in the histogram plotted by matplotlib. Similarly, the maximum density also lies in the 4-4.5 bucket in the distplot.

 

The advantage of the distplot view is that it adds a layer of probability distribution without any additional inputs and preserves the same inter-bin relationship as in the Matplotlib version. This statistical view of things is also far more informative and aesthetic than the earlier one.

 

You are expected to go through the Seaborn documentation from the link given above and answer the following questions.


So, after changing the number of bins to 20, you were able to observe that most of the ratings lie in the 4-5 range. This is quite a useful insight, which highlights the peculiarities of this domain, as mentioned by Rahim. If people dislike an app, they don’t generally wait to give it bad ratings; rather, they go ahead and remove it immediately. Therefore, the average ratings of the apps are pretty high.

 

Also, you learnt about some more customisations that can be done on the same view. You can change the colour of the view and even use Matplotlib functionalities on top of Seaborn to make your graphs more informative. 


Additional Notes:

*The terms “Probability Density” and “Probability Density Curve” may seem a bit alien to you right now if you do not have the necessary statistical background. But don’t worry, you will learn about them in a future module on Inferential Statistics. However, if you’re still curious, you can take a look at this link for further understanding.
Another chart analogous to the histogram is the countplot. It essentially plots the frequency of values for a categorical variable. Basically, the values are the same as when you take a value_counts() for that variable. Take a look at its documentation to understand how it is implemented.
Now that you are reasonably proficient in creating a distplot and performing some basic customisations, in the next segment, let's dive even deeper into the different ways in which you can customise a plot. 

https://seaborn.pydata.org/generated/seaborn.countplot.html


https://www.khanacademy.org/math/statistics-probability/random-variables-stats-library/random-variables-continuous/v/probability-density-functions

Styling Options
As discussed earlier, one of the biggest advantages of using Seaborn is that you can retain its aesthetic properties and also the Matplotlib functionalities to perform additional customisations. Before we continue with our case study analysis, let’s study some styling options that are available in Seaborn.

As you just learnt, you can use several styling options by using the sns.set_style() function. This gives you control over the way the axes and grid are presented. Here’s the link to its official documentation. Given below are certain style options that you can use for Seaborn in conjunction with the original customisations.

You should go ahead and try out the styling options and select the one that suits you the best and stick to it for the rest of the case study demonstration. In the next segment, you will explore the case study data using pie charts and bar graphs from the seaborn library. 



### Scatter Plots

Previously, you had dealt with only a single numeric column and therefore used either a box-plot or a histogram to portray the insights visually. What about two numeric columns, say Rating and Size? If you want to plot the relationship between two numeric variables, you will be using something known as a scatter plot. In the following video, Rahim will explain the situations when a scatter plot can be used. 

Scatter plots are perhaps one of the most commonly used as well one of the most powerful visualisations you can use in the field of machine learning. They are pretty crucial in revealing relationships between the data points and you can generally deduce some sort of trends in the data with the help of a scatter plot. 

 

The “Sales and Discount” example that you had seen earlier at the beginning of the module is an example of a scatter plot ( technically these are 4 different scatter plots, each of them showing a different city)





