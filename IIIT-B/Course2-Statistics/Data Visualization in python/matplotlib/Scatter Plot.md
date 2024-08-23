Scatter plot, as the name suggests, displays how the variables are spread across the range considered. It can be used to identify a relationship or pattern between two quantitative variables and the presence of outliers within them.

 

Let’s watch the next video to understand how a scatter plot can be useful when you are dealing with two quantitative variables

You can use the following command to build a scatter plot:

plt.scatter(x_axis, y_axis)
 

Using this command, the data points will spread across the graph corresponding to the values on the y and x axes. The plot that was developed in the demonstration is given below. 

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

# Adding and formatting title
plt.title("Sales versus Profits across various Countries and Product Categories\n", fontdict={'fontsize': 20, 'fontweight' : 5, 'color' : 'Green'})

# Labeling Axes
plt.xlabel("Profit", fontdict={'fontsize': 12, 'fontweight' : 5, 'color' : 'Brown'})
plt.ylabel("Sales", fontdict={'fontsize': 12, 'fontweight' : 5, 'color' : 'Brown'})

plt.legend()

plt.show()
 

After using the command to add a note, your scatter plot will look like the one given below. 

As you can see in the figure above, the products that were traded in India are marked. This is how the annotate statement that was added to a point in the scatter plot helps you distinguish the data points. 


In this segment, you learnt how a scatter plot helps you visualise two numeric variables. Attempt the following questions to cement the concepts that were covered in this segment. 

[Note: Please use the updated matplotlib documentation here]



Matplotlib also offers multiple features to make these plots as descriptive as possible using the different dimension variables associated with the plot.bar() method.


In the next segment, you will learn about another set of graphs: Line Graph and Histogram. A line graph is used to visualise trends, and a histogram is used when you want to study the frequency distribution of a numeric variable. 







## official documents
https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
