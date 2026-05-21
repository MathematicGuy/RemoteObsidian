Link: https://youtu.be/5NgNicANyqM?t=6715&si=FZP1pD8wEy0MMJcP
> How AI know the Infomation, Reason about the infomation, Draw Conclusion and the Principle behind it.

**Sentence** -> assertion about the world (khẳng định về thế giới)
**Proposition** -> **ký hiệu** mệnh đề (fact or sentence abou the world)
![[Pasted image 20230913090513.png]]

## Logical Connectives 
> Kí hiệu Logic
![[Pasted image 20230913090559.png]]

## Model
![[Pasted image 20230913090912.png]]

# Knowledge Bases
![[Pasted image 20230913091046.png]]

## Entails
> A entails B (A kéo theo B)
![[Pasted image 20230913091202.png]]
 VD: Nếu hôm nay là thứ7 thì bây h là cuối tuần

## Inference
> Sự suy luận. (Tạo ra thứ mới từ thông tin có rồi)
> Example of an **Inference of R**
![[Pasted image 20230913091629.png]]
> If it's a Tuesday and not rainning, Harry will go for a run.

> Using only knowledge KB that we know, can we conclude Alpha is True?
![[Pasted image 20230913091800.png]]
 one of algorithm that do that

# Model Checking
(Check all possible models if it True or False and the Condition (KB) is Met.)
![[Pasted image 20230913092009.png]]


![[Pasted image 20230913092240.png]]

**Implication** -> Hàm ý **( => )**

![[Pasted image 20230913093748.png]]
>**Output:**
![[Pasted image 20230913093215.png]]


![[Pasted image 20230913094026.png]]
> In all world, if the knowledge is True then the Query must be True.
![[Pasted image 20230913094019.png]]


# Knowledge Engineering
![[Pasted image 20230913094406.png]]
***Turn general knowledge into Knowledge that is representable by a computer.***

#### Game: find the Culprit (Murderer)
***Find the Culprit base on given information (inference)***
- Using AI to draw the conclusion from all case and base on all given clues.
![[Pasted image 20230913094842.png]]
Game Clue (from the Clue Envelop)
![[Pasted image 20230913095141.png]]

##### Summary: Using Logical Connective and Clues for AI to draw their own Inference. 

## Modus Ponens
If it Rain, Harry will stay at home
It Rain
-> Harry stay at home.
![[Pasted image 20230914163528.png]]


![[Pasted image 20230914164408.png]]
AND ELIMINATION
	If both is True then 1 one them is true
![[Pasted image 20230914164425.png]]



![[Pasted image 20230914164500.png]]
### Double Negation Elimination
![[Pasted image 20230914164517.png]]


Conclude 1 of them must be True.
Convert AND statement into OR statement
![[Pasted image 20230914164535.png]]
### Implication Elimination
![[Pasted image 20230914164700.png]]


![[Pasted image 20230914164743.png]]
### Biconditional Elimination
![[Pasted image 20230914164804.png]]


Turn AND into an OR
![[Pasted image 20230914164835.png]]
### De Morgan's Law
![[Pasted image 20230914164911.png]]

Turn OR to AND
![[Pasted image 20230914164952.png]]
![[Pasted image 20230914165004.png]]


Distribute property
![[Pasted image 20230914165121.png]]

![[Pasted image 20230914165131.png]]



# Theorem Proving
![[Pasted image 20230914165422.png]]

### Complimentary literal
![[Pasted image 20230914165529.png]]



**2 OR Clause oppose eachother** in order to compliment other Clause.  
![[Pasted image 20230914214057.png]]
### Disjunction (phân ly)
![[Pasted image 20230914214630.png]]

![[Pasted image 20230914214707.png]]

> All of this called
![[Pasted image 20230914214018.png]]

![[Pasted image 20230914214814.png]]



**Biconditional:** 2 điều kiện (điều kiện )
**Implication:** hàm ý (Ý chỉ là...)
### Conversion to CNF 
*+ CNF: Conjunction Normal Form (dạng kết hợp thông thường)*
![[Pasted image 20230914215356.png]]

**Elimination Implication:** luật loại trừ (1 chỉ trong 2 tồn tại)
**De Morgan's Law:**  
![[Pasted image 20230914220652.png]]

 ### Inference by Resolution (suy luận từ hiểu biết)
+ **Resolution:** đáp án/hiểu biết trước đó
VD:![[Pasted image 20230914221752.png]]

### Factoring
![[Pasted image 20230914222005.png]]
Turn into
![[Pasted image 20230914222016.png]]


### Empty Clause
![[Pasted image 20230914222035.png]]

### How to check what leading to constradiction
![[Pasted image 20230914222227.png]]

![[Pasted image 20230915080038.png]]+ **Entail**: kéo theo



**Propositional Logic:** mệnh đề logic
![[Pasted image 20230915080328.png]]

**First-Order Logic**  (Logic bậc nhất - Liên kết 1 Lớp)
![[Pasted image 20230915080441.png]]
+ **Predicate:** thuộc tính
+ **Constant:** alway be its self

  ![[Pasted image 20230915080819.png]]
-> For all value of x, if x belong to Gryff then x does not belong to Huff.
<-> Anyone in Gryff is not belong to Huff


## Existential Quantification
![[Pasted image 20230915081006.png]]

![[Pasted image 20230915081103.png]]
![[Pasted image 20230915081205.png]]
	There can be second-order, third and n-order logic applies the same principal as this.

**Conclusion:** Turn Human Logic into Computational/Machine Logic. So that we teach AI to Think on its own and Solve/Guess real world logical problems.  

