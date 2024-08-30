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


