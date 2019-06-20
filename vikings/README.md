# What I learned

## Special methods

* They are meant to be used by python interpreters by built-in function like: len -> __len__
* For built-in objects like list and str it takes a shortcut to the CPython implementation attributes

## Tuples
* Typles are not only immutable lists, they are used to represent records too.
* Use \* to grab excess items.
* Named tuples using collections.namedtuple

## Functions as first-class objects
* Functions can be objects, assigned to a variable, and returned as result for another function.
* A function that takes a function as argument or returns a function as the result is a higher-order function like: map and filter. 
* Types of functions:
    * User-defined functions: lambda or created with def.
    * Built-in functions: like len.
    * Built-in methods: like list.append
    * Function: they are defined in classes
    * Classes: like Farmer in the example.
    * Class instances: if __call__ is implemented.
    * Generator functions: if a function use yeild keyword to return result.

## Keyword-Only Parameters:
* It is a new feature in python 3. To use it add it to the method signature after positional arguments so it won't be included.

## Function Annotations
* Annoations for the method that is stored __annotations__

## Freezing Arguments with functools.partial
* freezing arguments in a function and produce another callable function.