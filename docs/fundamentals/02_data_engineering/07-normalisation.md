# **Normalisation** 🧙🏻‍♂️

Normalization is a process in database design that organizes data to reduce redundancy and improve data integrity. The goal is to divide large tables into smaller ones and establish relationships between them using primary and foreign keys. This process follows a series of "normal forms" (rules), each building on the previous one.

The goal of normalization is efficiency in transactional databases (OLTP systems). A *Star Schema* is a denormalized data model primarily used in data warehousing and analytics tools like Power BI to optimize query performance for reporting and analysis.

Unnormalized Table (UNF)
Imagine a table storing information about customers and their orders:

| CustomerID | CustomerName | OrderID | Product | Quantity |
| - | - | - | - | - |
| 1 | Alice | 101 | Laptop, Smartphone | 1|
| 2 | Bob | 103 | Tablet | 1 |

Problems:

- Data redundancy: CustomerName is repeated for every order.
- Update anomaly: If Alice changes her name, multiple rows must be updated.
- Insertion anomaly: Adding a new customer without an order is problematic.
- Deletion anomaly: Deleting all orders of a customer also removes their details.

## **First Normal Form (1NF)**

1NF removes duplicate columns and ensures each field contains only atomic (indivisible) values.

| CustomerID | CustomerName | OrderID | Product | Quantity |
| - | - | - | - | - |
| 1 | Alice | 101 | Laptop | 1|
| 1 | Alice | 102 | Smartphone | 1 |
| 2 | Bob | 103 | Tablet | 1 |

## **Second Normal Form (2NF)**

2NF eliminates partial dependencies. A table is in 2NF if:

- It is in 1NF.
- All non-key columns depend on the entire primary key, not just a part of it.

In the table above, CustomerName depends only on CustomerID, not the entire key (CustomerID, OrderID).

### **Customers Table 2NF**

| CustomerID | CustomerName |
|------------|--------------|
| 1          | Alice        |
| 2          | Bob          |

### **Orders Table 2NF**

| OrderID | CustomerID | Product    | Quantity |
|---------|------------|------------|----------|
| 101     | 1          | Laptop     | 1        |
| 102     | 1          | Smartphone | 2        |
| 103     | 2          | Tablet     | 1        |

## **Third Normal Form (3NF)**

3NF eliminates transitive dependencies. A table is in 3NF if:

- It is in 2NF.
- No non-key column depends on another non-key column.

If we add a Category column to the Orders table that describes the product (e.g., "Electronics"), this creates a dependency between Product and Category.

### **Customers Table 3NF**

| CustomerID | CustomerName |
|------------|--------------|
| 1          | Alice        |
| 2          | Bob          |

### **Orders Table 3NF**

| OrderID | CustomerID | Product    | Quantity |
|---------|------------|------------|----------|
| 101     | 1          | Laptop     | 1        |
| 102     | 1          | Smartphone | 2        |
| 103     | 2          | Tablet     | 1        |

### **Products Table**

| Product    | Category    |
|------------|-------------|
| Laptop     | Electronics |
| Smartphone | Electronics |
| Tablet     | Electronics |
