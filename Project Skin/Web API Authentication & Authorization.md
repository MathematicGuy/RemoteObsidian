


```csharp
    [HttpPost]
    public async Task<IActionResult> Register(RegisterViewModel model)
    {
        HttpResponseMessage response = await _httpClient.PostAsJsonAsync("https://example.com/api/register", model);
        if (response.IsSuccessStatusCode)
        {
            // Registration successful
            return RedirectToAction("Login");
        }
        else
        {
            // Registration failed
            ModelState.AddModelError(string.Empty, "Registration failed. Please try again.");
            return View(model);
        }
    }
```

note: Chỉ cần Auth trên WebAPI
**Connect WebMVC to WebAPI**
1) Chỉ cần Auth trên WebAPI. Hợp lệ Thì được phép dùng các Action
2) Cài đặt IdentityUser trên WebMVC
2) Sử dụng Web API để lấy Role xác nhận. 

```cs


[HttpPost]
public async Task<IActionResult> Login(LoginViewModel loginViewModel)
{
	// Get the access token from the session, local storage, or cookie
	var accessToken = _httpContextAccessor.HttpContext.Session.GetString("AccessToken");

	// Set the access token in the request headers
	_httpClient.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", accessToken);

	// Make a request to a protected endpoint in the Web API
	HttpResponseMessage response = await _httpClient.GetAsync("https://localhost:7116/login?useCookies=false&useSessionCookies=false");

	if (response.IsSuccessStatusCode)
	{
		 // Handle successful response
			  return RedirectToAction("Hang", "ViewHang");
	}
	else
	{
		 // Handle error response
		 return RedirectToAction("Login");
	}
}
```
