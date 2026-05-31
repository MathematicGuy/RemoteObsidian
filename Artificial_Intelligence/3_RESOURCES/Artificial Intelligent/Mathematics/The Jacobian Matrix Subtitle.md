hello everyone and welcome to another

video so today I want to spend a couple

of minutes talking about the Jacobian

matrix and I know that name might sound

a little bit intimidating but really the

idea behind it is surprisingly simple

we're going to see that the Jacobian

matrix is really nothing more than

taking the idea of a derivative

extending that to a gradient and then

extending that again to what's known as

this Jacobian matrix and this Matrix

actually shows up a lot in science and

engineering because we're going to see

at the end of the day what this thing

does is it allows us a way to calculate

and quantify the Sens it of a particular

function element to perturbations in a

given independent variable so that might

sound like a mouthful but if we take uh

a crawl walk run approach to this I

think you'll see that uh this is

actually pretty pretty consumable so to

start with our crawl phase let's jump

back to the idea of a derivative right

derivative is surprisingly simple right

we all remember this from high school

calculus if we have some function f like

this and it takes in some input X and

does something to it to produce an

output in this case what it does is

subtracts two from that value it raises

it to the power three and then

multiplies by three right so again you

can think about this from a functional

perspective as a function which takes in

a single independent variable X and it

spits out F ofx right okay so you might

ask yourself okay this is what this

function is we can easily plot this this

is nothing uh Earth shattering right

I'll plot F ofx versus X right and it

looks something like this okay and now

the next logical step might be asked

what is the derivative of this function

f and again don't overthink this right

you can break out your old high school

calculus textbooks right and you can say

okay the derivative of this function

it's just this right um now the only

thing that maybe we should mention is

we're going to write this like this

right the function f it's only a

function of a single variable so I don't

need partial symbols I can just use a d

right because it's only a function of

one variable so d FDX is just this and

what I want to make a note of is notice

here right that this is still a function

of the independent variable or the input

X right so to make this explicit what I

want to write and a lot of times you'll

see this is something like this right

I'm going to add this notation just to

remind ourselves that the derivative of

the function it's still potentially a

function of the independent variable and

in fact when you plot this I think

you'll see that yeah that's definitely

the case it's just some other function

of X right as X changes the derivative

value changes right and again nothing

Earth shattering because what this is

doing right is everyone knows the

derivative is basically telling you the

slope of the original function f right

so if I look at different points along

this or a different input values of X

like let's say I choose some x value out

here like at uh I don't know minus

0.75 right so what this derivative is

telling me and sorry I didn't draw this

very well I should have probably

extended this a little bit more right is

what this is telling me is I can read

this value here and that's telling me

effectively the slope or how fast is

this function f changing at this

particular x value so if I'm sitting

here if the input to this function is

0.75 right and now I perturb it by some

little amount like let's add on a

0.1 right what this derivative is

telling me is how much is this

perturbation basically Amplified in the

output right because this little 0.1

perturbation here it's going to result

in some type of perturbation in the

output right so it's basically a

specific run is going to produce a rise

right so you can see this that obviously

this sensitivity of this function

changes as you change the value of x

right so for example if I choose another

value x = 2 right over here

here right we see that it actually

doesn't change here right the slope of

this function is completely flat here

meaning if you're sitting here at two if

the input to this function is now

two right and you put in a little bit of

a 0.1 or the tiniest little input

perturbation you don't expect the output

to change at all right that's what this

is telling you and again you can change

this so let's see red um oh sorry I

probably should have made this green

sorry to be consistent with uh sorry I I

got too excited with the colors tell you

what let's leave it like uh no let's

change this let's make this green cuz

later on I I have another example okay

so this should have been green two

because I want to go red green blue just

to kind of be consistent okay there we

go okay so there's my green value and

then let's choose a blue value over here

you know something uh what did I pick

here

3.25 right here's some other blue value

and again you can read this up here to

get the slope of the function or the

sensitivity of the function there right

so you can now ask yourself okay if the

function has an input of

3.25 and I put some little tiny

perturbation on it how much does the

output change right so again all the

derivative is giving you right the

derivative one physical way to think

about this is sure it's the slope of the

function but really physically what

that's telling you is how much does the

function change when you change the

input or you perturb it a little bit

away from a given input value right

that's what this slope is effectively

giving you it's right it's how sensitive

is the function to changes at this

particular particular location right so

that's what the derivative tells you and

obviously as we discussed it changes

depending on where X is right okay so

that's the idea of a derivative um let's

extend this idea now to the idea of a

gradient okay so remember the idea with

the gradient now is let's still go ahead

and consider a scalar function meaning

the function still outputs a single

variable but now you could have

potentially multiple inputs or multiple

independent parameters or variables

feeding into the function right so in

this case let's say there are n

different inputs or independent

variables to this function X1 X2 all the

way down to xn right now if you remember

our previous video where we discussed

the gradient we know that the gradient

then of this given function f which has

these inputs it's just given as this

right it's written sometime as DF or

nobla F the other alternative notation

for this is it's now it's a partial of

this function f with respect to this

Vector X okay and what that actually

means right is it means again you got to

remember that this Vector this xar is a

vector right there are n independent

inputs right so what this notation means

is it just means the partial of f with

respect to X1 stack that on top with

partial of f with respect to X2 all the

way down stacked at the bottom with

partial of this function f with respect

to xn right and again we got to remind

ourselves and remember that I and others

like the notation that you got to

remember that by the time you take these

partials this is likely still a function

of the independent variables X so again

I'm going to put the notation like this

right so the gradient of f is a function

of X it depends on where you are just

like we saw here right its value depends

on what the value of x is and again I'm

going to put this notation up here as

well right and actually what we should

probably do is we should put this

notation here as well right because

every single one of these components is

going to be a function of the input

variable or the input Vector X all right

so at the end of the day you end up with

an N by1 Vector which represents the

gradient okay and again depending on

which uh reference you're looking at or

what author some people like to stack it

the gradient Vector uh uh sorry stack

the vector as a column Vector like like

I'm drawing here this is what I prefer

some other people like it as a row

Vector um but again just be careful of

what notation is being used and um be

consistent right so I like to stack this

up vertically a lot of people do so

you'll see the gradient written as a

vertical column Vector okay so that's

the idea right so again let's look at a

concrete example just to drive this home

in fact in this gradient video right

where we discussed this gradient in a

little bit more detail this is the

example function that I used so just to

refresh your memory right the way we can

visualize this again it's still a scalar

function right in the sense that it

still outputs a single number right the

way it computes the single number though

is this function has two inputs now it

has an X1 and it has an X2 right two

independent variables or independent

parameters however you want to think

about this these two inputs produce a

single output right which is f of x1x2

right and here's the algorithm or the

formula of how it does this right um so

to compute the gradient of this

particular function right I'm just going

to use my expression or my equation over

here all I got to do is the first entry

is the partial of this function with

respect to X1 while holding X2 constant

or treating X2 as a constant the second

element is the is the exact opposite

right I'm going to take the partial of

this function with respect to X2 while

holding X1 constant so what you end up

with here is I think everyone can see

you can take the partial derivatives of

these two you'll get these two

expressions right so again what this in

physically means is let's go ahead and

um actually I'm going to spin a movie

over of this function on the side um

what you're seeing in this picture is

the orange surface is obviously this

function for a whole bunch of different

X1 and X2 values and as you can see

right the slopes uh of this function

change depending on where you are so

again maybe what we'll do is let me use

our same red green blue idea so

depending let's choose a red Vector X of

in this case I think what you're seeing

here is these red dots let me just make

sure I've got this correct right I used

uh Min -3 for X1 and positive2 for X2

and then the Green Dot you're seeing

here is another x value of I think this

is actually 0 0 okay and then the blue

one that I'm drawing on that surface

here is 12 0 okay so at these different

locations right these numbers change

right so the gradient changes right and

what you can see from this picture is

what the gradient is actually telling us

right physically what comes up right is

this first element it's telling you the

sensitivity of this function f to

changes or perturbations in only X1 so

if you move in the X1 direction right

how much does that do you expect that to

change the output of the function right

does the function grow quickly or slowly

does it go positive or negative right

that's what this first entry of the

gradient is telling you right it's the

sensitivity of the function to

pertubations in the first independent

variable right the second element of the

gradient right is is very similar right

it's the sensitivity the function to

changes SL perturbations in X2

considering that you hold X1 constant

right so again depending on where you

are if you're at that red green or blue

dot in that pcture in in the movie

you're seeing on the side here right you

can see that the function changes um at

different rates at those different

locations and depending if you're moving

in the X1 or the X2 direction right so

that's what the gradient is is measuring

right so really if you come back to this

idea of the derivative right it's

nothing more the gradient is just a

multi-dimensional derivative right

that's all that's telling you right both

of these things right all these

derivatives are telling you right either

it's the total derivative here or a

partial derivative over here it's just

telling you the sensitivity of the

function how is the output of the

function going to change as you change

one of these independent parameters so

that's the idea with the gradient let's

see let's let's leave this uh discussion

of the gradient up on this side of the

board let me erase this over here to get

a little bit more space because all

we're going to do now is extend this

idea of the gradient to build the

Jacobian matrix all right so now we've

got the Jacobian matrix discussion and

all the Jacobian matrix is is now

instead of dealing with a scalar

function let's talk about using a vector

valued function meaning that now this

function instead of having a scalar

output it has a vector output so in this

case I've drawn three and one way to

visualize this or to think about this is

that this Vector valued function it's

nothing more than in this case three

scalar V uh scalar functions stacked on

top of one another right so that's all

this thing is you can take a look at

this stack these three up and now let's

call this Orange Box right it's still

it's a function which takes two

independent variables or two inputs and

now outputs three

things okay so what we can do is we can

just call this now let's call it F Bar

of xar right so again the notation here

is that this function f the bar on top

if we contrast that with over here is

the bar on top means that the output

right this is a vector function in the

sense that now there are 1 2 3 the

output is a vector and the input X is

still a VOR Vector just like we had over

on this

side we called this F of

xar okay so that's what we've got it's

nothing more than three scalar uh

functions stacked on top of one another

so if you want to think about this we

can write this as defining okay F Bar of

xar is our Vector valued function which

is nothing more than a certain number

let's call it maybe M Mike m number of

these different scalar functions stacked

on top of one another so you could have

F1 of X F2 of X all the way down to

F M of

X something like this okay so that's all

this function is right the vector value

function is nothing more than M scalar

function stacked on top of one another

okay so with with this in mind now we

can ask ourselves the exact same

question we've been asking ourselves

earlier is how does this function FB how

is it sensitive to changes in different

parameters or different input variables

X1 X2 all the way down to

xn okay so that's all the Jacobian

matrix is so the jobian Matrix is just a

partial set of derivatives asking how do

each one of these scalar functions fub1

FS2 all the way down to FM change as a

function of how these input variables uh

input parameters change so if you think

about this stare at this first one right

here okay this is exactly what we just

did correct so all that we want is

basically the gradient of function F1

that already told us how function F1 is

sensitive to perturbations in X1 and X2

correct so all you need is uh again let

me use this other notation I'm just

going to write DF bar DX bar right same

same idea except now I've got instead of

a scaler F I've got a vector F and all

this thing is okay is we can stack up

and put the gradient in the first row

now remember I was stressing earlier

that in in this notation we are

considering the gradient to be a column

Vector what we're going to do right here

is we're going to knock this over on its

side and actually make it a row Vector

okay so again you just going to be a

little careful depending on what

notation or what reference you're using

so in this case what we want to write

here is we want the gradient of

fub1 of X okay then you have the

gradient of F2 of X all the way down to

gradient of f f m subx and again what we

have to do is we have to transpose each

one of these to take the column Vector

knock it over on its side make it a row

Vector like this okay and again let's

make sure and remind ourselves we're

going to use this notation that this

Jacobian matrix it's a function of where

the inputs are or what inputs are going

into this right so we should use

consistent notation just like we did

over here with the gradient right

because all we see is the Jacobian

matrix it's nothing more than M

gradients stacked on top of one another

that's all it is okay and in fact we

want to be explicit and write this out

let me go ahead and erase some of this

see if we can fit all of this onto one

board let me get get ourselves a little

bit of room I think we can make this

work okay so if you look at this long

enough let's go ahead and just get this

first row right it's nothing more than

the gradient of FS1 with uh the gradient

of FS1 right and we said the gradient is

nothing more than the the partial der of

the function with respect to each one of

the independent parameters so this is

partial of F1 with respect to X1 okay

and again let's make a note that this is

a function of where you are then you

have partial of F1 with respect to X1

and it's still a function of where you

are all the oh sorry X2 okay all the way

down to partial of

fub1 with respect to xn right because

they're are n independent variables okay

or n inputs to this function okay that's

the first row it's just the gradient of

F1 knocked over on its side so the

second is similar right it's just

partial of

F2 with respect to X1 partial of

FS2 with respect to X2 all the way down

to partial of

FS2 with respect to xn and you repeat

this all the way down to the last row

which is now partial of

FM with respect to X1 then you get

partial of FM of X with respect to X2

all the way down to partial of

FM with respect to

xn there you go okay so what we end up

with is this entire thing is now an M by

n

Matrix okay because we see it's nothing

more than M gradient vectors laid out on

their side in row vector format okay so

that's all the Jacobian matrix is it's

basically a giant Matrix of all the

mixed partial derivatives of all of the

these functions and in fact maybe what

we should do is we should write this

down in the sense that the Jacobian

matrix we see here it's an M by n Matrix

okay but the row I column J okay what

this tells you is it is basically it's

the sensitivity right it's whoops let me

write this down

sensitivity of function I outut

right

to the

change in

XJ right so and in fact maybe the the

better way we should have said this it's

really it's the entire function it's the

function f let's let's rewrite this

maybe in a little bit more clear fashion

right it's a sensitivity of f

Bar's I

output to the change in XJ okay so if I

want to understand

how

the third output this third output

responds to changes in the first input

okay that would be located in this

Jacobian matrix Row 3 column 1 right

that that's how this works so again the

Jacobian matrix it basically tells you

the complete sensitivity or all the

slopes if you want to think about it

that way of all of these different

scalar functions and how they change so

to help visualize that maybe let me let

me stand over here I'll try to put a

picture over on the other side of the

board where you can visualize each one

of these in this case there are

basically two dimensional functions

right in sense that there are two input

parameters and each one of them produce

a single output and that's what I'm

plotting over on the side you can see in

the red green and blue they're just

different surfaces so they have

different sensitivities depending on how

you change X1 and X2 you're you're

basically walking in different

directions on either the red surface for

this first one the green surface for the

second one or the blue surface for for

the bottom one so all the Jacobian

matrix is basically capturing is every

single derivative and as we see you can

be anywhere on that surface depending on

what your X1 and X2 values are so this

Jacobian matrix changes depending on the

values of X1 and X2 just like how we saw

the gradient Vector changes depending on

what the inputs were and just like how

we saw a derivative changes depending on

what its input was so again we now see

the whole picture right we start with

the single derivative we then move and

extend that idea to a gradient and then

we move and extend a gradient idea now

to the Jacobian matrix so this is going

to be a pretty powerful tool um some

history behind it the Jacobian matrix

it's named after Carl Gustaf Jacob

jacobe you can see over here this is

what he looked like he was uh born in

1804 died in

1851 um he was a German mathematician

who made some pretty fundamental

contributions to things like elliptical

functions um Dynamics which we're

actually going to take a look at in just

a second um differential equations uh in

fact he there was a the the famous name

that sometimes you'll hear is the

Hamilton jacobe equations which is

basically an alternative way to express

um equations of motion for dynamic

systems um and in fact a kind of fun

note there's actually a crater on the

near side of the moon named after him

and as we see in this case there's also

the Jacobian matrix which is named after

him so with that history aside maybe

what we should do is let's let's go get

into an example and in fact why don't we

use this picture we've got right here

we've got these three functions this is

as good as a set of functions as any

let's go ahead and compute the Jacobian

of this function which has two inputs

and three outputs and the way those

inputs and outputs are computed are

given these three function so we have

enough information at this point to go

ahead and compute the Jacobian matrix by

just taking all of these partial

derivatives so let me clear off the

board and let's do that next all right

so let's go ahead and compute the

Jacobian for this orange function so

I've just written it down um as we saw

it's just the the gradient of the first

function laid on its side the gradient

of the function of the second function

laid on side and the gradient of the

third function laid on its side so it's

all of these mixed partial derivatives

here so for example let's look at the

one one element it's the partial of F1

with respect to X1 right so all you got

to do is take here's F1 take this

partial with respect to X1 and as you

can see that gets us what just 6 X1 so

that's this element here right and then

the one two element it's the partial of

fub1 with respect to X2 so again still

keep your eye on this first function F1

take its partial with respect to X2 2

and you can see that just turns into

what 3x2 2 which is that element right

so you just go through this and now

moving down to the second row it's now

you repeat this operation now for the

second function with respect to X1 and

you get this right by just taking this

partial and blah blah blah right so at

the end of the day what we see is you

end up with this 3x 2

Matrix right and again its physical

interpretation of what this Matrix is is

each element of this Matrix right it's

measuring the sensitivity of the I

output to the change in the J input so

in other words if we look at the input

outputs let me see if I can do this

right if I make a little table if I want

to look at what the the sensitivity of

the first function output is to the

first input variable that's the one one

element right here correct and then this

one two element tells me the sensitivity

or the slope effectively of the first

function's output to perturbations in

the second input all right and etc etc

you keep moving down so the the

sensitivity of the second function with

respect to the

first input is there and then the

sensitivity of the second function to

the second input is here and then

similarly you just kind of you can pick

off each element of this Matrix right

and what it's basically Al telling you

right is that Matrix is fully

characterizing every possible

combination of the output to input

sensitivity right so now you can pretty

much fully characterize this orange

Vector valued function we understand now

if you perturb or change the inputs X1

and X2 how is that going to change each

one of these three outputs right and

that is exactly what the Jacobian matrix

is giving us right so this is a nice

abstract mathematical form formulation

and example um let's look at an example

of how this might show up in an actual

engineering application all right so

let's look at an example of an

engineering system uh namely a dynamic

system uh as many of you know I'm a

controls engineer and a lot of times the

classic example that controls Engineers

love to look at for a nonlinear um set

of ordinary differential equations is a

classic pendulum right it's just a

pendulum which is swinging about some

point up here it has some Mass on the

end of it and that's it it's just

swinging and as we've seen in the past

this admits a set of nonlinear Dynamics

to make this a little bit more

interesting um I've tried to spice up

this pendulum a little bit so let's

assume that instead of this just being

like a simple boring pendulum maybe this

is a test stand with a two uh

bidirectional rocket engine down here

where you can fire the engine in either

direction and that is going to create an

a propulsive force um that I'm denoting

as is f engine and as this thing is

swinging around due to this Engine Force

there's going to be some drag on it some

aerodynamic drag so I've denoted this as

FD okay um as we've seen there's going

to be obviously gravity pulling down on

the pendulum which is going to impart

some kind of moment and then the only

other moment we're going to add on this

test stand is let's say that there's a

break up here that an operator can turn

on and off so the operator can really

control two things they control the

throttle to the engine that will

basically influence this Engine Force

they can also control the break between

like zero meaning no break and one

meaning full break or something like

that and that's going to go ahead and

control how much it tries to stop this

whole test stand from spinning around

right and again here's some of the

relevant geometry it's a length L and

then as you can expect given the

geometry this moment arm here is L sin

Theta again this is a pretty standard

problem at this point so let's just walk

through it and again some of these

details are just I pulled it out of thin

air just to kind of illustrate R um how

this might generate some set of

equations of motion so again I'm going

to assume that the engine thrust is you

know it's maybe nonlinear depending on

the throttle setting between I don't

know maybe like a negative one means

Back It Up In Reverse a positive one

means go forward but it looks like this

it's some coefficient Alpha times U1

cubed okay that's that's the engine

thrust the uh aerodynamic drag let's

just assume that this is something

really simple it's some coefficient

times the velocity of the vehicle or

this engine so it's basically it's it's

a linear sort of viscous uh type of

damping you've got here so again

velocity you could write that as just L

* Theta dot okay and then the breaking

moment I you know again I I made this up

it's some breaking coefficient gamma

times how much break is being applied by

the operator between zero and one and

then it's going to matter how fast it's

spinning if this thing is spinning

quicker The Brak is going to be more

effective and if the if it's not

spinning at all like Theta dot is zero

the breaking moment is going to be zero

no matter what the operator puts on it

so again I'm just I'm picking this out

of thin air it's not super Germain to

the problem but I just want to have some

somewhat quasi realistic um reasonable

set of Dynamics okay so if you've got

all these forces on moments on this

thing let's just go ahead and sum up all

of the moments right so you've got the

moment due to the engine f * L you've

got the moment the retarding moment due

to drag the retarding moment due to um

due to the break and then this term here

is the moment due to gravity which is

either going to impart a positive or A

negative moment depending on S of theta

right how this term looks okay so this

is our moments so let's go ahead and

apply Newton's Second Law right so

Newton's second law for rotation right

it's the moment of inertia times the

angular acceleration is just the sum of

the moment so I'm going to go say dot

dot dot and skip a couple of steps if

you're interested in all the

nitty-gritty details actually for this

or for any other part of this discussion

right right check the link in the

description of this video where you can

download my um PDF set of notes where

I've got uh pretty much line by line of

how to get here but I'm going to assume

that people are comfortable with

developing equations of motion so you

basically get this right this is your

equation of motion so now let's choose a

state and control Vector for this um in

this case the state Vector is just going

to be Theta and Theta Dot and then the

control Vector the two controls that the

that the user would have is you want U2

right so it's the engine throttle and

the brake command okay so if you've got

these two we can now take a step back

and say okay this is how I would

formulate the problem as a controls

engineer but as a mathematician wanting

to look at this from sort of a sterile

abstract mathematical point of view both

these control vector or sorry the state

vector and the control Vector they're

kind of just they're independent param

independent variables or they inputs to

this set of equations of motion right so

what I mean by that is let's just go

ahead and consider those two as

independent variables I'm going to

create an independent variable Vector

let's call it Z and I'm just going to

stack X on top of U so Z is four

elements long and it's just X1 X2 U1 U2

okay now the reason I want to do that is

because then I can rewrite my equations

of motion and get a nonlinear State

space representation and again if you

want a refresher on state space

representations right we've got a

dedicated video talking about that but

you can write your equations of motion

to look like this okay so it's x dot

right which is basically Z1 and Z dot or

Z1 and Z2 dot right as you see right

here x dot is equal to this ugly

nonlinear function okay and this is a

vector valued function correct you put

in four things you put in these four

independent variables Z1 Z2 Z3 and Z4

and this spits out two things it spits

out a uh Z1 Dot and a Z2 dot so again

think about this this is nothing more

than the the vector valued function f

that we were talking about earlier okay

so I'm going to call this whole thing F

and again the picture that goes along

with it is this orange picture again the

vector valued function f it's nothing

more than two scalar functions stacked

on top of one another this whole thing

takes in four inputs spits out two

outputs okay so now we can now start

talking about the Jacobian of this F

function FB bar right that's all we need

to do and again we saw earlier that the

Jacobian is basically assessing the

sensitivity of all of these outputs to

perturbations in these inputs okay so

what I can write here is that the change

in the output right is the Jacobian

matrix times some perturbation in the

inputs a Delta Z okay so Delta output is

the Jacobian time Delta input again this

is just the higher Dimension Vector

valued interpretation of a derivative a

derivative is basically saying the

change in the output is the slope times

the change in the input okay that's all

this is saying in Matrix form so if I

want to write this it's basically um

sorry maybe what we should do then is

let's calculate this Jacobian J so I'm

going to do that over here okay so the

Jacobian J as we see it's nothing more

than four

um independent parameters sorry I missed

a parenthesis there okay so it's a 2x4

Matrix of all of these partials okay so

all you got to do is just start taking

all these partial derivatives this first

row is super easy because it's the

derivative of F1 with respect to all the

independent variables and F1 luckily for

us it's super easy it's just Z2 so you

end up with just 0 1 0 0 okay now that's

not the case for the second row the

second row is where all the Dynamics

come into the into play okay so it's the

derivative of this ugly nasty expression

with respect to Z1 Z2 Z3 Z4 okay so this

is what you end up with correct this is

the Jacobian matrix here and this is

your two whoopsie my pen is super dead

um I guess this one is dead let's try

this blue pen I've been using blue to

denote the the the dimensions right this

is a 2x4 Matrix okay so here's your

Jacobian matrix so now I can plug it

into this equation down here which is

telling us the change in outputs is the

Jacobian times the change in input so

it's just this 4x2 Matrix times Delta Z

and remember Delta Z is just Delta of

all these X1 X2 U1 U2 so that's what I'm

writing right here and if you stare at

this long enough you can see that okay

the X terms here right this multiplies

this first 2x two block okay the U terms

or your control vectors multiplies this

second 2x two block so why don't I go

ahead and just I'm going to rewrite this

I'm going to break this up okay I'm

going to break this up into some 2x two

Matrix times your state Vector plus

another 2x2 matrix times your control

Vector right if you go ahead and if we

call this

a and this Matrix over here B this

starts to look and I I got to be a

little bit careful here I'm uh let let

me just say this equals a * Delta x + B

time Delta U okay now I'm not going to

say here that this is x dot okay because

that's actually not true we got to be a

little bit careful and I'm going to have

to handwave a little bit and punt this

discussion down to our other video where

we will talk about formally linearizing

a system because if you stare at this

long enough this is the foundation of

how we're going to do this what we end

up with this should look really familiar

right this is sort of like X do is equal

to ax + bu U of course we've got these

Deltas we're going to have to reconcile

a little bit later but at the end of the

day like we said this is the foundation

of basically your

linear OD right it's your linear set of

Dynamics and remember where did we start

from we started from this function it's

ugly it's nonlinear this thing

effectively at the end of the day right

it's this is describing X do is equal to

f of x and U this is your nonlinear OD

or set of dynamic so you have an ugly

nonlinear system like this you can

describe it here and now we can use this

Jacobian matrix to basically linearize

the system and turn it into and again

hold we're not totally turning on so so

don't quote me on this right but we

we're we're 90% of the way to the x do

is equal to a Delta X plus b Delta U

right so we're going from nonlinear to

linear Dynamics and the Jacobian is the

key to making all of this work and again

let's just reiterate this for for for to

to to Really Drive the point home right

all the Jacobian matrix is talking about

right what the A and the B Matrix

capture here it's the sensitivity of the

Dynamics to perturbations in the state

and control Vector depending on where

you happen to be located and where

you're operating in state and control

space so if this pendulum is you know

caned over like this with a certain set

of input conditions right its Dynamics

behave differently than if it were say

vertically straight up right and the

Jacobian matrix captures all of that in

a nice graceful elegant fashion okay so

I think this is super exciting because

yeah this is the key and the foundation

for linearizing dynamic systems now I

know not all of you are interested Ed in

controls and dynamic systems but let's

just say this Jacobian matrix idea this

is also the foundation for our next

video where we're going to start talking

about the chain Rule and the chain rule

we're going to see is basically uh it's

it's a way that we can look at composite

functions and try to understand again

how pertubations in inputs affect

outputs at all of these different layers

of this composite function that is going

to be the building blocks for a lot of

other engineering uh tools for example

um in Ai and machine learning there's

the concept of a neural network and back

propagation and how to train that

Network and we're going to see that that

is founded on the idea of the chain rule

which we are going to show the chain

rule is founded on the idea of the

Jacobian we just saw the Jacobian is

found on the idea of a gradient and the

gradient is founded on the idea of a

derivative so really all of this is just

fancy ways of looking at how the

derivative affects a lot of these

interesting Eng Engineering Systems so

with that being said I think this is

probably a great spot to leave it um I

hope you enjoyed the video and if so I

also hope you'll consider subscribing to

the channel um if you scroll a little

ways down and click on that subscribe

button it really does help me continue

making these videos and remember the new

videos come out every Monday so I hope

we'll be able to catch you at a future

discussion and we can all learn

something new together so until then I

think I'm going to sign off talk to you

later bye

