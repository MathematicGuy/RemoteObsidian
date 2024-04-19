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

> URL/api/Hang/UpdateHang

> URL/api/Hang/DelelteHang2

> URL/api/Hang/CreateHang

