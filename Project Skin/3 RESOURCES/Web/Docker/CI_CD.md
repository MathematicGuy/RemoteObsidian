![[Pasted image 20240219191105.png]]

### CI (Continuous Integration)
> Test Run to see if the New Code can be integrated, compatible and running with the old code.
**Purpose**: To make sure new code changes work well with the existing codebase and don't cause problems.

**How it works:** When you add new code (think of this as changing parts of your website or app), CI will automatically:
	+ Run tests to check if anything breaks.
	+ Build your project to make sure all the pieces fit together.	
+ ? Like an Rocket testing in a simulation to see if it fly.    

### CD (Continuous Delivery)
**Purpose:** To get your finished code changes ready for release (putting it where people 
can use it. eg. github) 	

**How it works**: After your code passes all the checks in CI, CD takes the following steps
	+ Packages the code in a way that's easy to deploy.
	+ Places the package in a location ready to be put live (this could be a staging environment for more testing or directly to a production environment).
+ ? Like When Each Part of the Rocket bing safly delivered to ther launchers and ready to launch

**Git's Role:**
	Git is a version control system. Here's how it fits in with CI/CD:

- You store your code and all its changes in a Git repository.
- CI is often triggered when you push new code changes to Git.
- CD might grab the finished package from Git to deliver.

```ad-summary
CI/CD is a team of helpers that make sure new code works great and gets to everyone who wants to use it quickly!
```

[[Docker]]

### Project: Deploy CI/CD for ASP.NET Core applications to Azure DevOps

- **ASP.NET Core:** Tool used to make websites and apps that run on computers.

- **Azure DevOps:** A special place in the cloud where people who build these websites and apps work together. It has tools to help them build, test, and share their creations.

- **CI/CD Pipeline:** A super helpful robot that lives in Azure DevOps. It can do these things automatically:
    - **Check if new code works:** Every time a builder adds new code (like changing a website's color), the pipeline makes sure it doesn't break anything.
    - **Package the website:** The pipeline puts all the pieces of the website together in a neat package, ready to be used.
    - **Deliver the website:** The pipeline sends the package to a special place where everyone can access the website or app.

- **CI (Continuous Integration):** The practice of automating code merging and testing as developers make changes.
- **CD (Continuous Delivery/Deployment):** The practice of automating the steps to get new code versions into production environments.

- [ ] What is CI/CD ? 
- [ ] How to CI/CD ?
- [ ] Integrate CI/CD ?


### Azure Repos
![[Pasted image 20240316231047.png]]

![[Pasted image 20240316232311.png]]

![[Pasted image 20240316232321.png]]
![[Pasted image 20240316232425.png]]
Test and Build
Build and Push Image with docker 

![[Pasted image 20240317174705.png]]
But nowaday we use Docket Images
![[Pasted image 20240317174745.png]]