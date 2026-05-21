1. B
2. B
3. A
4. B
5. C 
6. B
7. B
8. A 
9. A 
10. B 
11. A
12. A
13. B
14. B
15. A
16. B
17. B
18. A
19. A
20. B
21. C
22. B
23. B
24. C
25. A
26. A (4)
27. B 
28. D
29. C
30. B
31. A
32. C
33. A
34. A
35. C
36. B
37. A 
38. C
39. A
40. B
41. A
42. B
43. C
44. C
45. D
46. Calculate Mean
```python
class Solution:
    def calculate_mean(self, X):
        N = len(X)
        return np.sum(X) / N
```
47. Calculate Median
```python
class Solution:
    def calculate_median(self, X):
        X = sorted(X)
        n = len(X)
        if n % 2 == 0:
            median = (X[n // 2 - 1] + X[n // 2]) / 2
        else:
            median = X[n // 2]
        return median
```
48. Calculate Variance and Standard Variance
```python
class Solution:
    def calculate_variance_std(self, data):
        # Calculate the mean
        mean = np.sum(data) / len(data)
        
        # Calculate the variance
        variance = np.sum((data - mean)**2) / len(data)

        # Calculate the standard deviation
        std_dev = np.sqrt(variance)

        return variance, std_dev
```
49. Calculate Correlation Coefficient
```python
    def calculate_correlation_coefficient(self, X, Y):
        p = 0
        n = len(X)

        bot_x = np.sum(n * np.sum(X**2) - sum(X)**2)
        bot_y = np.sum(n * np.sum(Y**2) - sum(Y)**2)
        top = n*np.sum(np.dot(X, Y)) - np.dot(np.sum(X), np.sum(Y))
        bot = np.sqrt(bot_x) * np.sqrt(bot_y)
        p = round(top / bot, 2)

        if p == float('nan'):
            return -1

		return p
```
50. Calculate Dot Product
```python
class Solution:
    def calculate_dot_product(self, v, u):
        return np.dot(v, u)
```
51. Calculate Matrix Product
```python
class Solution:
    def calculate_matrix_product(self, A, B):
        A = np.array(A, dtype=np.float32)
        B = np.array(B, dtype=np.float32)

        if A.shape[0] != B.shape[1]:
            return -1

        return np.dot(A, B)
```
52. Eigen Value and Eigen Vector
```python
import math

class Solution:
    def calculate_eigenvalues_eigenvectors(self, A):
        def get_eigenvalues(matrix):
            # Your code here

            return eigenvalue1, eigenvalue2

        def get_eigenvectors(matrix, eigenvalue):
            # Your code here

            return eigenvector1, eigenvector2

        return {eigenvalbbue1: eigenvector1, eigenvalue2: eigenvector2}
```
52. Cosine Similarity
```python
class Solution:
    def cosine_similarity(self, X, Y):
        if len(X) != len(Y):
            return -1

        top = 0
        bot_x = 0
        bot_y = 0

        for x, y in zip(X, Y):
            print(x, y)
            top += (x*y)
            bot_x += x**2
            bot_y += y**2

        return top / (math.sqrt(bot_x) * math.sqrt(bot_y))
```
