[what is REST](https://www.codecademy.com/article/what-is-rest)
REST - REpresentational State Transfer
	REST-compliant systems, often called RESTful systems
	+ stateless, separate the concerns of client and server
	+ **Components** that can be **managed, updated, and reused without affecting the system as a whole,** **even during operation of the system.**
HTTP Verbs
- GET — retrieve a specific resource (by id) or a collection of resources
- POST — create a new resource
- PUT — update a specific resource (by id)
- DELETE — remove a specific resource by id

For example, when a client is accessing a resource with `id` 23 in an `articles` resource with this GET Request:

```
GET /articles/23 HTTP/1.1
Accept: text/html, application/xhtml
```

The server might send back the content with the response header:

```
HTTP/1.1 200 (OK)
Content-Type: text/html
```

### Response Codes
| Status code                 | Meaning                                                                                                           |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| 200 (OK)                    | This is the standard response for successful HTTP requests.                                                       |
| 201 (CREATED)               | This is the standard response for an HTTP request that resulted in an item being successfully created.            |
| 204 (NO CONTENT)            | This is the standard response for successful HTTP requests, where nothing is being returned in the response body. |
| 400 (BAD REQUEST)           | The request cannot be processed because of bad request syntax, excessive size, or another client error.           |
| 403 (FORBIDDEN)             | The client does not have permission to access this resource.                                                      |
| 404 (NOT FOUND)             | The resource could not be found at this time. It is possible it was deleted, or does not exist yet.               |
| 500 (INTERNAL SERVER ERROR) | The generic answer for an unexpected failure if there is no more specific information available.                  |
| 401                         | Unauthorize                                                                                                       |

For each HTTP verb, there are expected status codes a server should return upon success:
- GET — return 200 (OK)
- POST — return 201 (CREATED)
- PUT — return 200 (OK)
- DELETE — return 204 (NO CONTENT) If the operation fails, return the most specific status code possible corresponding to the problem that was encountered.

```json
"email": "hA@gmail.com",
"password": "hA@123"
```


```cs
@using Microsoft.AspNetCore.Identity
@inject SignInManager<IdentityUser> signInManager

                        @if (signInManager.IsSignedIn(User) && User.IsInRole("Admin"))
                        {
                                       
						 <li class="nav-item dropdown">
							 <a class="nav-link dropdown-toggle text-light" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
							  Admin
							 </a>
					
							 <ul class="navbar-nav flex-grow-1">
								  <li class="nav-item">
										<a class="nav-link text-dark" asp-area="" asp-controller="Hang" asp-action="ViewHang">View_Hang</a>
								  </li>
						
								  <li class="nav-item">
										<a class="nav-link text-dark" asp-area="" asp-controller="Hang" asp-action="CreateHang">Create_Hang</a>
								  </li>
						
								  <li class="nav-item">
										<a class="nav-link text-dark" asp-area="" asp-controller="Hang" asp-action="ViewHangById">View_Hang_By_Id</a>
								  </li>
							 </ul>
						</li> 
						}
					}

```


```cs
                   @if (signInManager.IsSignedIn(User))
                   {
                       // Display the User Name if Logged In
                       <div class="btn me-3 text-light">
                           @User?.Identity?.Name
                       </div>

                       <a class="btn me-3 text-light"
                          asp-area=""  
                          asp-controller="Account"
                          asp-action="Logout">
                           Logout
                       </a>
                   }
                   else
                   {
                       <a class="btn me-3 bg-light text-dark"
                          asp-area=""
                          asp-controller="Account"
                          asp-action="Register">
                           Register
                       </a>

                       <a class="btn me-3 text-light"
                          asp-area=""
                          asp-controller="Account"
                          asp-action="Login">
                           Login
                       </a>
                   }
 
```