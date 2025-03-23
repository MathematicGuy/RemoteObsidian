

Dưới đây là phiên bản code hoàn chỉnh (chạy trên Google Colab) chỉ sử dụng mô hình RNN và LSTM. Code này:

- Tải dữ liệu Reuters (46 chủ đề) từ `tensorflow.keras.datasets.reuters`.
- Hiển thị mẫu dữ liệu đầu tiên trong tập huấn luyện.
- Xây dựng các mô hình học sâu dựa trên RNN và LSTM với ba độ dài chuỗi khác nhau.
- In ra số tham số (parameters) của từng mô hình RNN và LSTM.
- Huấn luyện và đánh giá các mô hình sử dụng độ đo RMSE.

```python
#%% [code]
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
from tensorflow.keras.datasets import reuters
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# 1. Load dữ liệu Reuters
# ---------------------------
num_words = 10000  # Sử dụng top 10,000 từ
(x_train, y_train), (x_test, y_test) = reuters.load_data(num_words=num_words)
num_classes = np.max(y_train) + 1  # số chủ đề (46)
print("Số chủ đề:", num_classes)

# Lấy từ điển ánh xạ và tạo hàm giải mã
word_index = reuters.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

def decode_newswire(sequence):
    # Các chỉ số trong dataset được dịch chuyển 3 đơn vị (0,1,2 dành cho các token đặc biệt)
    return ' '.join([reverse_word_index.get(i - 3, '?') for i in sequence])

# Hiển thị mẫu dữ liệu đầu tiên trong tập huấn luyện (đã giải mã)
print("\nMẫu dữ liệu đầu tiên:")
print(decode_newswire(x_train[0]))
print("Label:", y_train[0])

# ---------------------------
# 2. Định nghĩa Dataset cho Reuters
# ---------------------------
class ReutersDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
    def __len__(self):
        return len(self.data)
    def __getitem__(self, idx):
        return torch.tensor(self.data[idx], dtype=torch.long), torch.tensor(self.labels[idx], dtype=torch.long)

# ---------------------------
# 3. Định nghĩa các mô hình RNN và LSTM
# ---------------------------
class RNNClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim,
                 num_layers=1, dropout=0.5):
        super(RNNClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.rnn = nn.RNN(embedding_dim, hidden_dim, num_layers=num_layers,
                           batch_first=True, dropout=dropout)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        # x: [batch_size, seq_len]
        embedded = self.embedding(x)  # [batch_size, seq_len, embedding_dim]
        out, _ = self.rnn(embedded)   # out: [batch_size, seq_len, hidden_dim]
        last_out = out[:, -1, :]      # Lấy output của bước cuối
        last_out = self.dropout(last_out)
        logits = self.fc(last_out)    # [batch_size, output_dim]
        return logits

class LSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim, output_dim,
                 num_layers=1, dropout=0.5):
        super(LSTMClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, num_layers=num_layers,
                            batch_first=True, dropout=dropout)
        self.dropout = nn.Dropout(dropout)
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        # x: [batch_size, seq_len]
        embedded = self.embedding(x)         # [batch_size, seq_len, embedding_dim]
        out, (hidden, _) = self.lstm(embedded) # out: [batch_size, seq_len, hidden_dim]
        last_hidden = hidden[-1]               # [batch_size, hidden_dim]
        last_hidden = self.dropout(last_hidden)
        logits = self.fc(last_hidden)          # [batch_size, output_dim]
        return logits

# Hàm đếm số tham số của mô hình
def count_parameters(model):
    return sum(p.numel() for p in model.parameters() if p.requires_grad)

# Hàm tính RMSE giữa xác suất dự đoán và nhãn one-hot thật
def compute_rmse(pred_probs, true_labels, num_classes):
    true_one_hot = np.eye(num_classes)[true_labels]
    rmse = np.sqrt(np.mean((pred_probs - true_one_hot)**2))
    return rmse

# ---------------------------
# 4. Huấn luyện và đánh giá các mô hình với các độ dài chuỗi khác nhau
# ---------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("\nSử dụng device:", device)

# Siêu tham số chung
embedding_dim = 128
hidden_dim = 128
output_dim = num_classes  # 46 chủ đề
num_layers = 2
dropout = 0.5
batch_size = 64
num_epochs = 5

# Ba độ dài chuỗi để thử nghiệm
sequence_lengths = [50, 100, 200]

# Lưu kết quả RMSE cho từng mô hình
rmse_results = {'RNN': {}, 'LSTM': {}}

for seq_len in sequence_lengths:
    print(f"\n=== Độ dài chuỗi: {seq_len} ===")
    
    # Pad chuỗi đến độ dài cố định
    x_train_pad = pad_sequences(x_train, maxlen=seq_len)
    x_test_pad = pad_sequences(x_test, maxlen=seq_len)
    
    # Tạo Dataset và DataLoader
    train_dataset = ReutersDataset(x_train_pad, y_train)
    test_dataset = ReutersDataset(x_test_pad, y_test)
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size)
    
    # Khởi tạo các mô hình RNN và LSTM
    rnn_model = RNNClassifier(num_words, embedding_dim, hidden_dim, output_dim,
                              num_layers=num_layers, dropout=dropout).to(device)
    lstm_model = LSTMClassifier(num_words, embedding_dim, hidden_dim, output_dim,
                                num_layers=num_layers, dropout=dropout).to(device)
    
    # In số tham số của các mô hình
    print("\n--- Mô hình RNN ---")
    print(rnn_model)
    print("Số tham số (RNN):", count_parameters(rnn_model))
    
    print("\n--- Mô hình LSTM ---")
    print(lstm_model)
    print("Số tham số (LSTM):", count_parameters(lstm_model))
    
    # Định nghĩa loss và optimizer cho từng mô hình
    criterion = nn.CrossEntropyLoss()
    optimizer_rnn = optim.Adam(rnn_model.parameters(), lr=1e-3)
    optimizer_lstm = optim.Adam(lstm_model.parameters(), lr=1e-3)
    
    # Huấn luyện mô hình RNN
    rnn_model.train()
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        for texts, labels in train_loader:
            texts = texts.to(device)
            labels = labels.to(device)
            optimizer_rnn.zero_grad()
            outputs = rnn_model(texts)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer_rnn.step()
            epoch_loss += loss.item()
        print(f"RNN (seq_len={seq_len}) - Epoch {epoch+1}/{num_epochs}: Loss = {epoch_loss/len(train_loader):.4f}")
    
    # Đánh giá mô hình RNN
    rnn_model.eval()
    all_preds = []
    all_true = []
    with torch.no_grad():
        for texts, labels in test_loader:
            texts = texts.to(device)
            labels = labels.to(device)
            outputs = rnn_model(texts)
            probs = torch.softmax(outputs, dim=1)
            all_preds.append(probs.cpu().numpy())
            all_true.append(labels.cpu().numpy())
    all_preds = np.concatenate(all_preds, axis=0)
    all_true = np.concatenate(all_true, axis=0)
    rnn_rmse = compute_rmse(all_preds, all_true, num_classes)
    print(f"RNN (seq_len={seq_len}) - Test RMSE: {rnn_rmse:.4f}")
    rmse_results['RNN'][seq_len] = rnn_rmse
    
    # Huấn luyện mô hình LSTM
    lstm_model.train()
    for epoch in range(num_epochs):
        epoch_loss = 0.0
        for texts, labels in train_loader:
            texts = texts.to(device)
            labels = labels.to(device)
            optimizer_lstm.zero_grad()
            outputs = lstm_model(texts)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer_lstm.step()
            epoch_loss += loss.item()
        print(f"LSTM (seq_len={seq_len}) - Epoch {epoch+1}/{num_epochs}: Loss = {epoch_loss/len(train_loader):.4f}")
    
    # Đánh giá mô hình LSTM
    lstm_model.eval()
    all_preds = []
    all_true = []
    with torch.no_grad():
        for texts, labels in test_loader:
            texts = texts.to(device)
            labels = labels.to(device)
            outputs = lstm_model(texts)
            probs = torch.softmax(outputs, dim=1)
            all_preds.append(probs.cpu().numpy())
            all_true.append(labels.cpu().numpy())
    all_preds = np.concatenate(all_preds, axis=0)
    all_true = np.concatenate(all_true, axis=0)
    lstm_rmse = compute_rmse(all_preds, all_true, num_classes)
    print(f"LSTM (seq_len={seq_len}) - Test RMSE: {lstm_rmse:.4f}")
    rmse_results['LSTM'][seq_len] = lstm_rmse

# ---------------------------
# 5. In kết quả RMSE của các mô hình với từng độ dài chuỗi
# ---------------------------
print("\nKết quả RMSE:")
for model_type in rmse_results:
    for seq_len, rmse in rmse_results[model_type].items():
        print(f"{model_type} với độ dài chuỗi {seq_len}: RMSE = {rmse:.4f}")

# ---------------------------
# 6. Nhận xét hiệu suất
# ---------------------------
print("\nNhận xét hiệu suất:")
print("- RMSE càng thấp cho thấy mô hình dự đoán xác suất gần với nhãn one-hot thật hơn.")
print("- Với độ dài chuỗi ngắn (ví dụ: 50), mô hình có thể bỏ sót ngữ cảnh quan trọng.")
print("- Với độ dài chuỗi quá dài (ví dụ: 200), mô hình có thể bị nhiễu do thông tin không cần thiết.")
print("- Mô hình LSTM thường hoạt động tốt hơn mô hình RNN trong việc ghi nhớ thông tin dài hạn, đặc biệt với chuỗi dài hơn.")
print("- Hiệu suất cuối cùng còn phụ thuộc vào cách tiền xử lý dữ liệu và lựa chọn siêu tham số.")
```

---

### Giải thích Code

1. **Tải dữ liệu và hiển thị mẫu:**
    
    - Dữ liệu Reuters được tải với top 10,000 từ và in ra mẫu đầu tiên đã được giải mã cùng với nhãn của nó.
2. **Định nghĩa Dataset:**
    
    - Lớp `ReutersDataset` chuyển dữ liệu đã pad và nhãn sang định dạng của PyTorch.
3. **Định nghĩa mô hình:**
    
    - Hai lớp `RNNClassifier` và `LSTMClassifier` được định nghĩa, mỗi lớp gồm Embedding, lớp hồi quy (RNN hoặc LSTM), Dropout và Fully Connected Layer.
    - Hàm `count_parameters` dùng để đếm số tham số của mô hình.
4. **Huấn luyện và đánh giá:**
    
    - Với mỗi độ dài chuỗi (50, 100, 200), dữ liệu được pad, tạo DataLoader, sau đó khởi tạo và huấn luyện mô hình RNN và LSTM.
    - Sau huấn luyện, mô hình được đánh giá trên tập test bằng cách tính RMSE giữa xác suất dự đoán (sau softmax) và nhãn one-hot thật.
    - Số tham số của từng mô hình được in ra.
5. **Kết quả và nhận xét:**
    
    - RMSE của từng mô hình cho từng độ dài chuỗi được in ra.
    - Nhận xét về hiệu suất của các mô hình dựa trên RMSE và độ dài chuỗi được đưa ra.

Chạy đoạn code này trên Google Colab để kiểm tra số tham số, kết quả huấn luyện và đánh giá, từ đó có thể so sánh hiệu suất của các mô hình RNN và LSTM cho bài toán phân loại tin tức Reuters.

---
note: **Use RNN for short-term dependencies and LSTM for long-term dependencies**

### Count Parameters
10000 là số lượng từ trong toàn bộ vocab/dataset 
`Embedding(10000, 128)`  (vocab_size = 10000 i.e. `[0, 9999]`, 128 dimensionality or vector with 128 float elements)
→ Số tham số = 10000 × 128 = **1,280,000**.


`RNN(128, 128, num_layers=2, batch_first=True, dropout=0.5)`
Example:
![[Pasted image 20250226115243.png]]
![[image/Untitled 3.png]]
![[RNN-Language-model1.png]]
+ RNN truyền thống gặp vấn đề vanishing gradient khi xử lý chuỗi dài
+ ? **vanishing gradient** (độ dốc biến mất) khi chuỗi đầu vào dài. Khi lan truyền ngược qua nhiều bước thời gian, các **đạo hàm của hàm kích hoạt (như hàm tanh) có giá trị nhỏ** hơn 1, làm cho các **gradient giảm theo cấp số nhân theo số bước thời gian.**


`LSTM(128, 128, num_layers=2, batch_first=True, dropout=0.5)`
![[Pasted image 20250226115334.png]]

![[Pasted image 20250226112131.png]]
+ LSTM (Long Short-Term Memory) được thiết kế với các cổng (gates) – bao gồm **cổng vào, cổng quên và cổng ra – nhằm điều chỉnh và kiểm soát dòng thông tin qua các bước thời gian**. Điều này giúp LSTM ghi nhớ thông tin dài hạn một cách hiệu quả hơn so với RNN truyền thống. 
+ ? Time-step: mỗi phần tử của chuỗi trong chuỗi dữ liệu.

**LSTM layer** 
- **Embedding layer**
- **LSTM layer** – This module is parameterized by `num_layers`. For example, if you pass `num_layers=1` (the default), then the LSTM has a single layer of LSTM cells; if you pass `num_layers=2`, then it has two stacked LSTM layers.
- **Dropout layer**
- **Fully Connected (Linear) layer**

---


![[Pasted image 20250226111821.png]]
Fully Pooling layer = (input * output) + output_bias_num



![[Pasted image 20250226111834.png]]

![[Pasted image 20250226121404.png]]
RNN và LSTM đều có công thúc tính chung cho params là
$(W.x + W_{h}.h + b)$ nên mỗi phép tính  
