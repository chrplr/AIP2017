-----------------------
Concepts you should know in Python :

Objects
=======

A programming language like Python manipulates **objects** of different **types**:

Scalar objects
--------------

* `int`  used to represent integers, e.g. -3, 0, 1000...
* `float`  use to represent real numbers, e.g. 3.0, 5.34, -33.33
* `bool` to represent True and False
* `NoneType` to represent `None`

Start `ipython` and type:


	type(2)
	type(3.4)
	type(True)
	type(None)
	
	
**Objects** and **operators** can be combined to form **expressions**, each of which evaluates to an object of some type. We will refer to this as the **value** of the expression. For example, the expression `3 + 2` denotes the object `5` of type `int`, and the expression `3.0 + 2.0` denotes the object `5.0` of type float .


	type(3 + 2)
	type(3.0 + 2.0)
	type(3 + 2.0)  # note the automatic int->float conversion

Example of operators on int and float:

	11 + 3
	11 - 3
	11 * 3
	11 / 3
	11 ** 3  # power
	11 % 3  # modulo
    11 >= 3
	

Strings
-------



Lists
-----


Dictionnaries
-------------


Variables
=========



Programs (a.k.a Scripts)
========================


Input/Output
============


Branching
=========

Conditional


Iterating



