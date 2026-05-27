---
category: "3 RESOURCES/Programming/Flutter.md"
summary: "Lists prerequisite SDK manager and licensing commands for mobile app development with Flutter. Details Android Studio emulator launch."
keywords: ["flutter doctor", "mobile dev", "android emulator", "scaffold"]
confidence: "high"
analyzed_at: "2026-05-27T16:37:23.956503+00:00"
---
### Prequisites (Điều kiện tiên quyết)
Vào Command Line > Ghi  **Flutter Doctor** để kiểm tra điều kiện 
Chạy 2 dòng này.
```sh
path/to/sdkmanager --install "cmdline-tools;latest
flutter doctor --android-licenses
```
Nếu không chạy đc thì vào Android Studio tải cái này: 
+ SDK Manager > SDK Tools > kéo xuống > Android SDK Command-line Tools (latest)

### Download Guide: 
+ Flutter Extention (VSCode Extention)
	![[Pasted image 20240824225439.png]]


### Set-up: 
Dùng **Ctr + Shift + P để tìm kiếm**
+ Flutter: New Project
	![[Pasted image 20240824225536.png]]
+ Đợi dự án tạo xong rồi...
+ Launch Emulator
	![[Pasted image 20240824225626.png]]
+ Devide: Pixel 7 API 29
	 ![[Pasted image 20240824225753.png]]
+ Vào **main.dart** >  bấm **F5**

---

![[Pasted image 20240824231715.png]]
Stateless can be change in runtime


**Scraffold** 
![[Pasted image 20240825000528.png]]


