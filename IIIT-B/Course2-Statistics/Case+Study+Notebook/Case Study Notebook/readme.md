

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



