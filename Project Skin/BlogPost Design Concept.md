```html
<!-- BlogPosts Container -->
<div class="container">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            @if (Model != null && Model.Any())
            {
                foreach (var blogPost in Model)
                {
                    <article class="blog-post mb-5 card">
                        <div class="card-body">
                            <header class="blog-post-header">
                                <h1 class="blog-post-title display-6 mb-4">@blogPost.Heading</h1>
                                <div class="blog-post-meta text-muted d-flex justify-content-between">
                                    <span>@blogPost.PublishedDate.ToString("MMMM dd, yyyy")</span>
                                    <span>@blogPost.Author</span>
                                </div>
                            </header>


                            <div class="blog-post-content mt-4">
                                <p class="lead">@blogPost.ShortDescription</p>
                                <a href="/blog/@blogPost.UrlHandle" class="btn btn-primary">Read More</a>
                            </div>

                            <footer class="blog-post-footer mt-4">
                                @if (blogPost.Tags != null && blogPost.Tags.Any())
                                {
                                    <div class="blog-post-tags">
                                        @foreach (var tag in blogPost.Tags)
                                        {
                                            <a href="/blog/tag/@tag.Name" class="badge bg-secondary text-decoration-none">@tag.Name</a>
                                        }
                                    </div>
                                }
                            </footer>
                        </div>
                    </article>
                }
            }
        </div>
    </div>
</div>

```

**Key Parts of Your BlogPost Design**

1. **BlogPosts Container:** This is the overarching structural element that holds all of your blog post listings.
```html
<div class="container">
  <div class="row justify-content-center">
    <div class="col-lg-8">
      </div>
  </div>
</div>
```

2. **Blog Article:** Each individual blog post is represented by this section.
```html

<div class="blog-post-image">
  <img src="@blogPost.FeaturedImageUrl" alt="@blogPost.Heading" class="img-fluid" />
</div>
```

3. **Blog Post Header:** Contains the title, date, and author information.
```cs
<header class="blog-post-header">
    <h1 class="blog-post-title display-6 mb-4">@blogPost.Heading</h1>
    <div class="blog-post-meta text-muted d-flex justify-content-between">
        <span>@blogPost.PublishedDate.ToString("MMMM dd, yyyy")</span>
        <span>@blogPost.Author</span>
    </div>
</header>

```

4. **Blog Post Image (Example):** This is where you'd display a featured image.
```cs
<div class="blog-post-image">
    <img src="@blogPost.FeaturedImageUrl" alt="@blogPost.Heading" class="img-fluid" />
</div>
```


5. **Blog Post Content, Description, Read More (Example):** Includes short description and the 'Read More' button.
```html
<div class="blog-post-content mt-4">
    <p class="lead">@blogPost.ShortDescription</p>
    <a href="/blog/@blogPost.UrlHandle" class="btn btn-primary">Read More</a>
</div>
```

**How to Integrate**
Here's how you could integrate these new examples into your existing code structure:
```html
<article class="blog-post mb-5 card">
    <div class="card-body">
     <header class="blog-post-header">
       </header>

     <div class="blog-post-image">
         <img src="@blogPost.FeaturedImageUrl" alt="@blogPost.Heading" class="img-fluid" />
     </div>

     <div class="blog-post-content mt-4">
       <p class="lead">@blogPost.ShortDescription</p>
       <a href="/blog/@blogPost.UrlHandle" class="btn btn-primary">Read More</a>
     </div>
</article>
```


![[Pasted image 20240403135427.png]]