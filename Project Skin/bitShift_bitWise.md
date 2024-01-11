128  64 32 16 8 4 2 1

```c
if (n & (1 << 2)) {
  n &= ~(1 << 2);
}
```
1. `1 << 2`: This is a left shift operation. It shifts the bits of the number `1` two places to the left. In binary, `1` is `0001`. After shifting two places to the left, it becomes `0100`, which is `4` in decimal.
    
2. `num & (1 << 2)`: This is a bitwise AND operation. It checks if the third bit (from the right, 0-indexed) of `num` is set (i.e., if it's `1`). If the third bit is set, the result is `4` (`0100` in binary), otherwise it's `0`.
    
3. `~(1 << 2)`: This is a bitwise NOT operation. It flips all the bits of the number `1 << 2` (`0100` in binary). So `~(1 << 2)` is `1011` in binary, which is `-5` in decimal if we consider it as a signed integer.
    
4. `num &= ~(1 << 2)`: This is a bitwise AND operation followed by an assignment. It clears the third bit of `num`. It does this by ANDing `num` with `~(1 << 2)`. Since `~(1 << 2)` has all bits set except the third one, ANDing it with `num` will leave all bits of `num` unchanged, except the third bit, which will be cleared (set to `0`).

+ ! So, in summary, this code checks if the third bit of `num` is set, and if it is, it clears that bit


Bitwise operations are operations that directly manipulate the bits of binary numbers. Here are the most common bitwise operations:

1. **Bitwise AND (`&`):** The bitwise AND operation takes two numbers as operands and does AND on every bit of two numbers. The result of AND is 1 only if both bits are 1.
```c
int a = 12; // binary: 1100
int b = 10; // binary: 1010
int result = a & b; // result is 8 (binary: 1000)
```
   
2. **Bitwise OR (`|`):** The bitwise OR operation takes two numbers as operands and does OR on every bit of two numbers. The result of OR is 1 if any of the two bits is 1.
```c
int a = 12; // binary: 1100
int b = 10; // binary: 1010
int result = a | b; // result is 14 (binary: 1110)
```

3. **Bitwise XOR (`^`):** The bitwise XOR operation takes two numbers as operands and does XOR on every bit of two numbers. The result of XOR is 1 if the two bits are different.
```c
int a = 12; // binary: 1100
int b = 10; // binary: 1010
int result = a ^ b; // result is 6 (binary: 0110)
```


4. **Bitwise NOT (`~`):** The bitwise NOT operation takes one number and inverts all bits of it.
```c
int a = 12; // binary: 1100
int result = ~a; // result is -13 (binary: 11111111111111111111111111110011)
```

5. **Left shift (`<<`):** The left shift operation shifts the bits of the number to the left by the specified number of positions. Each shift to the left doubles the number.
```c
int a = 5; // binary: 0101
int result = a << 1; // result is 10 (binary: 1010)
```

6. **Right shift (`>>`):** The right shift operation shifts the bits of the number to the right by the specified number of positions. Each shift to the right halves the number.
```c
int a = 10; // binary: 1010
int result = a >> 1; // result is 5 (binary: 0101)
```

### convert all the value 1 to 0 from the 3rd value of m 
```c
//! Ex 2
// Check 3rd bit and set 0 if it is 1. 
// Ex: 1 = 0001 (1 << 2) shift the bit two places to the left: 0001 -> 0100 which is 4 in decimal
// n & (1 << 2). On the right side we have 1 as the 3rd bit. 
// AND: 00 -> 0, 01 -> 0, 10 -> 0, 11 -> 1. So if n 3rd bit is 1, the result of n & (1 << 2) will be 1

m = n;
printf("before: %d\n", m);
// 1100 = 12
if (m & (1 << 2)){ // 1100 & 0100 = 1110 = 14 -> 3rd bit = 1 = True. If True then run the condition 
  m &= ~(1 << 2); // 1100 & 1011 = 1000 = 8 -> 3rd bit  = 0. Successfully convert 3rd of m from 1 to 0.
}

printf("after: %d\n", m);
```
+ If `m` is initially set to 4, the output will be as follows:
	
	The binary representation of 4 is `100`. The third bit (counting from the right, starting from 0) is 1.
	
	The line `if (m & (1 << 2))` checks if the third bit of `m` is 1. In this case, it is, so the condition is true.
	
	Then, the line `m &= ~(1 << 2);` clears the third bit of `m`. This changes `m` from `100` (4 in decimal) to `000` (0 in decimal).
+ if m = 12  = 1100 then the output will be 8
	1100 & 1011 = 1000 = 8 -> 3rd bit  = 0. Successfully convert 3rd of m from 1 to 0.

### convert all the value 0 to 1 from the 3rd value of m use 7 in bit 0111
0111 <-> 0000 0000 0111
-> 0111 = 1111 1111 1000 (use this to convert all 0 to 1 using XOR |= )
Ex: `16 = 10000 -> 16 | ~(7) = 0001_0000 | 1111_1000 = 1111_1000`   
-> 16 | ~ (7) turn 16 from 0001_0000 to 1111_1000 
```c
// convert all the value 0 to 1 from the 3rd value of m 
if (m & 1 << 2){ 
  m |= 7; // 7 = 111
  // ex: m = 44 = 101100 -> 0010 1100 & 0000 0111 = 0000 0100 = 4
}
printf("m |=  %d", m);
```


`0xFF` ->  (in binary: 0000000011111111)
