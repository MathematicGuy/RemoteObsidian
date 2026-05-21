### **Updated Transaction Flow Diagram with Authentication**

1. **Start**
2. **Authenticate User**
    - Verify the user’s authentication token to ensure they are who they claim to be.
    - If authentication fails → **Abort Transaction** → Return "Unauthorized" message.
3. **Check GP Balance**
    - If GP balance < 10 → **Abort Transaction** → Return "Insufficient GP" message.
    - If GP balance ≥ 10 → Proceed to the next step.
4. **Deduct 10 GP from User Balance**
5. **Update User's GP Balance in the Database**
6. **Record GP Transaction**
    - Store the deduction details in the **GPTransactions** table.
7. **Record Main Transaction**
    - Store the main transaction details in the **Transactions** table.
8. **End**

### **Diagram Representation with Authentication**
```txt
+---------------------------+
|         Start              |
+---------------------------+
           |
           v
+---------------------------+
|   Authenticate User        |
+---------------------------+
           |
   +-------+-------+
   |               |
   v               v
+-----------------------+    Authentication Fails
|  Authentication OK?   |----------------------------------->+-------------------------+
+-----------------------+                                     | Abort Transaction       |
           |                                                  | Return "Unauthorized"   |
           v                                                  +-------------------------+
+---------------------------+
|  Check User GP Balance     |
+---------------------------+
           |
   +-------+-------+
   |               |
   v               v
+-----------------------+    GP Balance < 10
| GP Balance >= 10?     |----------------------------------->+-------------------------+
+-----------------------+                                     | Abort Transaction       |
           |                                                  | Return "Insufficient GP"|
           v                                                  +-------------------------+
+---------------------------+
| Deduct 10 GP from Balance  |
+---------------------------+
           |
           v
+---------------------------+
| Update GP Balance in DB    |
+---------------------------+
           |
           v
+---------------------------+
| Record GP Transaction      |
+---------------------------+
           |
           v
+---------------------------+
| Record Main Transaction    |
+---------------------------+
           |
           v
+---------------------------+
|          End               |
+---------------------------+
```

### **Backend and Frontend Interaction**

The backend and frontend work together in the following way to accomplish the transaction flow:

#### **Frontend Responsibilities:**

1. **User Authentication:**
    
    - The frontend (typically a React, Angular, or Vue.js application) handles user authentication by obtaining a JWT token when the user logs in.
    - The token is stored in the frontend, often in local storage or a secure cookie.
2. **Initiating the Transaction:**
    
    - The frontend sends a request to the backend to initiate the transaction, typically by calling an API endpoint like `/api/transactions/process`.
    - This request includes:
        - The JWT token in the request header for authentication (`Authorization: Bearer <JWT_TOKEN>`).
        - The transaction details in the request body, such as `userId`, `requestId`, `documentType`, etc.
3. **Handling Responses:**
    
    - The frontend handles the response from the backend. Based on the response:
        - If the transaction is successful, the frontend may display a success message or update the user interface accordingly.
        - If the transaction fails (e.g., due to insufficient GP or authentication failure), the frontend displays an error message.

#### **Backend Responsibilities:**

1. **Authenticating the User:**
    
    - The backend verifies the JWT token in the incoming request.
    - If the token is valid, the backend proceeds with the transaction; if not, it returns an "Unauthorized" response.
2. **Processing the Transaction:**
    
    - The backend checks the user's GP balance.
    - If the user has sufficient GP, the backend deducts 10 GP and updates the database.
    - The transaction details are recorded in the appropriate tables (`GPTransactions`, `Transactions`).
3. **Responding to the Frontend:**
    
    - After processing the transaction, the backend sends a response to the frontend indicating the outcome of the transaction.
    - If successful, a success message is sent; otherwise, an appropriate error message is returned (e.g., "Insufficient GP" or "Unauthorized").

### **Example Request Flow**

1. **Frontend**:
    
    - Sends a POST request to `/api/transactions/process`.
    - Headers include:
        - `Authorization: Bearer <JWT_TOKEN>`
    - Body includes:
        - `userId`, `requestId`, `documentType`, `fileSize`, `filePath`, `resultFilePath`.
2. **Backend**:
    
    - Authenticates the user based on the provided JWT token.
    - Checks the user's GP balance.
    - Processes the transaction if the user is authenticated and has sufficient GP.
    - Responds with the status of the transaction (success or failure).
3. **Frontend**:
    
    - Receives the backend's response and updates the UI accordingly.


### **How JWT Works in Your Case**

#### 1. **User Authentication and Token Issuance**

- **Login Request**: When a user logs in, they send their credentials (usually a username and password) to the backend.
- **Credential Verification**: The backend verifies the credentials against the stored user data in the database.
- **Token Creation**: If the credentials are valid, the backend generates a JWT token. This token contains encoded information about the user, such as their user ID and role, and is signed using a secret key known only to the backend server.
- **Token Return**: The JWT token is returned to the frontend, typically in the response body of the login request.

#### 2. **Frontend Storage and Use of the Token**

- **Storing the Token**: The frontend stores the JWT token, usually in local storage, session storage, or a secure HTTP-only cookie.
- **Using the Token**: When the user performs any action that requires authentication (e.g., processing a transaction), the frontend includes the JWT token in the `Authorization` header of the HTTP request, formatted as `Bearer <JWT_TOKEN>`.

#### 3. **Backend Verification of the Token**

- **Receiving the Request**: When the backend receives a request that includes a JWT token, it first extracts the token from the `Authorization` header.
- **Token Decoding**: The backend decodes the JWT token using the same secret key that was used to sign it. This decoding allows the backend to verify that the token is valid and has not been tampered with.
- **Claim Verification**: The backend checks the claims in the token (e.g., user ID, role) to ensure they are correct and that the token has not expired.
- **Authorization**: If the token is valid, the backend allows the user to proceed with the requested action (e.g., processing the transaction). If the token is invalid or expired, the backend rejects the request and returns an "Unauthorized" response.

#### 4. **Token Expiry and Refresh**

- **Token Expiry**: JWT tokens usually have an expiration time (`exp` claim). After this time, the token becomes invalid.
- **Token Refresh**: When a token is near expiry or has expired, the frontend may automatically request a new token by sending the old one to a special "refresh" endpoint. If the old token is valid and the user is still authenticated, the backend issues a new token.

### **JWT Structure**

A JWT token consists of three parts, separated by dots (`.`):

1. **Header**: Contains metadata about the token, such as the type of token (JWT) and the signing algorithm (e.g., HS256).
2. **Payload**: Contains the claims, which are the actual data being transferred. This might include the user ID, username, roles, and token expiration time.
3. **Signature**: Ensures that the token has not been altered. It is created by taking the header and payload, encoding them, and then signing them using a secret key.

Example of a JWT:
```txt
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlcm5hbWUiOiJqb2huZG9lIiwicm9sZSI6IkFETUlOIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
```

- **Header**: `eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9`
- **Payload**: `eyJzdWIiOiIxMjM0NTY3ODkwIiwidXNlcm5hbWUiOiJqb2huZG9lIiwicm9sZSI6IkFETUlOIiwiaWF0IjoxNTE2MjM5MDIyfQ`
- **Signature**: `SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c`

### **How JWT Integrates with Your Transaction Process**

1. **Authentication**: The user logs in and receives a JWT token.
2. **Transaction Request**: The user initiates a transaction. The frontend includes the JWT token in the `Authorization` header of the HTTP request.
3. **Token Verification**: The backend verifies the JWT token to ensure that the user is authenticated.
4. **Process Transaction**: If the token is valid, the backend processes the transaction. If the token is invalid or expired, the backend returns an "Unauthorized" response, and the transaction does not proceed.

### **Security Considerations**

- **Secret Key Protection**: The secret key used to sign the JWT must be securely stored on the backend and never exposed to the public.
- **Token Expiry**: Tokens should have a reasonable expiration time to limit the duration of access if the token is compromised.
- **HTTPS**: Always use HTTPS to ensure that the JWT token is securely transmitted between the frontend and backend.

JWT tokens provide a stateless and scalable way to manage user authentication, making them well-suited for APIs and microservices architectures.

### **Detailed Explanation on How the Backend Verifies the JWT Token**

When a JWT token is used for authentication, the token itself contains all the necessary information for verification. The backend does not store the token; instead, it verifies the token each time it receives it from the frontend. Here's how this process works in more detail:

### **1. JWT Token Issuance**

When a user logs in successfully:

- The backend generates a JWT token, which includes:
    
    - **Header**: Specifies the signing algorithm (e.g., HS256).
    - **Payload**: Contains user information (e.g., `userId`, `role`) and any additional claims like `iat` (issued at) and `exp` (expiration time).
    - **Signature**: Created by encoding the header and payload, then signing them with a secret key known only to the backend.
- The backend sends this JWT token back to the frontend as part of the login response.
    

### **2. Token Storage in the Frontend**

Once the frontend receives the JWT token, it typically stores it in a way that allows it to be easily included in subsequent requests:

- **Local Storage or Session Storage**: Common choices for storing JWT tokens in web applications. These are persistent storage mechanisms in the browser, but they can be vulnerable to cross-site scripting (XSS) attacks if not handled carefully.
    
- **HTTP-Only Cookies**: A more secure option, where the token is stored in a cookie that is not accessible to JavaScript, reducing the risk of XSS attacks.
    

### **3. Sending the Token with Requests**

For any request that requires authentication (e.g., processing a transaction), the frontend includes the JWT token in the HTTP request header:

- **Authorization Header**: The token is sent as a Bearer token, formatted as:
    
    http