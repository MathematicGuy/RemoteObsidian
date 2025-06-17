![[Pasted image 20250617094558.png# left]]

### Version Control Systen (VCS)
Use to track and Save changes of a files, system through times.
![[Pasted image 20250617094931.png# left |260]]

#### 2 Types of VCS: Centralize VCS and Distributed VCS
**Centralize VCS:** risky if server broken/failing.   
![[Pasted image 20250617095201.png| 400]]

 
**Distributed VCS:** Everybody have their own version which is a direct copy from the Server. This allow everyone to modified their own version without worrying the original version from the Database (e.g. github is a database for code)
![[Pasted image 20250617095211.png| 400]]

Mỗi khi có sự thay đổi, git chỉ lưu lại đúng sự thay đổi đó giúp tiết kiệm tài nguyên. 
Mọi version đc lưu offline trên local. Chỉ khi cần lưu trên github thì ms online. 

### Git Status
![[Pasted image 20250617101105.png]]

![[Pasted image 20250617101117.png]]

**git log for tracking commit history information**
![[Pasted image 20250617101214.png]]
`git log` show commit comment and each git information
![[Pasted image 20250617101803.png|400]]
`git log --stat`
![[Pasted image 20250617101550.png|400]]

`git log --author="Sukmadi"` retrieve commit of a specific author

`git log --oneline --graph --all` view git connection (Only use when you don't have Gitlen)

### Restore Changes at Different Stages
`git restore <file>` - 
