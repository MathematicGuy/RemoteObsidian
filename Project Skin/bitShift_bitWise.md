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
