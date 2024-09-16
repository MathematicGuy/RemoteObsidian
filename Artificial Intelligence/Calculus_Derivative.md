
Given a classification problem, we got the graph below. Say we want to classified a region for sad and happy.
![[Pasted image 20240710074612.png]]
![[Pasted image 20240710074806.png]]

We would like to train the Model to tweak the classifier line to this position. 
![[Pasted image 20240710074722.png]]
+ ? So how the Model do this...

## Motivation to Derivatives - Part 1

+ $ Goal: **find the rate of change between 2 points**
![[Pasted image 20240710075538.png]]
> No, you calculate the speed by the distance t travel by the time: v = s / t
> Or calculate the distance it travel after a period of times.
+ ? In simple term: **Rate of Change**
> ![[Pasted image 20240710075744.png]]

> We can calculate the the average speed between a time interval and distance by dividing the changes in distances to times. **rise (y) over run (x)**
![[Pasted image 20240710080116.png]]


+ ? But, can we estimate the velocity of the car at time t = 12.5. Let's try using the slope 
	![[Pasted image 20240710080426.png]]
	![[Pasted image 20240710081706.png]]
	So the speed is more accurate this time. When we make the interval of time (t) and 
	distance (x) closer to eachother. 
	![[Pasted image 20240710082554.png]]
	And if we put the interval to be super close to each others. You get the limit which is dx over dt and that is precisely the tangent line to the curve at t equals 12.5
	![[Pasted image 20240710082148.png]]
	+ $ **Instantaneous rate of change is a measure of how fast the relation between two variables is changing at any point**. In other words, **imagine you move a tiny distance, dx in a tiny interval of time dt**. This is the instantaneous rate of change. -> It's also called **Derivative.**

> Like anything else, v = 0, if no distance changes in time.
![[Pasted image 20240710084453.png]]

## Derivatives and their notation
2 ways to express derivative: **Leibniz's notation** and **Lagrange's notation.**
![[Pasted image 20240710085121.png]]]]
![[Pasted image 20240710085315.png]]

## Some Common Derivative
### Lines
![[Pasted image 20240710085528.png]]

+ ? [[Slope]] is the changes of rise over run. Using Pythagorean, we conclude that $\frac{\nabla y}{\nabla x} = a$ 
![[Pasted image 20240710093127.png]]
So when 2 points are so close to each other it like they're in 1 position. We can say that f(x)' = a. Let's proven it more clearly
![[Pasted image 20240710085720.png]]
we have f(x) = y(x) as the line function
The 1st point have x as x and y as ax + b (typical line's function)
The 2nd point have  x as (x + $\nabla x$) so y must be a(x + $\nabla x$) + b
+ $ Now, apply the derivative for those 2 points. we achieve:
![[Pasted image 20240710090540.png]]
As we cancel out, what is left is:  a
![[Pasted image 20240710090615.png]]


### Quadratics
![[Pasted image 20240906151645.png]]
Explain how everything get square root, $x^{2}$  so both f have their x square root: $f_1(x^2)$ and $f_{2}(x+\Delta x)^2$  

![[Pasted image 20240710171435.png]]
Repeat the same step as the interval smaller and smaller. We finally got the result close to 2
![[Pasted image 20240710171142.png]]
![[Pasted image 20240710171803.png]]
> **As 2 points move closer**, $\nabla x \to 0$ (delta_x move closer to 0. the same for delta_y) There for the **Derivative of Quadratics function is: 2x or nx** with n as power of x. 
![[Pasted image 20240710172234.png]]

### Higher degree polynomials 
#### Derivatvative of Cubic Functions
![[Pasted image 20240710172608.png]]
>Like before, we calculate the slope. The 1st one is 3.25 as $\nabla x$ is 1. Decrease the interval between 2 points and repeat the same step we got.
![[Pasted image 20240710172917.png]]
So the result is as close as $3*0.5^{2} \approx 0.75$. This seem true since the derivative is actually  $3x^2$  
+ ? Let simplified the Slope and see what we got: Like before $\nabla x \to 0$ and we really got 
 the **Derivative of a Cubic is** $$3x^2$$
![[Pasted image 20240710173035.png]]


### Other power functions
> Like before, we calc the slope of a value. Then move the interval closer and closer.
![[Pasted image 20240710173642.png]]
![[Pasted image 20240710174409.png]]
 Simplified the Slope we got
![[Pasted image 20240710174828.png]]
 When you calc the Derivative of others power function, you can see there a pattern of (Power - 1):  $$\frac{d}{dx}f(x) = nx^{n-1}$$ 
![[Pasted image 20240710175119.png]]


## The Inverse Function and Its Derivative

If a function does a thing, the inverse function inverse that thing:
+ ? F(x) turn 1 to 5. So the inverse of F(x) will turn 5 into 1
### Inverse function
![[Pasted image 20240712084624.png]]

The 1st function have y = f(X) thus g(y) = $\sqrt{f(x)}$ 
![[Pasted image 20240712084813.png]]
+ secant: đường cát tuyến (đường cắt)


> Derivative = change in horizontal / change in vertical. Therefor
> 1st Slope: $\frac{\nabla f}{ \nabla x}$  & 2st Slope: $\frac{\nabla y}{\nabla g}$. 
+ ? Because g(y) and f(x) is just inverse of points. Their value doesn't changed, this mean $\nabla f$ = $\nabla y$  and $\nabla g$ = $\nabla x$. 

+ $ Let call the 1st Slope as f(x)' and 2nd slope as g(y)'. Since  g(y)' = f(x)' in reverse y-axis  $=> g(y) = \frac{1}{f(x)'}$    (just imagin 2 = 1/2 -> 2 = 1/(1/2))
![[Pasted image 20240712085418.png]]

**Examples**
![[Pasted image 20240712090826.png]]
![[Pasted image 20240712091033.png]]


## Derivative of Trigonometic  
note: revison some trigonometry ![[Pasted image 20240712093458.png]]

![[Pasted image 20240712093939.png]]

+ ? $\sin(x + \nabla x)$ is a point with $\nabla x$ as a natural number. We see that $\sin (x + \nabla x) > \sin x$
+ ? $\cos(x + \nabla x)$ also a point like sin. But $\cos(x + \nabla x) < \cos(x)$ 
+ [[Explain -delta(cos x)]] :  $-\nabla(\cos x)$  
	+ $ The change in the x-coordinate (cosine value) as we move from x to $x + \Delta$ is given by $\Delta(\cos x) = \cos(x + \Delta x) - \cos(x)$
		
	+ $ When $Δ(cos⁡x)$ is negative, it means the x-coordinate (cosine value) has decreased.
		
	- $ To visually and mathematically represent this decrease, we use the term $-\Delta(\cos x)$.
![[Pasted image 20240712094405.png]]

+ $ As the **trigangle shrink smaller and smaller (cause derivative) the hypotenuse align with the arc of the circle** (cung của hình tròn), thus making h = $\Delta x$
![[Pasted image 20240712094520.png]]
Replacing the 2 values. We achieve:
![[Pasted image 20240712094531.png]]

$\frac{\Delta(\sin x)}{\Delta x} = \cos x$  and  $-\frac{\Delta(\cos x)}{\Delta x} = \sin(x)$
 
 This actually comfirms the intuition we built before:
![[Pasted image 20240712103604.png]]

## Meaning of the Exponential (e) 
![[Pasted image 20240712162717.png]]

![[Pasted image 20240712163316.png]]
> When you applied your money with interest rate: `your_money + your_money * 1/interest_rate` one after another you got:
	![[Pasted image 20240712163539.png]]
> Therefor, Bank 3 would have the most money: 2.7$ 
	![[Pasted image 20240712163639.png]]
	From the Compound Effect, we can conclude a fomula:![[Pasted image 20240712163700.png]]
	![[Pasted image 20240712163934.png]]
	![[Pasted image 20240712164001.png]]
	If you keep increase n over time you would end up with e = 2.71826
		![[Pasted image 20240712165254.png]]
		![[Pasted image 20240712165338.png]]
		We can call e as the maximum of interest rate over a instance period of time.		

## Derivative of $e^x$
![[Pasted image 20240713141928.png]]
> To Theory, e^x cannot be larger than ~ 2.71828. And if there is it just a super minimum amount. Therefor e^x2 ~ e^x1. So The Derivative should just be e^x.

To verify that let calc the Slope of $e^x$. Since $\Delta x \to 0$,  $e^{x + \Delta x}$ will come closer to $e^x$ , calc the Slope for every x we see that the Slope will always end up with 7.39 which is $e^2$
![[Pasted image 20240713143208.png]]

### Derivative of log(x)
![[Pasted image 20240713150731.png]]
> **p is the logarithm of the n**
> If 10 ^ 4 is 10000. Then the logarithm is $\log_{10}10000 = 4$ . That it
> for 1 / 10^4 = 10^-4 then the logarithm is $\log_{10}10^{-4} = -4$ 
![[Pasted image 20240713151048.png]]
> In short, the b (base) raise to the p (power) of what equal to the n (number)

Let understand 3 furthur more, we know that:
![[Pasted image 20240713161337.png]]
replace 1/n with k
![[Pasted image 20240713161443.png]]
Let to the same for Derivative function
![[Pasted image 20240713161606.png]]
But before that, ket simplified it ($2^{x + h} = 2^{x}+ 2^h$)
![[Pasted image 20240713161640.png]]
Now we can calculate the right most function as h goes closer to 0 we reach a limit of 0.6931...
![[Pasted image 20240713161728.png]]
it actually ln(x) but for now let just call it as k2
![[Pasted image 20240713161922.png]]
![[Pasted image 20240713162000.png]]
But we have to calc k from scratch for every new n. can we find a way to calc k automatically
![[Pasted image 20240713162110.png]]

**Basic Concept**
+ ? note: e với số mũ nhỏ -> 0 sẽ tiến tới 1 giới hạn và e gần như không thể nhỏ hơn nữa. (min là 2.718281828)
+ ? Còn e^n với n > 0 sẽ tăng như 1 số bth (ex: e^2 = 7.38) 
Logarithm: If $e^{y}= x$, then $y=\log(x)$
	This means $\log(x)$ answers the question: "To what power must e be raised to get x?"
![[Pasted image 20240713150356.png]]
+ ? f [[inverse]] of y is the logarithm of y because **e to the logarithm of x is x** and **logarithm of $e^y$ is y**. 
+ $ In simple term, e turn $\log(x)$ back to x. $\log (e^{y})= y$ thus $f^{-1}(y)$ is log(y) .
![[Pasted image 20240715141232.png]]
![[Pasted image 20240713151947.png]]
> Since f inverse is the reciprocal of e^x then the derivative of g(y) and $e^x$ must be $$\frac{1}{e^{x}} or \frac{1}{y}$$ since log(y) = y. 
+ ?  Reciprocal function: hàm nghịch đảo (Check Derivative of an Inverse function: 1/f(x)

![[Pasted image 20240717093619.png]]
However, there're my some exception:
Like then x = 0 in this function. There cannot be a derivative if the line only pass 1 point. 
+ ! The Derivitive must exist for all points in the Domain (Fuction must be continuos)
![[Pasted image 20240717093826.png]]

+ ? Un-Continous Function -> No Derivative
![[Pasted image 20240717094435.png]]

+ ? This also non differentiable functions, because Derivative require rise over run (y/x). If there is only rise or run independantly -> No derivative 
![[Pasted image 20240717094725.png]]

**Summary:**
![[Pasted image 20240717094800.png]]


## Properties of the derivative
### Multiplication by Scalars
Just multiplication by a value/scaler. (nothing special)
$$f' = c.g'$$
![[Pasted image 20240717095116.png]]

### The Sum Rule
$$
f' = g' + h'
$$

The bout move, also as the child -> total distance the child move is 12 (not just 2)
![[Pasted image 20240717095327.png]]
So as the velocity![[Pasted image 20240717095441.png]]

![[Pasted image 20240717095537.png]]
![[Pasted image 20240717095605.png]]

### The Product Rule
$f = gh$ then $$f' = g'h + gh'$$
![[Pasted image 20240717095942.png]]
Let look at the house from the top
![[Pasted image 20240717100151.png]]
+ ? As $\Delta t$ come closer to 0. $\Delta g(t), \Delta h(t)$ become neligible (so small that it doesn't even matter). Well because it is the derivative (g' as the y' and h' as the x'). Thus we can simplified it into $$f'(t) = g'(t).h(t) + g(t).h'(t)$$

### The chain rule (Like product rule but it like Product of a Product)
$$\frac{d}{dt}g(h(t)) = \frac{dg}{dh} . \frac{dh}{dt}$$ 
It call the chain rule bc you can composing function (hàm hợp) (put a function inside a function)
![[Pasted image 20240717101147.png]]
+ ? The Lagrange Notation
![[Pasted image 20240717101230.png]]
![[Pasted image 20240717101306.png]]

**Example:**
(Mqh giữu sự biến thiên của 2 tính năng/đặc điểm)
![[Pasted image 20240717101430.png]]
The Derivative of the Temperature with Time is the Product of Tempreture with Height and Time with Height. 
![[Pasted image 20240717101648.png]]
As $Delta T \to 0$
(note: Derivative is just the changes between 2 points) 
![[Pasted image 20240717101950.png]]

[[Derivative Week1- Practice Quiz]]
[[Symbolic with Numpy]]
