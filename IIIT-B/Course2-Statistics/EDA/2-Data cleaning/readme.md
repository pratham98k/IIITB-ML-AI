Introduction
Welcome to the session on ‘Data Cleaning’.

 

In the previous session, you learnt about various sources of data. Once you have procured the data, the next step is to clean it to get rid of data quality issues.

 

There are various types of quality issues when it comes to data, and that’s why data cleaning is one of the most time-consuming steps of data analysis. For example, there could be formatting errors (e.g. rows and columns are ill-formatted, unclearly named etc.), missing values, repeated rows, spelling inconsistencies etc. These issues could make it difficult to analyse data and could lead to errors or irrelevant results. Thus, these issues need to be corrected before data is analysed.

​​​​​

In this session
You will learn how to identify the various quality issues and techniques to clean data.

 

Though data cleaning is often done in a somewhat haphazard way and it is too difficult to define a ‘single structured process’, we will study data cleaning in the following steps:

Fix rows and columns
Fix missing values
Standardise values
Fix invalid values
Filter data
 

Guidelines for In Module-Questions
The in-video and in-content questions for this session are not graded.

 

Guidelines for coding console questions
The lectures are interspersed with coding consoles to help you practise writing Python code. You will be given a brief problem statement and some pre-written code. You can write the code in the provided space, verify your answer using test cases, and submit when you are confident about the answer.

 

Note that the coding console questions are non-graded. Some instructions for these questions are as follows:

Ignore the pre-written code on the console. Please don't change it.
Write your answer where you're asked to write it.
You may run and verify your codes any number of times.



## Missing Values 

Missing Values
In the previous lecture, you learnt how to fix rows and columns. Let’s now study another common data quality issue — how to treat missing values.

 

You have already learnt how to treat missing values in Python. In the following lecture, Anand will walk you through some important points you should keep in mind while treating missing values.

Missing Values
What is correct in regards to missing values?

Values may be missing for multiple reasons such as non-response due to sensitivity of information, data entry error, censoring, etc. Without understanding the reason, replacing missing values might lead to a faulty analysis.


The most important takeaway from this lecture is - good methods add information, bad methods exaggerate information.

 

In case you can add information from reliable external sources, you should use it to replace missing values. But often, it is better to let missing values be and continue with the analysis rather than extrapolate the available information.


Let us summarise how to deal with missing values:

Set values as missing values: Identify values that indicate missing data, and yet are not recognised by the software as such, e.g treat blank strings, "NA", "XX", "999", etc. as missing.

Adding is good, exaggerating is bad: You should try to get information from reliable external sources as much as possible, but if you can’t, then it is better to keep missing values as such rather than exaggerating the existing rows/columns.

Delete rows, columns: Rows could be deleted if the number of missing values are significant in number, as this would not impact the analysis. Columns could be removed if the missing values are quite significant in number.

Fill partial missing values using business judgement: Missing time zone, century, etc. These values are easily identifiable.

Working with missiong values 

https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html


## Standardising Values

In the previous lecture, you learned how to fix missing values. You will now learn how to standardise values.

 

Let’s see how to go about standardising quantitative values in a data set. 

 

Note: At 0:12, In the first row of the table, it should be "Remove outliers" instead of "Remove ouliners".


Scaling ensures that the values have a common scale, which makes analysis easier. E.g. let's take a data set containing the grades of students studying at different universities. Some of the universities give grades on a scale of 4, while others give grades on a scale of 10. Therefore, you cannot assume that a GPA of 3 on a scale of 4 is equal to a GPA of 3 on a scale of 10, even though they are same quantitatively. Thus, for the purpose of analysis, these values need to be brought to a common scale, such as the percentage scale.


One of the concepts that surely caught your attention is outliers. Removing outliers is an important step in data cleaning. An outlier may disproportionately affect the results of your analysis. This may lead to faulty interpretations. It is also important to understand that there is no fixed definition of an outlier. It is left up to the judgment of the analyst to decide the criteria on which data would be categorised as abnormal or an outlier. We will look into one such method in the next session.


Let’s summarise what you learned about standardising variables. You could use this as a checklist for future data cleaning exercises.

Standardise units: Ensure all observations under a variable have a common and consistent unit, e.g. convert lbs to kgs, miles/hr to km/hr, etc.

Scale values if required:  Make sure the observations under a variable have a common scale

Standardise precision for better presentation of data, e.g. 4.5312341 kgs to 4.53 kgs.

Remove outliers: Remove high and low values that would disproportionately affect the results of your analysis.

 

Now that you have learned how to standardise numeric values, let us see how standardising text values is equally important.

Let us summarise what you learned about standardising text. You could use this as a checklist for future data cleaning exercises.

Remove extra characters like common prefix/suffix, leading/trailing/multiple spaces, etc. These are irrelevant to analysis.

Standardise case: There are various cases that string variables may take, e.g. UPPERCASE, lowercase, Title Case, Sentence case, etc.

Standardise format: E.g. 23/10/16 to 2016/10/23, “Modi, Narendra" to “Narendra Modi", etc.

 

Now answer the following question. (Note - Don't perform any type conversion after extracting the numbers from the Cust_id column.)

https://www.kdnuggets.com/2017/02/removing-outliers-standard-deviation-python.html


## Invalid Values
In the previous segment, you learnt how to standardise values. When standardising values, you do not really pay attention to the validity of the actual values of the variables. This is what we will discuss now as you learn to fix invalid values.

 

A data set can contain invalid values in various forms. Some of the values could be truly invalid, e.g. a string “tr8ml” in a variable containing mobile numbers would make no sense and hence would be better removed. Similarly, a height of 11 ft would be an invalid value in a set containing heights of children.

 

On the other hand, some invalid values can be corrected. E.g. a numeric value with a data type of string could be converted to its original numeric type. Issues might arise due to python misinterpreting the encoding of a file, thus showing junk characters where there were valid characters. This could be corrected by correctly specifying the encoding or converting the data set to the accurate format before importing.

 

Let us gain more insight into fixing invalid values.  


Note: In the above video, the temperature has been misspelt as tempreature. Kindly ignore the same.

 

If you have an invalid value problem, and you do not know what accurate values could replace the invalid values, it is recommended to treat these values as missing. E.g. in the case of a string “tr8ml” in a Contact column, it is recommended to remove the invalid value and treat it as a missing value.

 

Let’s summarise what you learnt about fixing invalid values. You could use this as a checklist for future data cleaning exercises.

 Encode unicode properly: In case the data is being read as junk characters, try to change encoding, E.g. CP1252 instead of UTF-8.
Convert incorrect data types: Correct the incorrect data types to the correct data types for ease of analysis. E.g. if numeric values are stored as strings, it would not be possible to calculate metrics such as mean, median, etc. Some of the common data type corrections are — string to number: "12,300" to “12300”; string to date: "2013-Aug" to “2013/08”; number to string: “PIN Code 110001” to "110001"; etc.
Correct values that go beyond range: If some of the values are beyond logical range, e.g. temperature less than -273° C (0 K), you would need to correct them as required. A close look would help you check if there is scope for correction, or if the value needs to be removed.
Correct values not in the list: Remove values that don’t belong to a list. E.g. In a data set containing blood groups of individuals, strings “E” or “F” are invalid values and can be removed.
Correct wrong structure: Values that don’t follow a defined structure can be removed. E.g. In a data set containing pin codes of Indian cities, a pin code of 12 digits would be an invalid value and needs to be removed. Similarly, a phone number of 12 digits would be an invalid value.
Validate internal rules: If there are internal rules such as a date of a product’s delivery must definitely be after the date of the order, they should be correct and consistent.
In next lecture, you will learn about filtering data for the ease of analysis.


## Filtering Data

In the previous segment, you learnt how to go about fixing invalid values. Now, let’s learn how to filter data.

 

After you have fixed the missing values, standardised the existing values, and fixed the invalid values, you would get to the last stage of data cleaning. Though you have a largely accurate data set by now, you might not need the entire data set for your analysis. It is important to understand what you need to infer from the data and then choose the relevant parts of the data set for your analysis. Thus, you need to filter the data to get what you need for your analysis.

 

Let’s now watch Anand as he takes us through the various steps of data filtering.


Let’s summarise what you learnt about filtering data. You could use this as a checklist for future data cleaning exercises.

Deduplicate data: Remove identical rows, remove rows where some columns are identical
Filter rows: Filter by segment, filter by date period to get only the rows relevant to the analysis
Filter columns: Pick columns relevant to the analysis
Aggregate data: Group by required keys, aggregate the rest
 

Comprehension

NOTE: The following questions is in on merging dataframes which was taught to you previously. This is done so that you can keep recall what you learnt sometime ago and revise those concepts if needed. You can find the relevant content here.

 

You have two data sets, each containing different columns of information regarding the employees of a company. The two data sets have a varying number of rows/observations. Dataset-1 contains information on Name, Age, and Salary against Employee ID. Dataset-2 contains information on Education and Experience against EmployeeID. It is unknown why the data sets have varying rows, i.e. why some employees were missed while collecting the data for each of the data sets. Employee ID is the identifier and thus the common column in both the data sets.



You are required to merge the two datasets such that only the employees common in both the data sets are a part of the new combined data set.

What operation would you use to get the desired result?

nner Join
✓ Correct
Feedback:
Inner join is used to merge the data sets, only keeping the rows corresponding to employee IDs that are common to both the data sets while removing the rest. Outer join, on the other hand, is used when you want to display all the rows from both the tables (even if the rows do not have a common key in both the tables)



Merge2
Which operation would you use to combine the two data sets such that it would list all employees common to both the datasets, while also having the employees unique to both the data sets., even if complete data is not available for each of them.

Full outer join
✓ Correct
Feedback:
Full outer join is used to merge the data sets such that, apart from keeping the common Employee IDs, it also includes the Employee IDs unique to both the data sets.


Duplicated Rows
Description
The given Dataframe 'rating' has repeated rows. You need to remove the duplicated rows. 

Example Code
----------------------------------------------------------------------------------------------------------------------
import pandas as pd
rating = pd.read_csv('https://media-doselect.s3.amazonaws.com/generic/JPAqXRWexo7nybkQ7BjPLWVN/rating_final.csv')
#print(rating.head())
rating_update = rating.drop_duplicates() #Type your code here

print(rating.shape)
print(rating_update.shape)
----------------------------------------------------------------------------------------------------------------------



