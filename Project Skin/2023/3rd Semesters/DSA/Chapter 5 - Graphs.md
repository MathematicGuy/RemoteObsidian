
---
annotation-target: Slide-DSA-Chapter5 1.pdf
---

### [[Graph Search in 100 seconds]]

> graph G = (V, E)
> + **edge** same as **arc** (Cạnh) 
> + and  **vertex** same as **node** (Đỉnh)
> 	a set of a fintite number.
![[Pasted image 20230815104745.png]]


> Một Grahp G tuần hoàn có thể có nhiều hơn một cây khung.
> + Một đồ thị tuần hoàn có thể có tối đa **n^(n-2)** cây khung, trong đó n là số nút. Trong ví dụ trên, n là 3 do đó **33−2 = 3** cây khung.
![[Pasted image 20230823001733.png]]
>Tất cả các cây khung của một Graph G đều có **cùng số cạnh và số đỉnh**.
> Cây khung **không có bất kỳ vòng tuần hoàn nào**.

>%%
>```annotation-json
>{"created":"2023-08-15T03:54:06.589Z","text":"Bậc của Graph là số cạnh của 1 Đỉnh\n","updated":"2023-08-15T03:54:06.589Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":966,"end":989},{"type":"TextQuoteSelector","exact":"Degree of a vertex/node","prefix":"edge forms a loop, e.g. Dnode.• ","suffix":": The total number of edges that"}]}]}
>```
>%%
>*%%PREFIX%%edge forms a loop, e.g. Dnode.•%%HIGHLIGHT%% ==Degree of a vertex/node== %%POSTFIX%%: The total number of edges that*
>%%LINK%%[[#^68ll14cee0t|show annotation]]
>%%COMMENT%%
>Bậc của Graph là số cạnh của 1 Đỉnh
>
>%%TAGS%%
>
^68ll14cee0t


>%%
>```annotation-json
>{"created":"2023-08-15T03:55:58.253Z","text":"Cạnh đi vào\n","updated":"2023-08-15T03:55:58.253Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":2709,"end":2717},{"type":"TextQuoteSelector","exact":"Indegree","prefix":" have a look at what these are• ","suffix":": The total number of edges that"}]}]}
>```
>%%
>*%%PREFIX%%have a look at what these are•%%HIGHLIGHT%% ==Indegree== %%POSTFIX%%: The total number of edges that*
>%%LINK%%[[#^npdakdr56g|show annotation]]
>%%COMMENT%%
>Cạnh đi vào
>
>%%TAGS%%
>
^npdakdr56g


>%%
>```annotation-json
>{"created":"2023-08-15T03:56:06.900Z","text":"Cạnh đi ra\n","updated":"2023-08-15T03:56:06.900Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":2925,"end":2934},{"type":"TextQuoteSelector","exact":"Outdegree","prefix":"dge CE coming into the E node.• ","suffix":": The total number of edges that"}]}]}
>```
>%%
>*%%PREFIX%%dge CE coming into the E node.•%%HIGHLIGHT%% ==Outdegree== %%POSTFIX%%: The total number of edges that*
>%%LINK%%[[#^cwal3j1ejf4|show annotation]]
>%%COMMENT%%
>Cạnh đi ra
>
>%%TAGS%%
>
^cwal3j1ejf4


>%%
>```annotation-json
>{"created":"2023-08-15T03:56:16.406Z","text":"Đỉnh Cô Lập khi mà cái bậc của Nó là 0. Không nối với cạnh nào, ko liên kết vs các đỉnh khác.\n","updated":"2023-08-15T03:56:16.406Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":3199,"end":3214},{"type":"TextQuoteSelector","exact":"Isolated vertex","prefix":"Directed and undirected Graphs• ","suffix":": A node or vertex is called an "}]}]}
>```
>%%
>*%%PREFIX%%Directed and undirected Graphs•%%HIGHLIGHT%% ==Isolated vertex== %%POSTFIX%%: A node or vertex is called an*
>%%LINK%%[[#^0lfv35e5x55|show annotation]]
>%%COMMENT%%
>Đỉnh Cô Lập khi mà cái bậc của Nó là 0. Không nối với cạnh nào, ko liên kết vs các đỉnh khác.
>
>%%TAGS%%
>
^0lfv35e5x55



>%%
>```annotation-json
>{"created":"2023-08-15T03:57:07.656Z","text":"Đỉnh Nguồn: Không có cạnh đi vào, Có cạnh đi ra","updated":"2023-08-15T03:57:07.656Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":3322,"end":3335},{"type":"TextQuoteSelector","exact":"Source vertex","prefix":", as shown as G node in Fig.3.• ","suffix":": A vertex is called a source ve"}]}]}
>```
>%%
>*%%PREFIX%%, as shown as G node in Fig.3.•%%HIGHLIGHT%% ==Source vertex== %%POSTFIX%%: A vertex is called a source ve*
>%%LINK%%[[#^bv97m9er1yj|show annotation]]
>%%COMMENT%%
>Đỉnh Nguồn: Không có cạnh đi vào, Có cạnh đi ra
>%%TAGS%%
>
^bv97m9er1yj


>%%
>```annotation-json
>{"created":"2023-08-15T03:57:46.940Z","text":"Đỉnh Chìm: Có bậc ngoài là 0,\n Meaning không có cạnh đi ra. Nhưng có Cạnh đi vào.","updated":"2023-08-15T03:57:46.940Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":3475,"end":3486},{"type":"TextQuoteSelector","exact":"Sink vertex","prefix":"e A node is the source vertex.• ","suffix":": A vertex is a sink vertex if i"}]}]}
>```
>%%
>*%%PREFIX%%e A node is the source vertex.•%%HIGHLIGHT%% ==Sink vertex== %%POSTFIX%%: A vertex is a sink vertex if i*
>%%LINK%%[[#^imk2rakyajn|show annotation]]
>%%COMMENT%%
>Đỉnh Chìm: Có bậc ngoài là 0,
> Meaning không có cạnh đi ra. Nhưng có Cạnh đi vào.
>%%TAGS%%
>
^imk2rakyajn


>%%
>```annotation-json
>{"created":"2023-08-15T03:59:18.548Z","text":"Đồ thị Thẳng  Tiến (Không vòng). Các nút hướng thẳng tới 1 nút khác. Không thể tạo ra 1 vòng lặp đóng.","updated":"2023-08-15T03:59:18.548Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":3965,"end":3988},{"type":"TextQuoteSelector","exact":"Directed acyclic Graphs","prefix":"e of the last edge in a sequence","suffix":"Fig.4. Example of a directed acy"}]}]}
>```
>%%
>*%%PREFIX%%e of the last edge in a sequence%%HIGHLIGHT%% ==Directed acyclic Graphs== %%POSTFIX%%Fig.4. Example of a directed acy*
>%%LINK%%[[#^lsje7xqpqn|show annotation]]
>%%COMMENT%%
>Đồ thị Thẳng  Tiến (Không vòng). Các nút hướng thẳng tới 1 nút khác. Không thể tạo ra 1 vòng lặp đóng.
>%%TAGS%%
>
^lsje7xqpqn


>%%
>```annotation-json
>{"created":"2023-08-15T04:01:49.276Z","text":"Đồ thị Vô Hướng, chỉ nối với nhau.\n","updated":"2023-08-15T04:01:49.276Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":4525,"end":4541},{"type":"TextQuoteSelector","exact":"Connected Graphs","prefix":" there is a path from vi to vj .","suffix":"Figure a) Connected graphs Figur"}]}]}
>```
>%%
>*%%PREFIX%%there is a path from vi to vj .%%HIGHLIGHT%% ==Connected Graphs== %%POSTFIX%%Figure a) Connected graphs Figur*
>%%LINK%%[[#^fjaqc0r0j2s|show annotation]]
>%%COMMENT%%
>Đồ thị Vô Hướng, chỉ nối với nhau.
>
>%%TAGS%%
>
^fjaqc0r0j2s


>%%
>```annotation-json
>{"created":"2023-08-15T04:05:08.361Z","text":"ĐỒ Thị liên thông, giữa 2 đỉnh bất kì khác nhau trên đồ thị thì phải có đường đi giữa nó.\n\n","updated":"2023-08-15T04:05:08.361Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":4551,"end":4567},{"type":"TextQuoteSelector","exact":"Connected graphs","prefix":"o vj .Connected GraphsFigure a) ","suffix":" Figure b) Unconnected graphs• A"}]}]}
>```
>%%
>*%%PREFIX%%o vj .Connected GraphsFigure a)%%HIGHLIGHT%% ==Connected graphs== %%POSTFIX%%Figure b) Unconnected graphs• A*
>%%LINK%%[[#^nvkezooxond|show annotation]]
>%%COMMENT%%
>ĐỒ Thị liên thông, giữa 2 đỉnh bất kì khác nhau trên đồ thị thì phải có đường đi giữa nó.
>
>
>%%TAGS%%
>
^nvkezooxond


>%%
>```annotation-json
>{"created":"2023-08-15T04:06:29.568Z","text":"Đò thị có Trọng Số.\n","updated":"2023-08-15T04:06:29.568Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":4857,"end":4872},{"type":"TextQuoteSelector","exact":"Weighted graphs","prefix":"ing on the purpose of the graph:","suffix":"Fig.5. Example of a weighted gra"}]}]}
>```
>%%
>*%%PREFIX%%ing on the purpose of the graph:%%HIGHLIGHT%% ==Weighted graphs== %%POSTFIX%%Fig.5. Example of a weighted gra*
>%%LINK%%[[#^v8wx0p43ynd|show annotation]]
>%%COMMENT%%
>Đò thị có Trọng Số.
>
>%%TAGS%%
>
^v8wx0p43ynd


>%%
>```annotation-json
>{"created":"2023-08-15T04:07:55.144Z","text":"Đồ Thị Hai Phía: \nĐồ thị được chia thành 2 Tập Hợp. \nCác đỉnh của cạnh này nối với cá đỉnh của bên kia.","updated":"2023-08-15T04:07:55.144Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":5270,"end":5286},{"type":"TextQuoteSelector","exact":"Bipartite graphs","prefix":"et to the nodes of another set. ","suffix":"Fig.6. Example of a bipartite gr"}]}]}
>```
>%%
>*%%PREFIX%%et to the nodes of another set.%%HIGHLIGHT%% ==Bipartite graphs== %%POSTFIX%%Fig.6. Example of a bipartite gr*
>%%LINK%%[[#^m6v0r6ga3p|show annotation]]
>%%COMMENT%%
>Đồ Thị Hai Phía: 
>Đồ thị được chia thành 2 Tập Hợp. 
>Các đỉnh của cạnh này nối với cá đỉnh của bên kia.
>%%TAGS%%
>
^m6v0r6ga3p


>%%
>```annotation-json
>{"created":"2023-08-15T04:14:03.971Z","text":"Cây với đồ Thị khác nhau ở việc\nĐồ thị không có các Mqh Cha Con như Cây.\n1 Cha có thể có nhiều con nhưng con thì chỉ có 1 Cha.\n","updated":"2023-08-15T04:14:03.971Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf"}
>```
>%%
>*%%PREFIX%%%%HIGHLIGHT%% ==== %%POSTFIX%%*
>%%LINK%%[[#^3xe536fi4tm|show annotation]]
>%%COMMENT%%
>Cây với đồ Thị khác nhau ở việc
>Đồ thị không có các Mqh Cha Con như Cây.
>1 Cha có thể có nhiều con nhưng con thì chỉ có 1 Cha.
>
>%%TAGS%%
>
^3xe536fi4tm




>%%
>```annotation-json
>{"created":"2023-08-15T04:17:00.401Z","text":"Danh sách Liên Kết\n","updated":"2023-08-15T04:17:00.401Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":5995,"end":6007},{"type":"TextQuoteSelector","exact":" linked list","prefix":"ist representation is based on a","suffix":". In this, we represent the grap"}]}]}
>```
>%%
>*%%PREFIX%%ist representation is based on a%%HIGHLIGHT%% ==linked list== %%POSTFIX%%. In this, we represent the grap*
>%%LINK%%[[#^q168djkl6j|show annotation]]
>%%COMMENT%%
>Danh sách Liên Kết
>
>%%TAGS%%
>
^q168djkl6j


>%%
>```annotation-json
>{"created":"2023-08-15T04:17:34.487Z","text":"Danh sách Liền kề dựa trên Danh sách Liên Kết. Ở đây, mình giới thiệu Đồ Thị bằng việc bảo toàn 1 danh sách các liên kết.","updated":"2023-08-15T04:17:34.487Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":5952,"end":5967},{"type":"TextQuoteSelector","exact":"adjacency list ","prefix":"atrix.Graph representations• An ","suffix":"representation is based on a lin"}]}]}
>```
>%%
>*%%PREFIX%%atrix.Graph representations• An%%HIGHLIGHT%% ==adjacency list== %%POSTFIX%%representation is based on a lin*
>%%LINK%%[[#^admxf258sxi|show annotation]]
>%%COMMENT%%
>Danh sách Liền kề dựa trên Danh sách Liên Kết. Ở đây, mình giới thiệu Đồ Thị bằng việc bảo toàn 1 danh sách các liên kết.
>%%TAGS%%
>
^admxf258sxi


>%%
>```annotation-json
>{"created":"2023-08-15T04:18:55.871Z","text":"Danh sách Liền Kề 2: \nMỗi Nút đại diện 1 Danh Sách liên kết.\n Đỉnh A có ds liền kề là B,C\nvới B ds liền kề là E,C,A\n","updated":"2023-08-15T04:18:55.871Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":6709,"end":6724},{"type":"TextQuoteSelector","exact":"Adjacency lists","prefix":" direct connection between them:","suffix":"Fig.7. An Example a graph of 5 n"}]}]}
>```
>%%
>*%%PREFIX%%direct connection between them:%%HIGHLIGHT%% ==Adjacency lists== %%POSTFIX%%Fig.7. An Example a graph of 5 n*
>%%LINK%%[[#^jpbhkd4owm|show annotation]]
>%%COMMENT%%
>Danh sách Liền Kề 2: 
>Mỗi Nút đại diện 1 Danh Sách liên kết.
> Đỉnh A có ds liền kề là B,C
>với B ds liền kề là E,C,A
>
>%%TAGS%%
>
^jpbhkd4owm


>%%
>```annotation-json
>{"created":"2023-08-15T04:23:22.657Z","text":"Ma Trận Liền Kề:\nCó giá trị là 0 và 1 \nNếu 2 đỉnh liên kết với nhau là 1;\nKhông có cạnh là 0","updated":"2023-08-15T04:23:22.657Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":7878,"end":7894},{"type":"TextQuoteSelector","exact":"Adjacency matrix","prefix":"ding adjacency matrix, in Fig.9.","suffix":"Fig.9. Adjacency matrix for a gi"}]}]}
>```
>%%
>*%%PREFIX%%ding adjacency matrix, in Fig.9.%%HIGHLIGHT%% ==Adjacency matrix== %%POSTFIX%%Fig.9. Adjacency matrix for a gi*
>%%LINK%%[[#^xg783bofybe|show annotation]]
>%%COMMENT%%
>Ma Trận Liền Kề:
>Có giá trị là 0 và 1 
>Nếu 2 đỉnh liên kết với nhau là 1;
>Không có cạnh là 0
>%%TAGS%%
>
^xg783bofybe


>%%
>```annotation-json
>{"created":"2023-08-15T04:37:52.146Z","text":"Duyệt Đồ Thị: Có duyệt theo thứ tự như cây\nTrước, Giữa, Sau","updated":"2023-08-15T04:37:52.146Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":9719,"end":9735},{"type":"TextQuoteSelector","exact":"Adjacency matrix","prefix":"oduced looks like the following:","suffix":"(1, 1): 0 represents the absence"}]}]}
>```
>%%
>*%%PREFIX%%oduced looks like the following:%%HIGHLIGHT%% ==Adjacency matrix== %%POSTFIX%%(1, 1): 0 represents the absence*
>%%LINK%%[[#^t0rzdgm7gz9|show annotation]]
>%%COMMENT%%
>Duyệt Đồ Thị: Có duyệt theo thứ tự như cây
>Trước, Giữa, Sau
>%%TAGS%%
>
^t0rzdgm7gz9


>%%
>```annotation-json
>{"created":"2023-08-15T04:39:28.971Z","text":"(hay Breath-frist Search)\nDuyệt theo Chiều Rộng - Đầu tiên\n| (giống duyệt theo mức ở cấu trúc cây)\n-> Thăm tất cá các nút ở cùng 1 tầng (mức) trước rồi mới quét tiếp.\n+ Bắt đầu từ nút Xuất Pháp (nút Nguồn)\n\nSử dụng Cấu Trúc hàng đợi","updated":"2023-08-15T04:39:28.971Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":12099,"end":12122},{"type":"TextQuoteSelector","exact":"Breadth-first traversal","prefix":" that no vertex is visited twice","suffix":"Breadth-first traversalFig.10 pr"}]}]}
>```
>%%
>*%%PREFIX%%that no vertex is visited twice%%HIGHLIGHT%% ==Breadth-first traversal== %%POSTFIX%%Breadth-first traversalFig.10 pr*
>%%LINK%%[[#^f22fq7styis|show annotation]]
>%%COMMENT%%
>(hay Breath-frist Search)
>Duyệt theo Chiều Rộng - Đầu tiên
>| (giống duyệt theo mức ở cấu trúc cây)
>-> Thăm tất cá các nút ở cùng 1 tầng (mức) trước rồi mới quét tiếp.
>+ Bắt đầu từ nút Xuất Pháp (nút Nguồn)
>
>Sử dụng Cấu Trúc hàng đợi
>%%TAGS%%
>
^f22fq7styis


>%%
>```annotation-json
>{"created":"2023-08-15T04:43:34.970Z","text":"THăm Lần lượt các đỉnh Láng Giềng. \nNhưng nếu kề nhiều điểm thì thăm đỉnh nào?\n+ CHỉ chọn 1 đỉnh để thăm, Gán đỉnh đó vào Danh sách chờ và sẽ không duyệt lại nó nữa.\n=> Đảm bảo rằng mỗi đỉnh chỉ thăm 1 lần","updated":"2023-08-15T04:43:34.970Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":11341,"end":11355},{"type":"TextQuoteSelector","exact":"BFS algorithm:","prefix":"in a tree data structure. • The ","suffix":" starts by visiting the root nod"}]}]}
>```
>%%
>*%%PREFIX%%in a tree data structure. • The%%HIGHLIGHT%% ==BFS algorithm:== %%POSTFIX%%starts by visiting the root nod*
>%%LINK%%[[#^5wkqltc99kt|show annotation]]
>%%COMMENT%%
>THăm Lần lượt các đỉnh Láng Giềng. 
>Nhưng nếu kề nhiều điểm thì thăm đỉnh nào?
>+ CHỉ chọn 1 đỉnh để thăm, Gán đỉnh đó vào Danh sách chờ và sẽ không duyệt lại nó nữa.
>=> Đảm bảo rằng mỗi đỉnh chỉ thăm 1 lần
>%%TAGS%%
>
^5wkqltc99kt


>%%
>```annotation-json
>{"created":"2023-08-15T04:45:39.108Z","text":"BFS\nBFS\nVisited: Đỉnh đã thăm.\n-> thăm A thì A sẽ đc gán vào list visited.\n+ Từ mỗi đỉnh sẽ suy ra được các Node. Node nào chưa có trong Queue thì append vào Queue.\n+ Queue (FIFO): nút chưa quét từ 1 Đỉnh (Chưa đc thăm)\nVD: Thăm A thì B,C,E sẽ được cho vào Queue\n(vào trước sẽ đc lấy ra trước)\n","updated":"2023-08-15T04:45:39.108Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":12145,"end":12152},{"type":"TextQuoteSelector","exact":"Fig.10 ","prefix":"traversalBreadth-first traversal","suffix":"presents a graph of five nodes o"}]}]}
>```
>%%
>*%%PREFIX%%traversalBreadth-first traversal%%HIGHLIGHT%% ==Fig.10== %%POSTFIX%%presents a graph of five nodes o*
>%%LINK%%[[#^5fdhusnbasq|show annotation]]
>%%COMMENT%%
>BFS
>BFS
>Visited: Đỉnh đã thăm.
>-> thăm A thì A sẽ đc gán vào list visited.
>+ Từ mỗi đỉnh sẽ suy ra được các Node. Node nào chưa có trong Queue thì append vào Queue.
>+ Queue (FIFO): nút chưa quét từ 1 Đỉnh (Chưa đc thăm)
>VD: Thăm A thì B,C,E sẽ được cho vào Queue
>(vào trước sẽ đc lấy ra trước)
>
>%%TAGS%%
>
^5fdhusnbasq


>%%
>```annotation-json
>{"created":"2023-08-15T04:53:59.713Z","text":"a , b, g, d, \nb, e, f , \ne, g \nf , c, h\n","updated":"2023-08-15T04:53:59.713Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf"}
>```
>%%
>*%%PREFIX%%%%HIGHLIGHT%% ==== %%POSTFIX%%*
>%%LINK%%[[#^ee9fselgbe|show annotation]]
>%%COMMENT%%
>a , b, g, d, 
>b, e, f , 
>e, g 
>f , c, h
>
>%%TAGS%%
>
^ee9fselgbe


>%%
>```annotation-json
>{"created":"2023-08-15T04:58:50.659Z","text":"BFS \na , b, g, d, \nb, e, f , \ne, g \nf , c, h\n\nNote: sử dụng queue vì để\n+ Các Đỉnh tới sau sẽ có các Node con tới sau. Ngược lại Đỉnh tới trc sẽ đc Quét trước","updated":"2023-08-15T04:58:50.659Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":13277,"end":13284},{"type":"TextQuoteSelector","exact":"Example","prefix":"-B-C-E-D.Breadth-first traversal","suffix":" implement the following graph i"}]}]}
>```
>%%
>*%%PREFIX%%-B-C-E-D.Breadth-first traversal%%HIGHLIGHT%% ==Example== %%POSTFIX%%implement the following graph i*
>%%LINK%%[[#^im2yyxfg3d9|show annotation]]
>%%COMMENT%%
>BFS 
>a , b, g, d, 
>b, e, f , 
>e, g 
>f , c, h
>
>Note: sử dụng queue vì để
>+ Các Đỉnh tới sau sẽ có các Node con tới sau. Ngược lại Đỉnh tới trc sẽ đc Quét trước
>%%TAGS%%
>
^im2yyxfg3d9


>%%
>```annotation-json
>{"created":"2023-08-15T05:07:22.987Z","text":"+ |V| là tổng số các đỉnh \n+ |E| là tổng số cạnh của đồ thị","updated":"2023-08-15T05:07:22.987Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":13984,"end":13997},{"type":"TextQuoteSelector","exact":"O(|V| + |E|),","prefix":"plexity of the BFS algorithm is ","suffix":" where |V| is the number of vert"}]}]}
>```
>%%
>*%%PREFIX%%plexity of the BFS algorithm is%%HIGHLIGHT%% ==O(|V| + |E|),== %%POSTFIX%%where |V| is the number of vert*
>%%LINK%%[[#^z846qgztidi|show annotation]]
>%%COMMENT%%
>+ |V| là tổng số các đỉnh 
>+ |E| là tổng số cạnh của đồ thị
>%%TAGS%%
>
^z846qgztidi


>%%
>```annotation-json
>{"created":"2023-08-15T05:09:12.497Z","text":"Tốt cho việc :\nTHu thập dữ liệu web\nDuy trì cấp độ chỉ mục cho các Domain (đg miền), search engine.","updated":"2023-08-15T05:09:12.497Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":14120,"end":14148},{"type":"TextQuoteSelector","exact":"FS algorithm is very useful ","prefix":"h.Breadth-first traversal• The B","suffix":"for constructing the shortest pa"}]}]}
>```
>%%
>*%%PREFIX%%h.Breadth-first traversal• The B%%HIGHLIGHT%% ==FS algorithm is very useful== %%POSTFIX%%for constructing the shortest pa*
>%%LINK%%[[#^xd8as8cuix8|show annotation]]
>%%COMMENT%%
>Tốt cho việc :
>THu thập dữ liệu web
>Duy trì cấp độ chỉ mục cho các Domain (đg miền), search engine.
>%%TAGS%%
>
^xd8as8cuix8


>%%
>```annotation-json
>{"created":"2023-08-15T05:10:21.990Z","text":"DFS  - Tìm kiếm theo chiều Sâu.\nVD: \nQUét xuống dưới cùng -> Chạm Đáy thì Quét lên Gốc -> Quét tiếp.","updated":"2023-08-15T05:10:21.990Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":14616,"end":14637},{"type":"TextQuoteSelector","exact":"Depth-first traversal","prefix":" a graph of different locations.","suffix":"• The depth-first search (DFS) o"}]}]}
>```
>%%
>*%%PREFIX%%a graph of different locations.%%HIGHLIGHT%% ==Depth-first traversal== %%POSTFIX%%• The depth-first search (DFS) o*
>%%LINK%%[[#^ufejgrr5qtc|show annotation]]
>%%COMMENT%%
>DFS  - Tìm kiếm theo chiều Sâu.
>VD: 
>QUét xuống dưới cùng -> Chạm Đáy thì Quét lên Gốc -> Quét tiếp.
>%%TAGS%%
>
^ufejgrr5qtc


>%%
>```annotation-json
>{"created":"2023-08-15T05:12:41.272Z","text":"Ví dụ cho Thuật toán DFS \n(Lấy đỉnh đầu tiên trong Stack):\nVisited = []\nStack = []\n+ Step1: Đứa A vào list Visited.\n+ Step2: Gán con của A là B vào trong Stack.\n\n + Step 3: DFS, chạm dáy -> quay lại A.\n\n+ 4) Quay lại S quét và cho C,G vào Stack.\n+ 5) Tới C, quét xung quanh có D, F, E\nStack = [D,E,F,G] \n+ 6) Thăm D thì ko có gì, quay lại C.\n+ 7) Quét E và cho H vào cuối Stack.\n+ 8) [E,H,F,G]","updated":"2023-08-15T05:12:41.272Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":15703,"end":15735},{"type":"TextQuoteSelector","exact":"Example: for the following graph","prefix":"n be added)Depth-first traversal","suffix":" Depth-first traversalExample: f"}]}]}
>```
>%%
>*%%PREFIX%%n be added)Depth-first traversal%%HIGHLIGHT%% ==Example: for the following graph== %%POSTFIX%%Depth-first traversalExample: f*
>%%LINK%%[[#^rd3gjmof4cm|show annotation]]
>%%COMMENT%%
>Ví dụ cho Thuật toán DFS 
>(Lấy đỉnh đầu tiên trong Stack):
>Visited = []
>Stack = []
>+ Step1: Đứa A vào list Visited.
>+ Step2: Gán con của A là B vào trong Stack.
>
> + Step 3: DFS, chạm dáy -> quay lại A.
>
>+ 4) Quay lại S quét và cho C,G vào Stack.
>+ 5) Tới C, quét xung quanh có D, F, E
>Stack = [D,E,F,G] 
>+ 6) Thăm D thì ko có gì, quay lại C.
>+ 7) Quét E và cho H vào cuối Stack.
>+ 8) [E,H,F,G]
>%%TAGS%%
>
^rd3gjmof4cm


>%%
>```annotation-json
>{"created":"2023-08-15T05:22:16.944Z","text":"Queue -> sinh sau đặt cuối (FIFO)\nStack -> Sinh sau cho lên đầu ( LIFO)\n+ Vào cuối đầu ra.\n","updated":"2023-08-15T05:22:16.944Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf"}
>```
>%%
>*%%PREFIX%%%%HIGHLIGHT%% ==== %%POSTFIX%%*
>%%LINK%%[[#^7l9c8t6hwb|show annotation]]
>%%COMMENT%%
>Queue -> sinh sau đặt cuối (FIFO)
>Stack -> Sinh sau cho lên đầu ( LIFO)
>+ Vào cuối đầu ra.
>
>%%TAGS%%
>
^7l9c8t6hwb


>%%
>```annotation-json
>{"created":"2023-08-16T03:21:05.689Z","text":"Tìm đường Ngắn Nhất\ndist = [vô tận] (Cho mọi điểm/cạnh chưa tới có độ dài là vô tận)\nvisited = [0,0,0,0]\n1) Quét các Nút Xung Quanh\n2) Tính Khoảng cách của Nút Hiện tại tới Cạnh của nó.\n+ Nếu Khoảng cách tới Cạnh  < Khoảng Cách trước đó thì Thay Giá Trị mới.  \n3) So sánh các giá trị từ Đỉnh tới các điểm với nhau. Chọn đường ngắn nhất và lặp lại Thuật Toán từ đó. ","updated":"2023-08-16T03:21:05.689Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":19573,"end":19593},{"type":"TextQuoteSelector","exact":"Dijkstra’s algorithm","prefix":"visited set.Dijkstra’s algorithm","suffix":"Example 1: For the graph as show"}]}]}
>```
>%%
>*%%PREFIX%%visited set.Dijkstra’s algorithm%%HIGHLIGHT%% ==Dijkstra’s algorithm== %%POSTFIX%%Example 1: For the graph as show*
>%%LINK%%[[#^htzfv43iib|show annotation]]
>%%COMMENT%%
>Tìm đường Ngắn Nhất
>dist = [vô tận] (Cho mọi điểm/cạnh chưa tới có độ dài là vô tận)
>visited = [0,0,0,0]
>1) Quét các Nút Xung Quanh
>2) Tính Khoảng cách của Nút Hiện tại tới Cạnh của nó.
>+ Nếu Khoảng cách tới Cạnh  < Khoảng Cách trước đó thì Thay Giá Trị mới.  
>3) So sánh các giá trị từ Đỉnh tới các điểm với nhau. Chọn đường ngắn nhất và lặp lại Thuật Toán từ đó. 
>%%TAGS%%
>
^htzfv43iib


>%%
>```annotation-json
>{"created":"2023-08-16T03:33:51.026Z","text":"Bắt đầu từ 1\n","updated":"2023-08-16T03:33:51.026Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":20627,"end":20638},{"type":"TextQuoteSelector","exact":"Example 2: ","prefix":"[1, 1, 1, 1]Dijkstra’s algorithm","suffix":"Input Output7 8 11 2 41 3 51 4 2"}]}]}
>```
>%%
>*%%PREFIX%%[1, 1, 1, 1]Dijkstra’s algorithm%%HIGHLIGHT%% ==Example 2:== %%POSTFIX%%Input Output7 8 11 2 41 3 51 4 2*
>%%LINK%%[[#^i1xzs4ch4n|show annotation]]
>%%COMMENT%%
>Bắt đầu từ 1
>
>%%TAGS%%
>
^i1xzs4ch4n


>%%
>```annotation-json
>{"created":"2023-08-16T03:51:28.693Z","text":"\nĐồ thị vô hướng có\nBFS dùng Queue\nDFS dùng Stack.\n\n\n\n","updated":"2023-08-16T03:51:28.693Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf"}
>```
>%%
>*%%PREFIX%%%%HIGHLIGHT%% ==== %%POSTFIX%%*
>%%LINK%%[[#^76g7zeh8hrf|show annotation]]
>%%COMMENT%%
>
>Đồ thị vô hướng có
>BFS dùng Queue
>DFS dùng Stack.
>
>
>
>
>%%TAGS%%
>
^76g7zeh8hrf


>%%
>```annotation-json
>{"created":"2023-08-16T04:04:07.024Z","text":"1 Node trong Đồ Thị vô hướng hướng tới mọi điểm nối với nó. \n+ VÌ thế nó cũng chưa trọng số  (khoảng cách) từ nó tới Node khác.\n1 Node trong Đồ Thị có hướng chỉ hướng tới Node được hướng tới.","updated":"2023-08-16T04:04:07.024Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf"}
>```
>%%
>*%%PREFIX%%%%HIGHLIGHT%% ==== %%POSTFIX%%*
>%%LINK%%[[#^zq801e1bazh|show annotation]]
>%%COMMENT%%
>1 Node trong Đồ Thị vô hướng hướng tới mọi điểm nối với nó. 
>+ VÌ thế nó cũng chưa trọng số  (khoảng cách) từ nó tới Node khác.
>1 Node trong Đồ Thị có hướng chỉ hướng tới Node được hướng tới.
>%%TAGS%%
>
^zq801e1bazh


>%%
>```annotation-json
>{"created":"2023-08-16T04:36:32.214Z","text":"Cây Khung\n(đồ thị vô hướng có thể tới mọi Node nên nó là cây Khung)\nCây a là cây theo chiều Sâu vì nó ko có nhánh. (cùng 1 tầng)\nCây b là câu theo chiều Rộng vì nó có phân cấp (3 nút nối tới 1 nút)\n ","updated":"2023-08-16T04:36:32.214Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":21352,"end":21365},{"type":"TextQuoteSelector","exact":"Spanning tree","prefix":" is called a spanning tree of G.","suffix":"a) b) c)Depending on the DFS or "}]}]}
>```
>%%
>*%%PREFIX%%is called a spanning tree of G.%%HIGHLIGHT%% ==Spanning tree== %%POSTFIX%%a) b) c)Depending on the DFS or*
>%%LINK%%[[#^c6dpuqcqfgl|show annotation]]
>%%COMMENT%%
>Cây Khung
>(đồ thị vô hướng có thể tới mọi Node nên nó là cây Khung)
>Cây a là cây theo chiều Sâu vì nó ko có nhánh. (cùng 1 tầng)
>Cây b là câu theo chiều Rộng vì nó có phân cấp (3 nút nối tới 1 nút)
> 
>%%TAGS%%
>
^c6dpuqcqfgl


>%%
>```annotation-json
>{"created":"2023-08-16T04:54:56.010Z","text":"Cây Khung tối thiểu\n\nNối tất cả các nút trên đồ thị vs tổng trọng số nhỏ nhất có thể.","updated":"2023-08-16T04:54:56.010Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":21628,"end":21656},{"type":"TextQuoteSelector","exact":"Minimum Spanning Tree (MST) ","prefix":"1)Spanning treea) b)          A ","suffix":"is a spanning tree of the connec"}]}]}
>```
>%%
>*%%PREFIX%%1)Spanning treea) b)          A%%HIGHLIGHT%% ==Minimum Spanning Tree (MST)== %%POSTFIX%%is a spanning tree of the connec*
>%%LINK%%[[#^sl8hd11znm|show annotation]]
>%%COMMENT%%
>Cây Khung tối thiểu
>
>Nối tất cả các nút trên đồ thị vs tổng trọng số nhỏ nhất có thể.
>%%TAGS%%
>
^sl8hd11znm


>%%
>```annotation-json
>{"created":"2023-08-16T04:55:46.636Z","text":"(Không có vòng tròn thì nó là Cây)","updated":"2023-08-16T04:55:46.636Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf"}
>```
>%%
>*%%PREFIX%%%%HIGHLIGHT%% ==== %%POSTFIX%%*
>%%LINK%%[[#^ru5es3rwpvl|show annotation]]
>%%COMMENT%%
>(Không có vòng tròn thì nó là Cây)
>%%TAGS%%
>
^ru5es3rwpvl


>%%
>```annotation-json
>{"created":"2023-08-16T05:08:27.944Z","text":"**Greedy Approach**: Nối mọi số có Trọng Số Nhỏ Nhất trước. ","updated":"2023-08-16T05:08:27.944Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":23894,"end":23935},{"type":"TextQuoteSelector","exact":"Kruskal’s Minimum Spanning Tree algorithm","prefix":"reated using Kruskal’s algorithm","suffix":"Example 201234 5123 13167 16 101"}]}]}
>```
>%%
>*%%PREFIX%%reated using Kruskal’s algorithm%%HIGHLIGHT%% ==Kruskal’s Minimum Spanning Tree algorithm== %%POSTFIX%%Example 201234 5123 13167 16 101*
>%%LINK%%[[#^a6thghw0od|show annotation]]
>%%COMMENT%%
>**Greedy Approach**: Nối mọi số có Trọng Số Nhỏ Nhất trước. 
>%%TAGS%%
>
^a6thghw0od


>%%
>```annotation-json
>{"created":"2023-08-22T03:12:52.474Z","text":"là chỉ số của đỉnh cạnh đỉnh i trên đường đi dài nhất từ đỉnh bắt đầu đến i","updated":"2023-08-22T03:12:52.474Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":31387,"end":31478},{"type":"TextQuoteSelector","exact":"is the index of the vertex next to vertex i on the longest path from the starting vertex to","prefix":" is: 𝑡𝑖𝑟=𝑡𝑖𝑙 - 𝑡𝑖𝑒• ki ","suffix":" iWe have: 𝑡1𝑒 = 𝑡1𝑙 = 0, 𝑡"}]}]}
>```
>%%
>*%%PREFIX%%is: 𝑡𝑖𝑟=𝑡𝑖𝑙 - 𝑡𝑖𝑒• ki%%HIGHLIGHT%% ==is the index of the vertex next to vertex i on the longest path from the starting vertex to== %%POSTFIX%%iWe have: 𝑡1𝑒 = 𝑡1𝑙 = 0, 𝑡*
>%%LINK%%[[#^vlg9wu65i0m|show annotation]]
>%%COMMENT%%
>là chỉ số của đỉnh cạnh đỉnh i trên đường đi dài nhất từ đỉnh bắt đầu đến i
>%%TAGS%%
>
^vlg9wu65i0m


>%%
>```annotation-json
>{"created":"2023-08-22T04:11:01.919Z","text":"Tính MAX\n+ **Trên** - Node hiện tại\n+ **Dưới** - Node trước nó  (hướng tới nó)\n+ **Trái **- Đường MAX tới nó\n+ **Phải** - LÀM SAU CÙNG. VÌ TÍNH NGƯỢC từ Nút cuối. \nvd: **nút 8 có giá trị là 70. thì Nút 7 sẽ có giá trị là 52 vì 70 - 18 (độ dài từ 7 tới 8) là 52.**","updated":"2023-08-22T04:11:01.919Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":35923,"end":35956},{"type":"TextQuoteSelector","exact":"Time calculation on PERT network ","prefix":"ation on PERT network •Example 3","suffix":"𝑦7[19]21512562834210 0321121431"}]}]}
>```
>%%
>*%%PREFIX%%ation on PERT network •Example 3%%HIGHLIGHT%% ==Time calculation on PERT network== %%POSTFIX%%𝑦7[19]21512562834210 0321121431*
>%%LINK%%[[#^ise2zjjfobg|show annotation]]
>%%COMMENT%%
>Tính MAX
>+ **Trên** - Node hiện tại
>+ **Dưới** - Node trước nó  (hướng tới nó)
>+ **Trái **- Đường MAX tới nó
>+ **Phải** - LÀM SAU CÙNG. VÌ TÍNH NGƯỢC từ Nút cuối. 
>vd: **nút 8 có giá trị là 70. thì Nút 7 sẽ có giá trị là 52 vì 70 - 18 (độ dài từ 7 tới 8) là 52.**
>%%TAGS%%
>
^ise2zjjfobg


>%%
>```annotation-json
>{"created":"2023-08-22T17:09:29.307Z","text":"2 Đỉnh nối tới nhau và độ dài của 2 đỉnh.\n(A,B,2) - A đến B là 2\nMỗi CẠNH và Độ dài Cạnh chỉ thêm vào Đồ thị 1 lần.\nQuét các nút theo thứ tự.\n","updated":"2023-08-22T17:09:29.307Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":24174,"end":24187},{"type":"TextQuoteSelector","exact":"Spanning Tree","prefix":"Tree algorithmKruskal’s Minimum ","suffix":" algorithmKruskal’s Minimum Span"}]}]}
>```
>%%
>*%%PREFIX%%Tree algorithmKruskal’s Minimum%%HIGHLIGHT%% ==Spanning Tree== %%POSTFIX%%algorithmKruskal’s Minimum Span*
>%%LINK%%[[#^ovtqq04hbtd|show annotation]]
>%%COMMENT%%
>2 Đỉnh nối tới nhau và độ dài của 2 đỉnh.
>(A,B,2) - A đến B là 2
>Mỗi CẠNH và Độ dài Cạnh chỉ thêm vào Đồ thị 1 lần.
>Quét các nút theo thứ tự.
>
>%%TAGS%%
>
^ovtqq04hbtd


>%%
>```annotation-json
>{"created":"2023-08-25T08:32:15.880Z","text":"Liền kế\n","updated":"2023-08-25T08:32:15.880Z","document":{"title":"PowerPoint Presentation","link":[{"href":"urn:x-pdf:10705ddaebecff46a8c7ded225ec511b"},{"href":"vault:/Slide-DSA-Chapter5 1.pdf"}],"documentFingerprint":"10705ddaebecff46a8c7ded225ec511b"},"uri":"vault:/Slide-DSA-Chapter5 1.pdf","target":[{"source":"vault:/Slide-DSA-Chapter5 1.pdf","selector":[{"type":"TextPositionSelector","start":1163,"end":1172},{"type":"TextQuoteSelector","exact":"Adjacency","prefix":" in the previous diagram is 4.• ","suffix":": This refers to the connection("}]}]}
>```
>%%
>*%%PREFIX%%in the previous diagram is 4.•%%HIGHLIGHT%% ==Adjacency== %%POSTFIX%%: This refers to the connection(*
>%%LINK%%[[#^2gta2b14hlj|show annotation]]
>%%COMMENT%%
>Liền kế
>
>%%TAGS%%
>
^2gta2b14hlj
