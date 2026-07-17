Arguments, type of arguments , recursion, docstring

1. arguments

Function = Pizza shop

Argument= Pizza Flavor

def order_pizza(flavor)://floavor ---->parameter

print("your" , flavor,"pizza is ready)

order_pizza("cheese")//cheese---->argument

order_pizza("vegies")

outcome: your cheese pizza i sready

your vegie pizza i sready

2.Types Of argumnets

A. Positional argument

The values must be passed in the correct order

ex : Birthday

def introduce(name,age):

print("Name is ", name)

print("Age is ", age)

introduce("Alice",10)

introduce(10,"Alice")//incorrect order

B. Default Argument

A parameter alreadyt has a default value


def drink(name,beverage="Water"):

print(name,"gets", beverage)

drink("john")

drink("Kishan","juice")

ouput:

john gets Water

Kishan gets Juice

3. Recursrion

A function vcalling itself

def countdown(n):

if n==0:

print("blast off")

else:

print(n)

countdown(n-1)

countdown(5)

5

4

3

2

1

Blast off

4.DocString

"""gdghgfhjhgjkjbk"""

def add(a,b):

"""

return the sum of two numbers

"""


return a+b

result=add(4,6)

print(result)

result1=result *2

print(add....doc.....)

terminal

return the sum of two numbers

10

def total_calc(bill_amount,tip_perc)

define function to calcalute teh tip on bill

total=bill_amount *(1+0.01*tip_perc)

total=round(total,2)

print("please pay",total)

total_calc(150,20)

Desription:

Food bill =150

Tip= 20 perc

bill_amount=150

tip_perc=20

0.01* tip_perc

20%---->20/100--->0.20

why 1 is added

bill -- 100%

tip---20 %

100%+20%=120%

1+0.20=1.20

150*1.20=180

def add