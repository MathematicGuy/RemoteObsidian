**SOMMER**
	User push project to Web to publish online
+ Sommer offer free Web Hosting but no personal SSL
+ User just push Project folder to Sommer. And Sommer handle the rest
	Pros: 
		+ Easy to use, Good for Beginner
		+ Website only Stop if unactive > 30 days
	Cons: 
		+ Must go directly to Sommer website and replace old project folder with the new one to Update the WebApp
		+ Have to self pick Project file to upload.
+ $ zip Project Foler -> go to Sommer -> Replace Old Project Folder with New Project Folder into /site -> Reload Website
+ ! Do most thing Manually



**SMARTERASAP.NET**
	User get Website Connection info and Publish all data to the Website easily.
	Pros:
		+ Website being deploy right on the Web
		+ User just need to get WebDeploy_Info to connect directly to Visual Studio.
		+ just need to click re-publish to Update the whole website. No further action
	Cons: Limtited to 60-days-trial
+ $ Get WebDeploy_profile -> Add connection profile -> Publish -> Done
+ ! Just Integrate WebDeploy profile everything else is automated.

```js
       //   const username = '11165828';
       //   const password = '60-dayfreetrial';
	      //const url = 'http://pitech-001-site1.ftempurl.com/Circle/CalculateAreaAndPerimeter?radius=${radius}';


		 // const basic = `${username}:${password}`;
		 // const basicAuthHeader = `Basic ${btoa(basic)}`;

		 // const options = {
			//method: 'GET',
			//mode: 'no-cors',
			//headers: {
			//  'Authorization': basicAuthHeader
			//}
		 // };

           fetch('https://localhost:7116/api/Hang') // Assuming your API is running on port 5000
          .then(response => response.json())
          .then(data => {
              // Process the received product data (data will be your hang_hoa list)
              console.log(data);
          });


	//	const proxyUrl = 'http://localhost:8080/proxy/Circle/CalculateAreaAndPerimeter'; 

	//	fetch(`${proxyUrl}?radius=${radius}`)
	//	  .then(response => response.json())
	//	  .then(data => {
	//		resultDiv.innerText = `Diện tích hình tròn là: ${data.area}`;
	//	  })
	//	  .catch(error => {
	//		alert('Đã xảy ra lỗi khi gọi API.');
	//	  });
	//});
```