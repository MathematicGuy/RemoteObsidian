---
category: "_unsorted/Python Bugs.md"
summary: "#### TypeError when accessing sublist from a list
```python
pairs = [[[0, 1, 1, 0, 1], [1, 0, 1, 0, 0]], [[0, 0, 1, 0, 1], [1, 0, 1, 1, 1]], [0, 0, 0, 1, 0]]

def swap_gene_value_at_index(pairs, th..."
keywords: []
confidence: "low"
analyzed_at: "2026-06-01T02:22:41.153230+00:00"
---
#### TypeError when accessing sublist from a list
```python
pairs = [[[0, 1, 1, 0, 1], [1, 0, 1, 0, 0]], [[0, 0, 1, 0, 1], [1, 0, 1, 1, 1]], [0, 0, 0, 1, 0]]

def swap_gene_value_at_index(pairs, threshold):
	for pair in pairs:
		print(pair)
		print('pair0:', pair[0])
		print('pair1:', pair[1][0]) #! TypeError: int is not subscriptable
```
+ ! The reason is, the last list inside `pairs` is not a pair: `[0, 0, 0, 1, 0]`

