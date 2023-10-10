![[Pasted image 20230910233644.png]]
```python
def power(x, n):
  """
  Tính lũy thừa của x mũ n.

  Args:
    x: Số nguyên dương.
    n: Số nguyên dương.

  Returns:
    Lũy thừa của x mũ n.
  """

  if n == 0:
    return 1
  elif n % 2 == 0:
    return power(x * x, n // 2)
  else:
    return x * power(x, n - 1)

print(f"power Even: {power(2,3)}")
print(f"power Odd: {power(3,4)}")


def power_by_divide_and_conquer(x, n):
  """
  Tính lũy thừa của x mũ n bằng phương pháp chia để trị.

  Args:
    x: Số nguyên dương.
    n: Số nguyên dương.

  Returns:
    Lũy thừa của x mũ n.
  """

  if n == 0:
    return 1
  else:
    k = n // 2
    y = power_by_divide_and_conquer(x, k)
    if n % 2 == 0:
      return y * y
    else:
      return x * y * y

even_power = power_by_divide_and_conquer(2, 3)
odd_power = power_by_divide_and_conquer(3, 4)

print(f"power_by_divide_and_conquer Even: {even_power}")
print(f"power_by_divide_and_conquer Odd: {odd_power}")
```
#### Result
![[Pasted image 20230910233821.png]]



![[Pasted image 20230910233652.png]]
```python
def factorial(n):
	"""
  Tính giai thừa của một số nguyên dương.

  Args:
    n: Số nguyên dương.

  Returns:
    Giai thừa của n.
  """

	if n == 0:
		return 1
	else:
		return n * factorial(n - 1)


for i in range(1, 6):
	print(f"factorial_by_divide_and_conquer: {i} - {factorial(i)}")

'''
Việc tính giai thừa đòi hỏi phải nhân tất cả các số vào với nhau 
nên không có cách nào để "chia"
'''
```
#### Result
![[Pasted image 20230910233933.png]]


![[Pasted image 20230910233709.png]]
```python
from itertools import zip_longest

def multiply_polynomials(a, b):
    """
    Multiply two polynomials a and b.

    Args:
        a: The first polynomial.
        b: The second polynomial.

    Returns:
        The polynomial that is the result of the multiplication.
    """
    if len(a) == 0 or len(b) == 0:
        return []
    else:
        n = max(len(a), len(b))
        if n == 1:
            return [a[0] * b[0]]
        a, b = pad_poly(a, n), pad_poly(b, n)
        half = n // 2
        a_low, a_high = a[:half], a[half:]
        b_low, b_high = b[:half], b[half:]
        low = multiply_polynomials(a_low, b_low)
        mid = subtract(multiply_polynomials(add(a_low, a_high), add(b_low, b_high)), add(low, multiply_polynomials(a_high, b_high)))
        high = multiply_polynomials(a_high, b_high)
        return add(shift(low, 2 * half), add(shift(mid, half), high))

def pad_poly(p, n):
    return p + [0] * (n - len(p))

def shift(p, n):
    return [0] * n + p

def add(p1, p2):
    return [a + b for a, b in zip_longest(p1, p2, fillvalue=0)]

def subtract(p1, p2):
    return [a - b for a, b in zip_longest(p1, p2, fillvalue=0)]


a = [1, 2, 3]
b = [4, 5, 6]
print("multiply_polynomials")
print(multiply_polynomials(a, b))


# Devide and Conquer
def multiply_polynomials_by_divide_and_conquer(p1, p2):
    """Multiplies two polynomials using the divide-and-conquer algorithm.
    Args:
        p1 (list): The coefficients of the first polynomial.
        p2 (list): The coefficients of the second polynomial.
    Returns:
        list: The coefficients of the product polynomial.
    """
    # Check that the inputs are valid.
    if not isinstance(p1, list) or not isinstance(p2, list):
        raise ValueError("Inputs must be lists.")
    if len(p1) == 0 or len(p2) == 0:
        raise ValueError("Inputs must not be empty.")

    n = max(len(p1), len(p2))

    # Base case: If either polynomial is of degree 0, then return the product.
    if n == 1:
        return [p1[0] * p2[0]]

    p1, p2 = pad_poly(p1, n), pad_poly(p2, n)

    half = n // 2
    p1_low, p1_high = p1[:half], p1[half:]
    p2_low, p2_high = p2[:half], p2[half:]

    low = multiply_polynomials_by_divide_and_conquer(p1_low, p2_low)
    mid = subtract(multiply_polynomials_by_divide_and_conquer(add(p1_low, p1_high), add(p2_low, p2_high)),
                   add(low, multiply_polynomials_by_divide_and_conquer(p1_high, p2_high)))
    high = multiply_polynomials_by_divide_and_conquer(p1_high, p2_high)

    return add(shift(low, 2 * half), add(shift(mid, half), high))


def pad_poly(p, n):
    return p + [0] * (n - len(p))

def shift(p, n):
    return [0] * n + p

def add(p1, p2):
    return [a + b for a, b in zip_longest(p1, p2, fillvalue=0)]

def subtract(p1, p2):
    return [a - b for a, b in zip_longest(p1, p2, fillvalue=0)]


print("multiply_polynomials_by_divide_and_conquer")
print(multiply_polynomials_by_divide_and_conquer(a, b))
```
#### Result
![[Pasted image 20230910234023.png]]


![[Pasted image 20230910233728.png]]

```python
def count_partitions(n):
    # Khởi tạo mảng dp với tất cả các giá trị là 0
    dp = [0] * (n + 1)
    # Có một cách duy nhất để phân tích số 0
    dp[0] = 1

    # Xét tất cả các số từ 1 đến n
    for i in range(1, n + 1):
        # Xét tất cả các số nhỏ hơn hoặc bằng i
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]

n = 5
print(f"Total partitions of {n} is {count_partitions(n)}")
```
#### Result
![[Pasted image 20230910234837.png]]



![[Pasted image 20230910233736.png]]

```python
# longest_increasing_subsequence(A)
# trả về độ dài của dãy con đơn điệu tăng dài nhất của A
def longest_increasing_subsequence(A):
	n = len(A)
	# Khởi tạo mảng dp với tất cả các giá trị là 1
	dp = [1] * n

	# Xét tất cả các cặp phần tử (i, j) với i < j
	for i in range(1, n):
		for j in range(i):
			# Nếu A[i] > A[j] và dp[i] < dp[j] + 1 thì cập nhật dp[i]
			if A[i] > A[j] and dp[i] < dp[j] + 1:
				dp[i] = dp[j] + 1

	# Trả về độ dài lớn nhất trong mảng dp
	return max(dp)


A = [5, 7, 4, 8, 6, 9]
B = [1, 2, 3, 8, 9, 4, 5, 6, 2, 3, 9, 10]

print(f"Độ dài của dãy con đơn điệu tăng dài nhất của {A} là: {longest_increasing_subsequence(A)}")
print(f"Độ dài của dãy con đơn điệu tăng dài nhất của {B} là: {longest_increasing_subsequence(B)}")

```
#### Result
![[Pasted image 20230910235746.png]]

