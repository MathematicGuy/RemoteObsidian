SQL
pro: query


NoSQL
pro: when data changes constantly
cons: duplicate, abnormal data

**Project summary:** Quản lý công việc của các nhân viên tham gia trong các dự án ở các ban. 

- **employees** (empl)
    M (empl) - 1 (dep) 
- **departments** (dep)
    1 (dep) - M (proj)
- **projects** (proj)
	1 (proj) - M (tas)
- **tasks** (tas)

VD: 
SQL có 1 bảng riêng cho từng thể loại film
-> 1 người ko thể tự nhiên có 1 thể loại film

NoSQL có thể thêm tùy ý vô số lần. 1 người có thể gán thêm hàng trăm thể loại film thì ko bị ràng buộc.
+ Tra cứu tệ. Tra theo ràng buộc 


```json
/*
    1.	Add a document to the "movies" collection with specified details 
*/
db.movies.insertOne({
  title: "My Assignment II",
  year: 2023,
  genre: "Drama",
  director: "",
  plot: "",
  runtime: "100 minutes"
});
db.getCollection("movies").find({title: "My Assignment II"})

/*
    2.	Insert a comment document into the "comments" collection
*/
var movieId = ObjectId("6615a0125376ae3a311cae7c");

db.comments.insertOne({
  movie_id: movieId,
  name: "",
  email: "student@nbcc.ca",
  text: "",
  date: new Date() // Adds the current date and time
});
db.getCollection("comments").find({email: "student@nbcc.ca"})

/*
    3.	Retrieve the document titled "My Assignment II" from the "movies" collection 
*/
db.movies.findOne({ title: "My Assignment II" });

/*
    4.	Determine the count of documents in the "movies" collection that are categorized as "Drama"
*/
db.movies.countDocuments({ genres: "Drama" }); //12385

/*
    5.	Retrieve and display the top 5 comments from the "comments" collection, sorted in descending order by the "date" field.
*/
// 1: acs, -1: desc
db.comments.find().sort({ date: -1 }).limit(5);


/*
    6. Display movies from the "movies" collection categorized as "Action" or "Adventure" with a runtime of less than 150 minutes.
*/
db.movies.find({
  $or: [{ genres: "Action" }, { genres: "Adventure" }],
  runtime: { $lt: 150 }
});

/*
7.	Add a new comment for the movie "My Assignment II" with updated name and email details, then retrieve and display this updated comment.
*/
// Step 1: Retrieve the Movie for "My Assignment II"
var movie = db.movies.findOne({ title: "My Assignment II" },{_id:1});
//Step 2: Insert a New Comment for "My Assignment II"
db.comments.insertOne({
  movie_id: movie._id, // Use the actual ID
  name: "New Commenter Name",
  email: "newcommenter@example.com",
  text: "This is a new comment.",
  date: new Date() // Adds the current date and time
});
db.getCollection("comments").find({email: "newcommenter@example.com"})
db.getCollection("comments").find({movie_id: ObjectId("6615a0125376ae3a311cae7c")})

/*
8.	Modify the director field of the movie "My Assignment II" to "MongoDB geek", then fetch and display the updated document.
*/
db.movies.updateOne(
  { title: "My Assignment II" },
  { $set: { directors: "MongoDB geek" } }
);
// To show the updated document
db.movies.findOne({ title: "My Assignment II" });

/*
9.	Remove all documents from the "movies" collection for movies released in the year 2023.
*/
db.movies.find({ year: 2023 });
db.movies.countDocuments({ year: 2023 });
db.movies.deleteMany({ year: 2023 });

/*
    10.	Delete the initially inserted comment document from task 2 
*/
db.comments.find({ email: "student@nbcc.ca" });
db.comments.deleteOne({
  email: "student@nbcc.ca"
  // Add additional fields if necessary to uniquely identify the document
});


```