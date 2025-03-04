**Insert 100 Sample Data**
```js
// The current database to use.
use("customerDB");

let users = [];
for (let i = 0; i < 101; i++) {
    const gender = i % 2 === 0 ? 'Male' : 'Female';  // Simple alternating gender for the example
    const location = `City ${i + 1}`;  // Simple location generation
    const purchases = [];
    const numPurchases = Math.floor(Math.random() * 3) + 1;  // Random number of purchases (1 to 3)
    
    for (let j = 0; j < numPurchases; j++) {
        purchases.push({
            product: `Product ${Math.floor(Math.random() * 100) + 1}`,  // Generate simple product name
            price: (Math.random() * 1000).toFixed(2),  // Random price between 0 and 1000
            date: new Date().toISOString().split('T')[0]  // Today's date in YYYY-MM-DD format
        });
    }

    users.push({
        name: `User ${i + 1}`,  // Simple name generation
        email: `user${i + 1}@example.com`,  // Generate a simple email
        age: Math.floor(Math.random() * 53) + 18,  // Random age between 18 and 70
        gender: gender,
        location: location,
        purchases: purchases,
        membership: i % 3 === 0 ? 'Gold' : (i % 3 === 1 ? 'Silver' : 'Bronze')  // Simple alternating membership
    });
}

// Insert generated users into the MongoDB collection
db.customers.insertMany(users);
```


## Queries and Analysis
### 3. Basic Queries
- Get a list of all customers:
- Search for customers by location (e.g., New York):
- Find customers within a certain age range 
### 4. Aggregation Queries
- Calculate total spending of each customer
- Find the customer who spends the most
- Number of products a customer has purchased
- Most popular products purchased
- Total spending by age group
- Analyze spending by gender


## Data Visualization
(Use Python Matplotlib, Seaborn)
### 5. Draw a Pie Chart: Customer Gender Distribution
Use aggregation to count the number of customers by gender, then plot a pie
chart.
### 6. Draw a Bar Chart: Total Spending of Each Customer
Retrieve total spending per customer and visualize it using a bar chart.
### 7. Line Graph: Spending Trends Over Time
Group purchases by date and plot total spending trends over time.

## Advanced Analysis
### 8. Customer Segmentation
Use clustering techniques (e.g., K-Means, DBSCAN to segment customers based
on spending behavio