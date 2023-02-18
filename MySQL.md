# MySQL Research

## General

Source: [MySQL Tutorial for Beginners](https://www.youtube.com/watch?v=7S_tz1z_5bA)

### Install

[MySQL Community Server](https://dev.mysql.com/downloads/mysql/)

### MySQL Workbench Tips

- Data can be entered/altered by typing directly into a table (no query).
- Click the wrench next to a table to view it in design mode. This allows for manipulation of primary key, nullables, so on.

### Creating Databases

- Databases are, themselves, created with and populated by SQL queries: CREATE DATABASE, CREATE TABLE, INSERT INTO, among others.

### Database Objects

- Tables
- Views: combine data from multiple tables
- Stored Procedures: a bit like saved queries
- Functions: a bit like saved queries

### The SELECT Statement

SELECT columns FROM table;

- Additional clauses can be included to make the statement more expressive.
- Two hyphens (--) is the syntax to begin a comment.
- An asterisk (\*) in the SELECT clause will grab all columns.
- Individually named columns are separated by comma.
- Arithmetic expressions can be included in SELECT clause.
- Can give aliases using AS keyword.
- DISTINCT keyword will omit duplicates.
- LIMIT clause will limit the number of records from a query. If the limit is not reached, all will be returned.
- Limits can include an offset as \<LIMIT 6,3\>, which skips the first six records before returning three.

### The WHERE Clause

SELECT columns FROM table WHERE conditions;

- A filter for gathering data.
- \>, \>=, \<, \<=, \=, \!= or \<> are the syntax for relational operators.
- Date comparisons supported, write them in format 'YYYY-MM-DD'.
- AND, OR, NOT are included as keywords.
- AND is always evaluated first, followed in precedence by OR then NOT.
- To use the IN operator, follow it with a list of values enclosed in parentheses.
- To use the BETWEEN operator, follow it with AND-separated bounds (they are inclusive).
- The LIKE operator is used to pattern match strings. For example, consider \<WHERE last_name LIKE b%\>, this would filter strings starting with b.
- In string patterns, the \% represents any number of characters and the \_ represents only one.
- The REGEXP (regular expression) operator can represent more complex string patterns: \^ is begins with, \$ is ends with, \| is or, \[\] specify characters, \- is range.
- IS NULL can be used to search for records with missing values.

### The ORDER BY Clause

SELECT columns FROM table ORDER BY columns;

- Statement can by followed by ASC or DESC to specify the order.
- Each column in the ORDER BY can be sorted differently.
- Data can be sorted by an alias.

## Addendum

### Topics for Further Research

- Hosting data remotely
- Specify relationships
- More on the commands for creating databases and tables
