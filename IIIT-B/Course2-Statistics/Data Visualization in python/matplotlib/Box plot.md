Box plots are quite effective in summarising the spread of a large data set into a visual representation. They use percentiles to divide the data range. 

 

The percentile value gives the proportion of the data range that falls below a chosen data point when all the data points are arranged in the descending order. For example, if a data point with a value of 700 has a percentile value of 99% in a data set, then it means that 99% of the values in the data set are less than 700.

 

Let’s watch the next video to learn more about box plots.

You can use the following command to create a box plot in Python using Matplotlib:

plt.boxplot([ list_1, list_2])
 

The figure below shows a typical box plot with explanations for each element in its construction.

 

 

 Box plots divide the data range into three important categories, which are as follows:

Median value: This is the value that divides the data range into two equal halves, i.e., the 50th percentile.
Interquartile range (IQR): These data points range between the 25th and 75th percentile values.
Outliers: These are data points that differ significantly from other observations and lie beyond the whiskers.
 

The box plot given below was constructed in the video.

 

 As you can see, there are quite a few outliers in the given data set.

 

 

Attempt the quiz given below to test your understanding of the box plots. 