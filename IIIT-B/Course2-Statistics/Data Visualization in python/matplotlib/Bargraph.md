Bar Graph
Plots are used to convey different ideas. For example, you can use certain plots to visualise the spread of data across two variables and other plots to gauge the frequency of a label. Depending on the objective of your visualisation task, you can choose an appropriate plot. As part of this session, you will learn how to select an appropriate plot. You can download the Jupyter Notebook attached below. The same notebook will be used in the demonstrations throughout the session.

In this segment, you will learn how to create the first plot: Bar Graph. In the following video, Behzad will explain the process of creating a bar graph. 

As you saw in the video above, the subpackage pyplot is used to build plots and graphs throughout this session. To load the subpackage, you need to run the following command:

 

import matplotlib.pyplot as plt
 

To recap, Matplotlib allows you to use a simple and intuitive workflow to create plots. The important Matplotlib commands used in the video above are as follows:

plt.bar(x_component, y_component): Used to draw a bar graph
plt.show(): Explicit command required to display the plot object
A bar graph is helpful when you need to visualise a numeric feature (fact) across multiple categories. In the example covered in the video, you plotted the sales amount (numeric feature) under three different product categories. Using the bar graph, you could easily distinguish between the performance of these categories.


Let’s watch the next video in which Behzad will demonstrate how to add elements to our graph to make it more easily understandable.

In the video above, you learnt the different ways in which you can modify your chart to make it more understandable. You can use the following code to add a title and labels to your graph:

plt.xlabel(), plt.ylabel(): Specify labels for the x and y axes
plt.title(): Add a title to the plot object.
You can also try to make the charts more appealing by using different attributes such as font size and colour. Adding labels and a title to your plot helps the audience interpret the graphs easily and also relays the required information to the viewer.


You can use the attributes of plt.bar() to make the desired changes to the bars of a graph. For example, you can use the following code to change the values and ticks on the x and y axes of a graph:

plt.yticks(tick_values, tick_labels)
 

After making all the changes demonstrated in the video, your graph will look like the one given below. 

Now that you have understood the basics of a bar plot, answer the following questions. 



#official document for bar graph

https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar

Bar Graph
Is it possible to have a separate colour for each category in a bar graph?
Yes
Colours can be provided as a list to the matplotlib.pyplot.bar function under the attribute ‘color’.: matplotlib.pyplot.bar(x, y, color = [‘red’, ‘blue’, ‘green’]) [Note: if there are more than three bars, the colours will start repeating themselves.]