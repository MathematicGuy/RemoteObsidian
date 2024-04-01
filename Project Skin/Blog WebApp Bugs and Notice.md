#### **Potential Misalignments**
1) **HTTP Method Mismatch:** If the form's `method` wasn't set to "post", the controller action wouldn't be triggered due to the `[HttpPost]` requirement. The form must use `method="post"`.
**Controller**
```cs
// POST is used to send data to a server to create/update a resource.
[HttpPost]
//[ActionName("Add")] // if they're not the same Cs still recognized which Add to use (context: compare Add above and Add below)
public IActionResult AddTag(AddTagRequest addTagRequest) {}
```
**View**
```cs
<form method="post" action="/AdminTags/AddTag">
	<button type="submit" class="btn btn-dark">Add Tag</button>
</form>
```


2) **Action Name Change:** If you refactored the controller method name and removed the `[ActionName]` attribute, the form's current `action` wouldn't find a matching target.
View Name = [ActionName] =>  AddTag = "Add" (which is the View Name)
```cs
  [HttpPost]
[ActionName("Add")] // if they're not the same Cs still recognized which Add to use (context: compare Add above and Add below)
public IActionResult AddTag(AddTagRequest addTagRequest)
{
	// Mapping AddTagRequest to Tag to domain model
	var tag = new Tag
	{
		 Name = addTagRequest.Name,
		 DisplayName = addTagRequest.DisplayName,
	};

	// get data from tag
	bloggieDbContext.Tags.Add(tag);
	// save changes
	bloggieDbContext.SaveChanges();

	return View("Add");
}
```

### Because of the Form tag have 
**1. Input Fields**
- **HTML Structure:** Yes, the `<input>`, `<label>`, and other form elements reside structurally within the boundaries of the `<form>` tag in your HTML document.
	
**2. Form Submission**
- **Data Packaging:** When a user submits the form, the browser collects data from the input fields **specifically associated with that form**. The key attributes here are:
    - **method:** Defines how the data is sent (e.g., 'post', 'get')
    - **action:** Specifies the URL (controller action) where the data is sent.
	   
- **HTTP Request:** The browser bundles the form's data and sends it to the server as part of an HTTP request.
	
+ ! This is not Alright at all
```html
<div class="container d-flex justify-content-around pl-0">
	<div class="mb-3">
		<label class="form-label">Name</label>
		<input type="text" class="form-control" name="Name" />
	</div>
	
	<div class="mb-3">
		<label class="form-label">Display Name</label>
		<input type="text" class="form-control" name="DisplayName" />
	</div>
	
	<form method="post" action="/AdminTags/AddTag">
		<button type="submit" class="btn btn-dark">Add Tag</button>
	</form>
	
	<form method="post" action="/AdminTags/SubmitTag
		<button type="submit" class="btn btn-dark">Update Tag</button>
	</form>
</div>
```
+ $ This is Alright
```cs
<div class="container d-flex justify-content-around pl-0">
  <form method="post" action="/AdminTags/AddTag">
		<div class="mb-3">
			 <label class="form-label">Name</label>
			 <input type="text" class="form-control" name="Name" />
		</div>
		<div class="mb-3">
			 <label class="form-label">Display Name</label>
			 <input type="text" class="form-control" name="DisplayName" />
		</div>
		<button type="submit" class="btn btn-dark">Add Tag</button>
  </form>

  <form method="post" action="/AdminTags/SubmitTag">
		<div class="mb-3">
			 <label class="form-label">Name</label>
			 <input type="text" class="form-control" name="Name" />
		</div>
		<div class="mb-3">
			 <label class="form-label">Display Name</label>
			 <input type="text" class="form-control" name="DisplayName" />
		</div>
		<button type="submit" class="btn btn-dark">Update Tag</button>
  </form>
</div>
```


### Delete read only id : 0000000000000000000000
+ ? Id -> 00000000 bug solve (Cause: Delete Action get id from Add View Form. Not route id)
```cs
// Delete BlogPost by id
[HttpPost]
// Delete - remove tag from bloggieDbContext
public async Task<IActionResult> Delete(EditBlogPostRequest editBlogPostRequest)
{
	// use find for get existing tag
	// Talk to the repository
	var deletedBlogPost = await blogPostRepository.DeleteAsync(editBlogPostRequest.Id);
	if (deletedBlogPost != null)
	{
		 // Show success notification
		 return RedirectToAction("List");
	}
	// show fail notification
	TempData["ErrorMessage"] = "Failed to delete tag. Please try again.";

	return RedirectToAction("List", new { id = editBlogPostRequest.Id });
}
```