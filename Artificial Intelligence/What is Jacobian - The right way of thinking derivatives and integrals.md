Derivatives. When we first learn this concept, 
it is most likely synonymous with slopes.  

More precisely, if we have a function f(x), we 
can plot the graph in our usual coordinate plane.  

The derivative of f at a is then the slope 
of the tangent at the associated point.  

This is a good intuition of derivatives ... or is 
it? [Vsauce music plays] It’s completely fine for  

functions like this, but what if we have functions 
like this instead, where we have 2 inputs x and y,  

and 2 outputs? Then we need 4 dimensions just 
to graph this function properly, let alone  

making sense of slopes in 4 dimensions. So if 
we want to generalise the notion of derivatives,  

derivatives CANNOT be slopes. On a similar 
note, usually integrals are thought of as areas.  

More precisely, if we again have a function f(x), 
then the integral can be thought of as the area  

under the curve. This is a good intuition of 
integrals … or is it? [Vsauce music plays]  

This is not as problematic as the derivative 
one, but this is still not the best intuition  

moving on. So how should we actually think about 
it? Let’s rethink derivatives and integrals.

[CHAPTER 1: LINEAR MAPS]

Linear maps might not seem relevant, but it 
actually is the key here, so let’s dive into it.  

We will first look at linear maps in 2 dimensions 
to get the hang of it. Linear maps are required  

to have these properties, which we are going to 
demonstrate using the animation we have just seen.  

In this illustration, we see that parallel lines 
stay parallel and if the lines had even spacings,  

they will space evenly after the map. If you 
didn’t catch it, note where the yellow and white  

lines are after the transformation. They are still 
parallel to each other, and although the spacings  

have changed, the lines are still EVENLY spaced. 
The final property is that the origin is fixed.  

The origin is the red dot in the middle here, 
and before the transformation, the origin was  

there as well, so the origin is fixed.
The nice thing about these linear maps  

is that we can simply track where these 
two points go, because once we know that,  

we can already create a grid system out of these 
two image points. In other words, these two points  

carry ALL the information of the linear map, 
by creating an alternative coordinate system.  

More concretely, if we have some random point, 
say (1.3, 0.8) in the original coordinate system,  

then after the linear map, it is still (1.3, 
0.8), but in the new, warped coordinate system.  

So once we know where these two points are, we 
know where every other point goes. To represent  

the locations of these two points, we need 
to refer back to the original coordinates.  

The point (1,0) on the **horizontal axis gets** 
**mapped to the point (1.33, -0.73) in this case;**  

**and (0,1) on the vertical axis gets mapped to** 
**the point (1.17, 0.75) in this case.** These four  

numbers completely determine the linear map, and 
so we usually represent them in an array like  

this. By convention, the first column represents 
where (1,0) goes, and the second column represents  

where (0,1) goes. This array of numbers is called 
a matrix, capturing the essence of a linear map.

Another thing about linear maps is what it does 
to 2-dimensional regions. Even though the region  

will be distorted, AREAS of any region actually 
scale by the same factor. In this example, this  

area grows by a factor of about 1.86, so for ANY 
region, the area also grows by exactly the same  

factor. This scaling factor is the determinant of 
the linear map. If the linear map involves some  

sort of reflection, for example in this case, we 
are simply reflecting along the horizontal axis,  

then even though the area hasn’t changed, the 
determinant is -1 rather than 1, where the  

negative sign means our orientation has changed. 
As I said a minute ago, a linear map is summed  

up in a matrix, so we should be able to compute 
the determinant just from these four numbers.  

In fact we can. In this 2 dimensional case, we 
can compute by first multiplying the two numbers  

on the main diagonal, then minus the product of 
the two numbers on the other diagonal. However,  

this formula is not very crucial in understanding, 
so I am not going too deep into it for now.

Let’s reduce to 1 dimension. As we said before, 
these three are the requirements of being a linear  

map. The first one isn’t too relevant, because we 
only have one line to deal with anyway. But the  

next two requirements mean that we are restricted 
to just scaling, so linear maps in 1 dimension  

ARE scaling. In 2D, the linear map is represented 
by a matrix like this, but in 1D, we only need to  

know where 1 goes, so the matrix reduces to 
just 1 number, which is the scaling factor.  

What about the determinant? Well in 2D, the 
determinant is the scaling factor for areas,  

so in 1D, we replace areas by lengths, but 
the scaling factor for lengths is just the  

scaling factor in general. So the determinant 
is just that number inside the matrix in 1D.  

So we have what we need to know 
about 1D and 2D linear maps.  

What about derivatives?
[CHAPTER 2: DERIVATIVES IN 1D]

Let’s think of one-dimensional functions this 
way: transformations of the number line. So this  

is how squaring looks like. We are talking about 
a general function, so the spacings can be uneven.  

Now pick a point on the input number line, 
say a. Obviously under the function f,  

it gets mapped to f(a). So what we actually want 
to know is the **behaviour of f on the NEIGHBOURING**  

**points.** So let’s zoom into the neighbourhood 
of the point a, and observe what f does to it.  

It does look like a scaling, and in fact, the 
neighbouring points are about three times apart.  

It’s not exact, but when we zoom in even further, 
the discrepancy from this scaling approximation  

would gradually vanish. Here is a little technical 
remark. In general, the point a will move to f(a),  

rather than just staying put. So in fact, we have 
been centering our perspective on a. This means  

that we can treat this as a linear map, well, 
sort of, because it is just approximately one.

In this case, the linear map is represented by the 
matrix 3, because this is a scaling by a factor of  

3. This is the Jacobian matrix at the point a for 
this 1 dimensional function f, and the number in  

the matrix is the derivative, denoted f’(a). In 
other words, the derivative is the scaling factor  

near the point a. It’s important to note that 
this depends on where a is. If we have moved a  

somewhere else instead, then the function near a 
looks like this, and there is even some sort of  

reflection involved. Points on the right of the 
red point goes to the left of it, with a scale  

factor of 2, so we can approximate this with a 
linear map with matrix (-2), and the derivative is  

-2. Even for the same function, the Jacobian and 
the derivative can be different depending on a.

[CHAPTER 3: DERIVATIVES IN 2D]

Similarly, for a two dimensional function, with 2 
inputs and 2 outputs, we can visualise this using  

transformations of the coordinate plane, so this 
function looks like this. It doesn’t look linear,  

and lines aren’t even lines under the function 
f. But again, if we pick a point (a,b), and then  

zoom in far enough, after centering our 
perspective on the point, it looks like a  

linear map. Again, this is not exact, but we can 
take the closest linear map approximation. This  

is the image of the exact linear map, with 
respect to the original coordinate system.  

As discussed in the first chapter of this video, 
the matrix for this linear map should look like  

this. This is where (1,0) on this coordinate 
system goes, which is (1,1.5). On the other hand,  

(0,1) went here, which is (-1, 1.5). 
This matrix, just like in the 1D case,  

is the Jacobian matrix at the point we are 
studying. Again, the Jacobian matrix depends  

on the position (a,b) of the point. Just to recap 
what we have done so far, the Jacobian matrix is  

the matrix representing the best linear map 
approximation of f near a particular point.

But given the function f, and the point 
(a,b), how do we compute the Jacobian matrix?  

To do that, we have to consider the components 
of f. For example, in this function, we can break  

it down into f_1 and f_2 components. We can then 
define another function g, which is basically f_1,  

but the second input is fixed. Then the 
function g has 1 input and 1 output,  

something we know how to deal with. Visually, 
what g does is to take the x-coordinate of points  

on this horizontal line, apply the original 
function f to the horizontal line, then take  

the x-coordinate again. Or equivalently, 
you can think of projecting back onto the  

horizontal line. Now what is g’(a)? We have said 
before that it should be the scaling factor of g  

near a. Equivalently, we want to see where this 
point 1 unit to the right of a goes. For example,  

if it ends up here after projecting back to this 
horizontal line, in this case, g’(a) will be 3.

But how does it relate to the Jacobian? The first 
column is precisely asking where this point goes,  

and g’(a) simply extracts the x-coordinate for us. 
Usually we don’t say the function g explicitly,  

and denote g’(a) directly in terms of f_1. But 
this is nothing new, just a notation to save  

us the trouble of explicitly defining g every 
time. In practice, we still need to at least  

THINK of g to do the differentiation. This helps 
us find the first number in the Jacobian matrix,  

and the other numbers are quite similar. 
For example, if we want to find this entry,  

we simply define another function that extracts 
the y-coordinate instead. More precisely,  

we define another function h using the 
second component of f instead. And similarly,  

we can denote h’(a) using a similar notation. 
So now, the second entry is equal to h’(a).

What about the second column? We now consider yet 
another function but on the vertical line instead,  

because we want to see where this point 
on the vertical line goes. So this time,  

we define the other two functions that are fixed 
in the first input instead, and we have very  

similar notation for their derivatives. The 
function p extracts the x-coordinate, while  

q extracts the y-coordinate, so the entries in the 
second column are p’(b) and q’(b) respectively.  

So writing in our other notation, this is 
the Jacobian matrix. But remember that these  

notations simply correspond to HOW we compute 
the entries, because in essence, it is still  

the matrix representing the best linear map 
approximation of f near the point (a,b).

But there is another thing we can say about a 
linear map, which is the determinant, or the  

scaling factor for areas. Not surprisingly, this 
determinant is called the Jacobian determinant,  

a measure of how much areas scale near the point 
(a,b). Again, the determinant can be computed  

using the matrix by the method we have 
discussed previously. These two concepts  

are crucial when it comes to changing variables, 
as we will see in the second half of the video.

[CHAPTER 4: WHAT IS INTEGRATION?] 

Think about a heavy rod, and we want to find its 
mass. Unfortunately, the densities at different  

places are different, and the density is described 
by the function f(x), x denoting the position on  

the rod. So how do we find the mass of this rod? 
Well, we can chop the rod into smaller pieces,  

then find the masses individually, then add them 
all up. The reason we want to do this is that  

the length of each little rod is so small that 
we can approximate it to have uniform density,  

let’s say the density at this point, f(x*). So 
we assume f(x*) to be the density throughout  

this little rod. Then the mass is the density 
multiplied by the length of the little rod. Repeat  

this for all the little rods, and summing the 
little masses up, we get the total mass. This is  

not perfect, but as the length of the little rod 
decreases, and there are more and more of them,  

we get closer to the true mass. This process is 
denoted using an integral. Here, a and b represent  

the two endpoints of the big rod, and f(x) dx can 
be thought of as the masses of the little rods.

What about in 2D? What is the mass of this region 
if the density at each point is given by f(x,y)?  

Well again, we divide this region into smaller 
pieces - this time using rectangles. However,  

we might see something that is not a 
rectangle. Feel free to ignore them,  

because as the rectangles become smaller in 
size, these will have negligible contribution  

to the mass anyway. For each of these rectangular 
regions, we again assume the density is uniform,  

say the density at this point (x*,y*). 
The mass of this little rectangle  

is then the density multiplied by the area of 
this little region. Again, repeat this for all  

the rectangular regions, and add the little masses 
up. This is also represented by an integral, but  

this time D represents the region, and f(x,y) dxdy 
is the mass of the little rectangular regions.

But how do we actually find this mass, 
or equivalently, compute this integral?  

To do this, we add the little masses in a 
strip first, then add them all up. Let’s  

focus on the middle strip here. We deliberately 
take the points all on the same vertical line,  

so that we can imagine a one-dimensional vertical 
rod. The difference is that the strip is not  

one-dimensional; it has a width, so the mass of 
the strip can be approximated by the product of  

width and a one-dimensional integral. It’s not 
really that scary. f(x,y) dy simply refers to the  

mass per unit width of the small rectangles. 
Or equivalently, if we combine the factor of  

width, this really refers to simply the mass of 
each rectangle. The other thing to note is the  

endpoints of the integral. They refer to the lower 
and upper endpoints of the strip, but different  

strips have different endpoints, and so the 
endpoints depend on x, the position of the strip.

This entire integral depends on which strip we are 
talking about, or x, the position of the strip,  

so let’s call this g(x), just some function of 
x. This is the mass per unit width of the strip.  

But this is exactly what we were doing with 
the one-dimensional rod; the only difference  

being that the density is described by g, not 
f. Essentially, each little rod contains the  

mass of an entire vertical strip. So we integrate 
g(x) to find the mass accordingly. To summarise,  

to compute this integral, we consider each 
strip first, which is the mass per unit  

width of a strip. Then we integrate along 
the horizontal axis. Not too surprisingly,  

we can also use horizontal strips first, 
which leads us to a similar formula here.  

These are again just ways of computing the 
integral; conceptually, we are still just  

adding up masses of these little rectangles. 
Sometimes, the fact that the endpoints are not  

constants can be annoying, and so 
we might want to change variables.

[CHAPTER 5: CHANGING 
VARIABLES IN INTEGRATION (1D)]

Let’s think of a rod again. Just like in the 
previous setting, the density is described by f.  

This time, the endpoints are described by g(a) 
and g(b) respectively, where g is just another  

function. As we’ve discussed just now, the mass 
of this rod is simply the integral shown here.  

But seeing the endpoints being g of something, 
isn’t it tempting to consider another rod with  

endpoints a and b instead? We want a rod so 
that when we apply g to the bottom rod, we get  
u = g(u)
the original one. So if I have a random point u 
here, we want this to correspond to the point g(u)  

on the original rod. The density at this point 
is given by f of the position, which is f(g(u)),  

and so we want the density on the bottom 
rod to be described by f(g(u)) as well.

That doesn’t make the two rods have the same 
mass, because their lengths can be different,  

but here’s the trick. We always chop the 
rod into smaller pieces to find the mass,  

but let’s focus on the one containing the point u. 
It is mapped to some little rod containing g(u).  

These two little rods have the same density 
f(g(u)), but different lengths. How different  

are they? The scale factor induced by 
g near the point u is precisely g’(u),  

so the length of the little rod scale by this 
factor. So if we add this factor into our density,  

we can make the two little rods have the same 
mass. u was arbitrary, and we can do the same  

thing to the other little rods, and so the 
mass of the original rod should now be the same  

as our modified bottom rod, which 
is this integral on the right. This  

formula is usually known as integration by 
substitution, but how does that work in 2D?

[CHAPTER 6: CHANGING 
VARIABLES IN INTEGRATION (2D)]

Quite similarly, we consider a region with density 
given by f(x,y). However, the region is g(D),  

where D is just another region, and these are 
related by the function g. The mass of the region  

g(D) is simply this integral on the left and 
we want to find the right density on the region  

D to give the same mass. Again, if we have 
some random point (u,v) in the region D,  

after mapping by g, it ends up in g(u,v), and we 
have density f(g(u,v)) at this point. This doesn’t  

make the two regions have the same mass yet. 
A small rectangle in region D containing (u,v)  

will map to some region containing g(u,v). These 
two regions have the same density, but different  

areas. The corresponding scale factor of areas 
near the point (u,v) is precisely the Jacobian  

determinant at the point (u,v). So by adding this 
scale factor to the density, the two small regions  

now have the same mass. Here, I simply use this J 
thing to denote the Jacobian determinant, and so  

the mass can be represented by this integral. 
Except… this is not quite the full story yet.

What if the Jacobian determinant is negative? The 
determinant being negative simply means reflection  

is involved during the linear map, but the area 
itself doesn’t care about the negative sign,  

which means the scale factor should be the 
ABSOLUTE VALUE of the Jacobian determinant,  

and so this should be the correct change of 
variables formula. Immediately you might have  

a question: what about the 1D changing 
variables formula? By the same logic,  

the scale factor should also be an absolute value, 
but it isn’t. If the scale factor is negative,  

it would flip the rod and would really have 
a negative contribution to the integral.  

Because of the way we define a one-dimensional 
integral, if we flip the endpoints around,  

the sign changes, even though we are talking 
about the same interval, and so inherently,  

the one-dimensional integral already considers 
the orientation of the rod. So if the scale  

factor is negative, it would really have 
a negative contribution. Contrast this  

with how we define a two-dimensional integral. 
Orientation is not built into its definition,  

and we always say that the integral is defined 
on a region, never specifying its orientation.

There is another detail that is often glossed 
over: g cannot look something like this.  

Because of the absolute value, this bit would be 
integrated twice. We don’t want this to happen,  

and so we require that g doesn’t do this. In 
more technical mathematical terms, we say that g  

is injective. Again, there isn’t such restriction 
on g in the 1-dimensional case, but I will leave  

the details out for now - maybe you can flesh out 
the details in the comment below! Essentially,  

it hinges on the fact that orientations 
are built into 1-dimensional integrals.  

So these two formulas can be 
used for changing variables,  

with the additional requirement that g needs 
to be injective for the 2-dimensional case.

[CHAPTER 7: CARTESIAN TO POLAR]

Suppose you have a unit disc, and you want 
to integrate f over this region. However,  

as we discussed before, we need to 
compute in one of these two ways.  

Annoyingly, the endpoints are square roots, which 
can be frustrating to deal with. And to be honest,  

whenever you see a circle, it probably is 
a crime not to consider polar coordinates,  

because in the polar world, we have this much 
simpler region, where r ranges from 0 to 1,  

and theta ranges from 0 to 2 pi. Here, the 
function g goes from the polar world to the  

Cartesian world, and so g looks like this. So 
according to our change of variables formula,  

we want to compute this integral instead, 
but now the region T is rectangular, and the  

original region D is simply g(T). Now all we need 
to do is to figure out the Jacobian determinant.

To do this, recall how to compute the Jacobian 
matrix first. Here, g_1 and g_2 are the first  

and second components of the outputs of g. Then 
all we need to compute is each of these entries,  

and do the crisscrossing to get the determinant. 
It is a good exercise to do this yourself,  

but in this case, there is a much more direct 
way of finding the Jacobian determinant.  

Let’s consider a very small rectangle 
with (r, theta) as one of its vertices,  

with width delta r, and height delta theta. After 
applying the function g, first off, the point (r,  

theta) maps to the point r units away from the 
origin, and at an angle theta from the horizontal.  

The bottom edge of the rectangle has theta stay 
fixed, and so it is mapped to a sort of extension  

of the line from the origin. The length 
of this extension is simply delta r.

What about the left edge of the rectangle? It has 
r stay fixed, so it should map to a circular arc.  

The change in angle is delta theta, 
so the length of this circular arc is  

r delta theta. So this part of an annulus 
is where the small rectangle gets mapped to.  

When delta r and delta theta are small enough, 
this will look more and more like a rectangle,  

so the area is approximately r delta 
r delta theta, while originally,  

the area was delta r delta theta. This means that 
the scale factor for areas near the point (r,  

theta) is simply r, and so this is the Jacobian 
determinant. This means that change of variables  

formula from Cartesian to polar looks something 
like this, r being the Jacobian determinant.  

One very standard exercise is to compute this 
integral and see what cool things come out of it.

Before you go, there are a few things I 
want to say. First, I have recently created  

a Patreon account. No obligation whatsoever - 
consider supporting this channel if you want to  

and can afford to, because these videos do take 
a huge amount of time and effort to produce.  

Secondly, there is always a Google form linked 
in the description to gauge your math levels,  

and from the form, since most of you know the 
basics of derivatives and integrals, I made this  

video assuming that knowledge, and also why third, 
I made this video series in the first place. The  

video series tackles a problem mentioned in 
the introduction of the video series. This  

video was made as the prerequisite for the final 
video of the series. So do consider watching the  

introduction video so that the final video makes 
sense. If you enjoyed this video, like, subscribe,  

hit the bell and leave a comment below, so that 
more people can watch this. See you next time!

