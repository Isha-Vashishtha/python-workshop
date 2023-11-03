def my_fun():#local scope means when we create the value of  a variable inside the function.
   x=10
   print(x)
my_fun()

def sum_fun():
    x=3
    y=7
    print(x+y)
sum_fun()
    
x=10#global scope means after assingning the value of a variable outside the function it cann't be change by using the variable global.and it we want to make changes to that variable we can change it.
def my_function():
    print(x)
my_function()

x=10
def modify_global():
    global x
    x=20
modify_global()    
print(x)

x=10
def modify_global():
    global x
    x=20
    print(x)
modify_global()    
