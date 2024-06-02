Pandas has two main data structures: 

Series
Dataframes 
The more commonly used data structure are DataFrames. So, most of this session will be focused on DataFrames. When you encounter series data structure, Behzad will explain them briefly to you. Let's begin the session by introducing Pandas DataFrames.  

DataFrame
It is a table with rows and columns, with rows having an index each and columns having meaningful names. There are various ways of creating dataframes, for instance, creating them from dictionaries, reading from .txt and .csv files. Let’s take a look at them one by one. 

Creating dataframes from dictionaries

If you have data in the form of lists present in Python, then you can create the dataframe directly through dictionaries. The ‘key’ in the dictionary acts as the column name and the ‘values’ stored are the entries under the column. 
 

You can refer to the Notebook provided below for this segment.

Pands commands 

https://pandas.pydata.org/pandas-docs/stable/reference/io.html


Pandas - Rows and Columns
An important concept in Pandas dataframes is that of the row and column indices. By default, each row is assigned indices starting from 0, which are represented to the left of the dataframe. For columns, the first row in the file (csv, text, etc.) is taken as the column header. If a header is not provided (header = none), then the case is similar to that of row indices (which start from 0).

 

Pandas library offers the functionality to set the index and column names of a dataframe manually. Let's now learn how to change or manipulate the default indices and replace them with more logical ones. The required notebook is the same as the previous segment.


You can use the following code to change the row indices:

dataframe_name.index
 

To change the index while loading the data from a file, you can use the attribute 'index_col':

pd.read_csv(filepath, index_col = column_number)
 

It is also possible to create a multilevel indexing for your dataframe; this is known as hierarchical indexing. Let’s watch the following video and learn how to do it.

For column header, you can specify the column names using the following code:

dataframe_name.columns = list_of_column_names

hile working with Pandas, the dataframes may hold large volumes of data; moreover, it would be an inefficient approach to load the entire data whenever an operation is performed. Hence, you must use the following code to load a limited number of entries:

dataframe_name.head()
 

By default, it loads the first five rows, although you can specify a number if you want fewer or more rows to be displayed. Similarly, to display the last entries, you can use the tail() command instead of head().
 

dataframe.info(): This method prints information about the dataframe, which includes the index data type and column data types, the count of non-null values and the memory used. 
dataframe.describe(): This function produces descriptive statistics for the dataframe, that is, the central tendency (mean, median, min, max, etc.), dispersion, etc. It analyses the data and generates output for both numeric and non-numeric data types accordingly. 
 


 https://www.youtube.com/watch?v=SYNEHBofpGE


 https://www.youtube.com/watch?v=txMdrV1Ut64

 




