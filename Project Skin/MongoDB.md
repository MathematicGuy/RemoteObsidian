[[MongoDb Overview]]

Store in Binary Json (BJ file type)
Mongol is short for Humongous (big) 

![[Pasted image 20240405080142.png]]
![[Pasted image 20240405080200.png]]
![[Pasted image 20240405080249.png]]

> Prerequisites: learn OOP (python, C#, java, etc..)

### [Mongo Cheat Sheet](https://www.mongodb.com/developer/products/mongodb/cheat-sheet/#helpers)
+ ? Collection (~ table in SQL)

#### Connect to my MongolDB
```json
mongosh
mongod // manage mongo data ?
```

#### Databases Helpers
```JSON
show dbs
db // prints the current database
exit // exit Mongo Terminal

use <database_name> // use Db
show collections // show all tables
load("myScript.js") // run all js file
```

#### CRUD Operation
+ ? coll: table name
CREATE
```json
db.coll.insertOne({name: "Max"})
db.coll.insertMany([{name: "Max"}, {name:"Alex"}]) // ordered bulk insert
db.coll.insertMany([{name: "Max"}, {name:"Alex"}], {ordered: false}) // unordered bulk insert
db.coll.insertOne({date: ISODate()})
db.coll.insertOne({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
```

**READ**
```json
db.coll.findOne() // returns a single document
db.coll.find()    // returns a cursor - show 20 results - "it" to display more
db.coll.find().pretty()
db.coll.find({name: "Max", age: 32}) // implicit logical "AND".
db.coll.find({date: ISODate("2020-09-25T13:57:17.180Z")})
db.coll.find({name: "Max", age: 32}).explain("executionStats") // or "queryPlanner" or "allPlansExecution"
db.coll.distinct("name")w

// Count
db.coll.countDocuments({age: 32}) // alias for an aggregation pipeline - accurate count
db.coll.estimatedDocumentCount()  // estimation based on collection metadata

// Comparison
db.coll.find({"year": {$gt: 1970}}) // greater th
db.coll.find({"year": {$gte: 1970}}) // greater than equal
db.coll.find({"year": {$lt: 1970}}) // less than
db.coll.find({"year": {$lte: 1970}}) // less than equal
db.coll.find({"year": {$ne: 1970}}) // not equal
db.coll.find({"year": {$in: [1958, 1959]}}) // in 1958 to 1959
db.coll.find({"year": {$nin: [1958, 1959]}}) // not in 1958 to 1959

// Logical
db.coll.find({name:{$not: {$eq: "Max"}}})
db.coll.find({$or: [{"year" : 1958}, {"year" : 1959}]})
db.coll.find({$nor: [{price: 1.99}, {sale: true}]})
db.coll.find({
  $and: [
    {$or: [{qty: {$lt :10}}, {qty :{$gt: 50}}]},
    {$or: [{sale: true}, {price: {$lt: 5 }}]}
  ]
})
db.mycollection.find({$and:
	[
		{name:"Noi"}, {age:211}
	]
}) 
// {} -> 1st layer for the command
// $and: [] -> for $and. Everything inside [] count as a object for and.
// Ex: [{name:"Noi"}, {age:211}] -> name="Noi" and age=211 

// Element
db.coll.find({name: {$exists: true}})
db.coll.find({"zipCode": {$type: 2 }})
db.coll.find({"zipCode": {$type: "string"}})

// Aggregation Pipeline
db.coll.aggregate([
  {$match: {status: "A"}},
  {$group: {_id: "$cust_id", total: {$sum: "$amount"}}},
  {$sort: {total: -1}}
])

// Text search with a "text" index
db.coll.find({$text: {$search: "cake"}}, {score: {$meta: "textScore"}}).sort({score: {$meta: "textScore"}})

// Regex
db.coll.find({name: /^Max/})   // regex: starts by letter "M"
db.coll.find({name: /^Max$/i}) // regex case insensitive

// Array
db.coll.find({tags: {$all: ["Realm", "Charts"]}})
db.coll.find({field: {$size: 2}}) // impossible to index - prefer storing the size of the array & update it
db.coll.find({results: {$elemMatch: {product: "xyz", score: {$gte: 8}}}})

// Projections
db.coll.find({"x": 1}, {"actors": 1})               // actors + _id
db.coll.find({"x": 1}, {"actors": 1, "_id": 0})     // actors
db.coll.find({"x": 1}, {"actors": 0, "summary": 0}) // all but "actors" and "summary"

// Sort, skip, limit
db.coll.find({}).sort({"year": 1, "rating": -1}).skip(10).limit(3)

// Read Concern
db.coll.find().readConcern("majority")
```


UPDATE
```json
// updateOne -> Update the 1st one it found
db.coll.updateOne({"_id": 1}, {$set: {"year": 2016, name: "Max"}})
db.coll.updateOne({"_id": 1}, {$unset: {"year": 1}})
db.coll.updateOne({"_id": 1}, {$rename: {"year": "date"} })
db.coll.updateOne({"_id": 1}, {$inc: {"year": 5}})
db.coll.updateOne({"_id": 1}, {$mul: {price: NumberDecimal("1.25"), qty: 2}})
db.coll.updateOne({"_id": 1}, {$min: {"imdb": 5}})
db.coll.updateOne({"_id": 1}, {$max: {"imdb": 8}})
db.coll.updateOne({"_id": 1}, {$currentDate: {"lastModified": true}})
db.coll.updateOne({"_id": 1}, {$currentDate: {"lastModified": {$type: "timestamp"}}})

// Array
db.coll.updateOne({"_id": 1}, {$push :{"array": 1}})
db.coll.updateOne({"_id": 1}, {$pull :{"array": 1}})
db.coll.updateOne({"_id": 1}, {$addToSet :{"array": 2}})
db.coll.updateOne({"_id": 1}, {$pop: {"array": 1}})  // last element
db.coll.updateOne({"_id": 1}, {$pop: {"array": -1}}) // first element
db.coll.updateOne({"_id": 1}, {$pullAll: {"array" :[3, 4, 5]}})
db.coll.updateOne({"_id": 1}, {$push: {"scores": {$each: [90, 92]}}})
db.coll.updateOne({"_id": 2}, {$push: {"scores": {$each: [40, 60], $sort: 1}}}) // array sorted
db.coll.updateOne({"_id": 1, "grades": 80}, {$set: {"grades.$": 82}})
// updateMany -> Update all the one it found
db.coll.updateMany({}, {$inc: {"grades.$[]": 10}})
db.coll.updateMany({}, {$set: {"grades.$[element]": 100}}, {multi: true, arrayFilters: [{"element": {$gte: 100}}]})

// FindOneAndUpdate
db.coll.findOneAndUpdate({"name": "Max"}, {$inc: {"points": 5}}, {returnNewDocument: true})

// Upsert
db.coll.updateOne({"_id": 1}, {$set: {item: "apple"}, $setOnInsert: {defaultQty: 100}}, {upsert: true})

// Replace
db.coll.replaceOne({"name": "Max"}, {"firstname": "Maxime", "surname": "Beugnet"})

// Write concern
db.coll.updateMany({}, {$set: {"x": 1}}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
```


DELETE
```json
db.coll.deleteOne({name: "Max"})
db.coll.deleteMany({name: "Max"}, {"writeConcern": {"w": "majority", "wtimeout": 5000}})
db.coll.deleteMany({}) // WARNING! Deletes all the docs but not the collection itself and its index definitions
db.coll.findOneAndDelete({"name": "Max"})
```


#### Databases and Collections

DROP
```json
db.coll.drop()    // removes the collection and its index definitions
db.dropDatabase() // double check that you are *NOT* on the PROD cluster... :-)
```


#### Create Collection
```json
// Create collection with a $jsonschema
db.createCollection("contacts", {
   validator: {$jsonSchema: {
      bsonType: "object",
      required: ["phone"],
      properties: {
         phone: {
            bsonType: "string",
            description: "must be a string and is required"
         },
         email: {
            bsonType: "string",
            pattern: "@mongodb\.com$",
            description: "must be a string and match the regular expression pattern"
         },
         status: {
            enum: [ "Unknown", "Incomplete" ],
            description: "can only be one of the enum values"
         }
      }
   }}
})
```

OTHER COLLECTION FUNCTIONS
```json
db.coll.stats()
db.coll.storageSize()
db.coll.totalIndexSize()
db.coll.totalSize()
db.coll.validate({full: true})
db.coll.renameCollection("new_coll", true) // 2nd parameter to drop the target collection if exists
```


> Limit displaz atribute of movies to 2
```js
db.actors.find({},{name: 1, movies: {$slice:2}, _id: 0})
```


Axios for MongoDb
```js
const axios = require("axios");

async function getMoviePoster(url){
    const {data} = await axios.get(url)
    return data.Poster;
};

use("sample_mflix");

(async () => {
    for (const movie of movies){
        const title = movie.title;
        const url = `https://www.omdapi.com/?t=${title}&apikey=${API_KEY}`;
        const moviePoster = await getMoviePoster(url); 
        db.movies.updateOne({ _id:movie_id }, { $set: { poster: moviePoster}});
    }
})();
```

