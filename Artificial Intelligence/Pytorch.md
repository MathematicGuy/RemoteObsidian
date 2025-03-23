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


----
# Model Training 

### Basic Import
```python
# Import necessary modules
from torchtext.datasets import AG_NEWS                     # Built-in dataset (news classification)
from torch.utils.data import random_split, DataLoader     # Splitting and loading data
from torchtext.data.utils import get_tokenizer            # Standard tokenizer utility
from torchtext.vocab import build_vocab_from_iterator     # Build vocab from token generator
from torchtext.data.functional import to_map_style_dataset # Convert iterable dataset to indexable
from torch.nn.utils.rnn import pad_sequence               # Pad sequences for batching
import torch
```

### 1. Tokenizer and Vocabulary
```python
tokenizer = get_tokenizer("basic_english")  # Load basic English tokenizer (lowercase, punctuation split)

# Helper to yield tokens from the dataset for building vocab
def yield_tokens(data_iter):
    for _, text in data_iter:               # Ignore label, just get text
        yield tokenizer(text)               # Tokenize text

train_iter = AG_NEWS(split='train')         # Load training split

# Build vocabulary using tokenized text
vocab = build_vocab_from_iterator(yield_tokens(train_iter), specials=["<unk>"])
vocab.set_default_index(vocab["<unk>"])     # Set unknown token index for out-of-vocab words
```

### Reload Iterator
```python
train_iter = AG_NEWS(split='train')  # Iterator was exhausted, reload to use again
```

### 2. Text and Label Pipelines
```python
# Convert string text to list of token IDs
def text_pipeline(text):
    return vocab(tokenizer(text))

# Convert label (1-based) to 0-based index (starting from 0 instead of 1)
def label_pipeline(label):
    return int(label) - 1
```

### 3. Convert Dataset to Tensor and Pad missing Value for Batching
```python
def collate_batch(batch):
    label_list, text_list = [], []

    for label, text in batch:
        label_list.append(label_pipeline(label))  # Process label
        processed_text = torch.tensor(text_pipeline(text), dtype=torch.int64)  # Tokenize and convert to tensor
        text_list.append(processed_text)

    # Pad all sequences to the same length in the batch
    text_batch = pad_sequence(text_list, batch_first=True, padding_value=vocab['<unk>'])
    label_batch = torch.tensor(label_list, dtype=torch.int64)  # Combine labels into one tensor

    return text_batch, label_batch  # Return padded input and label batch
```


### 4. Split Dataset into Train/Validation 
```python
train_dataset = to_map_style_dataset(train_iter)  # Convert to indexable dataset
num_train = int(len(train_dataset) * 0.95)         # 95% for training
split_train_, split_valid_ = random_split(train_dataset, [num_train, len(train_dataset) - num_train])  # Split
```

### 5. Dataloaders
+ ? Load train/test/valid data and convert them into batches using collate_batch function through collate_fn
```python
BATCH_SIZE = 64  # Adjust batch size depending on GPU RAM

train_loader = DataLoader(split_train_, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_batch)
valid_loader = DataLoader(split_valid_, batch_size=BATCH_SIZE, shuffle=False, collate_fn=collate_batch)

# Also prepare test set
test_dataset = to_map_style_dataset(AG_NEWS(split='test'))
test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False, collate_fn=collate_batch)
```

### 6. Training 
```python
def train(model, dataloader, optimizer, criterion, device):
    model.train()  # Set model to training mode
    total_loss, total_correct = 0, 0

    for inputs, labels in dataloader:
        inputs, labels = inputs.to(device), labels.to(device)  # Move data to GPU/CPU

        optimizer.zero_grad()           # Clear previous gradients
        outputs = model(inputs)         # Forward pass
        loss = criterion(outputs, labels)  # Compute loss
        loss.backward()                 # Backpropagate
        optimizer.step()                # Update weights

        total_loss += loss.item()       # Accumulate loss
        total_correct += (outputs.argmax(1) == labels).sum().item()  # Count correct predictions

    return total_loss / len(dataloader), total_correct / len(dataloader.dataset)

```
+ [[zero_grad]]: Clear out the `gradient` $\frac{\partial L}{\partial w}$ used to update weights $w_{i} = w_{i-1} - \alpha.\frac{\partial L}{\partial w}$ after each Back Propagation. 
	**Training _without_ `zero_grad()`**:  
	+  You're accumulating gradients across multiple batches before updating weights — this **simulates large batch gradient descent**.
	**Training _with_ `zero_grad()`**:  
	+ You update weights **after each batch**, then clear gradients — this follows **standard mini-batch stochastic gradient descent**.
	
### 7. Evaluation
```python
def evaluate(model, dataloader, criterion, device):
    model.eval()  # Set model to evaluation mode
    total_loss, total_correct = 0, 0

    with torch.no_grad():  # No gradient computation
        for inputs, labels in dataloader:
            inputs, labels = inputs.to(device), labels.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, labels)

            total_loss += loss.item()
            total_correct += (outputs.argmax(1) == labels).sum().item()

    return total_loss / len(dataloader), total_correct / len(dataloader.dataset)
```

### 8. Training Loop
```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")  # Use GPU if available

model = TextClassificationModel(vocab_size=len(vocab)).to(device)     # Instantiate and move model to device
criterion = torch.nn.CrossEntropyLoss()                                # Loss for multi-class classification
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)             # Optimizer with weight decay

EPOCHS = 5

for epoch in range(EPOCHS):
    train_loss, train_acc = train(model, train_loader, optimizer, criterion, device)
    val_loss, val_acc = evaluate(model, valid_loader, criterion, device)

    print(f"Epoch {epoch+1}:")
    print(f"  Train Loss: {train_loss:.4f}, Acc: {train_acc:.4f}")
    print(f"  Val   Loss: {val_loss:.4f}, Acc: {val_acc:.4f}")
```