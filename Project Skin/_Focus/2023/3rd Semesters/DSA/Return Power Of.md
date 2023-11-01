> Dưới đây là thuật toán đệ quy tính lũy thừa của một số nguyên dương trong Python:
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
```

**Để hiểu rõ hơn về thuật toán này, chúng ta có thể thực hiện theo các bước sau:**
1. Nếu n = 0, thì x^n = 1.
2. Nếu n là số chẵn, thì x^n = (x^2)^n/2.
3. Nếu n là số lẻ, thì x^n = x * x^(n-1).

> Ví dụ:
```Python
>>> power(2, 3)
8
>>> power(3, 4)
81
```

> Dưới đây là thuật toán chia để trị tính lũy thừa của một số nguyên dương trong Python:
```Python
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
```

**Để hiểu rõ hơn về thuật toán này, chúng ta có thể thực hiện theo các bước sau:
**1. Chia n thành hai phần bằng nhau, k = n // 2.
2. Tính x^k.
3. Nếu n là số chẵn, thì x^n = (x^k)^2.
4. Nếu n là số lẻ, thì x^n = x * (x^k)^2.

Ví dụ:
```Python
>>> power_by_divide_and_conquer(2, 3)
8
>>> power_by_divide_and_conquer(3, 4)
81
```

> **Cả hai thuật toán đều có thời gian chạy là O(log n).**