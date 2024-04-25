Calculate 3 row below it
```python
=SUM(OFFSET(C77, 1, 0, 3, 1))
```
- **C77:** Starting reference cell (replace with your actual starting cell)
    - **1:** Offset 1 rows down.
    - **0:** No offset in columns (we want the same column).
    - **3:** Height of the range (to sum 3 rows)
    - **1:** Width of the range (1 column)
> 1 Row Dow with the Heigh of 3 => 3 Row Down

**Explanation**
1. The `OFFSET` function shifts the reference down 3 rows from your starting cell.
2. It grabs a range of 3 cells in the same column, starting from the offset cell.
3. The `SUM` function then calculates the total of these values.

