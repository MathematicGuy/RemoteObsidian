1.2 ông đi phân tích chi tiết pipeline, dựa trên 4 vấn đề tui viết lúc sáng ấy

Phân tích kỹ phần 3,4 thôi. Phần khác viết tóm tắt qua là đc

Vấn đề 1: data ít, imbalance, nhưng accuracy rất cao (>99%) dẫn đến khả năng dự đoán của mô hình kém trước các test case => Phần này có thể dùng saliency để minh họa => Đề xuất Data Augmentation @Huan

Vấn đề 2: e5 vẫn chưa có khả năng hiểu ngữ nghĩa đủ sâu => Đề xuất BERT @Tung @Linh

Vấn đề 3: Embedding dùng mean pooling là không đủ để model hiểu ngữ nghĩa hơn.... => Đề xuất IDF Weight pooling @Phuong 

Vấn đề 4: majority vote còn quá đơn giản => đề xuất pp thay đổi@Ha

---


```python
    print("Creating FAISS index...")
    dimension = X_train_emb.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(X_train_emb.astype("float32"))
```