**Connect Database** (at the start of each query)
```js
// The current database to use.
use("customerDB");
```

**Sample Data**
```js
{
	"name": "John Doe",
	"email": "john.doe@example.com",
	"age": 28,
	"gender": "Male",
	"location": "New York",
	"purchases": [
		{ "product": "Laptop", "price": 1200, "date": "20250425" },
		{ "product": "Headphones", "price": 200, "date": "20240112" }
	],
	"membership": "Gold"
}
```

**Insert 100 Sample Data**
```js
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
```js
db.customers.find()
```
![[Pasted image 20250304084133.png]]

- Search for customers by location (e.g., New York):
```js
db.customers.find({'location': 'New York'})
```
![[Pasted image 20250304084242.png]]

- Find customers within a certain age range
```js
db.customers.find({
    "age":{
        $gte:25,
        $lte:30
    }
})
```
![[Pasted image 20250304084541.png]]
### 4. Aggregation Queries
- Calculate total spending of each customer
```js
db.customers.aggregate([
    {
      $unwind: "$purchases"  // Flatten the 'purchases' array
    },
    {
      $group: {
        _id: "$name",  // Group by customer name
        totalSpending: { $sum: { $toDouble: "$purchases.price" } }  // Sum all purchase prices (convert to double)
      }
    },
    {
      $sort: { totalSpending: -1 }  // Sort by total spending in descending order
    }
  ])
```
![[Pasted image 20250304091118.png]]

- Find the customer who spends the most
```js
db.customers.aggregate([
    {
      $unwind: "$purchases"  // Flatten the 'purchases' array
    },
    {
      $group: {
        _id: "$name",  // Group by customer name
        totalSpending: { $sum: { $toDouble: "$purchases.price" } }  // Sum all purchase prices
      }
    },
    {
      $sort: { totalSpending: -1 }  // Sort by total spending in descending order
    },
    {
      $limit: 1  // Limit to just the highest spender
    }
  ])
```
![[Pasted image 20250304091210.png]]


- Number of products a customer has purchased
```js
db.customers.aggregate([
  {
    $project: {
      _id: 0,
      name: 1,
      numProducts: { $size: "$purchases" }  // Count the number of purchases
    }
  }
])
```
![[Pasted image 20250304091236.png]]

- Most popular products purchased
```js

db.customers.aggregate([
    {
      $unwind: "$purchases"  // Flatten the 'purchases' array
    },
    {
      $group: {
        _id: "$purchases.product",  // Group by product name
        totalPurchased: { $sum: 1 }  // Count the number of times each product was purchased
      }
    },
    {
      $sort: { totalPurchased: -1 }  // Sort by total purchases in descending order
    },
    {
      $limit: 1  // Limit the result to the top product
    }
])
  
  ```
![[Pasted image 20250304091431.png]]

- Total spending by age group
```js
db.customers.aggregate([
  {
    $unwind: "$purchases"  // Flatten the 'purchases' array
  },
  {
    $project: {
      ageGroup: {
        $cond: {
          if: { $lt: ["$age", 26] },
          then: "18-25",
          else: {
            $cond: {
              if: { $lt: ["$age", 36] },
              then: "26-35",
              else: {
                $cond: {
                  if: { $lt: ["$age", 46] },
                  then: "36-45",
                  else: {
                    $cond: {
                      if: { $lt: ["$age", 56] },
                      then: "46-55",
                      else: "56+"
                    }
                  }
                }
              }
            }
          }
        }
      },
      spending: { $toDouble: "$purchases.price" }  // Convert price to double for calculation
    }
  },
  {
    $group: {
      _id: "$ageGroup",  // Group by age group
      totalSpending: { $sum: "$spending" }  // Sum the spending for each group
    }
  },
  {
    $sort: { totalSpending: -1 }  // Sort by total spending in descending order
  }
])
```
![[Pasted image 20250304091534.png]]

- Analyze spending by gender
```js
db.customers.aggregate([
    {
      $unwind: "$purchases"  // Flatten the 'purchases' array
    },
    {
      $group: {
        _id: "$gender",  // Group by gender
        totalSpending: { $sum: { $toDouble: "$purchases.price" } }  // Sum the spending for each gender
      }
    },
    {
      $sort: { totalSpending: -1 }  // Sort by total spending in descending order
    }
  ])
```
![[Pasted image 20250304091555.png]]


# Tasks Included in `connect.ipynb` file
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
on spending behavion.

