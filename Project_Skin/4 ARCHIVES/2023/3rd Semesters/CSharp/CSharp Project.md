
# C# Project Online Book Shop Using ASP.Net and SQL Server
(https://www.youtube.com/@MyCodeSpace1)

(Motivation: Thực tiễn hơn cho việc bán sách Online)
## Main Ideas

## **Export to Excel**


note
run this file
fix id to ID
![[Pasted image 20230827150004.png]]



khả năg có lỗi ở đoạn này
![[Pasted image 20230827164737.png]]


SQL Data Base
![[Pasted image 20230827173110.png]]

CatId -> CataID

ConStr = "Date File Copy&Paste"
![[Pasted image 20230827210111.png]]



![[Pasted image 20230827231510.png]]
Summary by reading all the Source Code. Review  briefly about the Project.
	Split and Map out the Main Things to Learn. Learn what is truly valuable (What made the most of value and  allow me to create) 
	Lazer focus about those Point -> Practice Practice (Document & Summarize, can be times wasting)

Cột trong SQL đếm từ 1.

Cat -> Cata (in catagory)


Desire layout
![[Pasted image 20230828090526.png]]

CategoryList comming from here
![[Pasted image 20230828093108.png]]
like this:
![[Pasted image 20230828092651.png]]


Free WebHost
https://youtu.be/IbUmbYKY_Q4?si=hniNuVqbF7yKMIzK

```html
<%@ Master Language="C#" AutoEventWireup="true" CodeBehind="AdminMaster.Master.cs" Inherits="NeinOnlineBookShop.Views.Admin.Admin" %>

<!DOCTYPE html>

<html>
<head runat="server">
    <title></title>
    <style>
        *{
            font-family:'FiraCode Nerd Font Propo';
        }
        #left{
            color:white;
            height:800px;
            background-color:rosybrown;
        }
        label{
            color:white;
        }
     

    </style>
    <link href="../../Assets/Lib/css/bootstrap.min.css" rel="stylesheet" />
    <asp:ContentPlaceHolder ID="head" runat="server"> </asp:ContentPlaceHolder>

</head>

<body>
    <div class="container-fluid">
        <div class="row">
            <div class="col-2 bg-danger"  id="left">
                <div style="height: 140px">
                </div>

                <div class="p-2">

                    <div class="mb-3">
                        <img src="../../Assets/Images/bookShelf.jpg" height="40" width="40" />
                        <a href="Books.aspx">
                            <label>Books </label>
                        </a>
                    </div>

                    <div class="mb-3">
                        <%-- connect to Author aspx file --%>

                        <img src="../../Assets/Images/typing.png" height="40" width="40" />
                        <a href="Author.aspx">
                            <label>Authors </label>
                        </a>
                    </div>

                    <div class="mb-3">
                        <img src="../../Assets/Images/administration.png" height="40" width="40" />
                        <a href="Sellers.aspx">
                            <label>Sellers </label>
                        </a>
                    </div>

                    <div class="mb-3">
                        <img src="../../Assets/Images/category.png" height="40" width="40" />
                        <a href="Categories.aspx">
                            <label>Categories </label>
                        </a>
                    </div>

                    <div style="height: 286px"></div>

                    <div class="mb-3">
                        <img src="../../Assets/Images/house_100px.png" height="40" width="40" />
                        <a href="Login.aspx">
                            <label>Logout </label>
                        </a>
                    </div>

                </div>
            </div>

        </div>

        <%-- This is the Content Holder. Take Contents from other file and push it here --%>
		  <div class="col-10">
		      <form id="form1" runat="server">
		          <div>
		              <asp:ContentPlaceHolder ID="MyContent" runat="server"></asp:ContentPlaceHolder>
		          </div>
		      </form>
		  </div>

    </div>

</body>    
</html>

```


Bug Đănh Nhập Khó Hiểu Đoạn này
![[Pasted image 20230830144828.png]]



Chú Ý
Bug1: Dữ Liệu {SelEmail} phải có {user@Gmail.com}
![[Pasted image 20230830192557.png]]
![[Pasted image 20230830192520.png]]

Bug2:  Cài sai tên.
![[Pasted image 20230830195721.png]]