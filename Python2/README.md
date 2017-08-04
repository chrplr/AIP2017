Introduction to programming: a self-learning guide
==================================================

Christophe Pallier 2017

This is a proposed road map to teach yourself programmin using some  excellent resources available on the web. 


* Start from Scratch

Scratch (https://scratch.mit.edu/) is a programming language designed to teach programming to complete beginners. For a quick start, read the _Getting Started Tutorial_ (https://resources.scratch.mit.edu/www/guides/en/Getting-Started-Guide-Scratch2.pdf)

Test yourself: try to program a Pong Game (a solution is provided in the tutorial  "Create a Pong Game")


* How computers work?

** _Computer Science Unplugged / L'informatique sans ordinateur_

Goto http://csunplugged.org/ and read the sections of the book  
http://csunplugged.org/books/ about the representations of integer numbers, images and text. Of course, you can read more if you like it.

Test: You should be able to write an algorithm (a recipies) to determine the binary representation of a given integer number.


** Low level programming: Machine language 

Read Chapter 24 "The seven secrets of computers revealed" of Daniel Dennett's _Intuition Pumps And Other Tools for Thinking_ (I recommend to buy this book, but if you do not have it, an older version of this text is available at http://sites.tufts.edu/rodrego/files/2011/03/Secrets-of-Computer-Power-Revealed-2008.pdf)

Test: Implement at least the Programs 1, 2, 3 and 4 described in the chapter using the Register Machine simulation "RodRego" available at http://sites.tufts.edu/rodrego/ 


** (optional) If you want to understand computers at the hardware level, you can read  _How computers work_ by Roger Young  http://www.fastchip.net/howcomputerswork/bookbpdf.pdf
or the more advanced _The Elements of Computing Systems: Building a Modern Computer from First Principles_ by  Noam Nisan and Shimon Schocken: http://www1.idc.ac.il/tecs/plan.html and http://www.nand2tetris.org/

* Introduction to Programming in Python 

First of all, install Python 3 from https://www.continuum.io/downloads
Then, select one of the following books and study it, trying to run the  examples and solve the exercices.

-  _Invent Your Own Computer Games with Python_ by Al Sweigart. http://inventwithpython.com

- _How to Think Like a Computer Scientist_ 

You can select one of the following three:

   * _Think Python_ by Allen B. Downey http://greenteapress.com/wp/think-python-2e/ 
   *  How to Think Like a Computer Scientist. Learning with Python 3
http://openbookproject.net/thinkcs/python/english3e/ 
   * A (slightly different) online version also exists:
https://interactivepython.org/runestone/static/thinkcspy/GeneralIntro/intro-TheWayoftheProgram.html


Remarks: 
- If you find these books too difficult, you can bootstrap your knowledge of Python with the Introductory Python courses on Code Academy or on OpencourseWare
- If you find them to easy, you can read the _Introduction to Computation and Programming Using Python_ (MIT)


* More advanced programming

- Thinking Complexity 2nd Edition by Allen B. Downey http://greenteapress.com/wp/think-complexity/  The code is available from https://github.com/AllenDowney/ThinkComplexity2

- Software Carpentry. https://software-carpentry.org/lessons/ . In particular, see the lessons _The Unix Shell_ and _Version Control with Git_.

- _Scipy Lecture Notes: One document to learn numerics, science, and data with Python_ by  Emmanuelle Gouillart, Olav Vahtras and Gaël Varoquaux http://www.freetechbooks.com/scipy-lecture-notes-one-document-to-learn-numerics-science-and-data-with-python-t1021.html

-----------------------


Aide mémoire Python :



Objects
=======

A programming language like Python manipulates **objects**

Every object has a **type**:

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






