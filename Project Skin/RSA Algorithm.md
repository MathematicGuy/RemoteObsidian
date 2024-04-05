  
1) p = 2, q = 7  
2) n = 14 (=2*7) (public key)  
3) phi(n) = 6 (= (2-1) * (7-1))  fomula -> (p-1)(q-1)
![[Pasted image 20240405143531.png]]
common factor of phi(n) = 1  
Write down and list out all numbers divided by n = 14
![[Pasted image 20240405143420.png]]
These leftover num called coprime with 14 (shared no common factor) 

4) Choose e 
{
	1 < e < phi(n) = 6 (2,3,4,5) -> choose number not divided by 14
	Co-prime with N, phi(n)
}
-> e = 5, lock (5, 14)

5) Choose d: 
+ de(mod phi(n)) = 1
+ e * d (mod 6) = 1
![[Pasted image 20240405144704.png]]
p, q -> 2 prime number (often super large)
d -> private key = 11
e -> public key = 5 (% to phi(n) and N)