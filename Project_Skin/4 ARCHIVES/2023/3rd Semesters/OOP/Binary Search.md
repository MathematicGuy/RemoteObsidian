#### **Why M = L + ((R - L) / 2) instead of M=(L+R)/2 avoid overflow in C++?**
Because it does...

Let's assume for a minute you're using unsigned chars (same applies to larger integers of course).

If L is 100 and R is 200, the first version is:
**> M = (100 + 200) / 2 = 300 / 2 = 22**

100+200 overflows **(because the largest unsigned char is 255)**, and you get 100+200=44 (unsigned no. addition).

The second, on the other hand:
**> M = 100 + (200-100) / 2 = 100 + 100 / 2 = 150**

No overflow.

As @user2357112 pointed out in a comment, there are no free lunches. **If L is negative, the second version might not work while the first will.**



