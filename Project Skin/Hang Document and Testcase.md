### POSTMAN test
URL = 'https://heval1st-001-site1.anytempurl.com'

> URL/api/Hang/GetAllHang
```json

pm.test("Response status code is 200", function () {
  pm.response.to.have.status(200);
});


pm.test("Response has the required fields", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('array');
    responseData.forEach(item => {
        pm.expect(item).to.have.property('id');
        pm.expect(item).to.have.property('ma_hang_hoa');
        pm.expect(item).to.have.property('ten_hang_hoa');
        pm.expect(item).to.have.property('so_luong');
        pm.expect(item).to.have.property('ghi_chu');
    });
});


pm.test("Id has a valid data type", function () {
    const responseData = pm.response.json();
    responseData.forEach(item => {
        pm.expect(item.id).to.be.a('number');
    });
});

pm.test("Ma_hang_hoa has a valid data type", function () {
    const responseData = pm.response.json();
    responseData.forEach(item => {
        pm.expect(item.ma_hang_hoa).to.be.a('number');
    });
});

pm.test("Content-Type header is application/json", function () {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});


pm.test("Ma hang hoa should be a non-negative integer", function () {
    const responseData = pm.response.json();
    
    pm.expect(responseData).to.be.an('array');
    responseData.forEach(function(item) {
        pm.expect(item.ma_hang_hoa).to.be.a('number');
        pm.expect(item.ma_hang_hoa).to.be.at.least(0);
    });
});
```
![[Pasted image 20240419110735.png]]

> URL/api/Hang/HangById2
```json
pm.test("Response status code is 200", function () {
    pm.response.to.have.status(200);
});

pm.test("Response has the correct Content-Type", function () {
    pm.response.to.have.header("Content-Type", "application/json; charset=utf-8");
});

pm.test("Response is an object with id property", function () {
    pm.expect(pm.response.json()).to.be.an('object').that.has.property('id');
});

pm.test("Response is an object with ma_hang_hoa property", function () {
    pm.expect(pm.response.json()).to.be.an('object').that.has.property('ma_hang_hoa');
});

pm.test("Response is an object with ten_hang_hoa property", function () {
    pm.expect(pm.response.json()).to.be.an('object').that.has.property('ten_hang_hoa');
});

pm.test("Response is an object with so_luong property", function () {
    pm.expect(pm.response.json()).to.be.an('object').that.has.property('so_luong');
});

pm.test("Response is an object with ghi_chu property", function () {
    pm.expect(pm.response.json()).to.be.an('object').that.has.property('ghi_chu');
});
```
![[Pasted image 20240419110815.png]]



> URL/api/Hang/DelelteHang2


**Input Note & mandatory conditions:** 
+  so_luong input are always number
+  ma_hang_hoa is always number
+  ten_hang_hoa is always string
### CreateHang testcase
> URL/api/Hang/UpdateHang

### CreateHang testcase
> URL/api/Hang/CreateHang

1. **Missing/Empty Fields:**
2. **Invalid** `ma_hang_hoa`
Less than 10:
```json
{ "id": 0, "ma_hang_hoa": 5, "ten_hang_hoa": "Item", "so_luong": 2, "ghi_chu": "Test" }
```
Greater than 99:
```json
{ "id": 0, "ma_hang_hoa": 105, "ten_hang_hoa": "Item", "so_luong": 2, "ghi_chu": "Test" }
```

3. **Invalid** `so_luong`
Negative
```json
{ "id": 0, "ma_hang_hoa": 12, "ten_hang_hoa": "Item", "so_luong": -3, "ghi_chu": "Test" }
```
Wrong Data Type
```json
{ "id": 0, "ma_hang_hoa": 12, "ten_hang_hoa": "Item", "so_luong": -3, "ghi_chu": "Test" }
```

4. 3. **Invalid** `ten_hang_hoa`
Numbers only:
```json
{ "id": 0, "ma_hang_hoa": 12, "ten_hang_hoa": "23", "so_luong": 2, "ghi_chu": "Test" }
```
Special Characters:
```json
{ "id": 0, "ma_hang_hoa": 12, "ten_hang_hoa": "Item!", "so_luong": 2, "ghi_chu": "Test" }
```

5. **Duplicate** `ma_hang_hoa`
![[Pasted image 20240419115914.png]]


6. ten_hang_hoa != string and so_luong !>0 
```json
{
  "id": 0,
  "ma_hang_hoa": 0,
  "ten_hang_hoa": "23",
  "so_luong": 0,
  "ghi_chu": "string"
}
```
![[Pasted image 20240419115143.png]]

7. Special Character in ten_hang_hoa test
```json
{
  "id": 0,
  "ma_hang_hoa": 30,
  "ten_hang_hoa": "**#2",
  "so_luong": 29,
  "ghi_chu": "string"
}
```
Error: response status is 400
```json
{
  "thanh_warning_msg": [
    "ten_hang_hoa must contain only letters and spaces."
  ]
}
```

