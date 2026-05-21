### Part I
![[Pasted image 20240422133907.png]]
1. Complete the command to return all the posts with number of likes greater than 100 and less than 200,
both inclusive?
```json
db.posts.find({ likes: { $gte: 100, $lte: 200 } });
```

2. Write a command to remove a single document that matches the condition that Author is Joe?
```sql
db.posts.deleteOne({ author: "Joe" });
```

3. Write a query to sort the posts collection with author key ascending.
```json
db.posts.find().sort({ author: 1 });
```

4. What is the equivalent command in MongoDB for the following SQL query?
SQL
```sql
SELECT * FROM posts WHERE author like "%john%"
```
MongoDB
```json
db.posts.find({ author: { $regex: /john/, $options: 'i' } });
```
5. What will be the equivalent MongoDB command for the following SQL command (Hint: MongoDB's
aggregation):
SQL
```sql
SELECT author, count(*) FROM posts GROUP BY author HAVING count(*) > 1
```
MongoDB
```json
db.posts.aggregate([
    { $group: { _id: "$author", count: { $sum: 1 } } },
    { $match: { count: { $gt: 1 } } }
]);
```


### Part II

The given file “restaurants.json” comprises of 3772 documents of the “restaurants” collection. This
collection is structured as below.
```json
{
	"_id" : ObjectId("662542c04e68f621584b28d9"),
	"address" : {
		"building" : "130","coord" : [-73.984758,40.7457939],"street" : "Madison Avenue","zipcode" : "10016"
	},
	"borough" : "Manhattan",
	"cuisine" : "Pizza/Italian",
	"grades" : [
		{ "date" : ISODate("2014-12-24T00:00:00.000+0000"),"grade" : "Z","score" :
		NumberInt(31) },
		{ "date" : ISODate("2014-06-17T00:00:00.000+0000"),"grade" : "C","score" :
		NumberInt(98) },
		{ "date" : ISODate("2013-12-12T00:00:00.000+0000"),"grade" : "C","score" :
		NumberInt(32) },
		{ "date" : ISODate("2013-05-22T00:00:00.000+0000"),"grade" : "B","score" :
		NumberInt(21) },
		{ "date" : ISODate("2012-05-02T00:00:00.000+0000"),"grade" : "A","score" :
		NumberInt(11)}
	],
	"name" : "Bella Napoli",
	"restaurant_id" : "40393488"
}
```
Tasks: Utilize the MongoDB shell/IDE to perform the following tasks within the "restaurants" collection:

6. Find documents in the restaurants collection that achieved a score is more than 80 but less than 100.
```json
db.restaurants.find({ grades:{ $elemMatch:{ score:{ $gt: 80, $lt: 100 }}}});
```
7. Display the next 5 restaurants after skipping first 5 which are in the borough Bronx.
```json
db.restaurants.find({ borough: "Bronx" }).skip(5).limit(5);
```
8. Find the restaurant Id, name, borough and cuisine for those restaurants which belong to the borough
Staten Island or Queens or Bronx or Brooklyn.
```json
db.restaurants.find(
    { borough: { $in: ["Staten Island", "Queens", "Bronx", "Brooklyn"] } },
    { _id: 0, restaurant_id: 1, name: 1, borough: 1, cuisine: 1 }
);
```

9. Find documents in the restaurants collection where the address field contains a street field.
```json
db.restaurants.find({ "address.street": { $exists: true } });
```

10. Find the average score for each restaurant (Hint: MongoDB's aggregation).
```json
db.restaurants.aggregate([
    { $unwind: "$grades" },
    { $group: { _id: "$name", avgScore: { $avg: "$grades.score" } } }
]);
```
