# **Spark** ⚡

## **Big Data**

Big data is a relative concept that can be difficult to grasp. It may be easier to define big data using the features that make it hard to handle in the first place. We can generally categorize big data by what are known as the three Vs: volume, velocity, and variety. Depending on where you look (or who you ask), there may be a different number of Vs. Some will say that there are 4, 5, 10, or even 17 Vs of big data! The three Vs we talk about here are the core of most definitions and give a complete picture of big data’s features.

### **Volume**

Big data is “big”. While this may seem obvious, it’s an important concept to cover. As previously mentioned, the definition of “big” is that the data is bigger than the amount of available computing power. Currently, zettabytes of data are created every year (for reference, a zettabyte is 1 billion terabytes).

### **Velocity**

Big data has velocity, meaning that it is growing quickly. If data were simply large, but slow-changing, then over time our computing power would eventually catch up to the size of the data. Through means like apps and sensors, data becomes faster, cheaper, and easier to collect automatically and continuously.

### **Variety**

Big data also has variety, meaning that it comes in different, and sometimes complex, forms. In today’s data ecosystem, data comes in many more formats than the data tables of old. Data can be categorized as structured (data tables with rows and columns), semi-structured (think JSON files with nested data), and unstructured (audio, image, and video data). Each of these data formats presents different challenges in processing.

## **PySpark**

As big data processing needs have grown, new technology has been developed. Spark is an analytics engine originally developed at UC Berkeley and eventually donated to the open-sourced Apache Software Foundation. Spark was designed as a solution for processing big datasets and was specifically developed to build data pipelines for machine learning applications. Like MapReduce, Spark does not have its own file storage system and is designed to be used with distributed file systems like HDFS. However, Spark can also be run on a single node (single computer) in stand-alone mode with a non-distributed dataset.

Spark uses the RAM of each cluster node in unison, harnessing the power of multiple computers. Spark applications execute analyses up to 100 times faster than MapReduce because Spark caches data and intermediate tables in RAM rather than writing them to disk. However, as datasets become larger, the advantage of using RAM decreases and can disappear altogether.

Spark was originally developed in Scala (an object-oriented and functional programming language). This presented users with the additional hurdle of learning to code in Scala to work with Spark. PySpark is an API developed to minimize this learning obstacle by allowing programmers to write Python syntax to build Spark applications. There are also APIs for Java and R.

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()
print("PySpark version:", spark.version)

# confirm your session is built
print(spark)
```

### **Resilient Distributed Datasets**

RDDs are the foundational data structures of Spark. Newer Spark structures like DataFrames are built on top of RDDs. While DataFrames are more commonly used in industry, RDDs are not deprecated and are still called for in certain circumstances. For example, RDDs are useful for processing unstructured data, such as text or images, that don’t fit nicely in the tabular structure of a DataFrame.

So what exactly is an RDD? According to our friends at Apache, the formal definition of an RDD is “a fault-tolerant collection of elements partitioned across the nodes of the cluster that can be operated on in parallel.” Those are some complicated words! Let’s break down the three key properties of RDDs together:

- Fault-tolerant or resilient: data is copied and recoverable in the event of failure
- Partitioned or distributed: datasets are split up across the nodes in a cluster
- Operated on in parallel: tasks are executed on all the chunks of data at the same time

We can use Spark with data stored on a distributed file system or just on our local machine. Without additional configurations, Spark defaults to local with the number of partitions set to the number of CPU cores on our local machine (often, this is four).

The sparkContext within a SparkSession is the connection to the cluster and gives us the ability to create and transform RDDs. We can create an RDD from data saved locally using the `parallelize()` function. We can add an argument to specify the number of partitions, which is generally recommended as 2-4 partitions per machine. Otherwise, Spark defaults to the total number of CPU cores.

```python
num_of_partions = 5
dataset_name = [
    ("Chris", 1523, 0.72, "CA"),
    ("Jake", 1555, 0.83, "NY"),
    ("Cody", 1439, 0.92, "CA"),
    ("Lisa", 1442, 0.81, "FL"),
    ("Daniel", 1600, 0.88, "TX"),
    ("Kelvin", 1382, 0.99, "FL"),
    ("Nancy", 1442, 0.74, "TX"),
    ("Pavel", 1599, 0.82, "NY"),
    ("Josh", 1482, 0.78, "CA"),
    ("Cynthia", 1582, 0.94, "CA"),
]

# default setting
rdd_par = spark.sparkContext.parallelize(dataset_name, num_of_partions)
```

We can only view the contents of an RDD by using a special function like `collect()`, which will print the data stored in the RDD. So to view the new RDD in the previous example, we would run the following:

```python
# confirm your RDD contains the correct data
rdd_par.collect()
```

We can verify the number of partitions using the following line:

```python
rdd_par.getNumPartitions()
```

Finally, we need to know how to end our SparkSession when we are finished with our work:

```python
spark.stop()
```

### **Transformation**

Many of the Spark functions we use on RDDs are similar to those we regularly use in Python. We can also use lambda expressions within RDD functions. Lambdas allow us to apply a simple operation to an object in a single line without defining it as a function.

Transformations in Spark are not performed until an action is called. Spark optimizes and reduces overhead once it has the full list of transformations to perform. This behavior is called lazy evaluation. In contrast, eager evaluation is how Pandas transformations behave.

#### Map Function

`map()` applies an operation to each element of the RDD, so it’s often constructed with a lambda expression. This map example adds 1 to each element in our RDD:

```python
rdd = spark.SparkContent.parallelize([1,2,3,4,5])
rdd.map(lambda x: x+1)
# output RDD [2,3,4,5,6]
```

If our RDD contains tuples, we can map the lambda expression to the elements with a specific index value. The following code maps the lambda expression to just the first element of each tuple but keeps the others in the output:

```python
student_data = [
    ("Chris", 1523, 0.72, "CA"),
    ("Jake", 1555, 0.83, "NY"),
    ("Cody", 1439, 0.92, "CA"),
    ("Lisa", 1442, 0.81, "FL"),
    ("Daniel", 1600, 0.88, "TX"),
    ("Kelvin", 1382, 0.99, "FL"),
    ("Nancy", 1442, 0.74, "TX"),
    ("Pavel", 1599, 0.82, "NY"),
    ("Josh", 1482, 0.78, "CA"),
    ("Cynthia", 1582, 0.94, "CA"),
]
student_rdd = spark.sparkContext.parallelize(student_data)
rdd_transformation = student_rdd.map(lambda x: (x[0], x[1], int(x[2] * 100), x[3]))
```

#### Filter Function

`filter()` applies an operation to each element of the RDD, so it’s often constructed with a lambda expression. This map example adds 1 to each element in our RDD:

```python
# input RDD [1,2,NULL,4,5]
rdd.filter(lambda x: x is not None)
# output RDD [1,2,4,5]
```

#### Take Function

In the last exercise, Spark executed our transformations only when the action `collect()` was called to return the entire contents of the new RDD as a list. We generally don’t want to use `collect()` to pull large amounts of data into memory, so we can use `take(n)` to view the first n elements of a large RDD.

```python
# input RDD [1,2,3,4,5]
rdd.take(3)
# output RDD [1,2,3]
```

#### Reduce Function

We can use the action `reduce()` to return fewer elements of our RDD by applying certain operators. For example, say we want to add up all the values in the RDD. We can use `reduce()` with a lambda to add each element sequentially.

```python
# input RDD [1,2,3,4,5]
rdd.reduce(lambda x,y: x+y)
# 15
```

If we are working with a tuple this is how you would deal with it:

```python
sum_gpa = rdd_transformation.map(lambda x: x[2]).reduce(lambda x, y: x + y)
# 843
```

There are limitations to the operations it can apply to RDDs. Namely, `reduce()` must be *commutative* and *associative* due to the nature of parallelized computation.

Example: $1+2+3+4+5=(3+4+5)+(1+2)=(4)+(2+5+1)+(3)=15$.

The output doesn’t depend on the order in which tasks complete (commutative) nor does it depend on how the data is grouped (associative).

#### Glom Function

With the very handy transformation `glom()` we can print out how our data is partitioned and the resulting summation and division of the partitions.

```python
data = [1, 2, 3, 4, 5]
for i in range(1, 5):
    rdd = spark.sparkContext.parallelize(data, i)
    print("partition: ", rdd.glom().collect())
    print("division: ", rdd.reduce(lambda a, b: a / b))

# partition:  [[1, 2, 3, 4, 5]]
# division:  0.008333333333333333
# partition:  [[1, 2], [3, 4, 5]]
# division:  3.3333333333333335
# partition:  [[1], [2, 3], [4, 5]]
# division:  1.875
# partition:  [[1], [2], [3], [4, 5]]
# division:  0.20833333333333331
```

Notice in the output that no matter how our list is being partitioned, the sum is still 15, but the division operation has different solutions based on the partitioning.

#### Broadcast Variables

In Spark, broadcast variables are cached input datasets that are sent to each node. This provides a performance boost when running operations that utilize the broadcasted dataset since all nodes have access to the same data. We would never want to broadcast large amounts of data because the size would be too much to serialize and send through the network.

```python
# dictionary to broadcast
states = {"NY": "New York", "CA": "California", "TX": "Texas", "FL": "Florida"}

# create broadcast variable
broadcastStates = spark.sparkContext.broadcast(states)

# map the broadcast variable to the RDD
rdd_broadcast = rdd_transformation.map(lambda x: (x[0], x[1], x[2], broadcastStates.value[x[3]]))
rdd_broadcast.collect()

# output :
# [('Chris', 1523, 72, 'California'),
#  ('Jake', 1555, 83, 'New York'),
#  ('Cody', 1439, 92, 'California'),
#  ('Lisa', 1442, 81, 'Florida'),
#  ('Daniel', 1600, 88, 'Texas'),
#  ('Kelvin', 1382, 99, 'Florida'),
#  ('Nancy', 1442, 74, 'Texas'),
#  ('Pavel', 1599, 82, 'New York'),
#  ('Josh', 1482, 78, 'California'),
#  ('Cynthia', 1582, 94, 'California')]
```

#### Accumulator Variables

Accumulator variables are shared variables that can only be updated through associative and commutative operations. They are primarily used as counters or sums in parallel computing since they operate on each node separately and adhere to both the associative and commutative properties. Conceptually, they’re similar to the sum and count functions in NumPy.

This seems like a simple concept, but accumulator variables can be very powerful in the right situation. They can keep track of the inputs and outputs of each Spark task by aggregating the size of each subsequent transformation. Instead of counting the number of east or west coast states, we could count the number of NULL values or the resulting size of each transformation. This is important to monitor for data loss.

This doesn’t mean you should add accumulator variables to everything though. It’s best to avoid using accumulators in transformations. Whenever Spark runs into an exception, it will re-execute the tasks. This will incorrectly increment the accumulator. However, Spark will guarantee that this does not happen to accumulators in actions.

Accumulators can be great as debugging or summary tools, but they’re not infallible when used in transformations.

```python
# start the accumlator at zero
sat_1500 = spark.sparkContext.accumulator(0)


def count_high_sat_score(r):
    if r[1] > 1500:
        sat_1500.add(1)


rdd_broadcast.foreach(lambda x: count_high_sat_score(x))

print(sat_1500)
# output: 5
```

#### Transformation Documentation

You may have noticed that each function took an RDD as input and returned an RDD as output. In Spark, functions with this behavior are called transformations. You can find more transformations in the [Official Spark documentation](https://spark.apache.org/docs/latest/rdd-programming-guide.html#transformations).

### **Modules**

The driver program is the core of the Spark application, but there are also modules that have been developed to enhance the utility of Spark. These modules include:

- Spark SQL: an API that converts SQL queries and actions into Spark tasks to be distributed by the cluster manager. This allows for the integration of existing SQL pipelines without redevelopment of code and subsequent testing required for quality control.
- Spark Streaming: a solution for processing live data streams that creates a discretized stream (Dstream) of RDD batches.
- MLlib and ML: machine learning modules for designing pipelines used for feature engineering and algorithm training. ML is the DataFrame-based improvement on the original MLlib module.
- GraphX: a robust graphing solution for Spark. More than just visualizing data, this API converts RDDs to resilient distributed property graphs (RDPGs) which utilize vertex and edge properties for relational data analysis.

While we can directly analyze data using Spark’s Resilient Distributed Datasets (RDDs), we may not always want to perform complicated analysis directly on RDDs. Luckily, Spark offers a module called Spark SQL that can make common data analysis tasks simpler and faster. The name Spark SQL is an umbrella term, as there are several ways to interact with data when using this module. We’ll cover two of these methods using the PySpark API:

- First, we’ll learn the basics of inspecting and querying data in a **Spark DataFrame**.
- Then, we’ll perform these same operations using **standard SQL** directly in our PySpark code.

Before using either method, we must start a `SparkSession`, the entry point to Spark SQL. The session is a wrapper around a `sparkContext` and contains all the metadata required to start working with distributed data. The code below uses `SparkSession.builder` to set configuration parameters and create a new session. In the following example, we set one configuration parameter `(spark.app.name)` and call the `.getOrCreate()` method to initialize the new `SparkSession`.

```python
from pyspark.sql import SparkSession

spark = (
    SparkSession.builder.master("local[2]")  # Use 2 cores instead of all available cores
    .config("spark.driver.memory", "2g")  # Or more, if your machine allows
    .config("spark.app.name", "learning_spark_sql")
    .getOrCreate()
)

type(spark)
# pyspark.sql.session.SparkSession
```

We can access the `SparkContext` for a session with `SparkSession.sparkContext`.

```python
print(spark.sparkContext)
# <SparkContext master=local[*] appName=learning_spark_sql>
```

From here, we can use the `SparkSession` to create `DataFrames`, read external files, register tables, and run SQL queries over saved data. When we’re done with our analysis, we can clear the Spark cache and terminate the session with `SparkSession.stop()`.

### **Spark DataFrame**

A PySpark SQL `DataFrame` is a distributed collection of data with a specific row and column structure. Under the hood, `DataFrames` are built on top of RDDs. Like `pandas`, PySpark SQL `DataFrames` allow a developer to analyze data more easily than by writing functions directly on underlying data.

`DataFrames` can be created manually from RDDs using `rdd.toDF(["column_1", "column_2", "column_3"])`.

```python
sample_page_views = spark.sparkContext.parallelize(
    [
        ["en", "Statue_of_Liberty", "2022-01-01", 263],
        ["en", "Replicas_of_the_Statue_of_Liberty", "2022-01-01", 11],
        ["en", "Statue_of_Lucille_Ball", "2022-01-01", 6],
        ["en", "Statue_of_Liberty_National_Monument", "2022-01-01", 4],
        ["en", "Statue_of_Liberty_play", "2022-01-01", 3],
    ]
)

sample_page_views_df = sample_page_views.toDF(["site_language", "site_page", "date", "views"])
```

Let’s take a look at our new `DataFrame`. We can use the `DataFrame.show(n_rows)` method to print the first `n_rows` of a Spark `DataFrame`. It can also be helpful to pass `truncate=False` to ensure all columns are visible.

```python
sample_page_views_df.show(5, truncate=False)
```

Now that this data is loaded in as a `DataFrame`, we can access the underlying RDD with `DataFrame.rdd`. You likely won’t need the underlying data often, but it can be helpful to keep in mind that a `DataFrame` is a structure built on top of an RDD.

```python
sample_page_views_rdd_restored = sample_page_views_df.rdd

# show restored RDD
sample_page_views_rdd_restored.collect()

# [Row(language_code='en', title='Statue_of_Liberty', date='2022-01-01', count=263),
#  Row(language_code='en', title='Replicas_of_the_Statue_of_Liberty', date='2022-01-01', count=11),
#  Row(language_code='en', title='Statue_of_Lucille_Ball', date='2022-01-01', count=6),
#  Row(language_code='en', title='Statue_of_Liberty_National_Monument', date='2022-01-01', count=4),
#  Row(language_code='en', title='Statue_of_Liberty_play', date='2022-01-01', count=3)]
```

You may notice that the restored RDD is not identical to the original RDD! Although the data is the same, when we converted the data to a DataFrame, PySpark automatically wrapped the original content into a Row. Behind the scenes, rows allow for more efficient calculations over large distributed data.

### **Reading Data**

Let’s take a look at the code we might use to read a CSV. You can refer to the PySpark documentation to explore all available [DataFrameReader](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.html) options and file formats.

```python
# Read CSV to DataFrame
wiki_uniq_df = (
    spark.read.option("header", True)
    .option("delimiter", " ")
    .option("inferSchema", True)
    .csv("views_2022_01_01_000000.csv")
)

# Read Parquet to DataFrame
wiki_uniq_df = spark.read.parquet("views_2022_01_01_000000.parquet")

# Pandas equivalent csv example
wiki_uniq_pandas_df = pd.read_csv("views_2022_01_01_000000.csv", delimiter=" ", header=0)
# Polars equivalent csv example
wiki_uniq_polars_df = pl.read_csv("views_2022_01_01_000000.csv", delimiter=" ")

# Pandas equivalent parquet example
wiki_uniq_pandas_df = pd.read_parquet("views_2022_01_01_000000.parquet")
# Polars equivalent parquet example
wiki_uniq_polars_df = pl.read_parquet("views_2022_01_01_000000.parquet")
```

There are a few things going on in this code, let’s go through them one at a time:

This code uses the `SparkSession.read` function to create a new `DataFrameReader`. The `DataFrameReader` has an `.option('option_name', 'option_value')` method that can be used to instruct Spark how exactly to read a file. In this case, we used the following options:

- `.option('header', True)` — Indicate the file already contains a header row. By default, Spark assumes there is no header.
- `.option('delimiter', ' ')` — Indicates each column is separated by a space (‘ ‘). By default, Spark assumes CSV columns are separated by commas.
- `.option('inferSchema', True)` — Instructs Spark to sample a subset of rows before determining each column’s type. By default, Spark will treat all CSV columns as strings.

The `DataFrameReader` also has a `.csv('path')` method which loads a CSV file and returns the result as a DataFrame.

#### Display Data

There are a few quick ways of checking that our data has been read in properly. The most direct way is checking `DataFrame.show()`.

```python
# Display first 5 rows of DataFrame
wiki_uniq_df.show(5, truncate=False)

# Pandas equivalent csv example
wiki_uniq_pandas_df.head(5)

# Polars equivalent csv example
wiki_uniq_polars_df.head(5)
```

### **Cleaning Data**

Like Pandas, Spark DataFrames offer a series of operations for cleaning, inspecting, and transforming data.

#### Display Column Types

Earlier in the lesson, we mentioned that all DataFrames have a schema that defines their structure, columns, and datatypes. We can use `DataFrame.printSchema()` to show a DataFrame’s schema.

```python
# Display DataFrame schema
wiki_uniq_df.printSchema()

# root
# |-- language_code: string (nullable = true)
# |-- article_title: string (nullable = true)
# |-- hourly_count: integer (nullable = true)
# |-- monthly_count: integer (nullable = true)

# Pandas equivalent csv example
wiki_uniq_pandas_df.dtypes

# Polars equivalent csv example
wiki_uniq_polars_df.dtypes
```

#### Summary Stats

We can then use `DataFrame.describe()` to see a high-level summary of the data by column. The result of `DataFrame.describe()` is a DataFrame in itself, so we append `.show()` to get it to display in our notebook.

```python
wiki_uniq_df_desc = wiki_uniq_df.describe()
wiki_uniq_df_desc.show(truncate=False)

# +-------+-------------+-------------+------------+-------------+
# |summary|language_code|article_title|hourly_count|monthly_count|
# +-------+-------------+-------------+------------+-------------+
# |  count|      4654091|      4654091|     4654091|      4654091|
# |   mean|         null|         null|     4.52417|          0.0|
# | stddev|         null|         null|   182.92502|          0.0|
# |    min|           aa|            -|           1|            0|
# |    max|       zu.m.d|            -|      288886|            0|
# +-------+-------------+-------------+------------+-------------+

# Pandas equivalent csv example
wiki_uniq_pandas_df.describe()

# Polars equivalent csv example
wiki_uniq_polars_df.describe()
```

#### Drop Columns

We can drop fields with `DataFrame.drop("column_1", "column_2", "column_3")`.

```python
# Drop `monthly_count` and display new DataFrame
wiki_uniq_df = wiki_uniq_df.drop("monthly_count")

# Pandas equivalent csv example
wiki_uniq_pandas_df.drop(columns=["monthly_count"], inplace=True)

# Polars equivalent csv example
wiki_uniq_polars_df.drop_in_place("monthly_count")
```

#### Rename Columns

We can replace this misleading header with a better name using `DataFrame.withColumnRenamed()`.

```python
wiki_uniq_df = wiki_uniq_df.withColumnRenamed("article_title", "page_title")

# Pandas equivalent csv example
wiki_uniq_pandas_df.rename(columns={"article_title": "page_title"}, inplace=True)

# Polars equivalent csv example
wiki_uniq_polars_df.rename({"article_title": "page_title"}, in_place=True)
```

### **Querying Data**

PySpark SQL DataFrames have a variety of built-in methods that can help with analyzing data. However, working with DataFrame methods still requires some practice, and the code can become quite verbose. Luckily, we can analyze data in Spark with standard SQL through the `SparkSession.sql()` method.

Before querying a DataFrame with SQL in Spark, it must be saved to the SparkSession’s catalog. The following code saves the DataFrame as a local temporary view in memory. As long as the current SparkSession is active, we can use `SparkSession.sql()` to query it.

```python
wiki_uniq_df.createOrReplaceTempView('wiki_uniq')
```

#### **Selecting Columns**

This is analogous to a SQL `SELECT` clause.

```python
# DataFrame method
wiki_uniq_df.select("language_code", "page_title", "hourly_count").show(5, truncate=False)

# SQL method
query = """
    SELECT language_code, page_title, hourly_count 
    FROM wiki_uniq
"""
spark.sql(query).show(5, truncate=False)

# Pandas equivalent csv example
wiki_uniq_pandas_df[["language_code", "page_title", "hourly_count"]].head(5)

# Polars equivalent csv example
wiki_uniq_polars_df.select(["language_code", "page_title", "hourly_count"]).head(5)
```

#### **Ordering Rows**

This is analogous to a SQL `ORDER BY` clause.

```python
# DataFrame method
wiki_uniq_df.orderBy("hourly_count", ascending=False).show(5, truncate=False)

# SQL method
query = """
    SELECT *
    FROM wiki_uniq
    ORDER BY hourly_count DESC
"""
spark.sql(query).show(5, truncate=False)

# Pandas equivalent csv example
wiki_uniq_pandas_df.sort_values(by="hourly_count", ascending=False).head(5)

# Polars equivalent csv example
wiki_uniq_polars_df.sort("hourly_count", reverse=True).head(5)
```

#### **Filtering Rows**

This is analogous to a SQL `WHERE` clause.

```python
# DataFrame method
wiki_uniq_df.filter(wiki_uniq_df.language_code == "kw.m").show(truncate=False)

# SQL method
query = """
    SELECT *
    FROM wiki_uniq
    WHERE language_code = 'kw.m'
"""
spark.sql(query).show(truncate=False)

# Pandas equivalent csv example
wiki_uniq_pandas_df = wiki_uniq_pandas_df[wiki_uniq_pandas_df.language_code == "kw.m"]

# Polars equivalent csv example
wiki_uniq_polars_df = wiki_uniq_polars_df.filter(wiki_uniq_polars_df.language_code == "kw.m")
```

#### **Aggregating Rows**

This is analogous to a SQL `GROUP BY` clause.

```python
# DataFrame method
wiki_uniq_df.groupBy("language_code").count().show(5, truncate=False)

# SQL method
query = """
    SELECT language_code, COUNT(*)
    FROM wiki_uniq
    GROUP BY language_code
"""
spark.sql(query).show(5, truncate=False)

# Pandas equivalent csv example
wiki_uniq_pandas_df.groupby("language_code").size()

# Polars equivalent csv example
wiki_uniq_polars_df.groupby("language_code").agg(pl.count("language_code"))
```

### **Writing Data**

Once you’ve done some analysis, the next step is often saving the transformed data back to disk for others to use. Similar to the S`parkSession.read()` method, Spark offers a `SparkSession.write()` method.

Because Spark runs all operations in parallel, it’s typical to write DataFrames to a directory of files rather than a single file. We can also use the `mode="overwrite"` argument of the `.csv()` method to overwrite any existing data in the target directory.

Unfortunately, there’s no way for a CSV to retain information about its format. Each time we read it, we’ll need to tell Spark exactly how it must be processed.

Luckily, there is a file format called “Parquet” that’s specially designed for big data and solves this problem among many others. Parquet offers efficient data compression, is faster to perform analysis on than CSV, and preserves information about a dataset’s schema. Let’s try saving and re-reading this file to and from Parquet instead.

```python
# Write DataFrame to Parquet
wiki_uniq_df.write.parquet("cleaned/parquet/views_2022_01_01_000000/", mode="overwrite")

# Write DataFrame to CSV
wiki_uniq_df.write.csv("cleaned/csv/views_2022_01_01_000000/", mode="overwrite")
```
