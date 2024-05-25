---
tags: CyberSecurity
---
**Dễ:**
1. Hàm băm và ứng dụng
2. Chữ ký số
3. Mã chứng thực bản tin HMAC
4. Chứng chỉ X.509
5. Giao thức SSL
6. Giao thức TLS


**Trung bình:**
1. Giao thức kiểm soát truy nhập mạng NAC
2. Giao thức chứng thực mở rộng EAP
3. Các vấn đề an ninh Web
4. Giao thức IPsec


**Khó:**
1. Giao thức Kerberos
2. Giao thức LDAP
3. Giao thức OAuth
4. Giao thức SALM
5. Giao thức Radius
6. An ninh trong SDN

---
**Hash Functions and Applications**

- **What is a hash function?** A cryptographic hash function takes an input of arbitrary size (text, files, etc.) and produces a fixed-size output known as a hash or digest. Key characteristics:
    
    - **Deterministic:** The same input always produces the same hash.
    - **Irreversible:** It's practically impossible to determine the original input from the hash value.
    - **Collision resistant:** Finding two different inputs creating the same hash should be computationally difficult.
- **Applications:**
    
    - **Data Integrity:** Hashing a file and comparing its hash later helps ensure the file hasn't been altered.
    - **Password Storage:** Storing hashes of passwords (with salting!) protects against exposing plain text passwords if a database is breached.
    - **Data Structures:** Hash tables use hash functions for efficient lookups.
- **Python Skills**
    
    - **`hashlib` library:** Provides common hash functions—MD5, SHA1, SHA256, etc

