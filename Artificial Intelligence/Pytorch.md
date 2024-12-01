**Create zeros matrix**
```python
import torch

amount_boxes = torch.zeros([2, 3])
print(amount_boxes)

# output
tensor([[0., 0., 0.],
        [0., 0., 0.]])
```

**Slicing (Extract elements while retaining tensors dimensions)**
```python
import torch

# Create a 3D tensor
tensor = torch.rand(2, 3, 4)
print(tensor)

# Using [..., 0:1]
result_slice = tensor[..., 0:1]
print("Shape with slicing:", result_slice.shape)

# Using [..., 0]
result_index = tensor[..., 0]
print("Shape with indexing:", result_index.shape)
```
```python
# output:
tensor([[[0.9826, 0.4277, 0.6385, 0.3960],
         [0.7635, 0.1746, 0.4837, 0.1429],
         [0.1696, 0.7933, 0.3067, 0.8841]],

        [[0.8951, 0.5398, 0.3310, 0.0974],
         [0.6731, 0.6795, 0.1445, 0.0182],
         [0.5267, 0.1939, 0.8648, 0.9479]]])
         
Shape with slicing: torch.Size([2, 3, 1]) # 2 rows, 3 cols, 1 depth (the 3rd Dimension)
Shape with indexing: torch.Size([2, 3])
```

