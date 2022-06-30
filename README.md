# Capstone Project AI Academy
## Time Seried Flask Application


### Check Point 1

##### Task 1.1 - Data Manipulation using Python
1.	Check for missing values in the dataset.
2.	Find out the outliers in numerical columns.
3.	Product Category with highest and lowest sales.
4.	The category of the product which is being sold with highest discounts
5.	Percentage share of sales at every state and region.

##### Task 1.2 - SQL & Oracle
Stage 1:
1.	Construct and ER-Diagram for the above-mentioned Requirement
2.	Construct Tables as per the ER-Diagram.
3.	Identify the relationships between tables and use appropriate standards for the same where applicable
4.	Insert the appropriate data into the identified tables from the sample dataset provided.
Stage 2:
1.	Display The category name of the products that earns highest profit
2.	Display Most valuable customer name who has frequently ordered products
3.	Display The segment and product name which yields highest profit 
4.	Display name of the City with highest sales
5.	Display Percentage share of profit of every region
6.	Display Percentage share of sales at every state
7.	Display the  Category of the product with highest demand in each region

##### Task 1.3 - Statistical Analysis using Python
1.	Descriptive statistics for both numerical and categorical and draw few insights from them. 
2.	Perform relevant hypothesis testing (t, chi-Square, Anova tests)  


### Check Point 2

##### Task 2.1 - Visualization using Python
Come up with appropriate results and visuals for the following:
Product Analysis:
1.  Different types of product categories
2.  Various sub-categories of products
3.  Product with highest demand in each segment 
4.  Category of the product with highest demand in each region
5.  The category of the product which is being sold with highest discounts
Sales/Profit Analysis:
1.  The category of the product that earns highest profit
2.  Most valuable customer
3.  The segment which yields highest profit
4.  City with highest sales
5.  Percentage share of profit of every region
6.  Percentage share of sales at every state

##### Task 2.2 - Exploratory Data Analysis
1.  Univariate, Bi- Variate Analysis and Multi- Variate Analysis 
2.  Missing values identification and treatment  
3.  Outlier analysis and treatment  
4.  Data scaling using min-max and/or  Z-score normalisation  
5.  Data transformation  
6.  Feature Engineering 

##### Task 2.3 - Visualization using PowerBI
Connect the data with Power BI desktop and perform Data Manipulation using Power Query Editor. Perform the below tasks in Power BI Desktop. 
1.  Determine which State in the Central Region has the highest sales
2.  Identify the City with Highest Sales in California
3.  In which Region do all Product Categories fall beneath the overall average profit?
4.  Find the top 10 Product Names by Sales within each region
5.  Product with highest demand in each segment 
6.  Which product is ranked #2 by Sales in the West region?
7.  Trend in profit/sales over region

##### Task 2.4 - Model Building using ML
You have to build a time series model by aggregating daily data into weekly or monthly data. 
Apply various time series models like Moving Average, Exponential smoothing.
1.  Compare various Time series models 
2.  Evaluate the performance of the model
3.  Identify the right metric to evaluate the performance of the model
4.  Identify issues and concerns on the given data and suggest the best technique/s to overcome the issues
Recommendations:
As a data analyst, what are the approaches do you suggest the sales team to forecast the sales more accurately?  Recommend based on your analysis.


### Check Point 3

##### Task 3.1 - PySpark and Hadoop
Big Data technologies like HDFS, Hive and PySpark need to be used as the historical data increases in size. 
As part of this task the following activities need to be done.
1.  Develop a PySpark application to load data Spark DataFrames and save it into Hive tables on a Hadoop cluster in Parquet format.
2.  Perform profiling of the data through PySpark and ensure that it is migrated correctly wherever the source is an RDBMS.
3.  Write PySpark routines to cleanse the data, prepare the data to handle missing values, and the data transformations identified in task 1.1 
again making sure that the data is written into Hive tables in an efficient format.
4.  If the predictive model identified in task 2.4 available in Spark MLlib then develop a PySpark application to implement and evaluate the ML model 
with appropriate metrics.
5.  Ensure that the best practices are followed and the design & code use the features of Spark and take advantage thereof.

##### Task 3.2 - AWS
1.	Move the Datasets to AWS s3
2.	Create Redshift Instance
3.	Ensure you create required tables in Redshift
4.	Create a data pipeline/copy command to move the data from storage to data warehouse(Redshift). You are allowed to use other copy commands as well
to move the data from storage to data warehouse.
5.	Connect the Redshift data to  PowerBI
6.	Perform the tasks  mentioned in Task 2.3(Only 4 core reports)

##### Task 3.3 - Flask Application
Deploy the Machine Learning Model created Task 2.4 in Flask application
