
Link:  https://youtu.be/5NgNicANyqM?t=13179&si=xzydrSjRPNs8BEY_
#### Probability: It might be right, it might be not.

**Axiom:** Tiên đề
**Intuitively:** trực quan

![[Pasted image 20230916082750.png]]

**Succinct:** ngắn gọn
**Disjoin:** tách rời

Evedent P(a|b) contribute to the later result P(b)
![[Pasted image 20230916083233.png]]


# Bayesian network
![[Pasted image 20230916085542.png]]

**The Node X arrow to Y meaning that, Y is the consequences of X.** 
![[Pasted image 20230916085620.png]]
> A Network indicate Event & Consequences
+ **Appoinment:** cuộc hẹn
![[Pasted image 20230916085950.png]]

**Possibility distribution of a Node**
![[Pasted image 20230916090154.png]]

> Probolity of getting maintainance is lower due to rainning.
![[Pasted image 20230916090511.png]]

note: Each cases are Independence.
![[Pasted image 20230916090910.png]]

> If we know that Train is on time/ delayed (the infomation before it doesn't matter) Which mean we can conclude the Appoinment be miss or attend.
![[Pasted image 20230916091025.png]]
### Computing Joint Probilities
*> The possibility of a cases happened given all those previously happened* 
![[Pasted image 20230916091617.png]]
Other example
![[Pasted image 20230916092042.png]]

+ **Deduction:** loại trừ / suy đoán (trong suy luận)
#### Conclusion: 
**The Odd of something that happened base on what already happened**

# Inference
#### *Problems of inference in a probabilistic setting*
![[Pasted image 20230916092508.png]]
> I obsered that it is rainning, i would like to know the distribution that the train will be delayed.
+ Query: like the probabolity the train is on time. 

![[Pasted image 20230919061954.png]]
> **Xác suất xảy ra 1 Biến cố** (độc lập) **trong 1 chuỗi các Biến Cố nối tiếp nhau.**  
> VD: "tôi cắn con chó và nó cắn lại tôi + tôi ko cắn con chó và nó ko cắn tôi"
+ Từ đây có thể biểu diễn các sự kiện dưới dạng Node trong Graph.

For Problem that take unreasonable amount of time (big) to be calculate using the Baysian network, we applied 
# Approximate inference

continues: https://youtu.be/5NgNicANyqM?si=yjtwrsBvlcXlnKvl&t=18483

![[Pasted image 20230920075616.png]]


> Event happened today taken from the day previous. 1 state determine 1 state
![[Pasted image 20230920083021.png]]

> Data AI see
![[Pasted image 20230920083956.png]]

> Probability from sensor Model
![[Pasted image 20230920083919.png]]


![[Pasted image 20230920084043.png]]
![[Pasted image 20230920084228.png]]

![[Pasted image 20230920083927.png]]


![[Pasted image 20230920084421.png]]
smoothing -> make decision more accurate base on past events

*+ use statistic to guess what more likely to be happened.*
*+ Baysian model: how a particular event can relate to other events. How this value relate to that value (base on distribution)*
**Conclusion: So that our AI can can make inferences  based on what it already know.** 

