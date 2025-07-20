# SQL 🐨

A relational database is a database that organizes information into one or more tables. A table is a collection of data organized into rows and columns. Tables are sometimes referred to as relations.

SQL, Structured Query Language, is a programming language designed to manage data stored in relational databases. SQL operates through simple, declarative statements. This keeps data accurate and secure, and it helps maintain the integrity of databases, regardless of size. SQL statements can be broadly grouped into four different classes, or sub-languages:

- **Data Definition Language (DDL)**: Includes commands used to define the database schema. These commands are used to create and modify the structure of database objects. Examples include CREATE, DROP, ALTER.
- **Data Manipulation Language (DML)**: Includes commands used to modify the data stored in the database. Examples include INSERT, UPDATE, DELETE.
- **Data Query Language (DQL)**: Includes commands for performing queries on data within schema objects, retrieving some schema relation based on the query passed to it. Examples include SELECT retrieves data from the database.
- **Data Control Language (DCL)**: Includes commands dealing with the controls and properties of the DBMS, such as rights and permissions to database objects. Examples include GRANT and REVOKE.

Different Database Management Systems (DBMS) use different variations of standard SQL and each DBMS offers different advantages over the remaining ones for different use cases.

- The most common DBMS in use today is **Microsoft SQL Server (MSSQL)**, which utilizes Transact-SQL (T-SQL), Microsoft’s proprietary SQL variant. Large enterprise applications mostly use SQL Server.
- **SQLite** is a popular open source SQL database. It can store an entire database in a single file. One of the most significant advantages this provides is that all of the data can be stored locally without having to connect your database to a server.
- **PostgreSQL** is an open source SQL database that is not controlled by any corporation. It is typically used for web application development.
- **DuckDB**  is a high-performance, in-memory/in-process analytical database management system designed to execute complex analytical SQL queries fast, efficiently, and reliably over large datasets. It is often referred to as the “SQLite for analytics” due to its lightweight nature and ease of integration. This makes it ideal for analytics tasks, allowing it to run entirely in memory or within an application.
