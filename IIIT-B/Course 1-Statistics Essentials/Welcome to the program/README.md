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

You saw how data visualisation can improve data density and improve the amount of information being conveyed. Just imagine how difficult it would be to interpret a spreadsheet with the score of each inning of each batsman being recorded along with his strike rate. In this case, data visualisation can help you figure out many insights just by looking at the plot. You can see the visualisation below.


# Market movement and Budget
https://gramener.com/budget/?Year=2007

You saw how a treemap diagram showed how multiple companies and sectors react to the budget. You can find the interactive graph here.

 

An important point to remember is that visualisations should be accompanied by a voice or text narrative if possible - it improves the experience of the user drastically. 

 

Next, let's see how visualisation can help in visual exploratory analytics. Here, you will see how data visualisation helped in understanding the connections between different software and clustering them together based on common features. You can find the visual here.

ss


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

plt.scatter(x_axis, y_axis)
 

Using this command, the data points will spread across the graph corresponding to the values on the y and x axes. The plot that was developed in the demonstration is given below. 

Let’s watch the next video to understand how a scatter plot can be useful when you are dealing with two quantitative variables

Take a look at the rightmost point in the plot. It represents a product that made a profit of 1,50,000 units when the sales generated were 8,00,000 units. Similarly, all the points in the plot represent a product and its profit and sales values. Just by looking at the chart, can you find the products that are more lucrative to trade than others? Yes, a lucrative product has high profit value with preferably low sales value, that is the points to the right side in the plot preferably also towards the bottom.

 

Now that you have learnt how to read a scatter plot, let’s proceed to more complex features of a scatter plot. Matplotlib offers a feature that allows you to incorporate a categorical distinction between the points plotted on a scatter plot. Using this feature, you can colour-code the points based on the category and distinguish them accordingly. Let’s watch the next video to learn how to colour-code points on a scatter plot.


You can run the scatter function with the following attributes to specify the colours and labels of the categories in a data set:

plt.scatter(x_axis, y_axis, c = color, label = labels)
 

Here, all the information (x_axis, y_axis, colour, labels) need to be provided in the form of a list or an array. You can use this command to assign colours to categories and distinguish them accordingly. 
 
Another feature of a scatter plot allows you to use labels to further distinguish points over another dimension variable. Suppose you have the array ‘country’, which indicates the country where the sales were generated. Now you want to highlight the points belonging to a particular country in the previous scatter plot.


You can use the following command to add a note (annotate) with a point in the scatter plot:

 

plt.scatter(profit[product_category == "Technology"], sales[product_category == "Technology"], 
            c= 'Green', alpha= 0.7, s = 150, label="Technology" )

plt.scatter(profit[product_category == "Office Supplies"], sales[product_category == "Office Supplies"], 
            c= 'Yellow', alpha= 0.7, s = 100, label="Office Supplies" )

plt.scatter(profit[product_category == "Furniture"], sales[product_category == "Furniture"], 
            c= 'Cyan', alpha= 0.7, s = 50, label="Furniture" )

for xy in zip (profit[country == "India"], sales[country == "India"]):
	plt.annotate(s = "India", xy = xy)

## Adding and formatting title
plt.title("Sales versus Profits across various Countries and Product Categories\n", fontdict={'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})

## Labeling Axes
plt.xlabel("Profit", fontdict={'fontsize': 12, 'fontweight' : 5, 'color' : 'Brown'})
plt.ylabel("Sales", fontdict={'fontsize': 12, 'fontweight' : 5, 'color' : 'Brown'})

plt.legend()

plt.show()
 

After using the command to add a note, your scatter plot will look like the one given below. 

As you can see in the figure above, the products that were traded in India are marked. This is how the annotate statement that was added to a point in the scatter plot helps you distinguish the data points. 


In this segment, you learnt how a scatter plot helps you visualise two numeric variables. Attempt the following questions to cement the concepts that were covered in this segment. 

[Note: Please use the updated matplotlib documentation here]
https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html?highlight=scatterplot


Scatterplot
Select the cases where a scatterplot would be helpful in generating insights.
(More than option one can be correct.)


To check whether a relationship exists between the age of a person and their income.

✓ Correct
You missed this!
Feedback:
A scatterplot shows the relationship between two sets of data. Hence, this is the correct option.


To check whether there are any irregular entries in the data range.

✕ Incorrect
Feedback:
A scatterplot can sometimes reveal outliers but not always. Hence, this is not the correct answer.


To check whether stock prices are positively related to the profit of a company.

✓ Correct
You missed this!
Feedback:
Since a scatterplot helps to visualise the relationship between two sets of data, it also reveals whether they are related positively or negatively.


To understand the distribution of the salaries of the employees in a company.

✕ Incorrect
Feedback:
The distribution of data can be better visualized using distribution plot which requires one input, whereas a scatterplot needs two variables as input.

Which attribute helps set the transparency of points in a scatterplot?
alpha

✓ Correct
Feedback:
This is the correct attribute. You can assign a value between 0 (transparent) and 1 (opaque).
