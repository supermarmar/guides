# Data Engineering 🛠️

## Introduction

Data Engineers make data usable. They build and monitor data pipelines, automate cleaning tasks, ensure data validity, manage ingestion, and are at the center of any data-driven organization.

The role of a Data Engineer is often compared to a plumber. They both make sure that a vital resource is delivered without leaks or contamination. In a perfect world, they also clean it up and develop tools for the end user to control the flow. Data Engineers are often compared to librarians as well: they won’t do your research for you, but they will make sure the resources you need are properly cataloged and accessible. When a team at a company needs data, it is the data engineer’s job to make sure the data they need exists and is organized in a database or business intelligence tool.

While there are user interfaces for building new tables in databases, data engineers often need to work with databases directly using computer programming languages like Python and SQL.

While Data Engineers are not themselves Data Scientists, the two teams work closely together to develop and deploy advanced analytics studies and models.

Data scientists work on the development side of this partnership, using tools like Python pandas to create models and analyses. But even the most advanced models aren’t that useful if they aren’t regularly updated with new data or published in an accessible location. Enter the data engineers! Once a data model or study is prepared by data scientists, data engineers deploy it by creating automated data pipelines that

- regularly update the data
- test for and log any errors
- load the output to a cloud or business intelligence tool

## Data

Data is a collection of facts such as numbers, descriptions, and observations used to record information. Data structures in which this data is organized often represent entities that are important to an organization (such as customers, products, sales orders, and so on). Each entity typically has one or more attributes, or characteristics (for example, a customer might have a name, an address, a phone number, and so on). You can classify data as structured, semi-structured, or unstructured.

### Structured Data

Structured data is data that adheres to a fixed schema, so all of the data has the same fields or properties. Most commonly, the schema for structured data entities is tabular - in other words, the data is represented in one or more tables that consist of rows to represent each instance of a data entity, and columns to represent attributes of the entity. For example, the following image shows tabular data representations for Customer and Product entities.

| ID | FirstName | LastName | Email |
| - | - | - | - |
| 1 | Mario | Ervedosa | <mario.ervedosa@gmail.com> |

### Semi-structured Data

Semi-structured data is information that has some structure, but which allows for some variation between entity instances. For example, while most customers may have an email address, some might have multiple email addresses, and some might have none at all.

One common format for semi-structured data is JavaScript Object Notation (JSON). The example below shows a pair of JSON documents that represent customer information. Each customer document includes address and contact information, but the specific fields vary between customers.

```json
# Customer 1
{
  "firstName": "Joe",
  "lastName": "Jones",
  "address":
  {
    "streetAddress": "1 Main St.",
    "city": "New York",
    "state": "NY",
    "postalCode": "10099"
  },
  "contact":
  [
    {
      "type": "home",
      "number": "555 123-1234"
    },
    {
      "type": "email",
      "address": "joe@litware.com"
    }
  ]
}

# Customer 2
{
  "firstName": "Samir",
  "lastName": "Nadoy",
  "address":
  {
    "streetAddress": "123 Elm Pl.",
    "unit": "500",
    "city": "Seattle",
    "state": "WA",
    "postalCode": "98999"
  },
  "contact":
  [
    {
      "type": "email",
      "address": "samir@northwind.com"
    }
  ]
}
```

### Unstructured Data

Not all data is structured or even semi-structured. For example, documents, images, audio and video data, and binary files might not have a specific structure. This kind of data is referred to as unstructured data.

## File Storage

The specific file format used to store data depends on a number of factors, including:

- The type of data being stored (structured, semi-structured, or unstructured).
- The applications and services that will need to read, write, and process the data.
- The need for the data files to be readable by humans, or optimized for efficient storage and processing.

### Delimited Text Files

Data is often stored in plain text format with specific field delimiters and row terminators. The most common format for delimited data is comma-separated values (CSV) in which fields are separated by commas, and rows are terminated by a carriage return / new line. Optionally, the first line may include the field names. Other common formats include tab-separated values (TSV) and space-delimited (in which tabs or spaces are used to separate fields), and fixed-width data in which each field is allocated a fixed number of characters. Delimited text is a good choice for structured data that needs to be accessed by a wide range of applications and services in a human-readable format.

```csv
FirstName,LastName,Email
Joe,Jones,joe@litware.com
Samir,Nadoy,samir@northwind.com
```

### JavaScript Object Notation (JSON)

JSON is a ubiquitous format in which a hierarchical document schema is used to define data entities (objects) that have multiple attributes. Each attribute might be an object (or a collection of objects); making JSON a flexible format that's good for both structured and semi-structured data.

The following example shows a JSON document containing a collection of customers. Each customer has three attributes (firstName, lastName, and contact), and the contact attribute contains a collection of objects that represent one or more contact methods (email or phone). Note that objects are enclosed in braces ({..}) and collections are enclosed in square brackets ([..]). Attributes are represented by name : value pairs and separated by commas (,).

### Binary Large Object (BLOB)

Ultimately, all files are stored as binary data (1's and 0's), but in the human-readable formats discussed above, the bytes of binary data are mapped to printable characters (typically through a character encoding scheme such as ASCII or Unicode). Some file formats however, particularly for unstructured data, store the data as raw binary that must be interpreted by applications and rendered. Common types of data stored as binary include images, video, audio, and application-specific documents.

When working with data like this, data professionals often refer to the data files as BLOBs (Binary Large Objects).

### Optimized File Formats

While human-readable formats for structured and semi-structured data can be useful, they're typically not optimized for storage space or processing. Over time, some specialized file formats that enable compression, indexing, and efficient storage and processing have been developed. Some common optimized file formats you might see include Avro, ORC, and Parquet.

## Databases

A database is used to define a central system in which data can be stored and queried. In a simplistic sense, the file system on which files are stored is a kind of database; but when we use the term in a professional data context, we usually mean a dedicated system for managing data records rather than files.

### Relational Databases

Relational databases are commonly used to store and query structured data. The data is stored in tables that represent entities, such as customers, products, or sales orders. Each instance of an entity is assigned a primary key that uniquely identifies it; and these keys are used to reference the entity instance in other tables. For example, a customer's primary key can be referenced in a sales order record to indicate which customer placed the order. This use of keys to reference data entities enables a relational database to be normalized; which in part means the elimination of duplicate data values so that, for example, the details of an individual customer are stored only once; not for each sales order the customer places. The tables are managed and queried using Structured Query Language (SQL), which is based on an ANSI standard, so it's similar across multiple database systems.

### NoSQL Databases

Non-relational databases are data management systems that don’t apply a relational schema to the data. Non-relational databases are often referred to as NoSQL database, even though some support a variant of the SQL language. There are four common types of Non-relational database commonly in use.

1. Key-value databases in which each record consists of a unique key and an associated value, which can be in any format.
2. Document databases, which are a specific form of key-value database in which the value is a JSON document (which the system is optimized to parse and query)
3. Column family databases, which store tabular data comprising rows and columns, but you can divide the columns into groups known as column-families. Each column family holds a set of columns that are logically related together.
4. Graph databases, which store entities as nodes with links to define relationships between them.

### OLTP

Transactional systems are often high-volume, sometimes handling many millions of transactions in a single day. The data being processed has to be accessible very quickly. The work performed by transactional systems is often referred to as Online Transactional Processing (OLTP).

OLTP solutions rely on a database system in which data storage is optimized for both read and write operations in order to support transactional workloads in which data records are created, retrieved, updated, and deleted (often referred to as CRUD operations). These operations are applied transactionally, in a way that ensures the integrity of the data stored in the database. To accomplish this, OLTP systems enforce transactions that support so-called ACID semantics:

- Atomicity – each transaction is treated as a single unit, which succeeds completely or fails completely. For example, a transaction that involved debiting funds from one account and crediting the same amount to another account must complete both actions. If either action can't be completed, then the other action must fail.
- Consistency – transactions can only take the data in the database from one valid state to another. To continue the debit and credit example above, the completed state of the transaction must reflect the transfer of funds from one account to the other.
- Isolation – concurrent transactions cannot interfere with one another, and must result in a consistent database state. For example, while the transaction to transfer funds from one account to another is in-process, another transaction that checks the balance of these accounts must return consistent results - the balance-checking transaction can't retrieve a value for one account that reflects the balance before the transfer, and a value for the other account that reflects the balance after the transfer.
- Durability – when a transaction has been committed, it will remain committed. After the account transfer transaction has completed, the revised account balances are persisted so that even if the database system were to be switched off, the committed transaction would be reflected when it is switched on again.

## Jupyter to Python

Data scientists work in Jupyter Notebooks. Jupyter Notebooks are browser-based workspaces that help data scientists quickly prototype analytics and visualizations. A data engineer's first task is to transform the notebook into a Python script that can be run on its own outside of the notebook environment.

While doing this, data engineer will also add unit tests, pieces of code that check to make sure the program is working as expected, and log errors if not. These tests weren’t strictly necessary for the Jupyter Notebook, which was always run directly by a data scientist. The Python version of the script will be run by a computer process, and so needs controls in place to stop it from improperly updating the study if something goes wrong.
