List - slow and Numpy fast 
Why -> numpy is Fixed type 
+ ? This is because computer see number as binary but numpy and list see number in 2 diff ways
	![[Pasted image 20240531151040.png]]
	List store the number as 4 kind of data. Therefor more memory need to be processed thus slower run time.
	![[Pasted image 20240531151157.png]]
+ $ Numpy Advantage over list
	Faster to read less bytes of memory
	No type checking when iterating through objects

+ $ Numpy use Contiguous Memory (data can be search on by one and not have to search base on each memory block)
	while List stored Memory scatter around (list use a array of pointers to point out values) -> more search time -> less performance
	![[Pasted image 20240531151758.png]]
+ ? How List different from Numpy
	![[Pasted image 20240531152019.png]]
	Numpy also core component of Pandas

