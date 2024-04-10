Tasks: Utilize the MongoDB shell to perform the following tasks within the "sample_mflix" database:

1. Add a document to the "movies" collection with specified details including title "My Assignment II", year 2023, and genre "Drama", leaving director and plot fields empty, and setting runtime to 100 minutes.
```json
db.movies.insertOne({name: "My Assignment II"}, {year: 2023}, {genres:"drama"}, {director:""}, {plot:""}, {runtime:100})
```


2. Insert a comment document into the "comments" collection with a placeholder movie ID, your name, email "student@nbcc.ca", and a blank text field.


3. Retrieve the document titled "My Assignment II" from the "movies" collection:



4. Determine the count of documents in the "movies" collection that are categorized as "Drama".

5. Retrieve and display the top 5 comments from the "comments" collection, sorted in descending order by the "date" field.


6. Fetch and display movies from the "movies" collection categorized as "Action" or "Adventure" with a runtime of less than 150 minutes.


7. Add a new comment for the movie "My Assignment II" with updated name and email details, then retrieve
and display this updated comment.

8. Modify the director field of the movie "My Assignment II" to "MongoDB geek", then fetch and display the updated document.


9. Remove all documents from the "movies" collection for movies released in the year 2023.


10. Delete the initially inserted comment document from task 2 (use the comment ID or match exact fields if the ID is not known):