0x0E. SQL - More queries

Basic query operation: the join

The join operation in SQL allows you to combine rows from two or more tables based on a specified relationship between them. It helps you retrieve related data from multiple tables in a single result set. There are different types of join operations available, including:

1. INNER JOIN:
   - Returns only the rows that have matching values in both tables being joined.
   - Syntax:
     ```sql
     SELECT columns
     FROM table1
     INNER JOIN table2 ON join_condition;
     ```

2. LEFT JOIN (or LEFT OUTER JOIN):
   - Returns all rows from the left (first) table and the matched rows from the right (second) table. If there is no match, NULL values are returned for the right table columns.
   - Syntax:
     ```sql
     SELECT columns
     FROM table1
     LEFT JOIN table2 ON join_condition;
     ```

3. RIGHT JOIN (or RIGHT OUTER JOIN):
   - Returns all rows from the right (second) table and the matched rows from the left (first) table. If there is no match, NULL values are returned for the left table columns.
   - Syntax:
     ```sql
     SELECT columns
     FROM table1
     RIGHT JOIN table2 ON join_condition;
     ```

4. FULL JOIN (or FULL OUTER JOIN):
   - Returns all rows from both tables, matching rows where possible and including NULL values where there is no match.
   - Syntax:
     ```sql
     SELECT columns
     FROM table1
     FULL JOIN table2 ON join_condition;
     ```

5. CROSS JOIN:
   - Returns the Cartesian product of the two tables, producing a result set with all possible combinations of rows from both tables.
   - Syntax:
     ```sql
     SELECT columns
     FROM table1
     CROSS JOIN table2;
     ```

When using joins, you need to specify the join condition, which is the relationship between the tables based on shared columns or expressions. The join condition is typically specified using the ON keyword, followed by the columns involved in the relationship.

By leveraging joins, you can combine data from different tables based on common values, establish relationships between tables, and retrieve the desired information in a single query.
