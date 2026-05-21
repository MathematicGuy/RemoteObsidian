[Docker in 100s](https://youtu.be/Gjnup-PuquQ?si=qhHV2MuiRhgwhLhU)
[[Docker PostgresSQL]]
[Learn Docker in 7 Easy Steps](https://youtu.be/gAkwW2tuIqE?si=iFCKMldzyn4zfPRa)
[[Docker tips & bugs]]

### [[Docker Q&A]]

### [[Docker Learning Motivation]]
```ad-success
+ **"Works on My Machine" Syndrome Vanishes:** Projects with complex setups often break when moving between environments (your laptop, a classmate's, or university servers). Docker erases this problem, ensuring your work runs consistently.

- **Project Collaboration Made Easy:** Work with teams seamlessly. Everyone pulls the same Docker image, guaranteeing a shared development environment – a huge headache saver!

- **Internships and Beyond:** Many companies in tech expect some level of container knowledge, making you a more competitive candidate.

- **Portfolio Builder:** Include Dockerfiles with your projects. Showcases your understanding of reproducible environments, a major plus for potential employers.
```

---
 **note:**
+ Container orchestration platforms like Kubernetes and Docker Swarm

---
### Docker offer an Isolated environments called containers.
```ad-summary
Docker provides you with portable environments (containers) that you can build once and use for any project, giving you flexibility and incredible consistency across different systems.
```


**What is Docker?**
- ? **Containerization Platform:** Docker is a powerful tool that simplifies the process of packaging, shipping, and running applications within isolated environments called containers.
	
+ ? **Lightweight Packages:** Think of a container as a neatly wrapped package that holds everything your application needs to run smoothly. This includes the code itself, **all the necessary libraries, system tools, and configuration files.**
	
- ? **Isolated Execution:** Containers **run as self-contained units**, each with its own isolated slice of the operating system's resources like file system, memory, and processes. This **isolation means that a containerized application won't interfere with other applications or the host system itself.**
	+ **Why care about Isolation ?**
		Running an env seperatly from other envs. (Just think of it like an virtual car engine. Which can be swap in & out whenever you want)
		
	1. **Portability:** Since a **container carries its entire environment**, you can move it from your development machine to a testing server, and then to production without worrying if the right dependencies and libraries are in place. It works the same everywhere!
		-> And I can duplicate the environment as many time as I want
		
	2. **Consistency:** Containers **eliminate the "it works on my machine" problem**. If it runs in a container during development, it will **run the same way in other environments**.
	    
	3. **Efficiency:** Unlike virtual machines (VMs), which include a full operating system for each instance, **containers share the host's operating system kernel**. This makes them **super lightweight**, meaning you **can run more of them on the same hardware**.
	    
	4. **Microservices:** Containers are **ideal for building microservices architectures**, where **your application** is **broken down into smaller, independent components (each running in its own container).**

#### How Docker Solve "It Work on my Machine" Problem
**Problem**
- **Operating system versions and configurations**
- **Installed libraries and dependencies**
- **System tools and configurations**

Docker solves this problem by creating a **standardized and isolated environment** for your application. Here's how:




---
### **Real-World Examples**

- **Spotify:** Spotify extensively uses Docker for its **microservices architecture**. This allows them to **rapidly develop services, scale independently and manage thousands of containers**.
    
- **Netflix:** Netflix uses Docker in its **testing and deployment processes**. They **run tests in containers to ensure consistent, reproducible environments.**

---

