# Getting to know the Program
Hello and welcome to this program on Executive Post Graduate Program in ML and AI. 

Since you have enrolled in the program, you must already be aware of the impact of ML technology on the world around us. In this program, you will be introduced to the world of ML, explore a broad spectrum of technologies and algorithms in ML and apply ML techniques to solve real-life problems. 

There are many popular ML models, such as Google Maps predicting ETA, Amazon using dynamic product pricing, email classification and many others.

These and any other ML solution needs three significant components:

## Data
## Algorithm
## Support infrastructure
Throughout this program, you will learn how to collect, handle and explore data. You will discover various data processing algorithms and how to fine-tune them to achieve the best performance. And towards the end of the course, you will also learn how to access the necessary infrastructure to put your ML solution to use. 

## The data
In recent years, data production has increased at a staggering rate and so have the tools and technologies that deal with data. ML techniques are used to extract insights from a limited amount of data and ensure that these insights reflect the real world scenarios. In this regard, the program covers various concepts, such as inferential statistics, exploratory data analysis, hypothesis testing and so on.  

 

## The Algorithm
The next important component of ML techniques is the algorithms that process data. Think of a data processes algorithm as a set of instructions for a computer to follow. The result of these instructions is a mathematical representation of a real-world phenomenon. For instance, the price of a house is some mathematical function of the area, the location and the features of the house.


This mathematical function represents real-world house pricing and the set of instructions that one would follow to create this function is called the algorithm. In this program, you will learn many algorithms, starting from basic algorithms, such as linear regression to fancy algorithms, such as boosting and PCA. 


The program will also introduce you to a new paradigm in ML algorithms called deep learning (DL). DL algorithms take inspiration from the functioning of the human brain. You will use DL to help the computer view things and read and understand the natural language. In the latter half of the program, you will learn how to use the DL models to build state-of-the-art applications. Apart from DL, there is another field of machine learning applications gaining popularity these days, the Natural Language Processing (NLP) algorithms. In the program, you will learn the basics of NLP in the fifth course, also the program has a dedicated elective for those of you who want to dive deeper into NLP. 

 
## The Support Infrastructure
Let’s take a look at a mind-boggling statistic about ML applications: approximately 80 percent of ML applications do not make it out of the experimentation phase. One major reason behind this is that the data community lacks the know-how of making ready-to-use solutions. In the case of a four-stroke combustion engine; building a test setup in a laboratory and building a mass-producible internal combustion engine are two very different things. So, we have also included some basics of how an ML solution can be made application-ready. 

 Electives 
This program also has an elective course. You don’t have to make the elective choice till much later in the program. When the time comes, you will have all the information necessary for you to make an informed choice. The two electives offered are MLops and Generative AI. 


Finally, you will use all the knowledge you have gained in this program to create an end-to-end solution to a real-life problem. The solution will be equivalent to an end-of-degree project. You will be given an industry-relevant problem to solve and you will be graded on the solution that you create. 


The program will start simple and become more difficult towards the end. So, to keep up with the program, you are expected to participate in all the different learning activities, such as live sessions, personalised mentoring, assignments, submissions and so on. All these elements are planned to make your learning experience more comprehensive.

Although the team at upgrad and the faculty here at IIITB are here to guide you, always remember that the best learning happens when you do something on your own. So, always give your best and you will succeed in the program.  

 ============================================================================================================================

 # Visualisations - Some Examples


# Cricket
https://gramener.com/cricket/

You saw how a treemap diagram showed how multiple companies and sectors react to the budget. You can find the interactive graph

# Market movement and Budget
https://gramener.com/budget/?Year=2007


# Facts and Dimensions

Graphics and visuals, when used intelligently and innovatively, can convey a lot more than what raw data alone can. Matplotlib serves the purpose of providing multiple functions to build graphs from the data stored in your lists, arrays, etc. So, let’s start with the first lecture on Matplotlib.

Before we start discussing different types of plots, you need to learn about the elements that help us create charts and plots effectively. There are two types of data, which are as follows:

## Facts

## Dimensions
Facts and dimensions are different types of variables that help you interpret data better. Facts are numerical data, and dimensions are metadata. Metadata explains the additional information associated with the factual variable. Both facts and dimensions are equally important for generating actionable insights from a given data set. For example, in a data set about the height of students in a class, the height of the students would be a fact variable, whereas the gender of the students would be a dimensional variable. You can use dimensions to slice data for easier analysis. In this case, the distribution of height based on the gender of a student can be studied.


Identifying facts and dimensions among variables effectively will help you start the analysis of a given data set.

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


## matplotlib documentation

https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html#matplotlib.pyplot.bar


## Bar Graph
Is it possible to have a separate colour for each category in a bar graph?

Feedback:
Colours can be provided as a list to the matplotlib.pyplot.bar function under the attribute ‘color’.: matplotlib.pyplot.bar(x, y, color = [‘red’, ‘blue’, ‘green’]) [Note: if there are more than three bars, the colours will start repeating themselves.]


# Scatter Plot

Scatter plot, as the name suggests, displays how the variables are spread across the range considered. It can be used to identify a relationship or pattern between two quantitative variables and the presence of outliers within them.

Let’s watch the next video to understand how a scatter plot can be useful when you are dealing with two quantitative variables


