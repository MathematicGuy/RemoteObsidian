Set up [SHH Keys](https://youtu.be/RGOj5yH7evk?si=uBO5M8sRXltefoGh&t=1230) (using GitBash Terminal)
Create a ssh key gen name a_name which store in C:/
```bash
ssh-keygen -t a_name -b 4097 -C "email@example.com"
```

The key fingerprint is:
SHA256:Mlrlp4+6k9oKQEsptoEDm0e9352WKJ433mh4WJqcZao nhatthanhdinh482@gmail.com
The key's randomart image is:
+---[RSA 4096]----+
|. ..             |
|o+. .            |
|**.  .  .        |
|=o+ .  o         |
|.o   .+.So.o     |
| .   ooo*o=      |
|  . .o #..       |
|   . .& ==       |
|    E++O+.o      |
+----[SHA256]-----+

**Check SSH keys** 
*grep on GitBash / Linux* 
```bash
ls | grep testKey
```
*findstr On Windows* 
```bash
ls | findstr KeyName
```

**Copy file data**
Git/Linux
```bash
pbcopy < ~/KeyName.pub
```
Windows
```bash
type C:\Path\To\KeyName.pub | clip
```
Then Add New SSH Key
![[Pasted image 20231105102455.png]]

**Start the ssh-agent in the background.**
```bash
eval "$(ssh-agent -s)"
```
output: Agent pid 59566


modify `~/.ssh/config`
```bash
Host *
  IgnoreUnknown AddKeysToAgent,UseKeychain
  AddKeysToAgent yes
  UseKeychain yes
```
If that not work then try this
```bash
Host *
  IgnoreUnknown AddKeysToAgent,UseKeychain
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa
```

**Add your SSH private key to the ssh-agent and store your passphrase in the keychain.**
> Replace `your_private_key` with the name of your private key file.
```bash
ssh-add ~/.ssh/your_private_key
```
or
```bash
ssh-add -K /.ssh/id_rsa
```

**Check your connection**
```bash
ssh -T git@github.com
```

