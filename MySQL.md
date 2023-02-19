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

### Inner JOINs

SELECT columns FROM table JOIN table ON conditions;

- Ambiguous columns, those that exist in either table, must be prefixed with the name of their table.
- Table names aliased by first letter, as convention.
- You can join across multiple databases by adding an extra layer to the dot operator chain (e.g., database.table.column).
- Tables can be joined with themselves, but each instance must be given a different alias. Otherwise the syntax is about the same.
- JOINs can be chained to join several tables at the same time, this is common.
- Compound conditions can be used to represent composite primary keys, among other things. These are made as typical compound boolean statements.
- Implicit join syntax allows for omitting JOIN in lieu of commas. Avoid this, it's dangerous.
- Natural JOINs are done without specifying column names, common columns are used. Once again, this is dangerous.

### Outer JOINs

SELECT columns FROM table LEFT/RIGHT JOIN table ON conditions;

- In SQL, there are LEFT and RIGHT JOINs.
- LEFT JOIN will return all records from the left table, regardless of the condition.
- RIGHT JOIN will return all records from the right table, regardless of the condition.
- Only the speficied unmatched records will be returned. That is, in a LEFT JOIN, unmatched records in the right table won't be returned.
- Outer joins can still be chained for several tables. In these chains, outer and inner joins can be mixed.
- As a best practice, avoid using right joins. Keeping the direction consistent will make code more readable.
- Outer joins can also be done on self.

### The USING Clause

SELECT columns FROM table JOIN table USING (columns);

- USING is syntax for the simplification of join conditions.
- It does the same job as an equality comparison between columns of different tables.
- Columns must have the same name in either table for it to work.

### Cross JOINs

SELECT columns FROM table CROSS JOIN table;

- Every record from one table joins every record from another.
- There are no conditions.
- This is sometimes referred to as the cartesian product between tables. It can be used to yield all possible combinations.
- Again, implicit syntax can be used here.

### UNIONs

query UNION query

- Combine data from multiple queries by row.
- The quieries involved don't have to be against the same table.

## Addendum

### Topics for Further Research

- Hosting data remotely
- Specify relationships
- More on the commands for creating databases and tables
