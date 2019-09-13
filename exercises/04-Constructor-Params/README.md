# `04` Parameterized Constructor
As you know, every class comes with a magic function called "constructor" that gets called
whenever a new instance of that class is created.

Right now, all objects of the class Person will be named Bob because it is hard-coded on the
constructor function that way.

Can you imagine a world where everyone is named Bob Dylan?

The parameterized constructor take its first argument as a reference to the instance being constructed
known as **self** and the rest of the arguments are provided by the programmer.



```Python
class ClassName:

    def __init__(self, foo1, foo2):
        # constructor code


```
Whenever you are instantiating a new object of that class, you will be able to do the following:
```Python
obj = ClassName('bar1','bar2')
```

## 📝 Instructions:
1. Please update the **constructor** of the class to allow the **name**, **last_name** and **birth_date** to be passed as a parameter, in that same order.


