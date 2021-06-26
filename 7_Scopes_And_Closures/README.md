# Closures:
In python, nested functions able to access the variables in enclosing scope

    def outerFunction(text):
        text = text

        def innerFunction():
            print(text)

        innerFunction()

innerFunction and the local variable in the function scope 'text' is accessible only inside outerFunction. Its not accessible outside.</br>

**🦸Closures to the rescue!**

In Closures, nested function is returned. Both the nested function and the local scope variables ('Free Variables') are accessible outside the closure as well.

    def outerFunction(text):
        text = text

        def innerFunction():
            print(text)

        return innerFunction 

1. Closure that takes a function and then check whether the function passed has a docstring with more than 50 characters. 50 is stored as a free variable 



2. Closure that gives you the next Fibonacci number (+ 2 tests) 
3. Closure that can keep a track of how many times add/mul/div functions were called, and update a global dictionary variable with the counts (+ 6 tests)
4. Modified above closure which takes different dictionary variables to update different dictionaries (+ 6 tests) 
