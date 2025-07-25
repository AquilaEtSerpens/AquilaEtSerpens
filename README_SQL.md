# SQL Query Solution

## Problem Statement
Complete the SQL query to count gold medals per country and gender for the 2004 Olympics, focusing on Nordic countries (Denmark, Norway, Sweden).

## Solution
The completed query fills in the missing fields with `Country` and `Gender` to properly group and display the medal counts.

### Query Logic
- **SELECT**: Returns Country, Gender, and count of gold medals
- **WHERE**: Filters for 2004 Olympics, gold medals only, and Nordic countries (DEN, NOR, SWE)
- **GROUP BY**: Groups results by Country and Gender for proper aggregation
- **ORDER BY**: Sorts results alphabetically by Country, then by Gender

### Expected Output
The query will return results showing gold medal counts for each gender within each country, such as:
- DEN Female: X medals
- DEN Male: Y medals  
- NOR Female: X medals
- NOR Male: Y medals
- SWE Female: X medals
- SWE Male: Y medals

See `medals_query.sql` for the complete implementation.