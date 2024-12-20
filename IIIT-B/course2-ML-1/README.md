https://github.com/ContentUpgrad/Linear-Regression

In the previous course, you learnt data preparation, which is the third step of the CRISP-DM framework. Following the same CRISP-DM framework, now let's move to the fourth and the most interesting stage, called modelling.

https://www.mathsisfun.com/equation_of_line.html


Summary


Here's a brief summary of what you learned in this session: 

Machine learning models can be classified into following two categories on the basis of learning algorithm:
Supervised learning method: Past data with labels is available to build the model
Regression: The output variable is continuous in nature
Classification: The output variable is categorical in nature
Unsupervised learning method: Past data with labels are not available
Clustering: No pre-defined notion of labels is there
Past data set is divided into two parts during supervised learning method: 
Training data  is used for the model to learn during modelling
Testing data is used by the trained model for prediction and model evaluation
Linear regression models can be classified into two types depending upon the number of independent variables: 
Simple linear regression: When the number of independent variables is 1
Multiple linear regression: When the number of independent variables is more than 1
The equation of the best fit regression line Y = β₀ + β₁X can be found by minimising the cost function (RSS in this case, using the Ordinary Least Squares method) which is done using the following two methods:
Differentiation
Gradient descent method
The strength of a linear regression model is mainly explained by R²,  where R² = 1 - (RSS / TSS)
RSS: Residual Sum of Squares
TSS: Total Sum of Squares


Assumption of simple linear regration.

https://www.jmp.com/en_in/statistics-knowledge-portal/what-is-regression.html


https://www.reliawiki.com/index.php/Main_Page


You can also go through the following link to see what happens when the assumptions are violated. But things will anyway get clearer once we keep moving ahead.


https://people.duke.edu/~rnau/testing.htm



Live session Google collab IIITB Live session 

https://colab.research.google.com/drive/1h41-Ww3HlsRwUm1TxUmCAwvT6pD-XUBK?usp=sharing



Hypothesis testing in Python
You can easily do hypothesis testing in Python by using stats from Scipy library.

1-sample t-test: testing the value of a population mean
To test, if the population mean of data is likely to be equal to a given value

scipy.stats.ttest_1samp()

stats.ttest_1samp(data['column'], x)
#where x is the mean value you want to test
 
2-sample t-test: testing for difference across populations
scipy.stats.ttest_ind()

stats.ttest_ind(column_1,column_2) 

 

Paired tests: repeated measurements on the same individuals
stats.ttest_rel()  

stats.ttest_rel(column_1,column_2)  


