Introduction
So far, you have learnt how to perform basic data analysis using Python and Excel. You have also learnt that it is risky to manage data from different files and that it may lead to inconsistency. An organisation cannot track its business activities efficiently by maintaining a large number of files. Hence, databases are used for accessing and managing data efficiently. A software known as Database Management System (DBMS) is used widely in the industry to analyse data easily.

In this session
You will be introduced to the basic concepts of a data warehouse, star schema, OLAP (Online Analytical Processing), OLTP (Online Transactional Processing), SETL (Select, Extraction, Transformation, and Loading), constraints and ERD (Entity Relationship Diagrams).

 

Think of yourself as a data analyst working for a company that has the following three departments: Marketing, Sales and Finance. Now, let’s assume that each department maintains a separate database.

 

This could lead to a situation wherein each department has its own version of the facts. For a question such as 'What is the total revenue of the last quarter?', every department might have a different answer. This is because each department draws information from a different database.

 

This is where a data warehouse can prove to be useful. It can help with creating a single version of the truth and the facts. A data warehouse would thus be the central repository of data of the entire enterprise.

 

Now, in the upcoming video, you will learn what a data warehouse is and how it is useful for companies in carrying out data analytics. You will also learn about OLAP, which stands for Online Analytical Processing systems. OLAP is used to extract business-relevant information and perform analysis on the data stored in data warehouses. In the next video, you will understand the data warehouse.

So, a data warehouse is a collection of data. It has the following properties:

Subject-oriented: A data warehouse should contain information about a few well-defined subjects rather than the enterprise.
Integrated: A data warehouse is an integrated repository of data. It contains information from various systems within an organisation.
Non-volatile: The data values in a database cannot be changed without a valid reason.
Time-variant: A data warehouse contains historical data for analysis.
In the next segment, you will learn about the structure of the data warehouse.

## Structure of a Data Warehouse
In the previous segment, you learnt about the basic concepts of data warehousing. Now, one of the primary methods of designing a data warehouse is dimensional modelling.

 

The two key elements of dimensional modelling include facts and dimensions, which are basically the different types of variables that are used to design a data warehouse. They are arranged in a specific manner, known as a schema diagram. So, in the following video, you will learn more about facts and dimensions.

So, essentially, facts are the numerical data in a data warehouse and dimensions are the metadata (that is, data explaining some other data) attached to the fact variables. Both facts and dimensions are equally important for generating actionable insights from a data set.

 

So, you have learnt about the structure of the data warehouse. In the next segment, you will get the idea about the star schema but before that let's solve some topic related MCQs.



